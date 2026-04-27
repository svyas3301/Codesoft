print("Welcome to my Calculator Project")

print("----- Simple Calculator -----")

while True:
    # taking input
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    # calculation
    if choice == "1":
        print("Result:", num1 + num2)

    elif choice == "2":
        print("Result:", num1 - num2)

    elif choice == "3":
        print("Result:", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid choice")

    # ask user to continue
    again = input("\nDo you want to calculate again? (yes/no): ").lower()

    if again != "yes":
        print("Calculator closed. Thank you!")
        break
