import os
import hashlib

def getAllFiles(path):

  fileList = []
  for folder_name, sub_folder, file_name in os.walk(path):

    for fname in file_name:
      fname = os.path.join(folder_name, fname)
      fileList.append(fname)

  return fileList

def calculateChecksum(file): 

  fobj = open(file, "rb")
  hobj = hashlib.md5()

  buffer = fobj.read(1024)

  while len(buffer) > 0:
    hobj.update(buffer)
    buffer = fobj.read(1024)

  fobj.close()

  return hobj.hexdigest()

def findDuplicates(fileList):

  checksumDict = {}
  for file in fileList:
    checksum = calculateChecksum(file)

    if checksum in checksumDict:
      checksumDict[checksum].append(file)
    else:
      checksumDict[checksum] = [file]

  return checksumDict

def deleteDuplicates(checksumDict):

  duplicates = list(filter(lambda x: len(x) > 1, checksumDict.values()))
  deleteCount = 0
  deletedFiles = []
  failedFiles = []
  for files in duplicates:
    for file in files[1:]:
      try:
        os.remove(file)
        deleteCount += 1
        deletedFiles.append(file)
      except Exception as e:
        failedFiles.append(file)

  return deleteCount, deletedFiles

    

    