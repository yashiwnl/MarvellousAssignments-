
def main():
  num = int(input("Enter a number: "))
  binary = 0
  place = 1

  while(num > 0):
    remainder = num % 2
    binary = binary +  (remainder * place)
    place = place * 10
    num = num // 2

  print(binary)

if __name__ == "__main__":
  main()