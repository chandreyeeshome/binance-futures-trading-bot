import argparse
import logging

from bot.order import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


def interactive_input():
    print("\n--- Binance Futures Testnet Trading Bot ---\n")

    symbol = input("Enter trading symbol (example BTCUSDT): ").upper()

    side = input("Enter side (BUY / SELL): ").upper()
    while side not in ["BUY", "SELL"]:
        print("Invalid side. Please enter BUY or SELL.")
        side = input("Enter side (BUY / SELL): ").upper()

    order_type = input("Enter order type (MARKET / LIMIT): ").upper()
    while order_type not in ["MARKET", "LIMIT"]:
        print("Invalid order type. Please enter MARKET or LIMIT.")
        order_type = input("Enter order type (MARKET / LIMIT): ").upper()

    quantity = float(input("Enter quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Enter price: "))

    return symbol, side, order_type, quantity, price


def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", help="Trading pair (example: BTCUSDT)")
    parser.add_argument("--side", help="BUY or SELL")
    parser.add_argument("--type", help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT orders")

    args = parser.parse_args()

    if not all([args.symbol, args.side, args.type, args.quantity]):
        symbol, side, order_type, quantity, price = interactive_input()
    else:
        symbol = args.symbol
        side = args.side
        order_type = args.type
        quantity = args.quantity
        price = args.price

    try:

        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        print("\nORDER REQUEST")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", quantity)

        if order_type.upper() == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            print("Price:", price)

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nORDER RESPONSE")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\nOrder placed successfully")

    except Exception as e:

        print("\nError:", str(e))
        logging.error("Error occurred: %s", str(e))


if __name__ == "__main__":
    main()