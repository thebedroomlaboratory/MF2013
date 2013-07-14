# Script which reads and prints all of the data received over
# USB from the Arduino

from time import sleep
from sys import exit
import serial

print("Setting up USB serial connection")
serialFromArduino = serial.Serial("COM4",9600)
serialFromArduino.flush()
print("Ready to read!")
startup = True
posInVal = 0
posOfVal = 1
values = [ 5, 0.0, None, 0, None ]
tempString = ""
tempFloat = 0.0
temperature = 0.0
tempLow=0
tempHigh=0
tempRight=0
heatingOn=True
buttonCount=0
buttonOverrideActive=False

webOn=False
webCount=0
webOverrideActive=False
while True:
    try:
        val = serialFromArduino.read()
        print(val)
        if (val == '\n'):
            if (startup == True):
                startup = False
            elif (startup == False):
                #print temp, light
                values [posOfVal] = int(tempString)
                print(tempString)
                print(values)
        elif (val == '\r'):
            i=0		
        elif (val == '?'):
            if (startup == False):
                tempFloat = float(int(tempString))
                tempFloat /= 10
                tempFloat -= 7
                temperature = tempFloat
                values [posOfVal] = tempFloat
                print(tempString)
                tempString = ""
                posInVal = 0
                posOfVal += 2
        else:
            if (startup == False):
                tempString += str(val)
            else:
                print("aaagh")

    except KeyboardInterrupt: 
        exit()
