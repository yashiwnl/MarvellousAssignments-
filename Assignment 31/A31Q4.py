import schedule
import time
import datetime
def LogFileCreator():

  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
  log_file_name = "MarvellousLog%s.txt"%timestamp
  log_file_name = log_file_name.replace(" ","_")
  log_file_name = log_file_name.replace(":","_")

  lfobj = open(log_file_name, "w")
  lfobj.write("Log File created Successfully \n")
  lfobj.write("Creation time: " + str(timestamp) +  "\n")
  lfobj.close()


def main():
  schedule.every(1).minute.do(LogFileCreator)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()