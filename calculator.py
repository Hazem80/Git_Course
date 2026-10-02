"""A simple interactive calculator."""


def main() -> None:
    while True:
        print("\n=== Calculator ===")
        print("Operations: +  -  *  /  quit")
        operation = input("Choose an operation: ").strip().lower()

        if operation == "quit":
            print("Goodbye! Thanks for using the calculator.")
            break

        if operation not in {"+", "-", "*", "/"}:
            print("Invalid operation. Please choose +, -, *, /, or quit.")
            continue

        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if operation == "+":
            result = first_number + second_number
        elif operation == "-":
            result = first_number - second_number
        elif operation == "*":
            result = first_number * second_number
        else:
            if second_number == 0:
                print("Cannot divide by zero.")
                continue
            result = first_number / second_number

        print(f"Result: {first_number} {operation} {second_number} = {result}")


if __name__ == "__main__":
    main()
