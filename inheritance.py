#inheritance
class Employee:
    # create the constructer
    def __init__(self, name, department, salary): #Self allows other functions and classes to access the function and attributes
        self.name = name
        self.salary = salary
        self.department = department
    def show_details(self):
        print(self.name,self.department, self.salary)


class PermanentEmployees(Employee):
    def __init__(self,  name, department, salary, cover, incriment):
        super().__init__(name, department, salary)
        self.cover = cover
        self.incriment = incriment
        

class ContractualEmployee(Employee):
    def __init__(self, name, department, salary, tenure):
        super().__init__(name, department, salary)
        self.tenure = tenure

p1 = PermanentEmployees("Judah James", "Human Resources", 100_000, "AA Health Insurance", 4)
c1 = ContractualEmployee("Simon Belles", "ICT", 90_000, 3)

p1.show_details()
c1.show_details()


# TODO OVERRIDING