from functools import reduce

def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  mul = lambda x, y: x * y

  result = reduce(mul, data)

  print("product of entered numbers :",result)


if __name__ == "__main__":
  main()