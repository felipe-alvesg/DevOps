import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.json")


def load_transactions():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)
    from .models import Transaction
    return [Transaction.from_dict(item) for item in raw]


def save_transactions(transactions):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in transactions], f, indent=2, ensure_ascii=False)