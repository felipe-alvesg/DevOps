def calcular_saldo(transactions):
    return sum(t.amount for t in transactions)


def total_receitas(transactions):
    return sum(t.amount for t in transactions if t.amount > 0)


def total_despesas(transactions):
    return sum(t.amount for t in transactions if t.amount < 0)


def resumo_por_categoria(transactions):
    resumo = {}
    for t in transactions:
        resumo[t.category] = resumo.get(t.category, 0) + t.amount
    return resumo