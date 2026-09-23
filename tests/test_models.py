from app_financeiro.models import Transaction


def test_transaction_to_dict():
    t = Transaction("Salário", 3000.0, "Renda", date="2024-01-05")
    assert t.to_dict() == {
        "description": "Salário",
        "amount": 3000.0,
        "category": "Renda",
        "date": "2024-01-05",
    }


def test_transaction_from_dict():
    data = {
        "description": "Aluguel",
        "amount": -1000.0,
        "category": "Moradia",
        "date": "2024-01-10",
    }
    t = Transaction.from_dict(data)
    assert t.description == "Aluguel"
    assert t.amount == -1000.0
    assert t.category == "Moradia"
    assert t.date == "2024-01-10"


def test_transaction_from_dict_sem_data_usa_hoje():
    data = {"description": "Mercado", "amount": -50.0, "category": "Alimentação"}
    t = Transaction.from_dict(data)
    assert t.date is not None
