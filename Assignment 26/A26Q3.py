class Arithmetic:
  def __init__(self):
    self.value1 = 0
    self.value2 = 0
  
  def Accept(self):
    self.value1 = int(input("Enter the first value: "))
    self.value2 = int(input("Enter the second value: "))

  def Addition(self):
    return self.value1 + self.value2

  def Subtraction(self):
    return self.value1 - self.value2

  def Multiplication(self):
    return self.value1 * self.value2

  def Division(self):
    return self.value1 / self.value2



def main():
  obj1 = Arithmetic()
  obj1.Accept()

  add = obj1.Addition()
  sub = obj1.Subtraction()
  mul = obj1.Multiplication()
  div = obj1.Division()

  print(f"Addition: {add} ")
  print(f"Subtraction: {sub} ")
  print(f"Multiplication: {mul} ")
  print(f"Division: {div} ")


  obj2 = Arithmetic()
  obj2.Accept()

  add = obj2.Addition()
  sub = obj2.Subtraction()
  mul = obj2.Multiplication()
  div = obj2.Division()

  print(f"Addition: {add} ")
  print(f"Subtraction: {sub} ")
  print(f"Multiplication: {mul} ")
  print(f"Division: {div} ")


if __name__ == "__main__":
  main()