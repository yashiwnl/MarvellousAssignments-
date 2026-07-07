from functools import reduce

def addElements(data):
  
  add = lambda x, y: x + y

  result = reduce(add, data)
  return result

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  result = addElements(data)
  print("Addition of elements: ", result)

if __name__ == "__main__":
  main()
