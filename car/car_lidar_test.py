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
    longrange2 = client.getLidarData(lidar_name='LongRangeRadar2')
    shortrange1 = client.getLidarData(lidar_name='ShortRangeRadar1')
    shortrange2 = client.getLidarData(lidar_name='ShortRangeRadar2')
    shortrange3 = client.getLidarData(lidar_name='ShortRangeRadar3')
    shortrange4 = client.getLidarData(lidar_name='ShortRangeRadar4')
    if (len(longrange1.point_cloud) < 3):  # If the point cloud does not have atleast one point
        print("\tNo points received from Lidar data")  # No data recieved
    if (len(longrange1.point_cloud) >= 3 and (len(longrange2.point_cloud) >= 3) and (len(shortrange1.point_cloud) >= 3) and (len(shortrange2.point_cloud) >= 3) and (len(shortrange3.point_cloud) >= 3) and (len(shortrange4.point_cloud) >= 3)):
        print("\tLidar collection no: %s" % i)
        longRangePoints1 = parse_lidarData(longrange1)
        longRangePoints2 = parse_lidarData(longrange2)
        shortRangePoints1 = parse_lidarData(shortrange1)
        shortRangePoints2 = parse_lidarData(shortrange2)
        shortRangePoints3 = parse_lidarData(shortrange3)
        shortRangePoints4 = parse_lidarData(shortrange4)
        lx1, ly1, lz1 = longRangePoints1.T
        lx2, ly2, lz2 = longRangePoints2.T
        sx1, sy1, sz1 = shortRangePoints1.T
        sx2, sy2, sz2 = shortRangePoints2.T
        sx3, sy3, sz3 = shortRangePoints3.T
        sx4, sy4, sz4 = shortRangePoints4.T

        ax.clear()
        ax.scatter(ly1, lx1, s=10, color='green')
        ax.scatter(ly2, lx2, s=10, color='green')
        ax.scatter(sy1, sx1, s=10, color='red')
        ax.scatter(sy2, sx2, s=10, color='red')
        ax.scatter(sy3, sx3, s=10, color='red')
        ax.scatter(sy4, sx4, s=10, color='red')
        # ax.scatter3D(y, x, z, c=z, cmap="RdGy")
        # ax.scatter(0, 0, 0, s=600, color='red', marker="^")
        ax.set_xlim([-50, 50])
        ax.set_ylim([-50, 50])
        ax.axis('off')
        ax.grid(b=None)


plt.style.use('seaborn')  # Pre defined plot style template
fig = plt.figure()
ax = plt.subplot(1, 1, 1)
client = airsim.CarClient()  # Create an airsim client
client.confirmConnection()  # Confirmt that the connection was successful

# This calls animate function every 5 ms
animation = FuncAnimation(fig, animate, fargs=(client,), interval=1)
ax.set_facecolor((1.0, 0.47, 0.42))
plt.show()  # Show the plot
