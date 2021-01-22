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
    lidarData = client.getLidarData(lidar_name="LidarSensor")
    if (len(lidarData.point_cloud) < 3):  # If the point cloud does not have atleast one point
        print("\tNo points received from Lidar data")  # No data recieved
    else:
        # print("\tLidar collection no: %s" % i)
        points = parse_lidarData(lidarData)
        x, y, z = points.T

        ax.clear()
        ax.scatter(y, x, s=5, color='black')
        ax.scatter(0, 0, s=600, color='red', marker="^")
        ax.set_xlim([-15, 15])
        ax.set_ylim([-15, 15])
        ax.axis('off')
        ax.grid(b=None)


plt.style.use('fivethirtyeight')  # Pre defined plot style template
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
client = airsim.CarClient()  # Create an airsim client
client.confirmConnection()  # Confirmt that the connection was successful
# This calls animate function every 5 ms
animation = FuncAnimation(fig, animate, fargs=(client,), interval=5)
plt.show()  # Show the plot
