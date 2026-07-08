import threading

def EvenFactor(num):

  sum = 0
  for i in range(2, num + 1, 2):
    if( num % i == 0):
        sum = sum + i
  print(f"sum of even factors: {sum}")

def OddFactor(num):

  sum = 0
  for i in range(1, num, 2):
    if( num % i == 0):
        sum = sum + i
  print(f"sum of odd factors: {sum}")
  
def main():

  t1 = threading.Thread(target= EvenFactor, args=(20,))
  t2 = threading.Thread(target= OddFactor, args=(20,))   

  t1.start()
  t2.start()

  t1.join()
  t2.join()

  print("Exit from main")

if __name__ == "__main__":
  main()