# Petra Kohler, a01762430@tec.mx

# Task 3
#  A bakery sales $15 each bread loaf. Every bread loaf that is not from today has a discount of 60%.
#  Write a program called "bread", that receives a number of non-fresh bread loaves.
# It will print a description of the normal price, the descount, and the total amount to pay given the discount.

number_non_fresh_loaves = int(input("Give me the number of non fresh loaves!"))
fresh_loaves_price = 15
discount_percentage = 60


def calculate_final_price(number, price, discount):
    total1 = number * price
    return total1 - total1 * discount/100


def bread(amount_loaves):
    final_price = calculate_final_price(amount_loaves, fresh_loaves_price, discount_percentage)
    print(f'The costs of a fresh loave is: {fresh_loaves_price} pesos')
    print(f'The discount is: {discount_percentage} %')
    print(f'The final price is {final_price}')


bread(number_non_fresh_loaves)
