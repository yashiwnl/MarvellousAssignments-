def chkNum(num):
  
  return (num % 5 == 0) 
  

def main():
  num = int(input("Enter a number: "))
  result = chkNum(num)
  
  if(result):
    print("Divisible by 5")
  else:
    print("Not Divisible by 5")



if __name__ == "__main__":
  main()