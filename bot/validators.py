def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol cannot be empty.")


def validate_side(side):
    valid_sides = ["BUY", "SELL"]
    if side.upper() not in valid_sides:
        raise ValueError("Side must be BUY or SELL.")


def validate_order_type(order_type):
    valid_types = ["MARKET", "LIMIT"]
    if order_type.upper() not in valid_types:
        raise ValueError("Order type must be MARKET or LIMIT.")


def validate_quantity(quantity):
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")


def validate_price(price, order_type):
    if order_type.upper() == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders.")