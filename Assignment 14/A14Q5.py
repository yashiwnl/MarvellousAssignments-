
def main():
  num = int(input("Enter a number: "))

  checkEven = lambda x : x % 2 == 0

  print(checkEven(num))


if __name__ == "__main__":
  main()