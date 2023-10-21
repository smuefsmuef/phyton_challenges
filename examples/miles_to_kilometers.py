# Petra Kohler, a01762430@tec.mx

# Task 1
# Write a function called "kilometers", that receives "miles". It will return the converted miles to kilometers.

miles_input = float(input("Give me the miles you run"))


def kilometers(ml):
    km = ml * 1.609
    print(f'{ml} are equal to {km}')


kilometers(miles_input)
