import Logger
import MailSender
import ProcessUtils
import sys
import time
import Validator

def performPlatformSurveillance():
  dirName = sys.argv[1]
  receiver = sys.argv[2]

  if not Validator.validateDirectory(dirName):
    print("Invalid Directory")
    sys.exit()

  if not Validator.validateEmail(receiver):
    print("Invalid Email")
    sys.exit()

  start_time = time.ctime()

  logPath = Logger.createLogFile(dirName)
  processCount = ProcessUtils.logAllProcesses(logPath)
  end_time = time.ctime()
  body = f"""
  Hello,
  
  The Platform Surveillence Operation has been completed successfully
  
  Operation Statistics
  
  Starting time : {start_time}
  
  Completion time : {end_time}
  
  Log Directory : {dirName}

  Processes Scanned : {processCount}
  
  Please find the detailed log file attached.
  
  Regards,
  
  Platform Surveillence Script
  """

  MailSender.sendMail(receiver,logPath,body)


def main():
  performPlatformSurveillance()

if __name__ == "__main__":
  main()