# Script which reads and prints all of the data received over
# USB from the Arduino

from time import sleep
from sys import exit
import serial

print("Setting up variables and USB serial connections")

# Global Variables for people counter stuff
# This arduino number is 0
pplSerial = serial.Serial("COM10",9600)
pplSerial.flush()
pplStartup = True
pplPosOfVal = 0
pplTempString = ""
pplArray = [ 0, 1 ]

# Global Variables for Thermostat
# This arduino number is 1
thermSerial = serial.Serial("COM10",9600)
thermSerial.flush()
thermStartup = True
thermPosOfVal = 0
thermTempString = ""
thermArray = [ 0, 1 ]

# Global Variables for Bagel Oven
# This arduino number is 2
ovenSerial = serial.Serial("COM10",9600)
ovenSerial.flush()
ovenStartup = True
ovenPosOfVal = 0
ovenTempString = ""
ovenArray = [ 0, 1 ]


print("Ready to read!")

def readSerial(thisArduino, thisSerial, thisStartup, thisPosOfValue, thisTempString, thisArray):    
    if (thisSerial.inWaiting() > 0):
        val = thisSerial.read()
        if (val == '\n'):
            if (thisStartup == True):
                print("hi");
                thisStartup = False
            elif (thisStartup == False):
                thisArray [thisPosOfValue] = int(thisTempString)
                print(thisArray)
                thisTempString = ""
                thisPosOfValue = 0
                exit()
        elif (val == '\r'):
            i=0		
        elif (val == '?'):
            if (thisStartup == False):
                thisArray [thisPosOfValue] = int(thisTempString)
                thisTempString = ""
                thisPosOfValue += 1
        else:
            if (thisStartup == False):
                thisTempString += str(val)
        if(thisArduino==0):
            global pplStartup
            pplStartup = thisStartup
            global pplPosOfVal
            pplPosOfVal = thisPosOfValue
            global pplTempString
            pplTempString = thisTempString
            global pplArray
            pplArray = thisArray
        elif(thisArduino==1):
            global thermStartup
            thermStartup = thisStartup
            global thermPosOfVal
            thermPosOfVal = thisPosOfValue
            global thermTempString
            thermTempString = thisTempString
            global thermArray
            thermArray = thisArray
        elif(thisArduino==2):
            global ovenStartup
            ovenStartup = thisStartup
            global ovenPosOfVal
            ovenPosOfVal = thisPosOfValue
            global ovenTempString
            ovenTempString = thisTempString
            global ovenArray
            ovenArray = thisArray
            


while True:
    try:
        readSerial(0, pplSerial, pplStartup, pplPosOfVal, pplTempString, pplArray)
        print(pplArray)
        
    except KeyboardInterrupt: 
        exit()
    
