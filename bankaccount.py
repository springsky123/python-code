#BANKACCOUNT

import csv

class MoneyError(Exception):
    pass
class bank_account:
    bank_name = "SBI"
    def __init__(self):
        self.name = "Bhawana"
        self.account_no = 235647890193
        self.branch_name = "Ranikhet"
        self.balance = 500
        self.display_info()
    #Instance method to display account holder info
    def display_info(self):
        print("........Bank account holder details........")
        print(f"Holder name:{self.name}")
        print(f"Account number:{self.account_no}")
        print(f"Branch name:{self.branch_name}")
        print(f"Bank balance:{self.balance}")
        print(f"Bank name:{bank_account.bank_name}")
    
    def deposit_amount(self):
        print("Your bank balance is",self.balance)
        amount = int(input("Enter amount for deposit:"))
        self.balance+=amount
        print("Your bank balance(after deposit)is",self.balance)
    def withdraw_amount(self):
        try:
            amount = int(input("Enter amount for withdrawal:"))
            if amount<=self.balance:
                self.balance-=amount
                print("Your bank balance(after withdrawal)is",self.balance)
            else:
                raise MoneyError()
        except MoneyError:
            print("you don't have enough money...please try again!!!!")
            self.withdraw_amount()
    def get_balance(self):
        print("Your bank balance :")
        print(self.balance)
    #Function for options to choose 
    def choose_option(self):
        print('......................................')
        print('1.FOR DEPOSIT AMOUNT')
        print('2.FOR WITHDRAW AMOUNT')
        print('3.FOR GET BALANCE')
        print('4.FOR CLOSE ACCOUNT')
        print('.......................................')
        choose = int(input('enter your choice:'))
        return choose
    #Instance method to work on choice
    def choice_by_option(self):
        choice ='y'
        while choice=='y':
            opt = self.choose_option()
            if opt==1:
                self.deposit_amount()
            elif opt==2:
                self.withdraw_amount()
            elif opt==3:
                self.get_balance()
            elif opt==4:
                print("Closed account.........")
                break
            else:
                print('......invaild choice,please try again!..........')
            print()
#Create object of bank_account 
s = bank_account()
#call method
s.choice_by_option()
print("__________________")
print("-----------------THE END-----------------")
print()

