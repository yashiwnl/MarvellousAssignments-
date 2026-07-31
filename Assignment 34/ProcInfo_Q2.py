import ProcessUtils
import sys
import Validator

def main():

  pname = sys.argv[1]

  if not Validator.validateProcessName(pname):
    print("Invalid Process")
    sys.exit()
    
  ProcessUtils.displaySpecificProcesses(pname)

if __name__ == "__main__":
  main