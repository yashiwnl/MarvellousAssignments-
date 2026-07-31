import ProcessUtils
import sys
import Logger
import Validator
def main():

  dirName = sys.argv[1]

  if not Validator.validateDirectory(dirName):
    print("Invalid Directory")
    sys.exit()
  logPath = Logger.createLogFile(dirName)
  ProcessUtils.logAllProcesses(logPath)

if __name__ == "__main__":
  main()