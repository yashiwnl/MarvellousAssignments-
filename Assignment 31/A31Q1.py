import schedule
import time

def display(message):
  print(message)

def main():
  message = input("Enter a message: ")
  interval = int(input("Enter the interval: "))

  schedule.every(interval).seconds.do(display, message)  

  while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == "__main__":
  main()
