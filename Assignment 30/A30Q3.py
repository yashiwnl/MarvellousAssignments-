import schedule 
import datetime
import time

def display():
  print("Coding Kar..!")

def main():

  schedule.every(30).minutes.do(display)
  
  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()