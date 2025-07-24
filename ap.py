import math

# My first python project. There is too much code repetition and it looks ugly but it works.
print("Welcome to Haznedar's fancy and luxury calculator!\n")

while True:
    choice = int(input(
        " 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division\n 5 - Power \n 6 - Square root\n"))

    if int(choice) == 1:
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"\nThe sum is: {num1 + num2}")
                break
            except ValueError:
                print("Please enter a valid number!")

    elif int(choice) == 2:
        while True:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                print(f"\nThe subtraction is: {num1 - num2}")
                break
            except ValueError:
                print("Please enter a valid number!")

    elif int(choice) == 3:
        while True:
            try:
                num1 = float(input("Enter the multiplicand: "))
                num2 = float(input("Enter the multiplier: "))
                print(f"\nThe product is: {num1 * num2}")
                break
            except ValueError:
                print("Please enter a valid number!")

    elif int(choice) == 4:
        while True:
            try:
                num1 = float(input("Enter the dividend: "))
                num2 = float(input("Enter the divisor: "))
                if num2 == 0:
                    print("\nThe division is: NaN")
                    break
                print(f"The division is: {num1 / num2}")
                break
            except ValueError:
                print("Please enter a valid number!")

    elif int(choice) == 5:
        while True:
            try:
                num1 = float(input("Enter the base: "))
                num2 = float(input("Enter the power: "))
                print(f"\nThe product is: {num1 ** num2}")
                break
            except ValueError:
                print("Please enter a valid number!")

    elif int(choice) == 6:
        while True:
            try:
                num1 = float(
                    input("Enter the number to take the square root "))
                print(f"\nThe product is: {math.sqrt(num1)}")
                break
            except ValueError:
                print("Please enter a valid number!")

    else:
        print("Enter a valid choice")

    while True:
        again = input(
            "\nWould you like to do a new calculation? (yes or no?): ")
        if again.lower() == "yes":
            break
        elif again.lower() == "no":
            print("\nThank you for using my calculator")
            exit()
        else:
            print("Please enter a valid ")
