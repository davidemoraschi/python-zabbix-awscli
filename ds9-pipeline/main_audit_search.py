import concurrent.futures
import argparse
import datetime
from lib.common import Common
from lib.auditSearchLogic import AuditSearchLogic
import logging
import os

class AuditSearch(AuditSearchLogic):
    '''
    This class queries the audit.search table.
    Usage:
        a. No argument, query all the datetime: audit_search_conc.py
        b. With arguments, query from [start, end): audit_search_conc.py "2021-02-26T10:35:26.135Z", "2022-02-26T10:35:26.135Z"
    '''
    def __init__(self, *args) -> None:
        super().__init__(*args)

class ParaSet:
    """
    Handles command line input, divides [start, end] into 20*5 chunks.
    """

    def set_input(self):
        '''Uses argparse package to set the input arguments: start, end.'''
        parser = argparse.ArgumentParser()
        start = "2021-02-26T10:35:26.135Z"  # the earliest record in audit.search
        end = datetime.datetime.now(datetime.timezone.utc)
        end = end.isoformat(timespec="milliseconds").replace("+00:00", "Z")

        parser.add_argument("--start", nargs="?", type=str, default=start,
                            help="start timestamp, like '2021-02-26T10:35:26.135Z' ")
        parser.add_argument("--end", nargs="?", type=str, default=end,
                            help="end timestamp, by default is today")
        args = parser.parse_args()

        return args.start, args.end

    def set_inputs_para_conc(self, credentialFileCDC: str, start: str, end: str) -> list[str, str, str, str]:
        '''Splits [start, end] into several chunks. The length of chunks depends on the time range. 
            By default, each day is split into 5*5 chunks.
        
            Returns:
            [[credentialFileCDC, start1, end1, mainPath], [credentialFileCDC, start2, end2, mainPath]]'''
        # split the time range into chunks
        groupN = ((Common().str2datetime(end) - Common().str2datetime(start)).days + 1) * 5
        if groupN < 100:
            groupN = 100
        elif groupN < 500:
            groupN = 500
        elif groupN < 2000:
            groupN = 2000
        else:
            groupN = 3000
        # groupN = 2
        dayArray = Common().datetime_split(start, end, groupN)

        inputs = []
        t1 = dayArray[0]
        for t2 in dayArray[1:]:
            inputs.append([credentialFileCDC, t1, t2,
                           f"audit_search_{start}---{end}"])
            t1 = t2
        return inputs

def main():
    # bucketName = "bx5050-test1"
    # BucketCredentialFile = "straumann-global-a27d2a8d8096.json"
    credentialFileCDC = "credentialCDC.json"

    # get start and end timestamp from command line
    start, end = ParaSet().set_input()
    # print(start, end)
    inputs = ParaSet().set_inputs_para_conc(credentialFileCDC, start, end)

    logging.getLogger().setLevel(logging.INFO)
    logging.info(f"=========chunks: {len(inputs)}, total JSON files: {len(inputs)}*5={len(inputs)*5}=============")

    # initialize auditTable class
    auditTables = [AuditSearch(*para) for para in inputs]

    # setup output JSON location to local or Google Bucket
    [aT.set_save_location("local") for aT in auditTables]
    # [aT.set_save_location("GCP_bucket", bucketName=bucketName,
    #                       BucketCredentialFile=BucketCredentialFile) for aT in auditTables]

    # start querying audit.search table concurrently
    num_cores = os.cpu_count()
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        [executor.submit(aT.query_CDC) for aT in auditTables]

if __name__ == "__main__":
    main()
# "2022-10-01T00:00:00.000Z"
