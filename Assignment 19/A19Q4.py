from functools import reduce

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  even = lambda x : x % 2 == 0
  square = lambda x : x * x
  addition = lambda x,y : x + y

  fData = list(filter(even, data))
  mData = list(map(square, fData))
  rData = reduce(addition, mData)

  print(f"List after filter: {fData} ")
  print(f"List after map: {mData}")
  print(f"List after reduce: {rData}")
  

if __name__ == "__main__":
  main()
