import MarvellousNum as mn

def ListPrime(data):
  
  prime = list(filter(mn.chkPrime, data))

  return prime

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  result = ListPrime(data)

  print(f"List of prime numbers in {data} is: {result}")
  

if __name__ == "__main__":
  main()
