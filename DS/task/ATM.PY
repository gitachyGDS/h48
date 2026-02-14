#create a ATM programms

"""
___init__
1.withdraw
2.deposite 
3.balance  check
4. change pin

"""
class Atm:
    def __init__(self):
        self.pin=input("Enter a pin:")
        self.balance=int(input("Enter a balance: "))

    print("pin and balance set successfully !!!!!") 

    def verify(self): #return boolean value
        counter=3
        while counter:
            password=input("Enter the  current pin : ")
            if password==self.pin:
                return True
            
            else: 
               print(f"{counter-1}attempt left ")
               counter=counter-1

        return False
    
    def change_pin(self):
        if self.verify():
            new_pin=input("Enter the new pin: ")
            self.pin=new_pin
            print("pin changes successfully !!!")

        else:
            print("pin is incorrect.")

    def withdraw(self):
        if self.verify():
            w_amount=int(input("Enter the amout to be withdraw:"))
            if w_amount>0:
                if w_amount<=self.balance:
                    self.amount=self.balance-w_amount
                    print(f'{w_amount}$ withdraw successfully: now your current balance is :{self.balance} $')
                else:
                    print("Insuffieince balance :")
            else:

                print("Invalid amount.") 
        else:
            print("Your pin is incorrect!!") 

    def deposite(self):
        if self.verify():
            d_amount=int(input("Enter the amount to be deposite"))
            if d_amount>0:
                self.balance=self.balance+d_amount
                print(f'{d_amount} $ id deposited successfully. Now your current balance is {self.balance} $')
            else:
                print("Invalid amount")

        else:
            print("Your pin is incorrect. ")    


    def check_balance(self):
        if self.verify():
            print(f'("Your current balance is "){self.balance} $ ')                        
        else:
            print("your pin is incorrect.")
a=Atm()
# a.withdraw()
# a.verify()













        
           



