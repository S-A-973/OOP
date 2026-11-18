class Product:
    # creating the constructer that contains attributes
    def __init__(self, name, model, release_date):
        self.name = name
        self.model = model
        self.release_date = release_date

    def display(self):
        return self.name, self.model, self.release_date

product_name = input("Enter Name: ")
product_model = input("Enter Model: ")
product_release_date = input("Enter release date: ")

product1 = Product(product_name, product_model, product_release_date)
product1_values = product1.display()

for i in product1_values:
    print(f"{i}")


        
        