# app/routes/user_routes.py
from flask import Blueprint, request, jsonify
import sqlite3

user_bp = Blueprint("users", __name__)
DB_PATH = "ecommerce.db"

@user_bp.route("/login", methods=["POST"])
def login():
    data     = request.get_json()
    email    = data.get("email")
    password = data.get("password")

    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # intentional SQL injection vulnerability
    query = f"SELECT * FROM users WHERE email='{email}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful", "user_id": user[0]})
    return jsonify({"message": "Invalid credentials"}), 401


@user_bp.route("/register", methods=["POST"])
def register():
    data  = request.get_json()
    name  = data.get("name")
    email = data.get("email")
    password = data.get("password")

    # no input validation — intentional issue
    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, password)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully"})


@user_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    conn   = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    if not user:
        return jsonify({"message": "User not found"}), 404

    # returning password in response — intentional issue
    return jsonify({
        "id":       user[0],
        "name":     user[1],
        "email":    user[2],
        "password": user[3]
    })
