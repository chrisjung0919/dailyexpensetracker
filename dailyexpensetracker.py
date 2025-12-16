user_choice = 0
current_balance = 0.00
deposit_amount = 0.00
withdraw_amount = 0.00
donate_amount = 0.00
number_of_people = 0
donate_total = 0.00

print("Welcome to the Daily Expense Tracker!!!!!")

while user_choice != 5:

    print("Menu:")
    print("(1) Show current balance")
    print("(2) Deposit money")
    print("(3) Withdraw money")
    print("(4) Donate money")
    print("(5) Exit")
    print("")

    user_choice = int(input())

    # Show current balance
    if user_choice == 1:
        print("Current balance: $", current_balance)

    # Deposit money
    elif user_choice == 2:
        deposit_amount = float(input("Enter amount of money you want to deposit: $"))

        if deposit_amount > 0:
            current_balance += deposit_amount
            print("Deposit success!")
        else:
            print("Please enter a positive real number")

    elif user_choice == 3:
        withdraw_amount = float(input("Enter amount of money you want to withdraw: $"))

        if withdraw_amount > current_balance:
            print("Withdraw failed!")
        elif withdraw_amount > 0 and withdraw_amount <= current_balance:
            current_balance -= withdraw_amount
            print("Withdraw success!")
        else:
            print("Please enter a positive real number")

    elif user_choice == 4:
        donate_amount = float(input("Enter amount of money you want to donate: $"))

        if donate_amount > 0:
            number_of_people = int(input("Enter the number of people you are donating to: "))

            if number_of_people > 0:
                donate_total = donate_amount * number_of_people
                if donate_total > current_balance:
                    print("Donate failed!")
                elif donate_total > 0 and donate_total <= current_balance:   
                    current_balance -= donate_total
                    print("You donated ", donate_amount, " to ", number_of_people, " people")
            else:
                print("Please enter a positive real number")

        else:
            print("Please enter a positive real number")

    elif user_choice == 5:
        print("Goodbye! See you again!")

    else:
        print("Choose from choices 1 - 5")