
def main():
  marks = int(input("Enter marks: "))
  grade = ""

  if(marks > 100 or marks < 0):
    print("invalid value")
    return

  if(marks >= 75):
    grade = "Distinction"
  elif(marks >= 60):
    grade = "First Class"
  elif(marks >= 50):
    grade = "Second Class"
  elif(marks < 50):
    grade = "Fail"

  print(grade)




if __name__ == "__main__":
  main()