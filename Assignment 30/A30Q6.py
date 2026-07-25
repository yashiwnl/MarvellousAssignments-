import schedule 
import time

def displayLunch():
  print("Lunch Time")

def displayWrapup():
  print("Wrap up work")

def main():

  schedule.every().day.at("13:00").do(displayLunch)
  schedule.every().day.at("18:00").do(displayWrapup)

  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()