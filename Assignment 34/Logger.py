import os
import datetime


def createLogFile(dirName):
  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
  logFileName = "ProcessInformationLog_%s.log"%timestamp

  logFilePath = os.path.join(dirName, logFileName)

  lfobj = open(logFilePath, "w")
  lfobj.close()

  return logFilePath

def writeLog(logPath, message):
  lfobj = open(logPath, "a")
  lfobj.write(str(message) + "\n")
  lfobj.close()
