from datetime import date,datetime
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
        date_format = "%d-%m-%Y"
        # convert strig to date
        birth_date = datetime.strptime(self.dob, date_format )
        today = datetime.today()
        age = today.year - birth_date.year
        return age



class BankAccount:
    # The constructer
    def __init__(self, owner:Client, acc_no:int, balance:float):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposite(self, amount: int):
        self.balance += abs(amount)

    def withdraw (self, amount: int):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    def print_details(self):
        print(f"Owner: {self.owner.names}\nAcc-no:{self.acc_no}\nBalance: {self.balance}")



def main():
    wendy = Client("Wendy Willow", "A01656", "12-12-2001", "Female")
    samuel = Client("Samuel Iamwell", "A01908", "14-4-1999", "Male")
    age = wendy.calc_age()
    print(f"{wendy.names} is {age} years old")

    acc1 = BankAccount(wendy, 456789021, 70_000.00)
    acc2 = BankAccount(samuel,  78912445, 123_678_897)

    print(f"{acc2.owner.names} : {wendy.calc_age()}")

    acc1.deposite(30_000)
    acc1.withdraw(12000)
    acc1.deposite(14000)
    acc1.print_details()


if __name__ == "__main__":
    main()






    


    
        