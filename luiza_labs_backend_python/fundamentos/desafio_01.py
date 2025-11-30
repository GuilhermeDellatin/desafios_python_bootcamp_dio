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


@log_transacao
def depositar(saldo: float, valor: float, transacoes: List[Dict], /):
    if valor > 0:
        saldo += valor
        transacoes.append({
            "tipo": "Depósito",
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo


@log_transacao
def sacar(*, saldo: float, valor: float, transacoes: List[Dict], limite: float, numero_saques: int, limite_saques: int):
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
        transacoes.append({
            "tipo": "Saque",
            "valor": valor,
            "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        })
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, numero_saques


@log_transacao
def exibir_extrato(saldo, /, *, transacoes):
    """
    Utiliza o Gerador para exibir o extrato.
    """
    print("\n================ EXTRATO ================")
    tem_transacao = False
    for transacao in gerador_relatorios(transacoes):
        tem_transacao = True
        print(f"{transacao['data']} - {transacao['tipo']}:\tR$ {transacao['valor']:.2f}")

    if not tem_transacao:
        print("Não foram realizadas movimentações.")

    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================\n")


def normalizar_cpf(cpf: str) -> str:
    return "".join(ch for ch in cpf if ch.isdigit())


def buscar_usuario_por_cpf(usuarios: List[Dict], cpf: str):
    cpf = normalizar_cpf(cpf)
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


@log_transacao
def criar_usuario(usuarios: List[Dict]):
    print("\n=== Cadastro de Usuário ===")
    cpf = normalizar_cpf(input("CPF (somente números): ").strip())
    if not cpf:
        print("CPF inválido.")
        return

    usuario = buscar_usuario_por_cpf(usuarios, cpf)
    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Nome completo: ").strip()
    endereco = input("Endereço completo (Logradouro, nro - Bairro - Cidade/UF): ").strip()
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


@log_transacao
def criar_conta(agencia: str, numero_conta: int, usuarios: List[Dict], contas: List[Dict]):
    print("\n=== Abertura de Conta ===")
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = buscar_usuario_por_cpf(usuarios, cpf)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero": numero_conta,
            "usuario": usuario,
            "saldo": 0.0,
            "transacoes": []
        }
        contas.append(conta)
        print(f"Conta criada com sucesso! Agência: {agencia}  Conta: {numero_conta:04d}")
    else:
        print("Usuário não encontrado.")


def listar_contas_com_iterador(contas: List[Dict]):
    print("\n=== Listagem de Contas (Via Iterador) ===")
    for info_conta in ContaIterador(contas):
        print(info_conta)
    print()

# Desafio
# Com os novos conhecimentos adquiridos sobre decoradores, geradores e iteradores
# você foi encarregado de implementar as seguintes funcionalidades no sistema:
# - Decorador de log
# - Gerador de relatórios
# - Iterador personalizado

# Decorador de log
# Implemente um decorador que seja aplicado a todas as funções de
# transações (depósito, saque, criação de conta, etc). Esse decorador
# deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação.

# Gerador de relatórios
# Criar um gerador que permita iterar sobre as transações de uma conta e retorne, uma a uma,
# as transações que foram realizadas. Esse gerador deve também ter uma forma de filtrar as
# transações baseado em seu tipo (por exemplo, apenas saques ou apenas depósitos).

# Iterador personalizado
# Implemente um iterador personalizado ContaIterador que permita iterar sobre todas as contas
# de banco, retornando informações básicas de cada conta (número, saldo atual, etc).

def log_transacao(func):
    """
    Decorador que registra a data, hora e nome da função executada.
    """
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado = func(*args, **kwargs)
        print(f"\n[LOG] {data_hora} - Função '{func.__name__}' executada.")
        return resultado

    return envelope

def gerador_relatorios(transacoes: List[Dict], tipo_filtro: str = None) -> Generator:
    """
    Gera transações uma a uma, permitindo filtrar por tipo ('saque' ou 'deposito').
    """
    for transacao in transacoes:
        if tipo_filtro is None or transacao['tipo'].lower() == tipo_filtro.lower():
            yield transacao

class ContaIterador:
    """
    Iterador que percorre a lista de contas e retorna informações básicas.
    """

    def __init__(self, contas: List[Dict]):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self.contas):
            conta = self.contas[self._index]
            self._index += 1
            return (f"Agência: {conta['agencia']} | "
                    f"Conta: {conta['numero']:04d} | "
                    f"Saldo: R$ {conta['saldo']:.2f} | "
                    f"Titular: {conta['usuario']['nome']}")
        raise StopIteration


def main():
    usuarios: List[Dict] = []
    contas: List[Dict] = []
    saldo_sessao = 0.0
    transacoes_sessao = []
    numero_saques_sessao = 0
    limite = 500.0

    while True:
        opcao = input(MENU).strip().lower()

        if opcao == "d":
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("Valor inválido.")
                continue

            saldo_sessao = depositar(saldo_sessao, valor, transacoes_sessao)

            if contas: contas[0]['saldo'] = saldo_sessao

        elif opcao == "s":
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("Valor inválido.")
                continue

            saldo_sessao, numero_saques_sessao = sacar(
                saldo=saldo_sessao,
                valor=valor,
                transacoes=transacoes_sessao,
                limite=limite,
                numero_saques=numero_saques_sessao,
                limite_saques=LIMITE_SAQUES
            )

            if contas: contas[0]['saldo'] = saldo_sessao

        elif opcao == "e":
            exibir_extrato(saldo_sessao, transacoes=transacoes_sessao)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA_PADRAO, numero_conta, usuarios, contas)

            if len(contas) == 1:
                contas[0]['saldo'] = saldo_sessao
                contas[0]['transacoes'] = transacoes_sessao

        elif opcao == "l":
            listar_contas_com_iterador(contas)

        elif opcao == "r":
            print("\n=== Relatório de Movimentações (Gerador) ===")
            tipo = input("Filtrar por (Saque/Depósito) ou [Enter] para todos: ").strip()
            filtro = tipo if tipo else None

            gen = gerador_relatorios(transacoes_sessao, filtro)
            try:
                for transacao in gen:
                    print(f"{transacao['data']} - {transacao['tipo']}: R$ {transacao['valor']:.2f}")
            except Exception as e:
                print(f"Erro ao gerar relatório: {e}")
            print()

        elif opcao == "q":
            print("Encerrando...")
            break

        else:
            print("Operação inválida.")

if __name__ == "__main__":
    main()
