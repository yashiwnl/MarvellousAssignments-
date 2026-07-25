def main():
  fname = input("Enter the input file name: ")
  try: 
    fobj = open(fname, "r")

    for line in fobj:
        print(line, end="")

    fobj.close()
  except FileNotFoundError:
    print("File not present in current directory")
      
if __name__ == "__main__":
    main()