import json
import time
class Bank:
    def __init__(self,owner="",balance=0):
        self.owner = owner
        self.balance = balance
    def read_accounts(self):
        with open("accounts.json", "r") as file:
            return json.load(file)
    #To write to it 
    def write_accounts(self,data):
        with open("accounts.json", "w") as file:
            json.dump(data, file)
    def welcome(self):
        accounts = self.read_accounts()
        #print(accounts["Favour"])  # 300
        owner = input("Name: ")
        owner = owner.title()
        self.owner = owner
        if owner in accounts:
            print(f"\nWelcome {owner}\nYour balance is ₦{accounts[owner]}")
        else:
            print("\nCreating new account...")
            accounts[owner] = 0
            self.write_accounts(accounts)
            time.sleep(0.25)
            print(f"Welcome {owner}")
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
                    print("Goodbye.")
                    break
                else:
                    print("Please input '1','2','3' or '4'.")
            except ValueError:
                print("Please input '1','2','3' or '4'.")
    def deposit(self,balance):
        accounts = self.read_accounts()
        while True:
            try:
                time.sleep(0.25)
                balance = int(input("How much do you want to deposit in ₦: "))
                #you cannot deposit a negative amount
                if balance<0:
                    print("You cannot deposit a negative amount.\n")
                else:
                    accounts[self.owner] += balance
                    self.write_accounts(accounts)
                    print(f"You have deposited ₦{balance}.\n")
                    break
            except ValueError:
                print("You must input an integer.\n")
    def withdraw(self,balance):
        accounts = self.read_accounts()
        while True:
            try:
                time.sleep(0.25)
                balance = int(input("How much do you want to withdraw in ₦: "))
                #you cannot withdraw more than you have
                if balance > accounts[self.owner]:
                    print ("Insufficient funds.\n")
                elif balance<0:
                    print("You cannot withdraw a negative amount.\n")
                else:
                    accounts[self.owner] -= balance
                    self.write_accounts(accounts)
                    print(f"You have withdrawn ₦{balance}.\n")
                    break
            except ValueError:
                print("You must input an integer.\n")
    def checkBalance(self):
        accounts = self.read_accounts()
        time.sleep(0.25)
        print(f"Your balance is ₦{accounts[self.owner]}.\n")

test = Bank()
test.welcome()
