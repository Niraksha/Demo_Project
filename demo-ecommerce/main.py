# main.py
from flask import Flask
from app.routes.user_routes import user_bp
from app.routes.product_routes import product_bp
from app.routes.order_routes import order_bp
import os

app = Flask(__name__)
app.secret_key = "hardcoded-secret-key-123"  # ← intentional security issue

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(product_bp, url_prefix="/products")
app.register_blueprint(order_bp, url_prefix="/orders")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
