from functools import reduce

def main():
  n = int(input("Enter count of strings you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(input())
  
  greatest = lambda x : len(x) > 5

  result = list(filter(greatest, data))

  print("List of stings whose length is greater than 5: ", result)


if __name__ == "__main__":
  main()