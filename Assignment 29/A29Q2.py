import os

def main():
  fname = input("Enter the file name: ")

  try:
    fobj = open(fname, "r")
    data = fobj.read()
    print(f"contents of {fname} : ")
    print(data)
    fobj.close()
  except FileNotFoundError as e:
    print("File does not exist: ", e)


if __name__ == "__main__":
  main()