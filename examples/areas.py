# A Function "menu", prints the following menu:
# Triangle area
# Cirlce area
# Square area
# Rectangle area

class Type:
    def __init__(self, id, name):
        self.id = id
        self.name = name


types = [Type(1, 'triangle'),
         Type(2, 'circle'),
         Type(3, 'square'),
         Type(4, 'rectangle')]

PI_VALUE = 3.14159265359


def menu():
    for t in types:
        print(f'For the area of a {t.name} press {t.id}')
    selection = int(input('What are do you want to print?'))
    if (selection < 5) and (selection > 1):
        return selection
    else:
        print("option does not exist!")


def calculate_triangle(base, height):
    return (base * height) / 2


def calculate_circle(r):
    return r * 2 * PI_VALUE


def calculate_rectangle(l, h):
    return 2 * l + 2 * h


def calculate_square(s):
    return 4 * s


# B Function "operation" prints the result of the chosen option (from the user).
def operation(selection):
    if selection == types[0].id:
        base = int(input("insert the base"))
        height = int(input("insert the height"))
        return calculate_triangle(base, height), types[0].name
    elif selection == types[1].id:
        radius = int(input("insert the radius"))
        return calculate_circle(radius), types[1].name
    elif selection == types[3].id:
        length = int(input("insert the length"))
        height = int(input("insert the height"))
        return calculate_rectangle(length, height), types[3].name
    elif selection == types[2].id:
        side = int(input("insert the side of a square"))
        return calculate_square(side), types[2].name
    else:
        print('something is wrong with your input!')
        return 0, 'undefined'


# C Consider what will happen if the user choose an illegal option.

def main():
    selection = menu()
    result, shape = operation(selection)
    print(f'The area of a {shape} is: {result}')


main()
