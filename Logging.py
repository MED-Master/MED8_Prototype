import pandas as pd
#data logging
reply_logger = []
def logToCSV():
    dict = {'Replies': reply_logger}
    dfLog = pd.DataFrame(dict)
    dfLog.to_csv('Transcriptions.csv')
    print("Logging complete")