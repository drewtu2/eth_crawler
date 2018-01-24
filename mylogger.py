import logging 
import datetime
import os

def config_logs():
    # Logfile
    logfolder = "logs/"
    logdate = datetime.datetime.now().strftime("%y-%m-%d_%H:%M") + "_"
    logfile = "targeted_crawl.log"

    logpath = logfolder + logfile
    #logpath = logfolder + logdate + logfile
    if not os.path.exists(logfolder):
            os.makedirs(logfolder)

    # Formats
    datefmt='%m/%d/%Y %I:%M:%S %p'
    logformat_w_date = '%(asctime)s %(levelname)s: %(message)s'
    logformat_wo_date = '%(levelname)s: %(message)s'

    # Get the Root Logger and
    rootLogger = logging.getLogger()

    # Create formatters
    logFormatter_w_date = logging.Formatter(logformat_w_date, datefmt)
    logFormatter_wo_date = logging.Formatter(logformat_wo_date)

    # Create and add the file stream handler to the logger
    fileHandler = logging.FileHandler(logpath)
    fileHandler.setFormatter(logFormatter_w_date)
    rootLogger.addHandler(fileHandler)

    # Create and add the console stream handler to the logger
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter_wo_date)
    #rootLogger.addHandler(consoleHandler)

    rootLogger.setLevel(logging.INFO)
