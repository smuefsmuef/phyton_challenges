# Petra Kohler, a01762430@tec.mx

# Task 3
# Convert from degrees Celsius to degrees Fahrenheit.
# Enter the number of degrees Celsius you want to convert to degrees Fahrenheit.
# F = C * (9/5) +32 (use the formula to perform the conversion)
# The result should show: "X degrees Celsius corresponds to X degrees Fahrenheit".

# input
degree_celsius = float(input("Insert the number or degree Celsius you want to convert!"))

# process
degrees_fahrenheit = degree_celsius * (9/5) + 32

# output
print(f' {degree_celsius} degrees Celsius corresponds to {degrees_fahrenheit} degrees Fahrenheit.')
