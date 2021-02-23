import airsim
import msvcrt
import sys
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoffAsync().join()

z = -7

duration = 0.1
speed = 1
delay = duration * speed


keepGoing = True
while (keepGoing):
    input_char = msvcrt.getch()
    if(input_char == b'w'):
        vx = speed
        vy = 0
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, 0)).join()
        time.sleep(delay)
    elif(input_char == b's'):
        vx = -speed
        vy = 0
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, 0)).join()
        time.sleep(delay)
    elif(input_char == b'a'):
        vx = 0
        vy = -speed
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, 0)).join()
        time.sleep(delay)
    elif(input_char == b'd'):
        vx = 0
        vy = speed
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, 0)).join()
        time.sleep(delay)
    elif(input_char == b'j'):
        vx = 0
        vy = 0
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, -90)).join()
        time.sleep(delay)
    elif(input_char == b'k'):
        vx = 0
        vy = 0
        client.moveByVelocityZAsync(
            vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom, airsim.YawMode(False, 90)).join()
        time.sleep(delay)
    elif(input_char == b'x'):
        keepGoing = False

client.hoverAsync().join()
client.landAsync().join()
