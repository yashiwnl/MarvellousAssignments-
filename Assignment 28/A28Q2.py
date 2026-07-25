def main():
  wordCount = 0
  fname = input("Enter the input file name: ")

  try: 
    fobj = open(fname, "r")

    for line in fobj:
          words = len(line.split())
          wordCount = wordCount + words

    print(f"No of words in Demo.txt: {wordCount} ")
    fobj.close()
  except FileNotFoundError:
    print("File not present in current directory")
      
if __name__ == "__main__":
    main()