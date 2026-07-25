import schedule 
import time
import shutil
import os

def copy_files(fname, dest):
  timestamp = time.ctime()
  filename, extension = os.path.splitext(fname)
  filename = os.path.basename(filename)
  backup_fname = filename + timestamp + extension
  backup_fname = backup_fname.replace(" ", "_")
  backup_fname = backup_fname.replace(":", "_")

  destination_path = os.path.join(dest, backup_fname)

  shutil.copy(fname, destination_path)

  lfobj = open("backup_log.txt", "a")

  lfobj.write("Backup Completed sucessfully at: " + str(timestamp) + "\n")
  lfobj.close()

  
def main():

  fname = input("Enter the file name")
  dest = input("Enter the destination directory")
  schedule.every(1).hour.do(copy_files, fname,dest)

  while True:
    schedule.run_pending()

if __name__ == "__main__":
  main()