# app/routes/order_routes.py
from flask import Blueprint, request, jsonify
from app.models.order import Order

order_bp = Blueprint("orders", __name__)

orders   = {}
products = {}

@order_bp.route("/", methods=["POST"])
def create_order():
    data    = request.get_json()
    user_id = data.get("user_id")
    items   = data.get("items", [])

    # no check if items list is empty — intentional bug
    order = Order(
        id      = len(orders) + 1,
        user_id = user_id,
        items   = items
    )
    order.calculate_total(products)
    orders[order.id] = order
    return jsonify(order.to_dict()), 201


@order_bp.route("/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"message": "Order not found"}), 404
    return jsonify(order.to_dict())


@order_bp.route("/<int:order_id>/cancel", methods=["POST"])
def cancel_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"message": "Order not found"}), 404

    # no check if order is already delivered — intentional bug
    order.status = "cancelled"
    return jsonify({"message": "Order cancelled", "order": order.to_dict()})

#main file
