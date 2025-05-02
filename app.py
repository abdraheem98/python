#oops

class Product:
    quantiy = 200

    def __init__(self,name,price):
        self.name = name
        self.price = price

p1 = Product("phone","300")
print(p1.name)
print(p1.price)