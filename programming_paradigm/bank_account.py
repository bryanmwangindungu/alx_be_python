# main-0.py

import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance: $100

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_input = sys.argv[1]
    parts = command_input.split(':')

    command = parts[0].lower()  # Command string
    amount = float(parts[1]) if len(parts) > 1 else None  # Optional amount

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
✅ Test Examples:
In terminal / command line:

shell
Copy
Edit
python main-0.py deposit:50
# Output: Deposited: $50

python main-0.py withdraw:20
# Output: Withdrew: $20

python main-0.py withdraw:150
# Output: Insufficient funds.

python main-0.py display
# Output: Current Balance: $[amount]