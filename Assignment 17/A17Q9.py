def chkLength(num):
    length = 0

    if num == 0:
       length = 1
    
    while num > 0:
       length = length + 1
       num //= 10 
    
    return length
def main():
  num = int(input("Enter a number: "))
  result = chkLength(num)
  print(f"Length of {num} is: {result}")

if __name__ == "__main__":
  main()