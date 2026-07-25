def main():
  fname = input("Enter the input file name: ")
  key = input("Enter the word you want to search: ")
  try: 
    fobj = open(fname, "r")
    found = False

    for line in fobj:
       words = line.split()

       for word in words:
        if word == key:
          found = True 
          break      
        
    if found:
      print(f"Entered word {key} is present in {fname}")
    else:
      print(f"Entered word {key} is not present in {fname}")

       
    fobj.close()
  except FileNotFoundError:
    print("File not present in current directory")
      
if __name__ == "__main__":
    main()