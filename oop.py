# object oriented programming concepts
# A class is a blue print for creating an object

class Person:
    # A constructer: main function in a class
    def __init__(self, name, dob, race, weight, height):
        self.name = name
        self.dob = dob
        self.race = race
        self.weight = weight
        self.height = height

    def display(self):
        print(f"Name is {self.name}, Date of birth is {self.dob}, Weight is {self.weight} kg")

    def get_bmi(self):
        result = round(self.weight/ self.height**2, 2)
        return result

    


# These variables are now the objects that we have created from the class person
human1 = Person("Hun Ying", "08-06-1996", "Asian", 75, 1.85)
human2 = Person("Boy Wonder", "07-07-2001", "White", 68, 1.72)

# After creating an object to access a function within the class we use dot notation 
# human1.display()
# human2.display()



print(f"{human1.name}'s BMI is {human1.get_bmi()}")
print(f"{human2.name}'s BMI is {human2.get_bmi()}")






class Product:
    def __init__(self, name, model, releaseyear, quantity):
        self.name = name
        self.model = model
        self.releaseyear = releaseyear
        self.quantity = quantity

    def display(self):
        print(f"Product name {self.name}, Product model {self.model}")
        