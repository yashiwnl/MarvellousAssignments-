import sys
import time
import schedule

import Validator
import Logger
import FileUtils
import MailSender


def displayHelp():
    print("Duplicate File Removal Automation")
    print("This script scans a directory, identifies duplicate files using checksums,")
    print("deletes duplicate files, creates a log file, and sends the log file through email.")
    print()
    print("Usage:")
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")
    print()
    print("Example:")
    print("python DuplicateFileRemoval.py /home/yash/Demo 30 abc@example.com")


def displayUsage():
    print("Usage:")
    print("python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>")


def performDuplicateRemoval(directoryPath, receiver):

  border = "-"*65
        
# ---------------- Logger ----------------

  Logger.createLogDirectory()
  logPath = Logger.createLogFile()

  # ---------------- Scan ----------------

  startTime = time.ctime()

  try: 
    fileList = FileUtils.getAllFiles(directoryPath)

    checksumDict = FileUtils.findDuplicates(fileList)

    deleteCount, deletedFiles = FileUtils.deleteDuplicates(checksumDict)

  except Exception as e:
    Logger.writeLog(logPath, f"Unexpected Error occurred: {e}")
    return

  endTime = time.ctime()

  # ---------------- Statistics ----------------

  totalFiles = len(fileList)

  duplicateCount = 0

  for files in checksumDict.values():
      if len(files) > 1:
          duplicateCount += len(files) - 1

  # ---------------- Write Log ----------------

  Logger.writeLog(logPath, f"Log Generated At : {startTime}")
  Logger.writeLog(logPath, border)
  Logger.writeLog(logPath, "")
  Logger.writeLog(logPath, border)
  Logger.writeLog(logPath, "              Disk Sanitizer Script                  ")
  Logger.writeLog(logPath, border)
  Logger.writeLog(logPath, "")

  Logger.writeLog(logPath, f"Directory Scanned : {directoryPath}")
  Logger.writeLog(logPath, f"Receiver Email : {receiver}")
  Logger.writeLog(logPath, f"Scanning Started : {startTime}")
  Logger.writeLog(logPath, f"Scanning Completed : {endTime}")

  Logger.writeLog(logPath, border)

  Logger.writeLog(logPath, f"Total Files Scanned : {totalFiles}")
  Logger.writeLog(logPath, f"Duplicate Files Found : {duplicateCount}")
  Logger.writeLog(logPath, f"Duplicate Files Deleted : {deleteCount}")

  Logger.writeLog(logPath, border)
  Logger.writeLog(logPath, "Duplicate Checksums")
  

  for checksum, files in checksumDict.items():

      if len(files) > 1:

          Logger.writeLog(logPath, border)
          Logger.writeLog(logPath, f"Checksum : {checksum}")

          for file in files:
              Logger.writeLog(logPath, file)

  Logger.writeLog(logPath, border)
  Logger.writeLog(logPath, "Deleted Files: ")

  for file in deletedFiles:
      Logger.writeLog(logPath, file)

  Logger.writeLog(logPath, border)

  body = f"""
  Jay Ganesh,

  The duplicate-file removal operation has been completed successfully.

  Operation Statistics

  Starting time of scanning : {startTime}

  Completion time of scanning : {endTime}

  Directory scanned : {directoryPath}

  Total files scanned : {totalFiles}

  Total duplicate files found : {duplicateCount}

  Total duplicate files deleted : {deleteCount}

  Please find the detailed log file attached.

  Regards,

  Marvellous Automation System
  """

  status = MailSender.sendMail(receiver, logPath, body)

  if status:
      Logger.writeLog(logPath, "Email Status: SUCCESS")
      Logger.writeLog(logPath, border)
  else:
      Logger.writeLog(logPath, "Email Status: FAILED")
      Logger.writeLog(logPath, border)
      

def main():

    border = "-" * 65
    print(border)
    print("                      Marvellous Automation Script                ")
    print(border)

    # ---------------- Help / Usage ----------------

    if len(sys.argv) == 2:

        if sys.argv[1] in ("--h", "--help"):
            displayHelp()
            sys.exit()

        elif sys.argv[1] in ("--u", "--usage"):
            displayUsage()
            sys.exit()

        else:
            print("Invalid option.")
            print("Use --help or --h for more information.")
            sys.exit()

    # ---------------- Argument Validation ----------------

    if len(sys.argv) != 4:
        print("Invalid number of arguments.")
        print("Use --help for more information.")
        sys.exit()

    directoryPath = sys.argv[1]
    interval = sys.argv[2]
    receiver = sys.argv[3]

    if not Validator.validateDirectory(directoryPath):
        print("Invalid Directory")
        sys.exit()

    if not Validator.validateInterval(interval):
        print("Invalid Time Interval")
        sys.exit()

    if not Validator.validateEmail(receiver):
        print("Invalid Email Address")
        sys.exit()

    schedule.every(int(interval)).minutes.do(performDuplicateRemoval, directoryPath, receiver)
    print("Script Started")
    print("Press Ctrl + C to Terminate Script")

    while True:
        schedule.run_pending()
        time.sleep(1)

  

if __name__ == "__main__":
    main()