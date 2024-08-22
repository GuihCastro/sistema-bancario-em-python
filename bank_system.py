menu = """

[d] Depositar
[s] Sacar
[e] Exibir Extrato
[q] Sair

===> """

balance = 0
limit = 500
extract = []
withdrawal_number = 0
WITHDRAWAL_LIMIT = 3

def deposit():
    global balance, extract
    value = float(input("Informe o valor do depósito: "))

    if value > 0:
        balance += value
        print(f"Depósito realizado com sucesso! Saldo atual: R${balance:.2f}")
        extract.append(f"Depósito no valor de: R${value:.2f}")

    else:
        print("Operação falhou! O valor informado é inválido.")

def withdraw():
    global balance, limit, extract, withdrawal_number, WITHDRAWAL_LIMIT
    value = float(input("Informe o valor do saque: "))

    exceed_balance = value > balance

    exceed_limit = value > limit

    exceed_withdrawal_limit = withdrawal_number >= WITHDRAWAL_LIMIT

    if exceed_balance:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif exceed_limit:
        print("Operação falhou! O valor do saque excede o limite.")

    elif exceed_withdrawal_limit:
        print("Operação falhou! Número máximo de saques excedido.")

    elif value > 0:
        balance -= value
        print(f"Saque realizado com sucesso! Saldo atual: R${balance:.2f}")
        extract.append(f"Saque no valor de: R${value:.2f}")
        withdrawal_number += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

def show_extract():
    global extract, balance
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações" if not extract else extract)
    print(f"\nSaldo atual: R${balance:.2f}")
    print("==========================================")

while True:

    option = input(menu).lower()

    if option == "d":
        deposit()
    elif option == "s":
        withdraw()
    elif option == "e":
        show_extract()
    elif option == "q":
        print("Obrigado por utilizar o nosso sistema!")
        break
    else:
        print("Operação inválida. Por favor, informe novamente a opção desejada.")
