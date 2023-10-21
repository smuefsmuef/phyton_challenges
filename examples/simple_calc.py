# Exercise 3
#
# Write a function that receives 2 integers as a parameter and a key that is a letter.
#
# The key represents an arithmetic operation according to the following table:
#
# Key Meaning
#
# a       Add
# s       Subtract
# m     Multiply
# d      Divide
#
# The function must apply the arithmetic operation to the 2 received values and return the result as a return value.
#
# Note that inside the function you will not display anything, you will only return the value using return.
#
# Now write a main function in which you ask the user to type 2 numeric values and a key (a, s, m, d), then call the
# function with the corresponding parameters and then display the result of the operation that the function returned.
#
# Input
#
# value 1
#
# value 2
#
# key code
#
# Output
#
# The result of the operation that is specified with the key
#
# Program execution examples:
#
# >>>5
# >>>3
# >>>s
#
# 2
#
# >>>10
# >>>2
# >>>m
# 20
#
def calculate(a, b, operation):
    if (operation == 'a'):
        return a + b
    elif (operation == 's'):
        return a - b
    elif (operation == 'm'):
        return a * b
    elif (operation == 'd'):
        return a / b
    else:
        return 0


def main():
    input1 = int(input("Enter input 1 "))
    input2 = int(input("Enter input 2 "))
    answer = input("what operation do you wanna do?")

    result = calculate(input1, input2, answer)
    print(f'{result}')


main()
