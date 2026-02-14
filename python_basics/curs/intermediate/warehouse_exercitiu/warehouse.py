import pickle
import time
from datetime import datetime
from functools import reduce

from decorators import run_on_thread

from product import Product, FoodProduct, ElectronicProduct
from logger import Logger

W_NAME = 42
W_QUANTITY = 10
W_PRICE = 10
W_CODE = 36

class Warehouse:
    def __init__(self, name):
        self.name = name
        self.products = []

    def print_products(self):
        # titles = [
        #     "name", "quantity", "price", "code",
        # ]
        #
        # print(f"┌{'─' * W_NAME}┬{'─' * W_QUANTITY}┬{'─' * W_PRICE}┬{'─' * W_CODE}┐")
        # print(f'|{titles[0]:{W_NAME}}│{titles[1]:{W_QUANTITY}}│{titles[2]:{W_PRICE}}│{titles[3]:{W_CODE}}│')
        # print(f"├{'─' * W_NAME}┼{'─' * W_QUANTITY}┼{'─' * W_PRICE}┼{'─' * W_CODE}┤")
        # for product in self.products:
        #     print(
        #         f'│{product.name:{W_NAME}}│{product.quantity:{W_QUANTITY}}│{product.price:{W_PRICE}}│{product.unique_code:{W_CODE}}│')
        #
        # print(f"└{'─' * W_NAME}┴{'─' * W_QUANTITY}┴{'─' * W_PRICE}┴{'─' * W_CODE}┘")
        food_products = list(filter(lambda x: isinstance(x, FoodProduct), self.products))
        print(f'Food prod: {food_products}')

        electronic_products = list(filter(lambda x: isinstance(x, ElectronicProduct), self.products))
        print(f'Electronic prod: {electronic_products}')

    def print_total_warehouse_value(self):
        # total = 0
        # for prod in self.products:
        #     total += prod.total_value()
        total = reduce(lambda x, y: x.total_value() + y.total_value(), self.products)

        print(f'Valoarea totala din depozit este: {total}')

    @run_on_thread
    def save_products(self):
        with open('products.pickle', 'wb') as f:
            pickle.dump(self.products, f)
        time.sleep(2) # simulam ca dureaza mult exec functiei

    @run_on_thread
    def load_products(self):
        try:
            with open('products.pickle', 'rb') as f:
                self.products = pickle.load(f)
            Logger.info('Loaded products successfully!')
        except Exception:
            # print('Error loading file!')
            Logger.warning('Couldn\'t load save file.')
        time.sleep(2)

    def buy_product(self, product_name: str, quantity: int):
        for prod in self.products:
            if prod.name.lower() == product_name.lower():
                if prod.quantity >= quantity:
                    prod.quantity -= quantity
                    print(f"✅ You bought {quantity} x {prod.name}")
                    return
                else:
                    print("❌ Not enough stock available!")
                    return
        # Logger.warning('product not found')
        print("❌ Product not found!")

    def add_food_product(self):
        print('Add new food product:')
        name = input('Name: ')
        price = int(input('Price: '))
        qtt = int(input('Quantity: '))
        desc = input('Description: ')
        expiration = datetime.strptime(input('Expiration date: '), "%Y-%m-%d").date()

        prod = FoodProduct(name, price, qtt, desc, expiration)

        self.products.append(prod)

    def add_electronic_product(self):
        print('Add new electronic product:')
        name = input('Name: ')
        price = int(input('Price: '))
        qtt = int(input('Quantity: '))
        desc = input('Description: ')

        prod = ElectronicProduct(name, price, qtt, desc)

        self.products.append(prod)

    def remove_old_product(self):
        # Loop product list and remove products that are past the expiration date
        products_copy = []

        for prod in self.products:
            try:
                if not prod.is_expired():
                    products_copy.append(prod)
            except AttributeError:
                # If the current product doesn't have an is_expired() function
                # skip to the next one
                continue

        # copy the list containing filtered elements
        self.products = products_copy
