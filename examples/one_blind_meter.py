#!/usr/bin/env python3
"""
File:          one_blind_meter.py
Author:        Binit Shah
Last Modified: Binit on 5/2
"""

import harpy
import time

bot = harpy.DifferentialDriveConfig(r=0.045, d=0.85)
bot.serial.set(port="COM5", baudrate=9600)

def main():
    """Sends the robot forward exactly 1 meter blindly.
    """
    s_m = 1
    r_m = bot.wheel_radius_m
    theta_rad = s / r
    wbothwheels_rad_s = 3
    t_s = theta_rad / wbothwheels_rad_s

    bot.command_wheel_vels(wbothwheels_rad_s, wbothwheels_rad_s, True)
    time.sleep(t_s)
    bot.command_wheel_vels(0, 0, True)

if __name__ == '__main__':
    main()