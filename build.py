
accounts = {}

def create_account():
    account_number = input("Enter account number: ")
    name = input("Enter account holder name: ")
    initial_balance = float(input("Enter initial balance: "))
    accounts[account_number] = {"name": name, "balance": initial_balance}
    print("Account created successfully.")

def perform_transaction():
    account_number = input("Enter account number: ")
    if account_number in accounts:
        transaction_type = input("Enter transaction type (deposit/withdraw): ")
        amount = float(input("Enter amount: "))
        if transaction_type == "deposit":
            accounts[account_number]["balance"] += amount
            print("Amount deposited successfully.")
        elif transaction_type == "withdraw":
            if accounts[account_number]["balance"] >= amount:
                accounts[account_number]["balance"] -= amount
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid transaction type.")
    else:
        print("Account not found.")

def update_account_info():
    account_number = input("Enter account number: ")
    if account_number in accounts:
        name = input("Enter new account holder name: ")
        accounts[account_number]["name"] = name
        print("Account information updated successfully.")
    else:
        print("Account not found.")

def delete_account():
    account_number = input("Enter account number: ")
    if account_number in accounts:
        del(accounts[account_number])
        print("Account deleted successfully.")
    else:
        print("Account not found.")

def search_account_info():
    account_number = input("Enter account number: ")
    if account_number in accounts:
        print("Account Number:", account_number)
        print("Account Holder Name:", accounts[account_number]["name"])
        print("Account Balance:", accounts[account_number]["balance"])
    else:
        print("Account not found.")

def view_customers_list():
    if accounts:
        for account_number, info in accounts.items():
            print("Account Number:", account_number)
            print("Account Holder Name:", info["name"])
            print("Account Balance:", info["balance"])
            print("-" * 20)
    else:
        print("No accounts found.")

def exit_system():
    print("Exiting system...")
    sys.exit()

def main():
    while True:
        print("""
        1. Create Account
        2. Perform Transaction
        3. Update Account Info
        4. Delete Account
        5. Search Account Info
        6. View Customer's List
        7. Exit System
        """)
        command = input("Enter your command: ")

        if command == '1':
            create_account()
        elif command == '2':
            perform_transaction()
        elif command == '3':
            update_account_info()
        elif command == '4':
            delete_account()
        elif command == '5':
            search_account_info()
        elif command == '6':
            view_customers_list()
        elif command == '7':
            exit_system()
        else:
            print("Invalid command. Please try again.")
if __name__ == "__main__":
    main()