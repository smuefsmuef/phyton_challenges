import matplotlib.pyplot as plt
import numpy as np

other_list = [5, 3, 4, 5, 2]

plt.xlabel("x axis blabla")
plt.ylabel("y axis upsi dupsi")
plt.title("this is a title")
plt.xticks(rotation=45)

plt.bar(["SON", "BC", "TEST", "TEST2", "TEST3"], [2.2, 6, 2.4, 3, 1.2])

plt.show()

# plot(x,y,z) = Plot the elements of list x against the elements of y with the settings in s.
# s is a string that indicates how to display the graph.

