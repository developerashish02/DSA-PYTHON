class Cart:
    # initializer methods
    def __init__(self):
        self.items = {}

    # Add in cart method
    def add_items(self, item_name, quantity):
        self.items[item_name] = quantity

    # delete items
    def delete_items(self, item_name):
        del self.items[item_name]

    # update quantity
    def update_quantity(self, item_name, update_quantity):
        self.items[item_name] = update_quantity

    # items list
    def items_list(self):
        items_names = []
        for item in self.items.keys():
            items_names.append(item)

        return items_names

# creating a objects of call


# initializer object
cart_01 = Cart()

cart_01.add_items("Books", 12)
cart_01.add_items("I phone 12", 1)
cart_01.update_quantity("Books", 4)

print(cart_01.items)
print(cart_01.items_list())
