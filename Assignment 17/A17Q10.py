def chkLength(num):
    sum = 0

    while num > 0:
      last = num % 10
      sum = sum + last
      num = num // 10   
    
    return sum
def main():
  num = int(input("Enter a number: "))
  result = chkLength(num)
  print(f"Addition of numbers in {num} is: {result}")

if __name__ == "__main__":
  main()