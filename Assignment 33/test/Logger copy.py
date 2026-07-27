import os
import datetime

def createLogDirectory():

  if os.path.isdir("Marvellous"):
    return

  os.mkdir("Marvellous")


def createLogFile():
  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
  logFileName = "DuplicateFileLog_%s.log"%timestamp

  logFilePath = os.path.join("Marvellous", logFileName)

  lfobj = open(logFilePath, "w")
  lfobj.close()

  return logFilePath

def writeLog(logPath, message):
  lfobj = open(logPath, "a")
  lfobj.write(str(message) + "\n")
  lfobj.close()
