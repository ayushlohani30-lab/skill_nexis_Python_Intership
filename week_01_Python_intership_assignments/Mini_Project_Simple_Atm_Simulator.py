import sys

def show_menu():
    print("\n=========================")
    print("      ATM SIMULATOR      ")
    print("=========================")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("=========================")

def main():
    # Starting balance and default PIN
    balance = 1000.0  # Starting with a default balance
    correct_pin = "1234"
    
    print("Welcome to the Python Bank ATM!")
    
    # 1. PIN Verification (Simple security check)
    attempts = 3
    while attempts > 0:
        entered_pin = input("Please enter your 4-digit PIN: ")
        if entered_pin == correct_pin:
            print("\nPIN Verified successfully!")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts remaining: {attempts}")
            if attempts == 0:
                print("Too many incorrect attempts. Card blocked. Exiting...")
                sys.exit()

    # 2. Main ATM loop
    while True:
        show_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            # Check Balance
            print(f"\nYour current balance is: ${balance:.2f}")
            
        elif choice == '2':
            # Deposit Money
            try:
                deposit_amount = float(input("\nEnter deposit amount: $"))
                if deposit_amount > 0:
                    balance += deposit_amount
                    print(f"Successfully deposited ${deposit_amount:.2f}")
                    print(f"New balance: ${balance:.2f}")
                else:
                    print("Error: Deposit amount must be greater than zero.")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '3':
            # Withdraw Money
            try:
                withdraw_amount = float(input("\nEnter withdrawal amount: $"))
                if withdraw_amount <= 0:
                    print("Error: Withdrawal amount must be greater than zero.")
                elif withdraw_amount > balance:
                    print("Error: Insufficient funds!")
                else:
                    balance -= withdraw_amount
                    print(f"Successfully withdrew ${withdraw_amount:.2f}")
                    print(f"Remaining balance: ${balance:.2f}")
            except ValueError:
                print("Error: Please enter a valid number.")
                
        elif choice == '4':
            # Exit
            print("\nThank you for using our ATM. Goodbye!")
            break
            
        else:
            print("\nInvalid selection. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()