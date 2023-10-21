# Petra Kohler, a01762430@tec.mx

# After reviewing the material and listening to the explanation, do the following:
# Create a list with your last semester grades from the three periods.

# Get the following using the functions seen in the presentation:
# Average.
# Mode.
# Maximum.
# Minimum.
# Standard deviation.
# How many 100 did you get?
# How many 70 did you get

import statistics

grades = []


def collectGrades():
    amount = int(input("How many values do you want to insert?"))
    while amount > 0:
        grades.append(int(input(f"Add your grade")))
        amount = amount - 1


def applyStatistics():
    average = statistics.mean(grades)
    print("My average is: ", average)
    mean = statistics.mode(grades)
    print("the one that repeats the most is: ", mean)
    maximum = max(grades)
    minimum = min(grades)
    print(f'the max is {maximum} and the min is {minimum}')
    standart_deviation = statistics.stdev(grades)
    print("standard deviation is: ", standart_deviation)
    what = input("what grade you want to count")
    counting = grades.count(what) + 1
    print(f'the grade {what} is present: {counting} times')

    if average > 70:
        return "you're doing fine"
    else:
        return "your average is under 70 - you suck"


def main():
    collectGrades()
    print("My grades are: ", grades)
    conclusion = applyStatistics()
    print(conclusion)


main()
