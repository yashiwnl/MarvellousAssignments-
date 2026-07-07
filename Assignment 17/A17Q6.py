def printPattern(num):

  for i in range(num):
    for j in range(num - i, 0, -1):
      print("*", end= " ")
    print()


def main():
  num = int(input("Enter a number: "))
  printPattern(num)


if __name__ == "__main__":
  main()