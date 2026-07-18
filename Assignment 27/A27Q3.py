class Numbers:

  def __init__(self, value):
    self.value = int(value)

  def chkPrime(self):

    isPrime = True

    if (self.value < 2):
      isPrime = False

    for i in range (2, self.value):
      if self.value % i == 0:
        isPrime = False
        break
    
    return isPrime
  
  def chkPerfect(self):
    sum = 0

    for i in range (1, self.value):
      if self.value % i == 0:
        sum = sum + i

    return (sum == self.value)
  
  def Factors(self):

    print(f"Factors of {self.value}: ")
    for i in range(1, self.value + 1):
      if self.value % i == 0:
        print(i)

  def sumFactors(self):
    sum = 0

    for i in range (1, self.value + 1):
      if self.value % i == 0:
        sum = sum + i

    return sum

def main():
  
  obj1 = Numbers(23)

  print(f"Prime: {obj1.chkPrime()} ")
  print(f"Perfect: {obj1.chkPerfect()} ")
  obj1.Factors()
  print(f"Sum of factors: {obj1.sumFactors()} ")

  obj2 = Numbers(28)

  print(f"Prime: {obj2.chkPrime()} ")
  print(f"Perfect: {obj2.chkPerfect()} ")
  obj2.Factors()
  print(f"Sum of factors: {obj2.sumFactors()} ")

if __name__ == "__main__":
  main()