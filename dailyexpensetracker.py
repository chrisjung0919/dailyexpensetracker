# Menu
def show_menu():
    print("Menu:")
    print("(1) Show current balance")
    print("(2) Deposit money")
    print("(3) Withdraw money")
    print("(4) Donate money")
    print("(5) Exit")
    print("")

# Show Current Balance
def show_balance(balance):
    print("Current balance: $", balance)

# Deposit Money
def deposit(balance):
    deposit_amount = float(input("Enter amount of money you want to deposit: $"))
    if deposit_amount > 0:
        balance += deposit_amount
        print("Deposit success!")
    else:
        print("Please enter a positive real number")
    
    return balance

# Withdraw Money
def withdraw(balance):
    withdraw_amount = float(input("Enter amount of money you want to withdraw: $"))

    if withdraw_amount > balance:
        print("Withdraw failed!")
    elif withdraw_amount > 0 and withdraw_amount <= balance:
        balance -= withdraw_amount
        print("Withdraw success!")
    else:
        print("Please enter a positive real number")
    
    return balance

# Donate Money
def donate(balance):
    donate_amount = float(input("Enter amount of money you want to donate: $"))

    if donate_amount > 0:
        number_of_people = int(input("Enter the number of people you are donating to: "))

        if number_of_people > 0:
            donate_total = donate_amount * number_of_people
            if donate_total > balance:
                print("Donate failed!")
            elif donate_total > 0 and donate_total <= balance:
                balance -= donate_total
                print("You donated ", donate_amount, " to ", number_of_people, " people")
        else:
            print("Please enter a positive real number")

    else:
        print("Please enter a positive real number")

    return balance

# Main
def main():
    user_choice = 0
    current_balance = 0.00

    print("Welcome to the Daily Expense Tracker!!!!!")

    while user_choice != 5:    
        show_menu()

        user_choice = int(input())

        if user_choice == 1:
            show_balance(current_balance)
        elif user_choice == 2:
            current_balance = deposit(current_balance)
        elif user_choice == 3:
            current_balance = withdraw(current_balance)
        elif user_choice == 4:
            current_balance = donate(current_balance)
        # Exit Program
        elif user_choice == 5:
            print("Goodbye! See you again!")
        # Wrong Choice
        else:
            print("Choose from choices 1 - 5")


if __name__ == "__main__":
    main()
