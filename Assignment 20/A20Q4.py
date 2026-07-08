import threading

def findUpper(string):

  print(f"ID of Capital thread: {threading.get_ident()}")
  print(f"Name of Capital thread: {threading.current_thread()}")


  count = 0
  for ch in string:
    if ch.isupper():
      count = count + 1
  print(f"number of uppercase characters in {string} are: {count}")

def findLower(string):

  print(f"ID of Small thread: {threading.get_ident()}")
  print(f"Name of Small thread: {threading.current_thread()}")

  count = 0
  for ch in string:
    if ch.islower():
      count = count + 1
  print(f"number of lowercase characters in {string} are: {count}")

def findNumber(string):

  print(f"ID of Digit thread: {threading.get_ident()}")
  print(f"Name of Digit thread: {threading.current_thread()}")

  count = 0
  for ch in string:
    if ch.isnumeric():
      count = count + 1
  print(f"number of numbers in {string} are: {count}")

def main():
  
  Small = threading.Thread(target=findLower, args= ("1AaZ2321WQfqsqE",))
  Capital = threading.Thread(target=findUpper, args= ("1AaZ2321WQfqsqE",))
  Digits = threading.Thread(target=findNumber, args= ("1AaZ2321WQfqsqE",))

  Small.start()
  Capital.start()
  Digits.start()

  Small.join()
  Capital.join()
  Digits.join()


if __name__ == "__main__":
  main()