import math

# My first python project. Refactored to remove repetition and improve readability.


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")


def addition():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"\nThe sum is: {num1 + num2}")


def subtraction():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    print(f"\nThe subtraction is: {num1 - num2}")


def multiplication():
    num1 = get_number("Enter the multiplicand: ")
    num2 = get_number("Enter the multiplier: ")
    print(f"\nThe product is: {num1 * num2}")


def division():
    num1 = get_number("Enter the dividend: ")
    num2 = get_number("Enter the divisor: ")
    if num2 == 0:
        print("\nThe division is: NaN")
    else:
        print(f"The division is: {num1 / num2}")


def power():
    num1 = get_number("Enter the base: ")
    num2 = get_number("Enter the power: ")
    print(f"\nThe result is: {num1 ** num2}")


def square_root():
    num1 = get_number("Enter the number to take the square root: ")
    print(f"\nThe result is: {math.sqrt(num1)}")


def main():
    print("Welcome to Haznedar's fancy and luxury calculator!\n")
    operations = {
        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: power,
        6: square_root
    }
    while True:
        try:
            choice = int(input(
                " 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division\n 5 - Power \n 6 - Square root\n"))
            if choice in operations:
                operations[choice]()
            else:
                print("Enter a valid choice")
        except ValueError:
            print("Please enter a valid choice!")
        while True:
            again = input(
                "\nWould you like to do a new calculation? (yes or no?): ")
            if again.lower() == "yes":
                break
            elif again.lower() == "no":
                print("\nThank you for using my calculator")
                return
            else:
                print("Please enter a valid answer (yes or no)")


if __name__ == "__main__":
    main()
