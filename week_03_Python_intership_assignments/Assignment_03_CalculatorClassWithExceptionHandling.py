# Calculator Class with robust Exception Handling & math library integration

import math

class Calculator:
    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Division by zero is undefined.")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    def square_root(self, val: float) -> float:
        if val < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(val)


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Invalid numeric input! Please enter a valid number.")


def main():
    calc = Calculator()

    while True:
        print("\n=== CALCULATOR WITH EXCEPTION HANDLING ===")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Exit")

        choice = input("Select operation (1-7): ").strip()

        if choice in ['1', '2', '3', '4', '5']:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")

            try:
                if choice == '1':
                    print(f"Result: {num1} + {num2} = {calc.add(num1, num2)}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {calc.subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {calc.multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Result: {num1} / {num2} = {calc.divide(num1, num2)}")
                elif choice == '5':
                    print(f"Result: {num1} ^ {num2} = {calc.power(num1, num2)}")
            except ZeroDivisionError as e:
                print(f"Math Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

        elif choice == '6':
            num = get_number("Enter number: ")
            try:
                print(f"Result: √{num} = {calc.square_root(num)}")
            except ValueError as e:
                print(f"Math Error: {e}")

        elif choice == '7':
            print("Exiting Calculator. Goodbye!")
            break
        else:
            print("Invalid selection! Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()