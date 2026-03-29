from __future__ import annotations

import textwrap
from collections.abc import Sequence

from bank_account import BankAccount, CheckingAccount, OperationResult
from bank_client import BankClient, Individual
from transaction import Deposit, Withdrawal

MENU_TEXT = textwrap.dedent(
    """\
    ================ MENU ================
    [d]\tDeposit
    [s]\tWithdraw
    [e]\tStatement
    [nc]\tNew account
    [lc]\tList accounts
    [nu]\tNew user
    [q]\tExit
    => """
)


def menu() -> str:
    return input(MENU_TEXT)


def filter_client(cpf: str, clients: Sequence[BankClient]) -> Individual | None:
    for client in clients:
        if isinstance(client, Individual) and client.cpf == cpf:
            return client
    return None


def get_client_account(client: BankClient) -> BankAccount | None:
    if not client.accounts:
        print("\nError: Client has no registered accounts!")
        return None

    return client.accounts[0]


def get_client_by_cpf(clients: Sequence[BankClient]) -> Individual | None:
    cpf = input("Enter client CPF: ")
    client = filter_client(cpf, clients)
    if client is None:
        print("\nError: Client not found!")
    return client


def read_amount(message: str) -> float | None:
    try:
        return float(input(message))
    except ValueError:
        print("\nError: Invalid amount.")
        return None


def print_operation_result(result: OperationResult) -> None:
    print(f"\n{result.message}")


def handle_deposit(clients: Sequence[BankClient]) -> None:
    client = get_client_by_cpf(clients)
    if client is None:
        return

    account = get_client_account(client)
    if account is None:
        return

    value = read_amount("Enter deposit amount: ")
    if value is None:
        return

    result = client.perform_transaction(account, Deposit(value))
    print_operation_result(result)


def handle_withdrawal(clients: Sequence[BankClient]) -> None:
    client = get_client_by_cpf(clients)
    if client is None:
        return

    account = get_client_account(client)
    if account is None:
        return

    value = read_amount("Enter withdrawal amount: ")
    if value is None:
        return

    result = client.perform_transaction(account, Withdrawal(value))
    print_operation_result(result)


def handle_statement(clients: Sequence[BankClient]) -> None:
    client = get_client_by_cpf(clients)
    if client is None:
        return

    account = get_client_account(client)
    if account is None:
        return

    print("\n================ STATEMENT ================")
    transactions = account.history.transactions

    if not transactions:
        print("No transactions have been made.")
    else:
        for transaction in transactions:
            print(
                f"{transaction['date']} - {transaction['type']}:\t"
                f"$ {transaction['value']:.2f}"
            )

    print(f"\nCurrent Balance:\t$ {account.balance:.2f}")
    print("===========================================")


def handle_new_user(clients: list[BankClient]) -> None:
    cpf = input("Enter CPF (Numbers only): ")
    if filter_client(cpf, clients):
        print("\nError: A client with this CPF already exists!")
        return

    name = input("Enter full name: ")
    birth_date = input("Enter birth date (dd-mm-yyyy): ")
    address = input("Enter address (Street, Nro - Neighborhood - City/StateAcronym): ")

    clients.append(Individual(cpf, name, birth_date, address))
    print("\nClient created successfully!")


def handle_new_account(
    clients: Sequence[BankClient], accounts: list[BankAccount]
) -> None:
    client = get_client_by_cpf(clients)
    if client is None:
        print("\nError: Account creation aborted!")
        return

    account_number = len(accounts) + 1
    account = CheckingAccount.new_account(client=client, number=account_number)

    accounts.append(account)
    client.add_account(account)
    print("\nAccount created successfully!")


def handle_list_accounts(accounts: Sequence[BankAccount]) -> None:
    if not accounts:
        print("\nNo accounts registered yet.")
        return

    for account in accounts:
        print("=" * 40)
        print(textwrap.indent(str(account), prefix="  "))


def main() -> None:
    clients: list[BankClient] = []
    accounts: list[BankAccount] = []

    while True:
        option = menu()

        match option:
            case "d":
                handle_deposit(clients)
            case "s":
                handle_withdrawal(clients)
            case "e":
                handle_statement(clients)
            case "nu":
                handle_new_user(clients)
            case "nc":
                handle_new_account(clients, accounts)
            case "lc":
                handle_list_accounts(accounts)
            case "q":
                print("\nThank you for using our banking system. Goodbye!")
                break
            case _:
                print("\nError: Invalid option. Please select a valid operation.")


if __name__ == "__main__":
    main()
