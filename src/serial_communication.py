#!/usr/bin/env python3
"""
File:          serial_communicator.py
Author:        Piyush Shah
Last Modified: Piyush on 5/2
"""

"""
serial_communication.py provide serial communication .
"""

import serial

class SerialComm:
    def __init__(self):
        port = "COM5"
        baud = 9600
        ser = None

    @property
    def handel_feedback (data):
        #if not data.startswith('<'): return None
        #if not data.endsswith('>\r\n'): return None
        dataarr = data[1:-3].split(",")
        for x in dataarr:
            try:
                val = float(x)
            except ValueError:
                val = None
            print(val)
        return dataarr

    def serial_open():
        self.ser = serial.Serial(self.port, self.baud, timeout=1)
        if self.ser.isOpen():
            print(ser.name + ' is open...')
        else:
            print("serial open error.")
            self.ser = None
        return self.ser

    def serial_read_input(ser):
        if ser == None or ser.isOpen == False: return;
        feedback_str = ""
        while True:
            cmd = input("Enter command or 'exit':")
            if cmd == 'exit':
                ser.close()
                exit()
            else:
                barr1=('<'+cmd+'>').encode()
                ser.write(barr1)
                #ser.write(cmd.encode('ascii')+'\r\n'.encode('ascii'))
                while ser.in_waiting > 0 or not feedback_str:
                    feedback_str += ser.read().decode()
                handel_feedback(feedback_str)
                feedback_str = ""

    def serial_send_read(ser, cmd):
        if ser == None or ser.isOpen == False: return;
        feedback_str = ""
        while True:
                barr1=cmd.encode()
                ser.write(barr1)
                while ser.in_waiting > 0 or not feedback_str:
                    feedback_str += ser.read().decode()
                data = handel_feedback(feedback_str)
                feedback_str = ""
        return data

    def close(ser):
        if ser == None or ser.isOpen == False: return;
        ser.close()
        exit()

if if __name__ == "__main__":
    #ser = serial_open()
    #serial_read(ser)
    sc = SerialComm()
    sc.handel_feedback("<123,xyz>")
