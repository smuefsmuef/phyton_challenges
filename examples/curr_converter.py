# Petra Kohler, a01762430@tec.mx

# Task 1
# Convert the price of a product from pesos to dollars,
# if you have the exchange rate of the dollar and the price in pesos of the product,
# the result should show "the price of the product in dollars is:" X.

# input
exchange_rate = float(input("Insert the exchange rate"))
mxn = float(input("Give me the pesos price for your product!"))

# process
if exchange_rate != 0 and mxn != 0:
    usd = (mxn / exchange_rate)
    # output
    print(f'the price of the product in dollars is: {usd}.')
else:
    print(f'some input is missing.')
