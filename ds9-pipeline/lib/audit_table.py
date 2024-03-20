import json
import time
import pandas as pd
import datetime
import dateutil.parser
import os
import shutil
import argparse


from common import Common
from gcpConnector import GcpConnector


class AuditSearch:
    """
    audit.search
    """

    def __init__(
        self, credentialFileCDC: str, start: datetime.datetime, end: datetime.datetime
    ):
        """

        Args:
            saveLocation(list): Place to save all .json files. Could be an element in ["local", "GCP_bucket"]
        """
        self.credentialFileCDC = credentialFileCDC
        self.start = start
        self.end = end

        # create instance of common funcitons
        self.commonFuncs = Common()

        # location class
        self.locationObj = object()

        # set file and folder hierarchy
        (
            self.folderPath,
            self.dataPath,
            self.FormattedLogFilePath,
        ) = self._folder_hierarchy()

        # set logger
        self.logger = self.commonFuncs.get_logger()
        self.logger.info(f"+++++++ {self.commonFuncs.datetime2str(start)} ---- {self.commonFuncs.datetime2str(end)} +++++++"+"\n")

    def set_save_location(self, saveLocation, **args):
        """'
        Assign save location object according to saveLocation which could be an element in ["local", "GCP_bucket"]
        """
        if saveLocation == "GCP_bucket":
            self.locationObj = GcpConnector(
                bucketName=args.get("bucketName"),
                BucketCredentialFile=args.get("BucketCredentialFile"),
            )
            self._prepare_gcp_blob(self.folderPath)
        elif saveLocation == "local":
            self.locationObj = None
            self._prepare_local_folders(self.folderPath, self.dataPath)

    def query_CDC(self):
        """
        Access CDC and write results to designated location
        """
        startTime = time.time()

        dayArray = self._get_dayArray(self.start, self.end)
        URL, params, timeIdentifier, table = self._get_cdc_connect(
            self.credentialFileCDC
        )

        totalWriteCounter, dfFormattedlog = self.commonFuncs.query_all_data(
            dayArray,
            URL,
            params,
            table,
            timeIdentifier,
            self.dataPath,
            locationObj=self.locationObj,
        )

        # output formattedLog.csv file
        self._write_formattedlog(dfFormattedlog, self.FormattedLogFilePath)

        self.logger.info("\n"+f"Done!! total running time: {(time.time() - startTime)/60} mins")
        self.logger.info(f"total count: {totalWriteCounter}")

    def _folder_hierarchy(self):
        '''setup folder architecture'''
        start = self.commonFuncs.datetime2str(self.start)
        end = self.commonFuncs.datetime2str(self.end)

        # root folder
        folderPath = os.path.join("audit_search", f"{start}---{end}")
        dataFolderName = "data"
        FormattedLogFileName = "formattedLog.csv"  # formatted log file
        dataPath = os.path.join(folderPath, dataFolderName)  # data path
        FormattedLogFilePath = os.path.join(
            folderPath, FormattedLogFileName
        )  # formatted log file path

        return folderPath, dataPath, FormattedLogFilePath

    def _prepare_gcp_blob(self, folderPath):
        self.locationObj.delete_blob(folderPath)

    def _prepare_local_folders(self, folderPath, dataPath):
        """prepare folders, only works when saveLocation = 'local'"""

        # delete the folder if exists, then create a new one
        if os.path.exists(folderPath):
            shutil.rmtree(folderPath)

        os.makedirs(folderPath)
        os.makedirs(dataPath)

    def _get_dayArray(self, start, end):
        """
        Prepare grouped timestamp. Split one day into 5 chunks
        """

        # split one day into 5 chunks
        step = ((end - start).days + 1) * 5

        dayArray = self.commonFuncs.datetime_split(
            self.commonFuncs.datetime2str(start),
            self.commonFuncs.datetime2str(end),
            step=step,
        )
        self.logger.info(f"total chunks: {len(dayArray)-1}")
        return dayArray

    def _get_cdc_connect(self, credentialFileCDC):
        """credentials and query parameters to access CDC"""
        # credentials to access CDC
        with open(credentialFileCDC) as f:
            cre = pd.json_normalize(json.load(f))
        URL = cre.iloc[0]["audit.search.URL"]
        params = {}
        params["secret"] = cre.iloc[0]["secret"]
        params["userKey"] = cre.iloc[0]["userKey"]
        params["apiKey"] = cre.iloc[0]["apiKey"]
        timeIdentifier = cre.iloc[0]["audit.search.timeIdentifier"]
        table = cre.iloc[0]["audit.search.table"]

        return URL, params, timeIdentifier, table

    def _write_formattedlog(self, dfFormattedlog, FormattedLogFilePath):
        # output formattedLog.csv file
        if self.locationObj is None:
            dfFormattedlog.to_csv(FormattedLogFilePath, index=False)
        elif isinstance(self.locationObj, GcpConnector):  # google bucket
            self.locationObj.write_df_to_gcp(FormattedLogFilePath, dfFormattedlog)


def set_input():
    '''use argparse package to set the input arguments: start, end'''
    parser = argparse.ArgumentParser()
    start = "2021-02-26T10:35:26.135Z"  # the earliest record in audit.search
    end = datetime.datetime.now(datetime.timezone.utc)
    end = end.isoformat(
        timespec="milliseconds").replace("+00:00", "Z")

    parser.add_argument("start", nargs="?", type=str, default=start,
                        help="start timestamp, like '2021-02-26T10:35:26.135Z' ")
    parser.add_argument("end", nargs="?", type=str, default=end,
                        help="end timestamp, by default is today")
    args = parser.parse_args()
    start = dateutil.parser.parse(args.start)
    end = dateutil.parser.parse(args.end)

    return start, end


def main():
    # get start and end tiemstamp from command line
    start, end = set_input()

    # credential, URL and query parameters to connect CDC
    credentialFileCDC = "credentialCDC.json"
    auditTable = AuditSearch(credentialFileCDC, start, end)

    # use GCP bucket
    bucketName = "bx5050-test1"
    BucketCredentialFile = "straumann-global-a27d2a8d8096.json"
    auditTable.set_save_location(
        "GCP_bucket", bucketName=bucketName, BucketCredentialFile=BucketCredentialFile
    )

    # use local hard disk
    # auditTable.set_save_location("local")

    auditTable.query_CDC()


if __name__ == "__main__":
    main()
# "2022-10-01T00:00:00.000Z"
