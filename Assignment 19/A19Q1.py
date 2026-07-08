

def main():
  num = int(input("Enter a number: "))

  power = lambda x : x**2

  print(f"Power of {num}: {power(num)}")

if __name__ == "__main__":
  main()