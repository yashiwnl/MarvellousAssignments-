
def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  smallest = lambda x, y : x < y
  
  if(smallest(num1, num2)):
    print("Number 1 is smallest: ",num1)
  else:
    print("Number 2 is smallest: ",num2)


if __name__ == "__main__":
  main()