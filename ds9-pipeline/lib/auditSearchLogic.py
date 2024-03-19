import json
import pandas as pd
import os
import shutil
import logging

from lib.common import Common
# from gcpConnector import GcpConnector


class AuditSearchLogic:
    """
    audit.search
    By default, one day is split into 20*5 chunks.
    """

    def __init__(
            self, credentialFileCDC: str, start: str, end: str, mainPath: str):
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
        # (
        #     self.folderPath,
        #     self.dataPath,
        #     self.FormattedLogFilePath,
        # ) = self._folder_hierarchy(mainPath)

        self.dataPath = mainPath

        # print(f"+++++++ {start} ---- {end} +++++++"+"\n")

    def set_save_location(self, saveLocation, **args):
        """'
        Assign save location object according to saveLocation which could be an element in ["local", "GCP_bucket"]
        """
        if saveLocation == "GCP_bucket":
            self.locationObj = GcpConnector(
                bucketName=args.get("bucketName"),
                BucketCredentialFile=args.get("BucketCredentialFile"),
            )
            self._prepare_gcp_blob(self.dataPath)
            # self._prepare_gcp_blob(self.folderPath)
        elif saveLocation == "local":
            self.locationObj = None
            self._prepare_local_folders( self.dataPath)

    def query_CDC(self):
        """
        Access CDC and write results to designated location
        """

        dayArray = self.commonFuncs.get_dayArray(self.start, self.end)
        URL, params, timeIdentifier, table = self.commonFuncs.get_cdc_connect(
            self.credentialFileCDC, "audit.search"
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
        # self._write_formattedlog(dfFormattedlog, self.FormattedLogFilePath)
        start = self.start
        end = self.end
        logging.getLogger().setLevel(logging.INFO)
        logging.info(f"{start}-{end} is done, total count: {totalWriteCounter}")

    def _folder_hierarchy(self, mainPath):
        '''setup folder architecture'''
        start = self.start
        end = self.end

        # root folder
        folderPath = os.path.join(mainPath, f"{start}---{end}")
        # folderPath = mainPath
        dataFolderName = "data"
        FormattedLogFileName = "formattedLog.csv"  # formatted log file
        dataPath = os.path.join(folderPath, dataFolderName)  # data path
        FormattedLogFilePath = os.path.join(
            folderPath, FormattedLogFileName
        )  # formatted log file path

        return folderPath, dataPath, FormattedLogFilePath

    def _prepare_gcp_blob(self, folderPath):
        self.locationObj.delete_blob(folderPath)

    def _prepare_local_folders(self, dataPath):
        """prepare folders, only works when saveLocation = 'local'"""

        # delete the folder if exists, then create a new one
        if os.path.exists(dataPath):
            shutil.rmtree(dataPath)

        # os.makedirs(folderPath)
        os.makedirs(dataPath)



    def _write_formattedlog(self, dfFormattedlog, FormattedLogFilePath):
        # output formattedLog.csv file
        if self.locationObj is None:
            dfFormattedlog.to_csv(FormattedLogFilePath, index=False)
        elif isinstance(self.locationObj, GcpConnector):  # google bucket
            self.locationObj.write_df_to_gcp(
                FormattedLogFilePath, dfFormattedlog)
