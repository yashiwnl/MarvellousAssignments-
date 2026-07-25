

def main():
  fname = input("Enter the file name: ")
  key = input("Enter the word you want to search: ")
  count = 0
  try:
    fobj = open(fname, "r")

    for line in fobj:
      words = line.split()
      for word in words:
        if word == key:
          count += 1

    print(f"Word {key} appeared {count} times in {fname}")
    fobj.close()
  except FileNotFoundError as e:
    print("File does not exist: ", e)


if __name__ == "__main__":
  main()