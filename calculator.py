
import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a, b):
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Cannot modulo by zero.")
    return a % b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return math.sqrt(a)


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    menu = (
        "\nPython Calculator\n"
        "1) Add\n"
        "2) Subtract\n"
        "3) Multiply\n"
        "4) Divide\n"
        "5) Power\n"
        "6) Modulo\n"
        "7) Square root\n"
        "8) Exit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an operation (1-8): ").strip()

        try:
            if choice == "1":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                result = add(x, y)
            elif choice == "2":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                result = subtract(x, y)
            elif choice == "3":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                result = multiply(x, y)
            elif choice == "4":
                x = get_float("Enter the numerator: ")
                y = get_float("Enter the denominator: ")
                result = divide(x, y)
            elif choice == "5":
                x = get_float("Enter the base number: ")
                y = get_float("Enter the exponent: ")
                result = power(x, y)
            elif choice == "6":
                x = get_float("Enter the first number: ")
                y = get_float("Enter the second number: ")
                result = modulo(x, y)
            elif choice == "7":
                x = get_float("Enter the numbers: ")
                result = square_root(x)
            elif choice == "8":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number from 1 to 8.")
                continue

            print(f"Result: {result}\n")
        except ValueError as exc:
            print(f"Error: {exc}\n")


if __name__ == "__main__":
    main()
