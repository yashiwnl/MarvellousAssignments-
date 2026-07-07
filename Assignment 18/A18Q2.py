from functools import reduce

def maxElement(data):
  
  max = lambda x, y: x if x > y else y

  result = reduce(max, data)

  return result

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))

  result = maxElement(data)
  print("Maximum Element: ", result)

if __name__ == "__main__":
  main()
