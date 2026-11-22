# main.py
# SmartCalc - Python Calculator & Website Launcher

import os
import webbrowser


def run_terminal_calculator():
    """Terminal calculator built using only loops and conditions."""
    while True:
        print("\n==============================")
        print("      SIMPLE CALCULATOR       ")
        print("==============================")

        # 1. Ask for first number
        try:
            num1 = float(input("Enter first number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # 2. Ask for operator
        operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")

        # Condition to quit
        if operator.lower() == "q":
            print("Exiting calculator. Goodbye!")
            break

        # 3. Ask for second number
        try:
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        # 4. Conditions for operations (+, -, *, /)
        if operator == "+":
            result = num1 + num2
            print("\nResult:", num1, "+", num2, "=", result)

        elif operator == "-":
            result = num1 - num2
            print("\nResult:", num1, "-", num2, "=", result)

        elif operator == "*":
            result = num1 * num2
            print("\nResult:", num1, "*", num2, "=", result)

        elif operator == "/":
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print("\nResult:", num1, "/", num2, "=", result)

        else:
            print("\nInvalid operator! Please use +, -, *, or /.")

        # 5. Loop condition: ask user if they want to continue
        choice = input("\nDo you want to do another calculation? (yes/no): ").lower()
        if choice != "yes" and choice != "y":
            print("Thank you for using the calculator. Goodbye!")
            break


def open_website():
    """Opens the interactive website (index.html) in your browser."""
    file_path = os.path.abspath("index.html")
    print(f"\nOpening interactive website: file://{file_path}")
    webbrowser.open(f"file://{file_path}")


def main():
    print("====================================")
    print("       SMARTCALC LAUNCHER           ")
    print("====================================")
    print("1. Launch Interactive Website (Browser)")
    print("2. Run Terminal Calculator (Loops & Conditions)")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        open_website()
    elif choice == "2":
        run_terminal_calculator()
    else:
        print("Goodbye!")


if __name__ == "__main__":
    main()
