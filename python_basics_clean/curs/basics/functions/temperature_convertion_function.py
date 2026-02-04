def celsius_farenheit_convertion(celsius_degree):
    fahrenheit_degrees = celsius_degree * 9 / 5 + 32
    return fahrenheit_degrees


def celsius_kelvin_conversion(celsius_degree):
    return celsius_degree + 273.15


def farenheit_celsius_convertion(farenheit_degree):
    return (farenheit_degree - 32) * (5 / 9)


def kelvin_celsius_conversion(kelvin_degree):
    return kelvin_degree - 273.15

def fahrenheit_kelvin_conversion(fahrenheit_degree):
    celsius_degree = farenheit_celsius_convertion(fahrenheit_degree)
    kelvin_degrees = celsius_kelvin_conversion(celsius_degree)
    return kelvin_degrees

def kelvin_fahrenheit_conversion(kelvin_degree):
    celsius_degrees = kelvin_celsius_conversion(kelvin_degree)
    fahrenheit_degree = celsius_farenheit_convertion(celsius_degrees)
    return fahrenheit_degree

# celsius_input = float(input("Set a Celsius degree to convert to Fahrenheit: "))
# print(f"{celsius_input}°C = {celsius_farenheit_convertion(celsius_input)}°F")
# celsius_input2 = float(input("Set a Celsius degree to convert to Kelvin: "))
# print(f"{celsius_input2}°C = {celsius_kelvin_conversion(celsius_input2)}°K")
in_ = float(input('set temp:'))
print(f"{in_} -> {kelvin_fahrenheit_conversion(in_):.2f}")
