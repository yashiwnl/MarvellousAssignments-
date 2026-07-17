class Circle:
  PI = 3.14

  def __init__(self):
    self.radius = 0.0
    self.area = 0.0
    self.circumference = 0.0

  def Accept(self):
    self.radius = int(input("Enter the radius of circle: "))

  def CalculateArea(self):
    self.area = self.PI * self.radius * self.radius
  
  def CalculateCircumference(self):
    self.circumference = 2 * self.PI * self.radius

  def Display(self):
    print(f"Radius: {self.radius}")
    print(f"Area: {self.area:.4f}")
    print(f"Circumference: {self.circumference:.4f}")


def main():
 obj1 = Circle()

 obj1.Accept()
 obj1.CalculateArea()
 obj1.CalculateCircumference()
 obj1.Display()


 obj2 = Circle()

 obj2.Accept()
 obj2.CalculateArea()
 obj2.CalculateCircumference()
 obj2.Display()



if __name__ == "__main__":
  main()