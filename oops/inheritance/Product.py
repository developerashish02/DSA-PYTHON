class Product:
    # initializer method its called a super class or parent call
    def __init__(self, price, name, deal_price, rating):
        self.price = price
        self.name = name
        self.deal_price = deal_price
        self.rating = rating
        self.your_save = price - deal_price

    # product details
    def product_details(self):
        print("Product:{}".format(self.name))
        print("Price:{}".format(self.price))
        print("Deal Price:{}".format(self.deal_price))
        print("rating:{}".format(self.rating))
        print("Your Save:{}".format(self.your_save))


class ElectronicItem(Product):

    def set_warranty(self, warranty_in_months):
        self.warranty_in_months = warranty_in_months

    def get_warranty(self):
        return self.warranty_in_months

    def gel_electronic_product_detail(self):
        self.product_details()
        print("warranty: ", self.warranty_in_months)


# This is called as sub class or child class
e_item = ElectronicItem(32000, "AsusVivobook", 30000, 4.6)
e_item.set_warranty(21)
# print("Getting warranty", e_item.get_warranty())
print(e_item.gel_electronic_product_detail())
