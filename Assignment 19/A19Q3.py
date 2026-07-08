from functools import reduce

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  greater = lambda x : x >= 70
  increment = lambda x : x + 10
  product = lambda x,y : x * y

  fData = list(filter(greater, data))
  mData = list(map(increment, fData))
  rData = reduce(product, mData)

  print(f"List after filter: {fData} ")
  print(f"List after map: {mData}")
  print(f"List after reduce: {rData}")
  

if __name__ == "__main__":
  main()
