def chkPrime(num):
  
  isPrime = True

  if num < 2:
    isPrime = False

  for i in range(2, num):
    if (num % i == 0):
      isPrime = False
      break
  
  return isPrime  

def main():
  num = int(input("Enter a number: "))
  result = chkPrime(num)
  
  if(result):
    print(f"Entered number {num} is a Prime Number")
  else:
    print(f"Entered number {num} is not a Prime Number")


if __name__ == "__main__":
  main()