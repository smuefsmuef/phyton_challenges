# Create a matrix of equal numbers per row
# Write a program that asks the user for the size n of a square matrix and then creates a matrix with n rows, each row must have n data with the number corresponding to the row number. Look at the example.
#
# Write two functions:
# 1) a function create_matrix_numbers that receives the size of the matrix and creates the matrix with the numbers, and
# 2) a function display_matrix that displays the elements in the form of a matrix on the screen
#
# Input
#
# An integer n greater than or equal to 2 that represents the number of rows in the matrix.
#
# Output
#
# A matrix of size n x n. Each line of the matrix must contain in each cell the value of the number of the row of the matrix.
#
# If the value n received is not greater than or equal to 2, the message "Error" is displayed.
#
# Program execution example:
#
# >>>4   <---- Square matrix size
# 0  0  0  0
# 1  1  1  1
# 2  2  2  2
# 3  3  3  3
#
#
# >>>2
# 0  0
# 1  1


def create_matrix_numbers(n):
    if n < 2:
        print("Error")
        return None

    matrix = []
    for i in range(n):
        row = [i] * n  # Create a row with the same number 'i' repeated 'n' times
        matrix.append(row)

    return matrix


def display_matrix(matrix):
    if matrix is None:
        return

    for row in matrix:
        print(" ".join(map(str, row)))  # Convert elements to strings and join them with spaces


# Get user input for the size of the square matrix
n = int(input("Enter the size of the square matrix (greater than or equal to 2): "))

# Create the matrix
matrix = create_matrix_numbers(n)

# Display the matrix
display_matrix(matrix)
