comandos_validos = ["d", "deposito", "depósito", "s", "saque", "e", "extrato"]

dinheiro = 0
SAQUES_DIARIOS = 3
LIMITE_SAQUE_DIARIO = 500.00


def main():
    while True:
        print("Seja bem vindo ao ATM V1.")
        print("Selecione uma das operações válidas:")
        print(comandos_validos)
        print("Para selecionar uma das opções digite o comando nesse formato [comando][valor].")
        print("Se o comando for 'e' ou 'extrato', o valor será ignorado.")
        print("Se desejar sair do programa, digite 'sair'.")
        print(f"Limite de Saques por dia: {SAQUES_DIARIOS}")
        opcao = input("> ")
        if opcao == "sair":
            break
        else:
            gerenciador_de_input(opcao)


def deposito(valor):
    if valor <= 0:
        print("Erro: não é possível depositar valores negativos.")
        return
    operacao(valor, "deposito")
    print(f"O depósito no valor de R${valor} reais foi efetuado.\nValor da conta-corrente: R${dinheiro}.")


def saque(valor):
    global SAQUES_DIARIOS
    if valor > dinheiro:
        print("Erro: não é possível sacar mais dinheiro do que o que está disponível em sua conta-corrente.")
        return
    if SAQUES_DIARIOS == 0:
        print("Erro: Você já usou o limite diário de saques (3).")
        return
    if valor > LIMITE_SAQUE_DIARIO:
        print(f"Erro: Você não pode sacar mais que R${LIMITE_SAQUE_DIARIO} por dia.")
        return
    operacao(valor, "saque")
    SAQUES_DIARIOS -= 1
    print(f"O saque no valor de R${valor} reais foi efetuado.\nNovo valor da conta-corrente: R${dinheiro}.")


def operacao(valor, tipo_operacao):
    global dinheiro
    if tipo_operacao == "deposito":
        dinheiro += valor
    elif tipo_operacao == "saque":
        dinheiro -= valor
    else:
        print("Erro: operação inválida: deve ser 'deposito' ou 'saque'")
        return


def extrato():
    print(f"R${dinheiro}")


def gerenciador_de_input(user_input):
    user_input = user_input.split()

    if len(user_input) > 2:
        print("Erro: comando deve ter até dois argumentos [operação][valor(opcional)]")
        return
    if user_input[0] not in comandos_validos:
        print(f"Erro: comando {user_input[0]} não reconhecido.")
        return
    if len(user_input) == 1 and user_input[0] in ["d", "deposito", "depósito", "s", "saque"]:
        print(f"Erro: comando {user_input[0]} exige um valor.")
        return

    comando = user_input[0].lower()
    valor = int(user_input[1]) if len(user_input) == 2 else None

    if comando in ["d", "deposito", "depósito"]:
        deposito(valor)
    elif comando in ["s", "saque"]:
        saque(valor)
    elif comando == "e":
        extrato()

    input("Pressione qualquer botão...")


if __name__ == "__main__":
    main()