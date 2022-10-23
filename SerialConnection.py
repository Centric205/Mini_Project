'''
    @Author: Theo Madikgetla
    @Date: 19 October 2022
    @Function:
            This class/module is responsible setting up the serial
            communication needed for transmission of data.
'''
import serial
from time import localtime, strftime

class SerialConnection:

    def __init__(self):
        self.serial_object = serial.Serial()
        self.isReading_data = True



    # Opens serial connection
    def open_connection(self):
        self.serial_object.open()

    # Closes serial connection
    def close_connection(self):
        self.serial_object.close()

    # Reads data sent via the COMx port
    def read_serial_data(self):
        # OPTION 1:
        while(self.isReading_data):
            line_of_data = self.serial_object.readline()
            print(line_of_data)

        # OPTION 2: Have a loop in the DISPLAY function and then call this function
        #           inside the loop. Still not certain at this stage.