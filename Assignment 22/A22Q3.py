import multiprocessing 
import os
import time
from functools import reduce

def checkPrime(num):
  
  isPrime = True

  if num < 2:
    isPrime = False

  for i in range(2, num):

    if(num % i == 0):
      isPrime = False
      break

  return isPrime

def countPrime(num):

  print("Process running with PID: ", os.getpid())

  primeCount = 0

  for i in range(num):

    if(checkPrime(i)):
      primeCount += 1

  return primeCount

    

def main():
  data = [10000, 20000, 30000, 40000]

  
  result = list()

  start_time = time.perf_counter()
  pobj = multiprocessing.Pool()
  result = pobj.map(countPrime, data)
  pobj.close()
  pobj.join()

  end_time = time.perf_counter()

  print(result)
  print(f"time required: {end_time - start_time}")

if __name__ == "__main__":
  main()