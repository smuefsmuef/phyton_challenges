# Design a program that asks the user for a 1,2 or 3 digit number. Print a message to show how many digits the number has,
# or an error message if the number has more than 3 digits. This program must have at least two functions.

# asks the user for a 1,2 or 3-digit number
def get_user_input():
    while True:
        user_input = input("Enter a 1, 2, or 3 digit number: ")
        if user_input.isdigit():
            number = int(user_input)
            if 1 <= number <= 999:
                return number
            else:
                print("Number must be between 1 and 999.")
        else:
            print("Please enter a valid numeric input.")


# check digits of input and validate
def count_digits(number):
    if number < 10:
        print(f"The number {number} has 1 digit.")
    elif number < 100:
        print(f"The number {number} has 2 digits.")
    else:
        print(f"The number {number} has 3 digits.")


# Main program
def main():
    number = get_user_input()
    count_digits(number)


main()
