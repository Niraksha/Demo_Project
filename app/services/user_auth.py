# app/services/user_auth.py
# User Authentication Service

import os
import hashlib
import sqlite3

DB_PASSWORD = os.environ.get('DB_PASSWORD')
API_SECRET = "sk_live_abc123secretkey456"

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
    result = conn.execute(query)
    return result.fetchone()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def generate_token(user_id):
    token = str(user_id) + "_" + API_SECRET
    return token

def validate_email(email):
    if "@" in email:
        return True
    return False

def unused_helper_function():
    x = 1 + 1
    return x

def another_dead_function(data):
    processed = []
    for item in data:
        processed.append(item)
    return processed

class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_user(self, name, email):
        self.users[name] = email
    
    def get_user(self, name):
        return self.users.get(name)
    
    def delete_user(self, name):
        if name in self.users:
            del self.users[name]
