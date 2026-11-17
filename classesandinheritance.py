from datetime import date
class Client:
    # creating the constructer
    def __init__(self, names, kra_pin, dob, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.dob = dob
        self.gender = gender
    
    def display_details(self):
        print(self.names,self.kra_pin, self.dob, self.gender)

    def calc_age(self):
        pass


class BankAccount:
    # The constructer
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposite(self, amount):
        self.balance += abs(amount)

    def withdraw (self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def print_details(self):
        print(f"Owner: {self.owner.names}\nAcc-no:{self.acc_no}\nBalance: {self.balance}")

wendy = Client("Wendy Willow", "A01656", "12-12-2001", "Female")
samuel = Client("Samuel Iamwell", "A01908", "14-4-1999", "Male")

acc1 = BankAccount(wendy, 456789021, 70_000.00)
acc2 = BankAccount(samuel,  78912445, 123_678_897)

dob = "2004-03-12"

today = date.today()

print(today.day, today.month, today.year)
# acc1.deposite(30_000.00)
# acc1.withdraw(12000.00)
# acc1.deposite(14000)
# acc1.print_details()







    


    
        