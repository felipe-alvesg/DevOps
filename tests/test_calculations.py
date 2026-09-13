from app_financeiro.calculations import (
    calcular_saldo,
    total_receitas,
    total_despesas,
    resumo_por_categoria,
)
from app_financeiro.models import Transaction


def _transacoes_exemplo():
    return [
        Transaction("Salário", 3000.0, "Renda"),
        Transaction("Aluguel", -1000.0, "Moradia"),
        Transaction("Mercado", -500.0, "Alimentação"),
    ]


def test_calcular_saldo():
    assert calcular_saldo(_transacoes_exemplo()) == 1500.0


def test_total_receitas():
    assert total_receitas(_transacoes_exemplo()) == 3000.0


def test_total_despesas():
    assert total_despesas(_transacoes_exemplo()) == -1500.0


def test_resumo_por_categoria():
    resumo = resumo_por_categoria(_transacoes_exemplo())
    assert resumo == {
        "Renda": 3000.0,
        "Moradia": -1000.0,
        "Alimentação": -500.0,
    }