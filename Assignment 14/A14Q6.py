
def main():
  num = int(input("Enter a number: "))

  checkOdd = lambda x : x % 2 != 0

  print(checkOdd(num))


if __name__ == "__main__":
  main()