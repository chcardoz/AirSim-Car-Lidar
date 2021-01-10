
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    with open('lidar_data.csv', 'r'):
        data = pd.read_csv('lidar_data.csv')
        x = data['x_coordinate']
        y = data['y_coordinate']

        plt.cla()

        plt.scatter(x, y, label='Channel 1')
        axes = plt.gca()
        axes.set_xlim([-100, 100])
        axes.set_ylim([0, 100])
        plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()
