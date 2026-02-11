class Laptop:
    def __init__(self, brand=None, model=None, os_v=None, price=None):
        self.brand = brand
        self.model = model
        self.os_v = os_v
        self.price = price
    
    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("OS Version:", self.os_v)
        print("Price:", self.price)
        print("--------------------")


# Creating objects in different ways
laptop1 = Laptop()
laptop2 = Laptop("HP")
laptop3 = Laptop("Dell", "Inspiron 15", "Windows 11")
laptop4 = Laptop("Apple", "MacBook Air", "macOS Ventura", 95000)

#laptop1.show_details()
#laptop2.show_details()
#laptop3.show_details()
laptop4.show_details()
