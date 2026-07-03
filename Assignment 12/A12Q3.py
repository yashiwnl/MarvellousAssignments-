def calculate(num1, num2):
  return num1 + num2,num1 - num2,num1 * num2,num1 / num2

def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  add,sub,mul,div = calculate(num1,num2)
  print("Addition:",add)
  print("Subtraction:",sub)
  print("Multiplication:",mul)
  print("Division:",div)
    
if __name__ == "__main__":
  main()