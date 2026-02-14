# The function returns the name and the surname
def print_full_name(name, surname):
    print(f"{name} {surname}")


# The function call without parameters
print_full_name("Jon", "Snow")

# The function call with all parameters names
print_full_name(name="Jon", surname="Snow")
print_full_name(surname="Snow", name="Jon")

# The function call with last parameter name
print_full_name("Jon", surname="Snow")
# print_full_name(surname="Snow", "Jon")
