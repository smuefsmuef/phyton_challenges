# Exercises
# Exercise 1
#
# Write a function called equivalent that receives as a parameter a number of hours, minutes and seconds and returns as a return value the equivalent time in seconds.
#
# For example:
#
# If the function receives the values hours = 2, minutes = 20 and seconds = 8, it will return the value 8408.
#
# Note that the function will not display anything, it just returns the equivalent number of seconds.
#
# Now write a main function in which you ask the user to type how long in hours, minutes and seconds 2 processes have taken, after asking for the time each process lasts, it must shows the equivalent time in seconds of such process.
#
# Input
#
# hours, minutes and seconds that the process 1 took
#
# hours, minutes and seconds that the process 2 took
#
# Output
#
# Time in seconds that process 1 took
#
# Time in seconds that process 2 took
#
# Examples of program execution:
#
# >>>3
# >>>15
# >>>22
# 11722
#
#
# >>>1
# >>>10
# >>>15
# 4215

def equivalent(h, m, s):
    time_in_seconds = h * 3600 + m * 60 + s
    return time_in_seconds


def main():
    hours = int(input("Enter the hours "))
    minutes = int(input("Enter the minutes "))
    seconds = int(input("Enter the seconds "))
    time = equivalent(hours, minutes, seconds)
    print(time)


main()
