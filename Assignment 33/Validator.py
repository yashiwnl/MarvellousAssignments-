import os

def validateDirectory(path):
  if not os.path.exists(path):
    return False

  if not os.path.isdir(path):
    return False

  if not os.path.isabs(path):
    return False

  if not os.access(path, os.R_OK):
    return False  

  return True

def validateInterval(interval):

  if not interval.isnumeric():
    return False

  interval = int(interval)  

  if interval <= 0:
    return False

  return True

def validateEmail(email):

  if email.count("@") != 1:
    return False

  email_parts = email.split("@")

  if email_parts[0] == "":
    return False

  if email_parts[1].count(".") < 1:
    return False

  return True

