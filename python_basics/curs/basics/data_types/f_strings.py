header1 = "Name"
header2 = "Age"
name = "John"
age = 22

print(f"| {header1:^10} | {header2:^10} |")
print("-" * 27)
print(f"| {name:^10} | {age:^10} |")

print(f"{f"abc"}")

# Changing the way the variable is displayed
n = 109.2345654324
print(f" {n:.3f}")  # will display 109.234

percent = 0.71
print(f" {percent:.1%}")  # will display 71.0%
