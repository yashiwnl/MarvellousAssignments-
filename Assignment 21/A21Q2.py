import threading
from functools import reduce

def findMax(data):
  max = lambda x,y: x if x > y else y
  rData = reduce(max, data)
  print(f" maximum element from {data} : {rData}")

def findMin(data):
  min = lambda x,y: x if x < y else y
  rData = reduce(min, data)
  print(f" minimum element from {data} : {rData}")
  



def main():

  data = list()

  n = int(input("Enter the number of elements you want to insert in the list: "))

  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  t1 = threading.Thread(target= findMax, args= (data,))
  t2 = threading.Thread(target= findMin, args= (data,))

  t1.start()
  t2.start()

  t1.join()
  t2.join()

if __name__ == "__main__":
  main()