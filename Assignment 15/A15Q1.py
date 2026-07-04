
def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  square = lambda x : x * x

  result = list(map(square, data))

  print("Square of entered numbers: ",result)

if __name__ == "__main__":
  main()