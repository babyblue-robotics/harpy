#!/usr/bin/env python3
"""
File:          harpy.py
Author:        Piyush Shah
Last Modified: Piyush on 5/2
"""

from src import serial_communicator

def command_wheel_vels(wtarget_left, wtarget_right, is_aggressive):
    """send command to robo wheels to move.
    :wtarget_left:        left wheel target value to move.
    :wtarget_right        right wheel target value to move. 
    :is_aggressive        False to do finer movement.
    
    """
    pass