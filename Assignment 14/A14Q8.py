
def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  add = lambda x, y : x + y

  print("Addition: ",add(num1, num2))

if __name__ == "__main__":
  main()