import schedule
import time
import datetime
def FileCreator():

  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
  file_name = "File%s.txt"%timestamp
  file_name = file_name.replace(" ","_")
  file_name = file_name.replace(":","_")

  fobj = open(file_name, "w")
  fobj.write("File Name: " + str(file_name) + "\n")
  fobj.write("Creation date and time: " + str(timestamp) +  "\n")
  fobj.close()


def main():
  schedule.every(1).minute.do(FileCreator)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()