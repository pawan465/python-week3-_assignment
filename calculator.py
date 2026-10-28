"""A calculator that handles common input and math errors."""

import math


class Calculator:
    def add(self, first, second):
        return first + second

    def subtract(self, first, second):
        return first - second

    def multiply(self, first, second):
        return first * second

    def divide(self, first, second):
        if second == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        return first / second

    def square_root(self, number):
        if number < 0:
            raise ValueError("A negative number has no real square root.")
        return math.sqrt(number)


def main():
    calculator = Calculator()
    print("Calculator: +  -  *  /  sqrt")
    operation = input("Operation: ").strip().lower()
    try:
        if operation == "sqrt":
            number = float(input("Number: "))
            answer = calculator.square_root(number)
        elif operation in ("+", "-", "*", "/"):
            first = float(input("First number: "))
            second = float(input("Second number: "))
            actions = {
                "+": calculator.add,
                "-": calculator.subtract,
                "*": calculator.multiply,
                "/": calculator.divide,
            }
            answer = actions[operation](first, second)
        else:
            print("Choose +, -, *, /, or sqrt.")
            return
        print(f"Answer: {answer:g}")
    except ValueError as error:
        print(f"Input error: {error}")
    except ZeroDivisionError as error:
        print(f"Math error: {error}")


if __name__ == "__main__":
    main()
