import schedule
import time

def monday_work():
  print("Start your weekly goals")


def wednesday_work():
  print("Review your weekly progress")


def friday_work():
  print("Weekly work completed")

def main():
  schedule.every().monday.at("09:00").do(monday_work)
  schedule.every().wednesday.at("17:00").do(wednesday_work)
  schedule.every().friday.at("18:00").do(friday_work)

  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
  main()