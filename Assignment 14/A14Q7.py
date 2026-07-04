
def main():
  num = int(input("Enter a number: "))

  divisible = lambda x : x % 5 == 0

  print(divisible(num))


if __name__ == "__main__":
  main()