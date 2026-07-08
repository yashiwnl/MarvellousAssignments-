import threading

counter = 0
lock = threading.Lock()

def increment():

  for i in range(1000):
    lock.acquire()
    global counter
    counter = counter + 1
    lock.release()

def main():
  t1 = threading.Thread(target=increment)
  t2 = threading.Thread(target=increment)
  t3 = threading.Thread(target=increment)

  t1.start()
  t2.start()
  t3.start()

  t1.join()
  t2.join()
  t3.join()

  global counter
  print(counter)

if __name__ == "__main__":
  main()