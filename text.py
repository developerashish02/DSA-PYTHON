class Cart:
    # initializer method
    def __init__(self):
        self.items = {}
        self.prices = {"Mango": 22, "Laptop": 30000}

    # add items method
    def add_items(self, item_name, item_quantity):
        self.items[item_name] = item_quantity

    # remove item method
    def remove_item(self, item_name):
        del self.items[item_name]

    # update quantity
    def update_quantity(self, item_name, updated_quantity):
        self.items[item_name] = updated_quantity

    # get total price
    def get_total_price(self):
        totalPrice = 0

        for item, quantity in self.items.items():
            totalPrice += quantity * self.prices[item]

        return totalPrice


# ----------------------------------------Object Works------------------------------------------ #

# create a object
cart_01 = Cart()

# Adding a quantity
cart_01.add_items("Mango", 45)
cart_01.add_items("Laptop", 1)

# remove items
# cart_01.remove_item("Mango")
# cart_01.remove_item("Laptop")

# update quantity

cart_01.update_quantity("Mango", 100)
print(cart_01.items)

print(cart_01.get_total_price())
