# --- Global Constants for Credentials ---
USER_ID = "chiru"
USER_PWD = "1234"

def deposit(balance, transactions):
    """Handles depositing money."""
    try:
        amt = int(input("Enter deposit amount: "))
        if amt > 0:
            balance += amt
            transactions.append(f"Deposited: {amt}")
            print(f"₹{amt} deposited successfully.")
        else:
            print("Amount must be positive.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def withdraw(balance, transactions):
    """Handles withdrawing money."""
    try:
        amt = int(input("Enter the withdrawal amount: "))
        if amt <= 0:
            print("Amount must be positive.")
        elif amt <= balance:
            balance -= amt
            transactions.append(f"Withdrew: {amt}")
            print(f"₹{amt} withdrawn successfully.")
        else:
            print("Insufficient balance!")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return balance

def show_history(transactions):
    """Prints the transaction list."""
    print("\n--- Transaction History ---")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)

def login():
    """Handles the login process."""
    attempts = 0
    while attempts < 3:
        uid = input("Enter User ID: ")
        pwd = input("Enter Password: ")
        if uid == USER_ID and pwd == USER_PWD:
            print("Login Successful!")
            return True
        attempts += 1
        print(f"Invalid credentials. Attempts left: {3 - attempts}")
    return False

def main_menu():
    """Main controller for the banking app."""
    balance = 0
    transactions = []
    
    while True:
        print("\n1. Deposit | 2. Withdraw | 3. Balance | 4. History | 5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            balance = deposit(balance, transactions)
        elif choice == '2':
            balance = withdraw(balance, transactions)
        elif choice == '3':
            print(f"Current Balance: ₹{balance}")
        elif choice == '4':
            show_history(transactions)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

# --- Start Program ---
if login():
    main_menu()