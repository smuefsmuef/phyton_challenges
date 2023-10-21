# Petra Kohler, a01762430@tec.mx

# Task 2
# Write a function called "modyMass", that will ask for the user's weight and height.
# It will return the calculated BMI (Body Mass Index).


weight_input = float(input("Give me your weight in kg"))
height_input = float(input("Give me your height in meters"))


def mody_mass(weight, height):
    bmi = weight / height**2
    print(f'Your BMI is {bmi}')


mody_mass(weight_input, height_input)