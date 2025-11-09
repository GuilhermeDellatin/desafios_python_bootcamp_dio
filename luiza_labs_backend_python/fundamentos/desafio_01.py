"""
Como era:
menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
"""


# Objetivo geral
#
# Separar os códigos existentes de saque, depósito e extrato em funções.
# Criar duas novas funções : cadastrar usuário (cliente) e cadastrar conta bancária.

# Desafio
#
# Precisamos deixar nosso código mais modularizado, para isso vamos criar funções
# para as operações existentes: sacar, depositar e visualizar histórico. Além disso,
# para a versão 2 do nosso sistema precisamos criar duas novas funções:
# criar usuário (cliente de banco) e criar conta corrente (vincular com usuário).

# Separação em funções
#
# Devemos criar funções para todos as operações do sistema. Para exercitar tudo o que
# aprendemos neste módulo, cada função vai ter uma regra na passagem de argumetos.
# O retorno e a forma como serão chamadas, pode ser definida por você da forma que
# achar melhor.

# Saque
#
# A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão
# de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
# Sugestão de retorno: saldo e extrato.

# Depósito
#
# A função depósito deve receber os argumentos apenas por posição (positional only).
# Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

# Extrato
#
# A função extrato deve receber os argumentos por posição e nome (positional only e keyword only).
# Argumentos posicionais: saldo, argumentos nomeados: extrato.

# Novas Funções
#
# Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para
# adicionar mais funções, exemplo: listar contas.

# Criar usuário (cliente)
#
# O programa deve armazenar os usuários em uma lista, um usuário é composto por:
# nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato:
# logradouro, número, bairro, cidade/sigla estado. Deve ser armazenado somente os números
# do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# Criar conta corrente
#
# O programa deve armazenar contas em uma lista, uma conta é composta por:
# agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1.
# O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta
# pertence a somente um usuário.

# Dica
#
# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF
# informado para cada usuário da lista.

# Solução:

from typing import List, Dict

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Novo usuário
[c] Nova conta
[l] Listar contas
[q] Sair
=> """

AGENCIA_PADRAO = "0001"
LIMITE_SAQUES = 3

def depositar(saldo, valor, extrato, /):
    """Depósito: argumentos apenas por posição."""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Saque: argumentos apenas por nome."""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    """Extrato: saldo por posição; extrato por nome."""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato, end="")
    print(f"Saldo:    R$ {saldo:.2f}")
    print("=========================================\n")

def normalizar_cpf(cpf: str) -> str:
    return "".join(ch for ch in cpf if ch.isdigit())

def buscar_usuario_por_cpf(usuarios: List[Dict], cpf: str):
    cpf = normalizar_cpf(cpf)
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuario(usuarios: List[Dict]):
    print("\n=== Cadastro de Usuário ===")
    cpf = normalizar_cpf(input("CPF (somente números ou em qualquer formato): ").strip())
    if not cpf:
        print("CPF inválido.")
        return

    usuario = buscar_usuario_por_cpf(usuarios, cpf)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Nome completo: ").strip()
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    uf = input("UF: ").strip().upper()

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{uf}"
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!\n")

def criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict], contas: List[Dict]):
    print("\n=== Abertura de Conta ===")
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = buscar_usuario_por_cpf(usuarios, cpf)

    if usuario:
        conta = {"agencia": agencia, "numero": numero_conta, "usuario": usuario}
        contas.append(conta)
        print(f"Conta criada com sucesso! Agência: {agencia}  Conta: {numero_conta:04d}\n")
    else:
        print("Usuário não encontrado. Cadastre o usuário antes de criar a conta.\n")

def listar_contas(contas: List[Dict]):
    print("\n=== Contas Cadastradas ===")
    if not contas:
        print("Não há contas cadastradas.\n")
        return
    for conta in contas:
        usuario = conta["usuario"]
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero']:04d} | Titular: {usuario['nome']} | CPF: {usuario['cpf']}")
    print()

def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0

    usuarios: List[Dict] = []
    contas: List[Dict] = []

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: ").strip())
            except ValueError:
                print("Entrada inválida.")
                continue
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: ").strip())
            except ValueError:
                print("Entrada inválida.")
                continue
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA_PADRAO, numero_conta, usuarios, contas)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("Encerrando. Até mais!")
            break

        else:
            print("Operação inválida. Tente novamente.")

if __name__ == "__main__":
    main()
