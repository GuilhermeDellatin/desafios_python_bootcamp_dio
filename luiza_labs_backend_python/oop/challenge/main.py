import textwrap
from typing import List, Optional

from bank_account import BankAccount, CheckingAccount
from bank_client import BankClient, Individual
from transaction import Deposit, Withdrawal

# ==========================================
# CLI INTERFACE & HELPER FUNCTIONS
# ==========================================

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDeposit
    [s]\tWithdraw
    [e]\tStatement
    [nc]\tNew account
    [lc]\tList accounts
    [nu]\tNew user
    [q]\tExit
    => """
    return input(textwrap.dedent(menu))


def filter_client(cpf: str, clients: List[BankClient]) -> Optional[Individual]:
    for client in clients:
        if isinstance(client, Individual) and client.cpf == cpf:
            return client
    return None


def get_client_account(client: BankClient) -> Optional[BankAccount]:
    if not client.accounts:
        print("\nError: Client has no registered accounts!")
        return None
    # Assuming the user operates on their first account for simplicity
    return client.accounts[0]


def main():
    clients: List[BankClient] = []
    accounts: List[BankAccount] = []

    while True:
        option = menu()

        if option == "d":
            cpf = input("Enter client CPF: ")
            client = filter_client(cpf, clients)

            if not client:
                print("\nError: Client not found!")
                continue

            account = get_client_account(client)
            if not account:
                continue

            try:
                value = float(input("Enter deposit amount: "))
                transaction = Deposit(value)
                client.perform_transaction(account, transaction)
            except ValueError:
                print("\nError: Invalid amount.")

        elif option == "s":
            cpf = input("Enter client CPF: ")
            client = filter_client(cpf, clients)

            if not client:
                print("\nError: Client not found!")
                continue

            account = get_client_account(client)
            if not account:
                continue

            try:
                value = float(input("Enter withdrawal amount: "))
                transaction = Withdrawal(value)
                client.perform_transaction(account, transaction)
            except ValueError:
                print("\nError: Invalid amount.")

        elif option == "e":
            cpf = input("Enter client CPF: ")
            client = filter_client(cpf, clients)

            if not client:
                print("\nError: Client not found!")
                continue

            account = get_client_account(client)
            if not account:
                continue

            print("\n================ STATEMENT ================")
            transactions = account.history.transactions

            if not transactions:
                print("No transactions have been made.")
            else:
                for t in transactions:
                    print(f"{t['date']} - {t['type']}:\t$ {t['value']:.2f}")

            print(f"\nCurrent Balance:\t$ {account.balance:.2f}")
            print("===========================================")

        elif option == "nu":
            cpf = input("Enter CPF (Numbers only): ")
            client = filter_client(cpf, clients)

            if client:
                print("\nError: A client with this CPF already exists!")
                continue

            name = input("Enter full name: ")
            birth_date = input("Enter birth date (dd-mm-yyyy): ")
            address = input("Enter address (Street, Nro - Neighborhood - City/StateAcronym): ")

            new_client = Individual(cpf, name, birth_date, address)
            clients.append(new_client)
            print("\nClient created successfully!")

        elif option == "nc":
            cpf = input("Enter client CPF: ")
            client = filter_client(cpf, clients)

            if not client:
                print("\nError: Client not found, account creation aborted!")
                continue

            account_number = len(accounts) + 1
            account = CheckingAccount.new_account(client=client, number=account_number)
            
            accounts.append(account)
            client.add_account(account)
            print("\nAccount created successfully!")

        elif option == "lc":
            if not accounts:
                print("\nNo accounts registered yet.")
            for account in accounts:
                print("=" * 40)
                print(textwrap.indent(str(account), prefix="  "))

        elif option == "q":
            print("\nThank you for using our banking system. Goodbye!")
            break

        else:
            print("\nError: Invalid option. Please select a valid operation.")


if __name__ == "__main__":
    main()
