
def main():
  n = int(input("Enter count of numbers you want to enter: "))
  data = list()

  for i in range(0, n):
    data.append(int(input()))
  
  divisible = lambda x : x % 3 == 0 and x % 5 == 0

  result = list(filter(divisible, data))

  print("List of numbers divisible by 3 and 5: ",result)

if __name__ == "__main__":
  main()