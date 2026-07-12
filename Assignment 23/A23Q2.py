import multiprocessing 
import os
import time

def count(num):


  print("Process running with PID: ", os.getpid())
  sum = 0

  for i in range(1, num + 1):
    
    if i % 2 != 0:
      sum = sum + i
      
  return sum


def main():
  data = [1000000,2000000,3000000,4000000]

  
  result = list()

  start_time = time.perf_counter()
  pobj = multiprocessing.Pool()
  result = pobj.map(count, data)
  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print("Sum of odd numbers: ",result)
  print(f"time required: {end_time - start_time}")

if __name__ == "__main__":
  main()