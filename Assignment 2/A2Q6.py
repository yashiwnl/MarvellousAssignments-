num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("What action you want to perform (+,-,/,*): ")

if operation == "+":
  print("Output: ",num1 + num2)
elif operation == "-":
  print("Output: ",num1 - num2)
elif operation == "/":
  print("Output: ",num1 / num2)
elif operation == "*":
  print("Output: ",num1 * num2)
else:
  print("Invalid Operation, try again")