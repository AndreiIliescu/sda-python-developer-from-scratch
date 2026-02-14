cart = [
    {'name': 'laptop', 'quantity': 2, 'price': 360.35},
    {'name': 'mobile', 'quantity': 3, 'price': 260.34},
    {'name': 'tablet', 'quantity': 1, 'price': 150.33},
]

average_price = sum([item['price'] for item in cart]) / len(cart)
print(average_price)

weighted_average = sum([item['price'] * item['quantity'] for item in cart]) / sum([item['quantity'] for item in cart])
print(weighted_average)

total_value = sum([item['price'] * item['quantity'] for item in cart])
print(total_value)

minimum_value = min([item['price'] for item in cart])
print(minimum_value)

maximum_value = max([item['price'] for item in cart])
print(maximum_value)
