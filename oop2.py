class  Circle:
    def __init__(self, radius):
        self.radius = radius
        

    def area(self):
        return 22/7 * self.radius **2
    def perimeter (self):
        return 22/7 * self.radius * 2

circle1 = Circle(7)
circle2 = Circle(4)

print(circle1.area(), circle1.area())
print(circle1.perimeter(), round(circle2.perimeter(), 2))

    
        