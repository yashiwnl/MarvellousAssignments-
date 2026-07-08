import threading
from functools import reduce

sumResult = 0
productResult = 0

def calculateSum(data):
  add = lambda x,y: x + y
  rData = reduce(add, data)
  global sumResult
  sumResult = rData #return value gets deleted so stored in a global variable


def calculateProduct(data):
  mul = lambda x,y: x * y
  rData = reduce(mul, data)
  global productResult
  productResult = rData #return value gets deleted so stored in a global variable
  

def main():

  data = list()

  n = int(input("Enter the number of elements you want to insert in the list: "))

  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  t1 = threading.Thread(target= calculateSum, args= (data,))
  t2 = threading.Thread(target= calculateProduct, args= (data,))

  t1.start()
  t2.start()

  t1.join()
  t2.join()

  global sumResult
  global productResult

  print(f"Sum of all elements : {sumResult}, Product of all elements {productResult} ")

if __name__ == "__main__":
  main()