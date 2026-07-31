import psutil
import Logger

def DisplayAllProcesses():

  for process in psutil.process_iter(['pid', 'name', 'username']):

    try:
      print("-"*65)
      print(f"Name: {process.info['name']} ")
      print(f"PID: {process.info['pid']} ")
      print(f"Username: {process.info['username']} ")
      print("-"*65)
    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess): 
      pass

def displaySpecificProcesses(pname):

  found = False
    
  for process in psutil.process_iter(['pid', 'name', 'username']):

    try:
      if pname.lower() ==  str.lower(process.info['name']):
        print(f"Name: {process.info['name']} ")
        print(f"PID: {process.info['pid']} ")
        print(f"Username: {process.info['username']} ")
        found = True

    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess): 
      pass

  if not found:
    print("Process not found")

def logAllProcesses(logPath):

  processCount = 0

  for process in psutil.process_iter(['pid', 'name', 'username']):

    try:
      name = process.info['name'] or "N/A"
      username = process.info['username'] or "N/A"
      pid = process.info['pid']
      processCount += 1

      Logger.writeLog(logPath, f"-"*65)
      Logger.writeLog(logPath, f"Name: {name}")
      Logger.writeLog(logPath, f"PID: {pid}")
      Logger.writeLog(logPath, f"Username: {username}")
      Logger.writeLog(logPath, f"-"*65)

    except (psutil.AccessDenied, psutil.NoSuchProcess, psutil.ZombieProcess) as e: 
      Logger.writeLog(logPath, f"Skipped Process: {e} ")

  return processCount
