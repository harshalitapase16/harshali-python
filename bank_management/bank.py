class Bank:
 def __init__(self,account_no,account_holder,balance=0.0):
  self.account_no = account_no
  self.account_holder = account_holder
  self.balance = balance

 def deposit(self,amount):
  if amount > 0:
   self.balance += amount
   print(f"{amount} Amount Deposited successfully")
  else:
   print("Insufficient amount you entered")
 
 def withdraw(self,amount):
  if amount > 0 and self.balance >= amount:
   self.balance -= amount
   print(f"Your withdraw amount is {self.balance}")
  elif self.balance < amount:
   print("Insufficient balance")
  else:
   print("Withdrawal amount must be positive.")
 def check_balance(self):
  print(f"The total balance is {self.balance}")
  

print("Welcome to the Bank Account Management System")

# Get user input to create a bank account
account_number = input("Enter account number: ")  
account_holder = input("Enter account holder name: ")
account = Bank(account_number, account_holder)

while True:
    print("\nPlease choose an option:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == '3':
        account.check_balance()
    elif choice == '4':
        print("Thank you for using the Bank Account Management System.")
        break
    else:
        print("Invalid choice. Please try again.")

