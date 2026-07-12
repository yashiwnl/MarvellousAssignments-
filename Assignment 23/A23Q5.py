import multiprocessing 
import os
import time
def factorial(num):

  print("Process running with PID: ", os.getpid())
  print("Input data: ", num)

  fact = 1

  for i in range(1, num + 1):
    fact = fact * i

  return fact


def main():
  data = [10,15,20,25]

  
  result = list()

  start_time = time.perf_counter()
  pobj = multiprocessing.Pool()
  result = pobj.map(factorial, data)
  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("Factorial: ",result)
  print(f"time required: {end_time - start_time}")

if __name__ == "__main__":
  main()