import logging
from .client import get_client


def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        logging.info(f"Placing MARKET order: {side} {quantity} {symbol}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
        logging.info("Order Placed Successfully")
        logging.info(
            f"Response Received | ID={response.get('orderId')} | "
            f"Status={response.get('status')} | "
            f"Symbol={response.get('symbol')} | "
            f"Side={response.get('side')} | "
            f"Qty={response.get('origQty')}"
        )

        return response

    except Exception as e:
        logging.error(f"Error placing MARKET order: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        logging.info(f"Placing LIMIT order: {side} {quantity} {symbol} at {price}")

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
        logging.info("Order Placed Successfully")
        logging.info(
            f"Response Received | ID={response.get('orderId')} | "
            f"Status={response.get('status')} | "
            f"Symbol={response.get('symbol')} | "
            f"Side={response.get('side')} | "
            f"Qty={response.get('origQty')} | "
            f"Price={response.get('price')}"
        )

        return response

    except Exception as e:
        logging.error(f"Error placing LIMIT order: {str(e)}")
        raise