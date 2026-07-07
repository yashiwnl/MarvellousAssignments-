def Add(num1, num2):
  return num1 + num2

def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  total = Add(num1,num2)

  print(f"Addition is: {total}")

  

if __name__ == "__main__":
  main()