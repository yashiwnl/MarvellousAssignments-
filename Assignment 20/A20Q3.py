import threading

def EvenList(data):

  sum = 0
  for i in data:
    if i % 2 == 0:
      sum = sum + i
  print(f"sum of even elements in list: {sum}")

def OddList(data):

  sum = 0
  for i in data:
    if i % 2 != 0:
      sum = sum + i
  print(f"sum of odd elements in list: {sum}")


def main():

  data = [32, 11,25,31,22,54,69,67,54]
  t1 = threading.Thread(target= EvenList, args=(data,))
  t2 = threading.Thread(target= OddList, args=(data,))

  t1.start()
  t2.start()

  t1.join()
  t2.join()

if __name__ == "__main__":
  main()