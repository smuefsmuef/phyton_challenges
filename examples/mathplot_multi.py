# To include several graphs on the screen, use the subplot (rcp - rows, columns, position) before making the graph.
import matplotlib.pyplot as plt

x = ['pears', 'apples', 'bananas']
y1 = [1, 5, 3]
y2 = [- 4, 3, 6]

# divide the screen into 1 line, 2 columns and start in quadrant 1
plt.subplot(121)
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('This month')
plt.plot(x, y1, 'g*:', label='This month')

# splits the screen into 1 line, 2 columns and start in quadrant 2
plt.subplot(122)
plt.xlabel('Fruits')
plt.ylabel('Quantity')
plt.title('Previous month')
plt.plot(x, y2, 'b<-')
plt.show()
