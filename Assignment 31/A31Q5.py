import os
import schedule
import time
import datetime
def FileCounter(directoryPath):

  total_files = 0
  for folder_name, sub_folder,file_name in os.walk(directoryPath):

    for fname in file_name:
      total_files += 1


  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
  lfobj = open("DirectoryCountLog.txt", "a")
  lfobj.write("Directory Path: " + str(os.path.abspath(directoryPath)) + "\n")
  lfobj.write("No of files: " + str(total_files) + "\n")
  lfobj.write("Creation date and time: " + str(timestamp) +  "\n")
  lfobj.close()

def main():
  directoryPath = input("Enter the directory path: ")
  schedule.every(5).minute.do(FileCounter, directoryPath)

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()