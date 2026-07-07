def chkNum(num):
  
  if(num == 0):
    print("Zero")
  elif(num < 0):
    print("Negative Number")
  else:
    print("Positive Number")

  

def main():
  num = int(input("Enter a number: "))
  chkNum(num)


if __name__ == "__main__":
  main()