def main():
    card_inserted()
    options_to_select()

def card_inserted():
    while True:
        card = input("Please insert your card ( yes/no)(press yes if selected): ").strip().lower()

        if card == "yes":
            print("Card accepted.")
            break
        else:
            print("Please insert your card.")

def options_to_select():
    balance = 10000
    while True:
        print("\n Select what yoy wabt to perform : ")
        print("1.Check Balance")
        print("2.Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=input("Select an option: (1 or 2 or 3 or 4) ").lower().strip()
        if choice == "1":
            print("Your balance is:", balance)

           
        elif choice == "2":
            amount = float(input("Enter amount you want to deposit: "))
            balance += amount
            print("Deposit complete.")
            print("Current balance:", balance)

        elif choice == "3":
            amount = float(input("Enter amount you want to withdraw: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash.")
                print("Current balance:", balance)
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid option.")


main()

