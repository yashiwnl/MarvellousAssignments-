import os
import schedule
import datetime
import shutil
import time

def deleteEmptyFiles(src):

  if not os.path.exists(src):
    print("Entered path does not exists")
    return

  if not os.path.isdir(src):
    print("Invalid Directory, please enter correct directory")
    return

  lfobj = open("Marvellous_DeleteLog.txt", "a")
  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
  lfobj.write("Log created at: " + timestamp + "\n\n")

  for folder_name, sub_folder, file_name in os.walk(src):
    for fname in file_name:
      fname = os.path.join(folder_name, fname)
      if os.path.getsize(fname) == 0:
        try:
          os.remove(fname)
          lfobj.write("Deleted file: " + str(fname) + "\n")
        except PermissionError as e:
          print("Cannot delete, Permission Error: ", e)
          lfobj.write("Cannot delete file: " + str(fname) + "\n")

                  
  lfobj.close()

def main():

  src = input("Enter source directory: ")
  schedule.every(1).hour.do(deleteEmptyFiles, src)

  while True:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
  main()