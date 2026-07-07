def factorial(num):
  fact = 1

  for i in range(1, num + 1):
    fact = fact * i
  
  return fact


def main():
  num = int(input("Enter a number: "))
  result = factorial(num)
  print(f"factorial of {num} is: {result}")

if __name__ == "__main__":
  main()