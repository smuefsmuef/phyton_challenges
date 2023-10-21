# a) Function "askColors" asks the user for a primary color (red, blue, yellow).
def askColors():
    color1 = input("What is the first primary color? Choose red, blue or yellow").lower()
    color2 = input("What is the second primary color? Choose red, blue or yellow").lower()
    return color1, color2


# b) Function "mixColors" prints the corresponding mixed color (purple, orange, green).
# red & blue = purple
# red & yellow = orange
# blue & yellow = green
def mixColors(colors):
    if colors[0] != colors[1]:
        if colors[0] == 'red' and colors[1] == 'blue':
            return 'purple'
        elif colors[0] == 'red' and colors[1] == 'yellow':
            return 'orange'
        elif colors[1] == 'red' and colors[0] == 'blue':
            return 'purple'
        elif colors[1] == 'red' and colors[0] == 'yellow':
            return 'orange'
        else:
            return 'green'
    else:
        return "No mixing! The color just stays " + colors[0]


def main():
    colors = askColors()
    # check that the colors are primary
    if ((colors[0] == 'red' or colors[0] == 'yellow' or colors[0] == 'blue') and (colors[1] == 'red' or colors[1] ==
                                                                                  'yellow' or colors[1] == 'blue')):
        result = mixColors(colors)
        print(result)
    else:
        print('no primary color')


main()
