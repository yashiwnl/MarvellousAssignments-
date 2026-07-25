import schedule
import sys
import os
import time
def FileReader(fname):
  fobj = open(fname, "r")

  if not os.path.exists(fname):
    print("File doesnt exits in current directory")
  elif os.path.getsize(fname) == 0:
    print("File is empty, cannot read")
  else:
    try:
      fobj.open(fname, "r")
      data = fobj.read()
      print(data)
    except PermissionError:
      print("Cannot read, permission denied")
    except IOError:
      print("Cannot read, file cannot be opened")

def main():
  schedule.every(1).minute.do(FileReader, sys.argv[1])

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()