#!/usr/bin/env python3
"""
File:          one_blind_meter.py
Author:        Binit Shah
Last Modified: Binit on 5/2
"""

import harpy
import time

def main():
    """Sends the robot forward exactly 1 meter blindly.
    """
    s_m = 1
    r_m = 0.045
    theta_rad = s / r
    wbothwheels_rad_s = 3
    t_s = theta_rad / wbothwheels_rad_s
    harpy.trainingbot.commandWheelVels(wbothwheels_rad_s, wbothwheels_rad_s, True)
    time.sleep(t_s)
    harpy.trainingbot.commandWheelVels(0, 0, True)

if __name__ == '__main__':
    main()