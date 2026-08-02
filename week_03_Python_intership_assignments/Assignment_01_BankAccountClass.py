# Bank Account Class demonstrating OOP basics (Classes, Attributes, Methods)

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print(f"Insufficient funds! Current Balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Successfully withdrew ${amount:.2f}. Remaining Balance: ${self.balance:.2f}")

    def display_balance(self):
        print(f"\n--- Account Summary ---")
        print(f"Account Holder : {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("-----------------------")


def main():
    print("=== BANK ACCOUNT DEMO ===")
    holder_name = input("Enter account holder name: ").strip() or "Guest User"
    account = BankAccount(holder_name, 100.0)  # Starts with default $100 bonus

    while True:
        print("\n1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            try:
                amt = float(input("Enter deposit amount: "))
                account.deposit(amt)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            try:
                amt = float(input("Enter withdrawal amount: "))
                account.withdraw(amt)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '3':
            account.display_balance()
        elif choice == '4':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()