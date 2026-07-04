from functools import reduce

def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  add = lambda x, y: x + y

  result = reduce(add, data)

  print("addition of entered numbers :",result)


if __name__ == "__main__":
  main()