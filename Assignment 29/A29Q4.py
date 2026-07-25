import os

def main():
  fname1 = input("Enter the first file name: ")
  fname2 = input("Enter the second file name: ")

  try:
    fobj1 = open(fname1, "r")
    fobj2 = open(fname2, "r")
    data1 = fobj1.read()
    data2 = fobj2.read()

    if data1 == data2:
      print("Success, Both files are same")
    else:
      print("Faliure, Both files are not same")

    fobj1.close()
    fobj2.close()
  except FileNotFoundError as e:
    print("File does not exist: ", e)


if __name__ == "__main__":
  main()