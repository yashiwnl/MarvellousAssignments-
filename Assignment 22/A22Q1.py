import multiprocessing 
import os
import time

def square(num):


  print("Process running with PID: ", os.getpid())
  sum = 0

  for i in range(1, num + 1):
    sum = sum + (i **2)

  return sum


def main():
  data = [1000000,2000000,3000000,4000000]

  
  result = list()

  start_time = time.perf_counter()
  pobj = multiprocessing.Pool()
  result = pobj.map(square, data)
  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print(result)
  print(f"time required: {end_time - start_time}")

if __name__ == "__main__":
  main()