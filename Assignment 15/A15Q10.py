from functools import reduce

def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))

  checkEven = lambda x : x % 2 == 0

  result = list(filter(checkEven, data))

  print("Number of even numbers in list:", len(result),", list:", result)

if __name__ == "__main__":
  main()