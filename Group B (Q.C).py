"""
x = [1, 2, 3, 4, 5,9]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("My Plot")
plt.show()

"""

#In the above code the dimension of x and y is not same. to fix the error, I have removed one object/num from x list
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.title("My Plot")
plt.show()
