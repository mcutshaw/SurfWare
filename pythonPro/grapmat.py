import random, logging
from more_itertools import divide
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

class tris3:

    #def setup():
    def __init__(self, fig, ax1, x, y, z):
        fig = plt.figure()                               # create a new figure for plotting
        self.ax1 = fig.add_subplot(111, projection='3d') # create a new subplot on our figure and set projection as 3d
        self.x = [0, 10, 5, 5]
        self.y = [0, 0, 10, 5]
        self.z = [0, 0, 0, 10]
        self.last = [5, 5, 10]
        #return ax1, x, y, z
    def midpoint(self):
        for i in range(1000):
            v_num = random.randint(0, 3) #select other starting point #TODO: make sure they are not the same point
            x = self.x[v_num]
            y = self.y[v_num]
            z = self.z[v_num]
            #logging.warning(f"a is {a} and b is {b} ")
            self.x.append((x + self.last[0]) / 2)
            self.y.append((y + self.last[1]) / 2)
            self.z.append((z + self.last[2]) / 2)
            self.last = [self.x[-1], self.y[-1], self.z[-1]]

    def display(self):
        self.ax1.scatter(self.x, self.y, self.z, c = 'm', marker = 'o')
        self.ax1.set_xlabel('x-axis')
        self.ax1.set_ylabel('y-axis')
        self.ax1.set_zlabel('z-axis')
        plt.show()
if __name__ == "__main__":
    logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.WARNING)
    j = tris3(1, 2, 3, 4, 5)
    j.midpoint()
    j.display()
