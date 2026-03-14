# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that allows users to place **MARKET** and **LIMIT** orders on the **Binance Futures Testnet**.  
The bot supports both **command-line arguments** and an **interactive CLI interface** with validation and logging.

---

# Features

- Place **MARKET orders**
- Place **LIMIT orders**
- Supports **BUY and SELL**
- Command-line execution
- Interactive CLI mode
- Input validation
- Logging of requests and responses
- Modular project structure

---

# Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py            # Binance API client setup
│   ├── order.py             # Order placement logic
│   ├── validators.py        # Input validation functions
│   └── logging_config.py    # Logging configuration
│
├── cli.py                   # Main CLI entry point
├── requirements.txt         # Dependencies
└── README.md
```

---

# Setup Instructions

## 1. Clone the repository

```
git clone <your-repository-url>
cd trading_bot
```

---

## 2. Create a virtual environment (recommended)

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

### Mac / Linux

```
source venv/bin/activate
```

---

## 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 4. Configure Binance Testnet API Keys

Create a `.env` file in the project root and add your **Binance Futures Testnet API credentials**.

Example:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_api_secret
```

You can create testnet keys here:

https://testnet.binancefuture.com/

---

# How to Run the Bot

## Interactive Mode

Run the CLI without arguments:

```
python cli.py
```

Example interaction:

```
--- Binance Futures Testnet Trading Bot ---

Enter trading symbol (example BTCUSDT): BTCUSDT
Enter side (BUY / SELL): BUY
Enter order type (MARKET / LIMIT): MARKET
Enter quantity: 0.002
```

---

## Command-Line Mode

You can pass parameters directly through CLI arguments.

### MARKET Order Example

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

---

### LIMIT Order Example

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 70000
```

---

# Example Output

```
ORDER REQUEST
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.002

ORDER RESPONSE
Order ID: 12808695174
Status: NEW
Executed Qty: 0.000
Avg Price: 0.00

Order placed successfully
```

---

# Logging

All actions and responses are logged to:

```
trading_bot.log
```

Example log entry:

```
2026-03-14 18:03:57 - INFO - Placing MARKET order: BUY 0.002 BTCUSDT
2026-03-14 18:03:58 - INFO - Order Placed Successfully
2026-03-14 18:03:58 - INFO - Response Received | ID=12808695174 | Status=NEW
```

---

# Input Validation

The bot validates:

- Trading symbol format
- Order side (**BUY / SELL**)
- Order type (**MARKET / LIMIT**)
- Quantity must be positive
- Price required for **LIMIT** orders

Invalid inputs produce clear error messages.

---

# Assumptions

- Orders are executed on the **Binance Futures Testnet**, not the live exchange.
- The user has valid **Binance Testnet API keys**.
- Binance minimum order notional requirements apply.
- Only single order execution is supported.

---

# Dependencies

Main libraries used:

```
python-binance
python-dotenv
```

See `requirements.txt` for the full list.

---

# Author

Chandreyee Shome  
B.Tech Computer Science