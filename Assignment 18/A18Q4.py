
def findElement(data, key):
  
  count = 0

  for i in data:
    if key == i:
      count = count + 1
  
  return count

def main():

  n = int(input("Enter the number of elements you want to insert: "))
  data = list()
  print("Enter the elements: ")
  for i in range(n):
    data.append(int(input(f"Element {i}: ")))
  
  key = int(input("Enter the element you want to search: "))

  result = findElement(data, key)
  print(f"Frequency of {key} in {data} is  : ", result)

if __name__ == "__main__":
  main()
