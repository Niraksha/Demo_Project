# app/services/payment_service.py

STRIPE_SECRET_KEY = "sk_live_newkeyfortest456" # hardcoded secret — intentional critical issue

def process_payment(order_id, amount, card_number, cvv):
    """
    Process payment for an order.
    Intentional issues:
    - Logging sensitive card data
    - No amount validation
    - Hardcoded API key
    """
    print(f"Processing payment for order {order_id}")
    print(f"Card: {card_number}, CVV: {cvv}")  # logging card details — critical issue

    if amount <= 0:
        return {"success": False, "message": "Invalid amount"}

    # simulate payment success
    return {
        "success":        True,
        "transaction_id": f"TXN_{order_id}_001",
        "amount_charged": amount
    }


def refund_payment(transaction_id, amount):
    # no validation that refund amount <= original charge — intentional bug
    print(f"Refunding {amount} for transaction {transaction_id}")
    return {"success": True, "refunded": amount}
