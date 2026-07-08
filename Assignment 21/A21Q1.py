import threading

def checkPrime(num):
  
  isPrime = True

  if num < 2 : 
    isPrime = False

  for i in range(2, num):
    if num % i == 0:
      isPrime = False
      break
  return isPrime



def findPrime(data):

  print(f"List of prime numbers: {list(filter(checkPrime, data))} ")

def findNonPrime(data):

  print(f"List of non prime numbers: {list(filter( lambda x : not checkPrime(x), data))}")

def main():
  Prime = threading.Thread(target= findPrime, args= ([21,22,7,30,11,8,2,1,50],))
  NonPrime = threading.Thread(target= findNonPrime, args= ([21,22,7,30,11,8,2,1,50],))

  Prime.start()
  NonPrime.start()

  Prime.join()
  NonPrime.join()

if __name__ == "__main__":
  main()