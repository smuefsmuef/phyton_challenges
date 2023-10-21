import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


list1 = [1, 3, 55, 6, 77]
list1.remove(55)  # removes value
print(list1)  # [1, 3, 6, 77]

list2 = [1, 3, 55, 6, 77, 55]
list2.remove(55)  # removes first match, [1, 3, 6, 77, 55]
print(list2)

list3 = [1, 3, 55, 6, 77]
del list3[2]  # index
print(list3)  # [1, 3, 6, 77]

print(39 in list3)
print(39 not in list3)

list2.append(33)
print(list2)

list2.insert(2, 44)  # insert 44 at index 2
print(list2)


other_list = [5, 3, 4, 5, 6, 3, 4, 6, 8, 11, 5]
x = statistics.mean(other_list)
print("the mean is: ", x)

y = statistics.median(other_list)
print("the median is: ", y)

z = statistics.mode(other_list)
print("the one that repeats the most is: ", z)

s = statistics.stdev(other_list)
print("standard deviation is: ", s)


max = max(other_list)
min = min(other_list)
print(f'the max is {max} and the min is {min}')

what = input("what o you want to count")
counting = other_list.count(what)
print(f'the number {what} is repeated {counting} times')
