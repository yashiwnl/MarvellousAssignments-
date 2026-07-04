from functools import reduce

def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  greatest = lambda x, y:  x if x > y else y

  result = reduce(greatest, data)

  print("greatest number from entered numbers :",result)


if __name__ == "__main__":
  main()