# Python client example to get Lidar data from a car
#

import setup_path
import airsim
import pprint
import csv
import sys
import math
import time
import argparse
import math
import numpy
import itertools
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


class LidarTest:

    def __init__(self):

        # connect to the AirSim simulator
        self.client = airsim.CarClient()
        self.client.confirmConnection()
        # self.client.enableApiControl(True)
        # self.car_controls = airsim.CarControls()

    def execute(self):
        for i in range(100):
            lidarData = self.client.getLidarData()
            if (len(lidarData.point_cloud) < 3):
                print("\tNo points received from Lidar data")
            else:
                print("\tLidar collection no: %s" % i)
                points = self.parse_lidarData(lidarData)
                self.csvwrite_lidarData(points)

            time.sleep(1)

    def parse_lidarData(self, data):

        points = numpy.array(data.point_cloud, dtype=numpy.dtype('f4'))
        points = numpy.reshape(points, (int(points.shape[0]/3), 3))
        return points

    # def animate_lidarData(self, points):
    #     """
    #     docstring
    #     """
    #     pass

    def csvwrite_lidarData(self, points):
        fieldnames = ["x_coordinate", "y_coordinate"]
        x, y, z = points.T

        with open('lidar_data.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for(a, b) in zip(x, y):
                info = {
                    "x_coordinate": a,
                    "y_coordinate": b
                }
                csv_writer.writerow(info)

    def stop(self):

        airsim.wait_key('Press any key to reset to original state')

        self.client.reset()

        # self.client.enableApiControl(False)
        print("Done!\n")


# main
if __name__ == "__main__":
    args = sys.argv
    args.pop(0)

    arg_parser = argparse.ArgumentParser(
        "Lidar.py makes car move and gets Lidar data")

    arg_parser.add_argument('-save-to-disk', type=bool,
                            help="save Lidar data to disk", default=False)

    args = arg_parser.parse_args(args)
    lidarTest = LidarTest()
    try:
        lidarTest.execute()
    finally:
        lidarTest.stop()
