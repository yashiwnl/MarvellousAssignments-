def main():
  count = 0
  fname = input("Enter the input file name: ")
  print(fname)
  try: 
    fobj = open(fname, "r")

    for line in fobj:
          count += 1

    print(f"No of lines in Demo.txt: {count} ")
    fobj.close()
  except FileNotFoundError:
    print("File not present in current directory")
      
if __name__ == "__main__":
    main()