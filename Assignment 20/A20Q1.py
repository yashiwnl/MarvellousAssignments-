import threading

def firstEven():

  for i in range(1, 11):
    if (i % 2 == 0):
      print((f"Even: {i}"))


def firstOdd():

  for i in range(1, 11):
    if (i % 2 != 0):
      print((f"Odd: {i}"))

def main():
  t1 = threading.Thread(target= firstEven)
  t2 = threading.Thread(target= firstOdd)

  t1.start()
  t1.join()

  t2.start()
  t2.join()

if __name__ == "__main__":
  main()