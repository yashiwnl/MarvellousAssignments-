import schedule
import time
import datetime
import sys
import os
def FileMonitor(fname):

  if not os.path.exists(fname):
    print("File doesnt exist in current directory")
  else:
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
    fsize = os.path.getsize(fname)
    lfobj = open("FileSizeLog.txt", "a")
    lfobj.write("File size: " + str(fsize) + "\n")
    lfobj.write("Creation date and time: " + str(timestamp) +  "\n")
    lfobj.close()


def main():
  schedule.every(30).seconds.do(FileMonitor, sys.argv[1])

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()