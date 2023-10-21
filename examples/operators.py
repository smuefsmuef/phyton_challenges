# a) Convert the following expressions in Python and test them in the shell.
# Attach screen impressions of the results obtained as an activity.


# 5 * 6 * (160 div 2 ** 3) mod 5 * 15 - 10
result1 = 5 * 6 * (160 / 2 ** 3) % 5 * 15 - 10
print("result1: ", result1)

# ((1580 mod 6 * 2 ** 7)> (7 + 8 * 3 ** 4 )) AND ((15 * 2) == (60 * 2/4))
result2 = ((1580 % 6 * 2 ** 7) > (7 + 8 * 3 ** 4)) and ((15 * 2) == (60 * 2 / 4))
print("result2: ", result2)

# (15> = 3 ** 3) OR NOT (43 - 8 * 2 div 4 or not 3 * 3 div 3)
result3 = (15 >= 3 ** 3) or not (43 - 8 * 2 / 4 != 3 * 3 / 3)
print("result3: ", result3)

# (120> = 7 * 3 ** 2 AND 8> 3 or 15> 6) AND NOT (7 * 3 <5 + 12 * 2 div 3 ** 2)
result4 = (120 >= 7 * 3 ** 2 and 8 > 3 or 15 > 6) and not (7 * 3 < 5 + 12 * 2 / 3 ** 2)
print("result4: ", result4)

# NOT (S> 3 AND S <= 10) OR (T> = 100 AND T <200), S = 5 and T = 70.
S = 5
T = 70
result5 = not (S > 3 and S <= 10) or (T >= 100 and T < 200)
print("result5: ", result5)

# Open the Python shell and initialize 5 variables with different data types (integer, real, logical, string).
integer_var = 42
float_var = 3.14
boolean_var1 = True
boolean_var2 = False
string_var = "Hello Friday!"




