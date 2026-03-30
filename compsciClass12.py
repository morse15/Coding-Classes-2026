import time
class Bank:
    def __init__(self,owner="",balance=0):
        self.owner = owner
        self.balance = balance
    def welcome(self):
        owner = input("Name: ")
        time.sleep(0.25)
        print(f"Welcome {owner.title()}")
        while True:
            try:
                time.sleep(0.25)
                option = int(input("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nChoose: "))
                if option == 1:
                    self.deposit(0)
                elif option == 2:
                    self.withdraw(0)
                elif option == 3:
                    self.checkBalance()
                elif option == 4:
                    print("Goodbye!")
                    break
                else:
                    print("Please input '1','2','3' or '4'.")
            except ValueError:
                print("Please input '1','2','3' or '4'.")
    def deposit(self,balance):
        while True:
            try:
                time.sleep(0.25)
                balance = int(input("How much do you want to deposit in ₦: "))
                #you cannot deposit a negative amount
                if balance<0:
                    print("You cannot deposit a negative amount.\n")
                else:
                    self.balance += balance
                    print(f"You have deposited ₦{balance}.\n")
                    break
            except ValueError:
                print("You must input an integer.\n")
    def withdraw(self,balance):
        while True:
            try:
                time.sleep(0.25)
                balance = int(input("How much do you want to withdraw in ₦: "))
                #you cannot withdraw more than you have
                if balance > self.balance:
                    print ("Insufficient funds.\n")
                elif balance<0:
                    print("You cannot withdraw a negative amount.\n")
                else:
                    self.balance -= balance
                    print(f"You have withdrawn ₦{balance}.\n")
                    break
            except ValueError:
                print("You must input an integer.\n")
    def checkBalance(self):
        time.sleep(0.25)
        print(f"Your balance is ₦{self.balance}.\n")

test = Bank()
test.welcome()