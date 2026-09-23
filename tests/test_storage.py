from app_financeiro import storage
from app_financeiro.models import Transaction


def test_load_transactions_quando_arquivo_nao_existe(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "transactions.json"))
    assert storage.load_transactions() == []


def test_save_and_load_transactions(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "DATA_FILE", str(tmp_path / "transactions.json"))

    transactions = [
        Transaction("Salário", 3000.0, "Renda", date="2024-01-05"),
        Transaction("Aluguel", -1000.0, "Moradia", date="2024-01-10"),
    ]
    storage.save_transactions(transactions)

    carregadas = storage.load_transactions()
    assert len(carregadas) == 2
    assert carregadas[0].description == "Salário"
    assert carregadas[1].amount == -1000.0
