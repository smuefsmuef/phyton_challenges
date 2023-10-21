# # Chair Store
#
# In an office chair store, there are 3 types: basic, standard and deluxe.
#
# In this same store there are regular and frequent customers.
#
# The price of the chairs is:
#
# Basic $700.00 each
# Standard $900.00 each
# Deluxe $1,500.00 each
# The store owner has decided to give a 20% discount to frequent customers
#
# It has also decided to apply the following wholesale discount policy to regular customers:
#
# if your purchase is >= $10,000 and < $20,000 a 10% discount
# if your purchase is >= $20,000 a 15% discount
# Write a program that reads:
#
# the type of chair (which is a capital letter that can be B, S, D)
# the type of client (which is an uppercase letter that can be F or R) and
# the quantity to buy (which is an integer).
# Suppose that only one type of chair is to be purchased.
#
# The program must calculate and display the following data (the data is float and you must display one in each row):
#
# the price before applying any discount,
# the amount of money that is granted by discount and
# the total to be paid by the client.
# Use functions to solve your program.
#
# Input
#
# A capital letter representing the type of chair (B, S, D)
# A capital letter representing the type of customer (F, R)
# An integer indicating the number of chairs to buy.
#
# Output
#
# The price before discount
# The discount
# The total to be paid by the client
#
# Program execution example:
#
# Example  1:
#
# >>>S
# >>>F
# >>>5
# 4500
# 900.0
# 3600.0
#
# Example  2:
#
# >>>D
# >>>R
# >>>10
# 15000
# 1500.0
# 13500.0
#
# user inputs
chair_type = (input(
    "What type of chair do you wnat to buy? Type B for a basic chair. S for Standart and D for a Deluxe chair.")).upper()
customer_type = (input("Are you a frequent (F) or a regular (R) buyer?")).upper()
quantity = int(input("How many chairs do you want to buy?"))

# initial variables
price_basic = 700
price_standart = 900
price_deluxe = 1500


# methods to calculate initial price, discount and final price
def calculate_initial_price(price, quantity):
    return price * quantity


def calculate_discount(purchase, type):
    if (type == 'F'):
        return purchase * 0.2
    elif (purchase >= 10000 and purchase < 20000):
        return purchase * 0.1
    elif (purchase >= 20000):
        return purchase * 0.15
    else:
        return 0


def calculate_final_price(initial, discount):
    return initial - discount


# calculate the initial price per chair type
def calculate_initial_price_by_type(type):
    if (chair_type == 'B'):
        return calculate_initial_price(price_basic, quantity)
    elif (chair_type == 'S'):
        return calculate_initial_price(price_standart, quantity)
    else:
        return calculate_initial_price(price_deluxe, quantity)


def chair_calculator():
    if (chair_type != 'B' and chair_type != 'S' and chair_type != 'D'):
        print("please select a valid chair type")
    elif (quantity > 0):
        initial = calculate_initial_price_by_type(chair_type)
        discount = calculate_discount(initial, customer_type)
        total = calculate_final_price(initial, discount)
        print(initial)
        print(discount)
        print(total)
    else:
        print("no valid quantity")


chair_calculator()
