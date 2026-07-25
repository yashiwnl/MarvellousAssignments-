import schedule 
import datetime
import time

def display():
  current =  datetime.datetime.now()
  formatted = current.strftime("%d-%m-%Y %I:%M:%S %p")
  print("Current Date and Time: ", formatted)     

def main():

  schedule.every(1).minute.do(display)
  
  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()