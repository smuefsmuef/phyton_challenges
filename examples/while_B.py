# Petra Kohler, a01762430@tec.mx

# Write a program that accumulates "number_of_deposits" deposits of a savings account during a month. You need to use
# a loop that asks the month and the amount to deposit. At the end you must print the total savings of that month.
# You must validate that the given month is the current month, print an error and proceed with the next iteration of
# the loop. You must also print, at the end, the amount of CORRECT deposits done.


# Get the current month
current_month = 'October'

number_of_deposits = int(input("Enter the number of deposits: "))
total_savings = 0
correct_deposits = 0


while number_of_deposits > 0:
    month = input("Enter the month for the deposit (f.e. October): ")

    if month != current_month:
        print("Invalid month. Please enter the current month.")
        continue

    amount = float(input("Enter the amount to deposit: "))
    total_savings = total_savings + amount
    correct_deposits = correct_deposits + 1
    number_of_deposits = number_of_deposits - 1

print(f"The total savings for {current_month} is: ${total_savings:.2f}")
print(f"Number of correct deposits made: {correct_deposits}")
