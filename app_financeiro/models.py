from dataclasses import dataclass, field
from datetime import date


@dataclass
class Transaction:
    description: str
    amount: float  # positivo = receita, negativo = despesa
    category: str
    date: str = field(default_factory=lambda: date.today().isoformat())

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
        }

    @staticmethod
    def from_dict(data):
        return Transaction(
            description=data["description"],
            amount=data["amount"],
            category=data["category"],
            date=data.get("date", date.today().isoformat()),
        )