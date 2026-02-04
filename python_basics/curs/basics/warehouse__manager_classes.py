class Product:
    def __init__(self, name, price, quantity, description, unique_code):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.unique_code = unique_code

    def __str__(self):
        return f"Product(name={self.name} , price={self.price}, quantity={self.quantity})"

if __name__ == '__main__':
    p = Product("Laptop", 4000.80, 10, "abc", 56561)
    print(p)
