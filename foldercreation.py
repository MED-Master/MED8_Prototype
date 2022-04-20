import os
import time
from datetime import datetime


class folder():
    baseFolder = 'logs/images/'

    @staticmethod
    def RenameLogFolder():
        now = time.time()
        dt = datetime.fromtimestamp(now)
        dt = str(dt).split('.')[0].replace(":", '-')
        logFolder = 'logs/' + dt + '/'
        os.rename(folder.baseFolder, logFolder)
        folder.Create()


    @staticmethod
    def Create():
        if not os.path.exists("logs"):
            os.mkdir('logs')
        if not os.path.exists(folder.baseFolder):
            os.mkdir(folder.baseFolder)
