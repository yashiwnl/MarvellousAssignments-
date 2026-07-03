
def main():
  num = int(input("Enter a number: "))

  isPrime = num >= 2

  for i in range(2, num):
    if(num % i == 0):
      isPrime = False
    
  if(isPrime):
    print("Entered number is a prime number")
  else:
    print("Entered number is not a prime number")


if __name__ == "__main__":
  main()