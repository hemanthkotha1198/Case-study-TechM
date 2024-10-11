class BankAccount:
    def __init__(self, account_number: str, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")
        print(f"Amount {amount} deposited successfully.")

    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn: {amount}")
            print(f"Amount {amount} withdrawn successfully.")

    def transfer(self, other_account: 'BankAccount', amount: float):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            other_account.balance += amount
            self.transactions.append(f"Transferred: {amount} to {other_account.account_holder}")
            other_account.transactions.append(f"Received: {amount} from {self.account_holder}")
            print(f"Amount {amount} transferred successfully.")

    def print_transactions(self):
        if not self.transactions:
            print("No transactions to show.")
        else:
            print("Transaction history:")
            for transaction in self.transactions:
                print(transaction)

def main():
    accounts = {}

    while True:
        print("\n1. Create Account")
        print("2. View Account Data")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer Funds")
        print("6. Print Transaction History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acc_number = input("Enter new account number: ")
            acc_holder = input("Enter account holder's name: ")
            if acc_number in accounts:
                print("Account number already exists!")
            else:
                accounts[acc_number] = BankAccount(acc_number, acc_holder)
                print(f"Account created for {acc_holder}.")

        elif choice == "2":
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                acc = accounts[acc_number]
                print(f"Account Holder: {acc.account_holder}")
                print(f"Account Balance: {acc.balance}")
            else:
                print("Account not found!")

        elif choice == "3":
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                try:
                    amount = float(input("Enter deposit amount: "))
                    accounts[acc_number].deposit(amount)
                except ValueError:
                    print("Invalid amount entered!")
            else:
                print("Account not found!")

        elif choice == "4":
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    accounts[acc_number].withdraw(amount)
                except ValueError:
                    print("Invalid amount entered!")
            else:
                print("Account not found!")

        elif choice == "5":
            from_acc = input("Enter your account number: ")
            if from_acc in accounts:
                to_acc = input("Enter recipient's account number: ")
                if to_acc in accounts:
                    try:
                        amount = float(input("Enter transfer amount: "))
                        accounts[from_acc].transfer(accounts[to_acc], amount)
                    except ValueError:
                        print("Invalid amount entered!")
                else:
                    print("Recipient's account not found!")
            else:
                print("Your account not found!")

        elif choice == "6":
            acc_number = input("Enter account number: ")
            if acc_number in accounts:
                accounts[acc_number].print_transactions()
            else:
                print("Account not found!")

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
