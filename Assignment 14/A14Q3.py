
def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  greatest = lambda x, y : x > y
  
  if(greatest(num1, num2)):
    print("Number 1 is greatest: ",num1)
  else:
    print("Number 2 is greatest: ",num2)


if __name__ == "__main__":
  main()