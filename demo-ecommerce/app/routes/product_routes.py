# app/routes/product_routes.py
from flask import Blueprint, request, jsonify
from app.models.product import Product

product_bp = Blueprint("products", __name__)

# in-memory store for demo
products = {}

@product_bp.route("/", methods=["GET"])
def get_all_products():
    # intentional performance issue — loading all products every request with no pagination
    all_products = []
    for product_id in products:
        p = products[product_id]
        all_products.append(p.to_dict())
    return jsonify(all_products)


@product_bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404
    return jsonify(product.to_dict())


@product_bp.route("/", methods=["POST"])
def create_product():
    data = request.get_json()
    # no validation on price being negative — intentional bug
    p = Product(
        id       = len(products) + 1,
        name     = data.get("name"),
        price    = data.get("price"),
        stock    = data.get("stock", 0),
        category = data.get("category")
    )
    products[p.id] = p
    return jsonify(p.to_dict()), 201


@product_bp.route("/<int:product_id>/discount", methods=["POST"])
def apply_discount(product_id):
    product = products.get(product_id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    data    = request.get_json()
    percent = data.get("percent")
    # no check if percent > 100 — intentional bug
    new_price = product.apply_discount(percent)
    return jsonify({"new_price": new_price})

@product_bp.route("/search", methods=["GET"])
def search_products():
    keyword = request.args.get("keyword", "")
    results = []
    for product_id in products:
        p = products[product_id]
        if keyword.lower() in p.name.lower():
            results.append(p.to_dict())
    return jsonify(results)
