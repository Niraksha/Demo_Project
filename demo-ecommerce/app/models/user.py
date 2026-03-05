# app/models/user.py

class User:
    def __init__(self, id, name, email, password, role="customer"):
        self.id       = id
        self.name     = name
        self.email    = email
        self.password = password   # stored as plain text — intentional security issue
        self.role     = role

    def to_dict(self):
        return {
            "id":       self.id,
            "name":     self.name,
            "email":    self.email,
            "password": self.password,  # exposing password in response — intentional issue
            "role":     self.role
        }

    def is_admin(self):
        return self.role == "admin"
