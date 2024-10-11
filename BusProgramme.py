

class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class Inventory:
    def __init__(self):
        self.products = {}

    
    def add_product(self, name, quantity, price):
        if name in self.products:
            self.products[name].quantity += quantity
        else:
            self.products[name] = Product(name, quantity, price)
        print(f"Added {quantity} of {name} to the inventory.")
    
    
    def sell_product(self, name, quantity_sold):
        if name in self.products and self.products[name].quantity >= quantity_sold:
            self.products[name].quantity -= quantity_sold
            print(f"Sold {quantity_sold} of {name}. Remaining stock: {self.products[name].quantity}")
            self.check_stock(name)
        else:
            print(f"Not enough stock of {name} to complete the sale.")
    
    
    def check_stock(self, name):
        if self.products[name].quantity < 5:
            print(f"Warning: Low stock for {name}. Only {self.products[name].quantity} left!")
    
    
    def display_inventory(self):
        print("\nCurrent Inventory:")
        for name, product in self.products.items():
            print(f"{name}: {product.quantity} units, Price: R{product.price:.2f}")
        print()


inventory = Inventory()


inventory.add_product("Apples", 20, 0.50)
inventory.add_product("Bananas", 10, 0.30)
inventory.sell_product("Apples", 18)
inventory.sell_product("Bananas", 7)
inventory.display_inventory()