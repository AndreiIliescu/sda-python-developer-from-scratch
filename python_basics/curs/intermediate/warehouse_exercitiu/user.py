class User:
    def __init__(self, username: str, password: str, role: str = "client"):
        self.username = username
        self.password = password
        self.role = role.lower()  # either "admin" or "client"

    def check_password(self, password: str) -> bool:
        return self.password == password

    def is_admin(self) -> bool:
        return self.role == "admin"

    def __str__(self):
        return f"User({self.username}, role={self.role})"
