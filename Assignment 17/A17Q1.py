import Arithmetic as ar

def calc(num1, num2, op):
  
  if op == "+":
    print(f"Addition of {num1} and {num2} is: {ar.Add(num1,num2)} ")
  elif op == "-":
    print(f"Subtraction of {num1} and {num2} is: {ar.Sub(num1,num2)} ")
  elif op == "*":
    print(f"Multiplication of {num1} and {num2} is: {ar.Mult(num1,num2)} ")
  elif op == "/":
    print(f"Division of {num1} and {num2} is: {ar.Div(num1,num2)} ")
  else:
    print("Invalid Operator")


def main():
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  op = input("Enter the operation (+,=,*,/): ")
  calc(num1, num2, op)

if __name__ == "__main__":
  main()


