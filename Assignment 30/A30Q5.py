import schedule 
import datetime
import time

def display():

  fobj = open("Marvellous.txt", "a")
  current =  datetime.datetime.now()
  formatted = current.strftime("%d-%m-%Y %I:%M:%S %p")

  fobj.write("Task Executed at: " + str(formatted) + "\n")
  fobj.close()
def main():

  schedule.every(5).minutes.do(display)
  
  while True:
    schedule.run_pending()
    time.sleep(5)

if __name__ == "__main__":
  main()