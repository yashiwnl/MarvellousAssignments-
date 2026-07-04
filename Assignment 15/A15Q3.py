
def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  checkOdd = lambda x : x % 2 != 0

  result = list(filter(checkOdd, data))

  print("List of odd numbers: ",result)

if __name__ == "__main__":
  main()