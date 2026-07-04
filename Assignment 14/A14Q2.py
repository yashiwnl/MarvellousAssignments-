
def main():
  num = int(input("Enter a number: "))
  cube = lambda x: (x * x *x)
  result = cube(num)
  print("Cube of entered number: ",result)



if __name__ == "__main__":
  main()