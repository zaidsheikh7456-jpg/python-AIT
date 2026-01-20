print("===== Welcome to ATM Machine =====")

# Fixed data
pin = 1234
balance = 5000

entered_pin = int(input("Enter your PIN: "))

if entered_pin == pin:
    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1:
            print("Your Balance is:", balance)

        elif choice == 2:
            withdraw = int(input("Enter withdraw amount: "))
            if withdraw <= balance:
                balance -= withdraw
                print("Withdraw successful")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance")

        elif choice == 3:
            deposit = int(input("Enter deposit amount: "))
            balance += deposit
            print("Deposit successful")
            print("Updated Balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN ❌ Access Denied")
