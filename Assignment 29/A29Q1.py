import os

def main():
  fname = input("Enter the file name: ")

  if os.path.exists(fname):
    print(f"{fname} exists in current directory")
  else:
    print(f"{fname} does not  exist in current directory")
    


if __name__ == "__main__":
  main()