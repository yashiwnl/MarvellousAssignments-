class BankAccount:
  ROI = 10.5

  def __init__(self, name, amount):
    self.name = name
    self.amount = int(amount)

  def Deposit(self):
    inc = int(input("Enter the amount you want to deposit: "))
    self.amount = self.amount + inc
    print(f"Successfully deposited {inc} rs, new balance is: {self.amount}")

  def Withdraw(self):
    dec = int(input("Enter the amount you want to withdraw: "))

    if( dec > self.amount):
      print("Exceeded sufficient balance, withdrawal not possible")
    else:
      self.amount = self.amount - dec
      print(f"sucessfully withdrawn {dec} rs, new balance is: {self.amount}")
  
  def calculateInterest(self):
    Interest = (self.amount * BankAccount.ROI) / 100
    return Interest
  
  def display(self):
    print(f"Account Name: {self.name}, Available balance: {self.amount}")

def main():
  obj1 = BankAccount("Yash", 2000)

  obj1.Deposit()
  obj1.Withdraw()
  print(f"Interest: {obj1.calculateInterest()} ")
  obj1.display()

  obj2 = BankAccount("Varad", 3000)

  obj2.Deposit()
  obj2.Withdraw()
  print(f"Interest: {obj2.calculateInterest()} ")
  obj2.display()

if __name__ == "__main__":
  main()