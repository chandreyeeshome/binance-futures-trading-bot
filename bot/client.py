import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

TESTNET_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(API_KEY, API_SECRET)

    client.FUTURES_URL = TESTNET_URL + "/fapi"

    return client