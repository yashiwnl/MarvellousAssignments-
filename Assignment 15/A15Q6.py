from functools import reduce

def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  smallest = lambda x, y:  x if x < y else y

  result = reduce(smallest, data)

  print("smallest number from entered numbers :",result)


if __name__ == "__main__":
  main()