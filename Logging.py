import pandas as pd
import time
from datetime import datetime, date

class Logger():
    reply_logger = []       # logs the replies from user and VA
    startEnd_logger = []    # logs the datetime when the program begins and ends
    button_logger = []      # logs button event for send and talk
    timerButton_logger = [] # logs the date of button events


    def logToCSV(self):
        self.startEnd_logger.append(self.dateTime())
        self.startEnd_logger.append(self.startEnd_logger[1]-self.startEnd_logger[0])
        dict = {'Replies': self.reply_logger, 'Start/End/Total Time': self.startEnd_logger,
                'Button Event': self.button_logger, "Event time": self.timerButton_logger}
        dfLog = pd.DataFrame.from_dict(dict, orient='index')
        dfLog.to_csv('logs/images/Transcriptions.csv')
        print("Logging complete")

    def dateTime(self):
        now = time.time()
        dt = datetime.fromtimestamp(now)
        #str(dt).split(' ')[1].replace(":", '-')
        return dt

