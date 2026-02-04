from warehouse import Warehouse
from user import User
from logger import Logger


# Hardcoded users for demo
USERS = [
    User("admin", "admin123", role="admin"),
    User("john", "client123", role="client"),
]

def login():
    print("=== Login ===")
    username = input("Username: ")
    password = input("Password: ")

    for user in USERS:
        if user.username == username and user.check_password(password):
            print(f"Welcome {user.username}! (role: {user.role})")
            return user
    # print("❌ Invalid credentials")
    Logger.error("❌ Invalid credentials")
    return None


if __name__ == "__main__":
    Logger.set_level(Logger.ERROR)

    # login before accessing warehouse
    user = None
    while not user:
        user = login()

    Logger.info("User logged in")

    w = Warehouse("Depozit1")
    w.load_products()

    is_program_running = True

    while is_program_running:
        w.print_products()

        if user.is_admin():
            print(
                "1: Add food product\n"
                "2: Remove old products\n"
                "3: Total warehouse value\n"
                "4: Add electronic product\n"
                "5: Buy product\n"
                "6: Quit program"
            )
        else:  # client menu
            print(
                "1: List products\n"
                "2: Buy product\n"
                "3: Quit program"
            )

        option = input("Insert option: ")

        if user.is_admin():
            match option:
                case "1":
                    w.add_food_product()
                case "2":
                    w.remove_old_product()
                case "3":
                    w.print_total_warehouse_value()
                case "4":
                    w.add_electronic_product()
                case "5":
                    name = input("Product name: ")
                    qty = int(input("Quantity: "))
                    w.buy_product(name, qty)
                case "6":
                    is_program_running = False
                case _:
                    print("Invalid option!")

        else:  # client role
            match option:
                case "1":
                    w.print_products()
                case "2":
                    name = input("Product name: ")
                    qty = int(input("Quantity: "))
                    w.buy_product(name, qty)
                case "3":
                    is_program_running = False
                case _:
                    print("Invalid option!")

    w.save_products()
    print("Goodbye!")
