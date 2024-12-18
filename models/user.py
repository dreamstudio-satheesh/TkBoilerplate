class User:
    def __init__(self):
        self.users = {"admin": "password123"}  # Sample data for authentication

    def authenticate(self, username, password):
        return self.users.get(username) == password
