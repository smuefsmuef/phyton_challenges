# Petra Kohler, a01762430@tec.mx

# Task 2
# A student wants to know the final grade of his Programming subject.
# The rubric of this subject is made up as follows:
# Partial 1 - 20%
# Partial 2 - 35%
# Final Project - 15%
# Final Exam - 30%

# input
p1 = int(input("What is your grade for partial 1?"))
p2 = int(input("What is your grade for partial 2?"))
fP = int(input("What is your grade for the final Project?"))
fE = int(input("What is your grade for the final Exam?"))

# process
rubric = int((p1 * 20 + p2 * 35 + fP * 15 + fE * 30) / 100)

# output
print(f'Your final grade is: {rubric}.')

