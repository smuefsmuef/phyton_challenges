# Create
# matrix
# of
# consecutive
# numbers
# per
# row
# Write
# a
# program
# that
# creates
# a
# matrix
# of
# n
# rows and m
# columns
# that
# must
# be
# filled
# with consecutive numbers per row starting with 1.
#
# Input
#
# Two
# integers
# greater
# than or equal
# to
# 2
# that
# will
# represent
# the
# number
# of
# rows
# n(number
# of
# lists) and the
# number
# of
# columns
# m(number
# of
# elements in each
# list), in that
# order.
#
# Output
#
# An
# n
# x
# m
# matrix
# with consecutive numbers starting at 1 and per row.
#
# If
# any
# of
# the
# numbers
# received is not greater
# than or equal
# to
# 2, the
# message
# "Error" is displayed.
#
# Program
# execution
# example
#
# >> > 3
# >> > 2
# [[1, 2], [3, 4], [5, 6]]
#
# >> > 3
# >> > 3
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# >> > 1
# >> > -3
# Error

import numpy as np

# Get input values for n (number of rows) and m (number of columns)
n = int(input("Enter the number of rows (greater than or equal to 2): "))
m = int(input("Enter the number of columns (greater than or equal to 2): "))

# Check if input values are valid
if n < 2 or m < 2:
    print("Error")
else:
    # Create a 2D NumPy array with consecutive numbers
    matrix = np.arange(1, n * m + 1).reshape(n, m)

    # Convert the NumPy array to a list of lists
    matrix_list = matrix.tolist()

    # Print the resulting matrix
    print(matrix_list)

# or without numpy

# Get input values for n (number of rows) and m (number of columns)
n = int(input("Enter the number of rows (greater than or equal to 2): "))
m = int(input("Enter the number of columns (greater than or equal to 2): "))

# Check if input values are valid
if n < 2 or m < 2:
    print("Error")
else:
    # Initialize a variable to keep track of the current number
    current_number = 1

    # Create an empty list to store the matrix
    matrix = []

    # Loop through rows
    for i in range(n):
        # Create an empty row
        row = []

        # Loop through columns
        for j in range(m):
            # Append the current number to the row
            row.append(current_number)

            # Increment the current number
            current_number += 1

        # Append the row to the matrix
        matrix.append(row)

    # Print the resulting matrix
    for row in matrix:
        print(row)
