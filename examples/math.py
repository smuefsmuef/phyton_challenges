# Petra Kohler, a01762430@tec.mx

import matplotlib.pyplot as plt

barlist = plt.bar(["a", "b", "c", "d"], [1, 2, 3, 4])
barlist[0].set_color('r')
barlist[1].set_color('g')
barlist[2].set_color('b')
barlist[3].set_color('c')
plt.suptitle('Barchart: Amount of 4 type of data (a, b, c, d)')  # what the code does
plt.title('f.e. prices of 4 products')
plt.show()

# 3. Graph the following. (Choose the types of graphics and settings you want, be creative).
#
# A graph that shows the price of the main products you handle (minimum 5). Use a list for the product name and
# another list for the price.
#
# Another graph showing the sales of the main products they sell (minimum 5). Use the
# same list of products. Add titles, legends and names to the axes.


# fruit list
products = ["Bananas", "Mangos", "Apples", "Kiwi", "Strawberries"]
prices = [2.5, 15.0, 7.0, 6.2, 16.0]
sales = [150, 200, 120, 180, 250] # in units

# fruit prices
plt.figure(figsize=(10, 5))
plt.bar(products, prices, color='lightgreen')
plt.xlabel('Fruits')
plt.ylabel('Price CHF (per kilo)')
plt.title('Fruit Prices')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# fruit sales
plt.figure(figsize=(10, 5))
plt.pie(sales, labels=products, autopct='%1.1f%%', shadow=False, startangle=50)
plt.title('Sales per Fruit (units)')
plt.show()
