# Exercise 2
#
# Write a function called areaRect that takes the length and width of a rectangle as a parameter and returns the area of ​​the rectangle as a return value.
#
# Write a function called perimeterRect that receives as a parameter the length and width of a rectangle and  returns the perimeter of the rectangle.
#
# Note that inside the functions you will not display anything, you will only return the calculated value using return.
#
# Now write a main function that asks the user for the length and width of the rectangle and then asks if he wants to calculate the area or the perimeter of the rectangle (ask for the key a for area and p for perimeter) and then displays the value corresponding to the calculation he asked for the user.
#
# Input
#
# length of the rectangle
#
# width of the rectangle
#
# key indicating what you want to calculate a - area or p - perimeter
#
# Output
#
# The area or the perimeter of the rectangle, according to the key that has been typed
#
# Program execution examples
#
# >>>10
# >>>5
# >>>a
# 50.0
#
#
# >>>10
# >>>3
# >>>p
# 26.0

def areaRect(l, w):
    area = l * w
    return area


def perimeterRect(l, w):
    perimeter = 2 * l + 2 * w
    return perimeter


def main():
    width = float(input("Enter the width "))
    length = float(input("Enter the length "))
    answer = input("Do you wnat to calculate the area (a) or the perimeter (p). Please type your answer a or p")
    if answer == 'p':
        result = perimeterRect(length, width)
        print(result)
    elif answer == 'a':
        result = areaRect(length, width)
        print(result)
    else:
        print('no selection')


main()
