# Petra Kohler, a01762430@tec.mx

# Task d) 1

# input
input_a = float(input("What is the value of a?"))
input_b = float(input("What is the value of b?"))
input_c = float(input("What is the value of c?"))


# process
def positive_root(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) * 1 / 2) / 2 * a


def negative_root(a, b, c):
    return (-b - (b ** 2 - 4 * a * c) * 1 / 2) / 2 * a


result_1 = positive_root(input_a, input_b, input_c)
result_2 = negative_root(input_a, input_b, input_c)

# output
print(f'Positive root is: {result_1}.')
print(f'Negative root is: {result_2}.')

