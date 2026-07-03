
def main():
  num = int(input("Enter a number: "))
  temp = num
  reverse = 0

  while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
  
  if(reverse == temp):
    print("Entered number is palindrome")
  else:
    print("Entered number is not palindrome")


if __name__ == "__main__":
  main()