import threading

def displayNumbers():

  for i in range(1, 51):
    print(i)

def displayReverseNumbers():

  for i in range(50, 0, -1):
    print(i)

def main():
  Thread1 = threading.Thread(target= displayNumbers)
  Thread2 = threading.Thread(target= displayReverseNumbers)

  Thread1.start()
  Thread1.join()

  print()
  Thread2.start()
  Thread2.join()

if __name__ == "__main__":
  main()