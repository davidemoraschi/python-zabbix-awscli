#!/usr/bin/python

'''To use gzip file between python application and S3 directly for Python3.
Python 2 version - https://gist.github.com/a-hisame/f90815f4fae695ad3f16cb48a81ec06e
Thenks to https://gist.github.com/a-hisame/be1c1746520b2b5589901a1045bb2174
'''

import io
import gzip
import json
import boto3
import paramiko
import base64
import fnmatch
from stat import S_ISDIR, S_ISREG


def get_newest_file_from_sftp(logger, aws_region, aws_secret_name, ftp_folder, ftp_file_pattern, s3client, s3_bucket, s3_path):
    '''Function to connect to SFTP server and download to S3 bucket'''
    credentials = get_secret_credentials(aws_region, aws_secret_name)
    ftp_host = credentials.get('FTP_HOST')
    ftp_port = int(credentials.get('FTP_PORT'))
    ftp_user = credentials.get('FTP_USER')
    ftp_pass = credentials.get('FTP_PASS')

    f = ''
    transport = paramiko.Transport((ftp_host, ftp_port))
    transport.connect(username=ftp_user, password=ftp_pass)
    with paramiko.SFTPClient.from_transport(transport) as sftp:
        sftp.chdir(ftp_folder)
        filesInSFTP = sftp.listdir_attr('')
        filesInSFTP.sort(reverse=True, key=lambda f: f.st_mtime)

        for entry in filesInSFTP:
            mode = entry.st_mode
            if S_ISREG(mode):
                f = entry.filename
                if fnmatch.fnmatch(f, ftp_file_pattern):
                    with io.BytesIO() as data:
                        logger.info('Found file: %s', f)
                        sftp.getfo(f, data)
                        data.seek(0)
                        s3client.upload_fileobj(data, s3_bucket, s3_path + '{0}'.format(f))
                    break
    return f


def get_secret_credentials(aws_region, aws_secret_name):
    '''Create a Secrets Manager client and returns SFP credentials'''
    session = boto3.session.Session()
    smclient = session.client(service_name='secretsmanager', region_name=aws_region)
    get_secret_value_response = smclient.get_secret_value(SecretId=aws_secret_name)
    if 'SecretString' in get_secret_value_response:
        secret = get_secret_value_response['SecretString']
    else:
        secret = base64.b64decode(get_secret_value_response['SecretBinary'])
    credentials = json.loads(secret)
    return credentials


def upload_json_gz(s3client, bucket, key, obj, default=None, encoding='utf-8'):
    ''' upload python dict into s3 bucket with gzip archive '''
    inmem = io.BytesIO()
    with gzip.GzipFile(fileobj=inmem, mode='wb') as fh:
        with io.TextIOWrapper(fh, encoding=encoding) as wrapper:# type: ignore
            wrapper.write(obj)
    inmem.seek(0)
    # logger.info('Uploading file: %s', bucket + '/' + key)
    s3client.put_object(Bucket=bucket, Body=inmem, Key=key)


def download_json_gz(logger, s3client, bucket, key):
    ''' download gzipped json file from s3 and convert to dict '''
    logger.info('Downloading file')
    response = s3client.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read()
    with gzip.GzipFile(fileobj=io.BytesIO(content), mode='rb') as fh:
        return json.load(fh)


if __name__ == '__main__':
    bucketname = ''      # input for your bucketname
    key = 'tmp.json.gz'  # input for your key on S3 (means S3 object fullpath)
    s3 = boto3.client('s3')
    upload_json_gz(s3, bucketname, key, {'あ': 'いうえお'})
    actual = download_json_gz(s3, bucketname, key)
    assert actual == {'あ': 'いうえお'}
