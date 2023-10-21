# Petra Kohler, a01762430@tec.mx

# Task d) 2

# input
input_radius = float(input("What is the value of the radius?"))
input_height = float(input("What is the value of the height?"))

PI_VALUE = 3.14159265359


# process
def calculate_volume(radius, height):
    return PI_VALUE * radius ** 2 * height


def calculate_area(radius, height):
    return 2 * PI_VALUE * radius * (height + radius)


result_1 = calculate_volume(input_radius, input_height)
result_2 = calculate_area(input_radius, input_height)

# output
print(f'The area of the cylinder is: {result_2}.')
print(f'The volume of the cylinder is: {result_1}.')
# Note! The result in the canvas example is wrong!
