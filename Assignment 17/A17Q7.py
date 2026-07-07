def printPattern(num):

  for i in range(num):
    for j in range(1, num + 1):
      print(j, end= " ")
    print()


def main():
  num = int(input("Enter a number: "))
  printPattern(num)


if __name__ == "__main__":
  main()