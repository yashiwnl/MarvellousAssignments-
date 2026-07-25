import os

def main():
  fname = input("Enter the input file name: ")


  try:
    rfobj = open(fname, "r")
    wfobj = open("demo.txt", "w")
    data = rfobj.read()
    wfobj.write(data)
    print(f"Contents of {fname} copied succesfully into demo.txt ")
    rfobj.close()
    wfobj.close()

  except FileNotFoundError as e:
    print("File does not exist: ", e)


if __name__ == "__main__":
  main()