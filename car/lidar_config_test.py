# Script that connects to Airsim simulator and reads lidar data
# To configure LiDAR, edit the settings.json file in AirSim folder

# for plotting and animating
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# for reading lidar data and formatting the lidar point cloud
import airsim
import numpy

# Parse the lidar point cloud and create a [x,y,z] tuple


def parse_lidarData(data):
    points = numpy.array(data.point_cloud, dtype=numpy.dtype('f4'))
    points = numpy.reshape(points, (int(points.shape[0]/3), 3))
    return points


def animate(i, client):
    longrange1 = client.getLidarData(lidar_name='LongRangeRadar1')

    ax.clear()

    if(len(longrange1.point_cloud) >= 3):
        longRangePoints1 = parse_lidarData(longrange1)
        lx1, ly1, lz1 = longRangePoints1.T
        ax.scatter(ly1[0], lx1[0], s=100, color='green')

    ax.scatter(0, 0, s=100, marker="^")
    ax.set_xlim([-100, 100])
    ax.set_ylim([-100, 100])
    ax.axis('off')
    ax.grid(b=None)


plt.style.use('seaborn')  # Pre defined plot style template
fig = plt.figure()
ax = plt.subplot(1, 1, 1)
client = airsim.CarClient()  # Create an airsim client
client.confirmConnection()  # Confirmt that the connection was successful

# This calls animate function every 5 ms
animation = FuncAnimation(fig, animate, fargs=(client,), interval=1)
plt.show()  # Show the plot
