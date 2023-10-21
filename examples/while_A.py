# Petra Kohler, a01762430@tec.mx

# Write a Program that calculates the total price of a purchase given "n" selected products. You must use a loop,
# inside this loop you need to ask and print the name of the product and its price, and after the loop you must print
# the total final price.

selected_products = int(input('how many products do you want to select?'))
total_price = 0
product_number = 1

while product_number <= selected_products:
    product_name = input(f"Enter the name of product {product_number}: ")
    product_price = float(input(f"Enter the price of {product_name}: "))

    total_price = total_price + product_price

    product_number = product_number + 1

# Print the total final price
print(f"The total price for {selected_products} products is: ${total_price}")