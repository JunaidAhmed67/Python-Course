# Abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")
    def stop(self):
        self.clutch = False
        self.acc = False
        self.brk= True
        print("Car stoped...")


person = Car()
person.start()
person.stop()



class Account:

    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self, amount):
        if(self.balance>amount):
         self.balance -=amount
         print("Rs. ", amount , "was debited from your account.")
        else:
         print("you entered insuficient amount.")
        self.get_balance()
    def credit(self, amount):
        self.balance +=amount
        print("Rs. ", amount , "was credited from your account.")
        self.get_balance()
    def get_balance(self):
        print("Your (",self.accountNo,")current balance is : ",self.balance)

 
person1 = Account(1000,12345)
person1.get_balance()
person1.debit(500)
person1.credit(1000)