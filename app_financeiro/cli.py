from .models import Transaction
from .storage import load_transactions, save_transactions
from .calculations import calcular_saldo, total_receitas, total_despesas, resumo_por_categoria


def menu():
    transactions = load_transactions()

    while True:
        print("\n=== Controle Financeiro Pessoal ===")
        print("1. Adicionar transação")
        print("2. Listar transações")
        print("3. Ver resumo (saldo, receitas, despesas)")
        print("4. Resumo por categoria")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            descricao = input("Descrição: ")
            valor = float(input("Valor (use negativo para despesas): "))
            categoria = input("Categoria: ")
            transactions.append(Transaction(descricao, valor, categoria))
            save_transactions(transactions)
            print("Transação adicionada!")

        elif opcao == "2":
            if not transactions:
                print("Nenhuma transação cadastrada.")
            for t in transactions:
                print(f"{t.date} | {t.category:15} | {t.description:20} | R$ {t.amount:.2f}")

        elif opcao == "3":
            print(f"Saldo atual: R$ {calcular_saldo(transactions):.2f}")
            print(f"Total de receitas: R$ {total_receitas(transactions):.2f}")
            print(f"Total de despesas: R$ {total_despesas(transactions):.2f}")

        elif opcao == "4":
            for categoria, valor in resumo_por_categoria(transactions).items():
                print(f"{categoria}: R$ {valor:.2f}")

        elif opcao == "5":
            print("Até logo!")
            break

        else:
            print("Opção inválida.")