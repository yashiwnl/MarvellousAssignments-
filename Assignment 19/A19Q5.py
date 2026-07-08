from functools import reduce

def checkPrime(num):

  isPrime = True

  if num < 2:
    isPrime = False

  for i in range(2, num):
    if (num % i == 0):
      isPrime = False
      break
  
  return isPrime

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  multiply = lambda x : x * 2
  maximum = lambda x,y : x if x > y else y

  fData = list(filter(checkPrime, data))
  mData = list(map(multiply, fData))
  rData = reduce(maximum, mData)

  print(f"List after filter: {fData} ")
  print(f"List after map: {mData}")
  print(f"List after reduce: {rData}")
  
  
if __name__ == "__main__":
  main()
