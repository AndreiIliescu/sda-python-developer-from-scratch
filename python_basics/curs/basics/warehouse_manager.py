import pickle
import os.path
from warehouse__manager_classes import Product

W_NAME = 42
W_QUANTITY = 10
W_PRICE = 10
W_CODE = 12

NAME = 'name'
QUANTITY = 'quantity'
DESCRIPTION = 'description'
CODE = 'unique_code'
PRICE = 'price'


def show_products(products):
    # print(dir(products[0]))
    # titles = list(products[0].keys())
    titles = [
        "name", "quantity", "price", "code",
    ]

    print(f"┌{'─' * W_NAME}┬{'─' * W_QUANTITY}┬{'─' * W_PRICE}┬{'─' * W_CODE}┐")
    print(f'|{titles[0]:{W_NAME}}│{titles[1]:{W_QUANTITY}}│{titles[2]:{W_PRICE}}│{titles[3]:{W_CODE}}│')
    print(f"├{'─' * W_NAME}┼{'─' * W_QUANTITY}┼{'─' * W_PRICE}┼{'─' * W_CODE}┤")
    for product in products:
        # print(f'│{product["name"]:{W_NAME}}│{product["quantity"]:{W_QUANTITY}}│{product["price"]:{W_PRICE}}│{product["unique_code"]:{W_CODE}}│')
        print(
            f'│{product.name:{W_NAME}}│{product.quantity:{W_QUANTITY}}│{product.price:{W_PRICE}}│{product.unique_code:{W_CODE}}│')

    print(f"└{'─' * W_NAME}┴{'─' * W_QUANTITY}┴{'─' * W_PRICE}┴{'─' * W_CODE}┘")
    print()


def save_products(products):
    with open('products.pickle', 'wb') as f:
        pickle.dump(products, f)


def load_products():
    if os.path.exists('products.pickle'):
        with open('products.pickle', 'rb') as f:
            return pickle.load(f)
    else:
        return [
            Product("Tablet", 55, 3, 'Bla bla', 46351),
            Product("Laptop", 560, 13, 'Bla bla', 56577),
            Product("Mobile", 15, 10, 'Bla bla', 7566445),
            Product("smartwatch", 105, 60, 'Bla bla', 7878777),
        ]


def add_products(products: list):
    name_input = input("Name: ")
    quantity_input = input("Quantity: ")
    price_input = input("Price: ")
    code_input = input("Code: ")
    description_input = input("Description: ")

    products.append(
        Product(name_input, float(price_input), int(quantity_input), description_input, int(code_input))
    )

    save_products(products)


def buy_product(products):
    product_name = input("Enter the product you want to buy: ").strip().lower()
    for item in products:
        if item.name.lower() == product_name:
            if item.quantity > 0:
                item.quantity -= 1
                print(f"you bought one {item.name}.")
                print(f"remaining quantity: {item.quantity}")
                print(f"new total price for {item.name}: {item.quantity * item.price:.2f}")
            else:
                print(f"sorry, {item.name} is out of stock.")
            break
    else:
        print("product not found in cart.")
    save_products(products)


def main():
    products = load_products()
    show_products(products)
    buy_product(products)
    show_products(products)


if __name__ == '__main__':
    main()
