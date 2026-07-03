
def main():
  num = int(input("Enter a number: "))
  total = 0

  for i in range(1, num + 1):
    total = total + i

  print("Sum of first N natural numbers: ",total)

if __name__ == "__main__":
  main()