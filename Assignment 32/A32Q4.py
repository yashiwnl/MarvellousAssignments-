import os
import schedule
import datetime
import shutil
import time

def copyTextFiles(src,dest):

  if not os.path.isdir(src) or not os.path.isdir(dest):
      print("Invalid Directores, please enter correct directories")
      return

  lfobj = open("Marvellous_CopyLog.txt", "a")
  timestamp = datetime.datetime.now()
  timestamp = timestamp.strftime("%d-%m-%Y %I:%M:%S %p")
  lfobj.write("Log created at: " + timestamp + "\n")

  for folder_name, sub_folder, file_name in os.walk(src):
     for fname in file_name:
        if fname.endswith(".txt"):
           fname = os.path.join(folder_name, fname)
           destination = os.path.join(dest, os.path.basename(fname))

           try:
            shutil.copy(fname, destination)
            lfobj.write(str(os.path.basename(fname)) + " copied successfully to: " + str(destination) + "\n")
           except IOError as e:
              print("Error ocurred during copying: ",e )
              lfobj.write("couldnt copy: " + str(os.path.basename(fname)) + "to: " + str(destination) + "\n")

  lfobj.close()

def main():

  src = input("Enter source directory")
  dest = input("Enter destination directory")

  schedule.every(10).minutes.do(copyTextFiles, src, dest)

  while True:
     schedule.run_pending()
     time.sleep(1)

if __name__ == "__main__":
  main()