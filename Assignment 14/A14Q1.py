
def main():
  num = int(input("Enter a number: "))
  square = lambda x: x * x
  result = square(num)
  print("Square of entered number: ",result)



if __name__ == "__main__":
  main()