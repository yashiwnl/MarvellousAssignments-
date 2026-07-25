def main():
  
  fname1 = input("Enter the input file name: ")
  fname2 = input("Enter the output file name: ")

  try: 
    fobj1 = open(fname1, "r")
    fobj2 = open(fname2, "w")

    data = fobj1.read()
    fobj2.write(data)
    print("File Copied sucessfully")
  except FileNotFoundError:
    print("File not present in current directory")
      
if __name__ == "__main__":
    main()