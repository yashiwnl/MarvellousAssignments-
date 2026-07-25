import os
import schedule
import time
import sys
def directoryScanner(directoryPath):

  total_files = 0
  sub_folders = 0
  for folder_name, sub_folder, file_name in os.walk(directoryPath):

    for fname in file_name:
      total_files += 1

    for subfname in sub_folder:
      sub_folders += 1
      

  print("Directory Scanned: ",os.path.abspath(directoryPath))
  print("Total Files: ", total_files)
  print("Total Subdirectories: ", sub_folders)
  print("Scan time: ", time.ctime() )




def main():
  schedule.every(1).minute.do(directoryScanner, sys.argv[1])

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()