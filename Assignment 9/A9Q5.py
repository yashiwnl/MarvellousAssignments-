
def main():
  num = int(input("Enter a number: "))

  if(num % 3 == 0 and num % 5 == 0):
    print("Entered number is divisible by 3 and 5")
  else:
    print("Entered number is not divisible by 3 and 5")



if __name__ == "__main__":
  main()