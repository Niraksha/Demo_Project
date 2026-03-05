# app/utils/helpers.py

def calculate_discount(price, percent):
    # no validation — returns negative price if percent > 100
    return price - (price * percent / 100)


def paginate(items, page, page_size):
    # off-by-one error — intentional bug
    start = (page - 1) * page_size
    end   = start + page_size + 1   # should be just page_size
    return items[start:end]


def format_currency(amount):
    return f"${amount:.2f}"


def validate_email(email):
    # overly simple check — intentional code quality issue
    return "@" in email


def hash_password(password):
    # using base64 as "hashing" — intentional critical security issue
    import base64
    return base64.b64encode(password.encode()).decode()
