# Script which reads and prints all of the data received over
# USB from the Arduino

from time import sleep
from sys import exit
import serial

print("Setting up variables and USB serial connections")

# Global Variables for people counter stuff
# This arduino number is 0
pplSerial = serial.Serial("COM5",9600)
pplSerial.flush()
pplStartup = True
pplPosOfVal = 0
pplTempString = ""
pplArray = [ 0, 1 ]
pplReadingComplete = False

# Global Variables for Thermostat
# This arduino number is 1
#thermSerial = serial.Serial("COM10",9600)
#thermSerial.flush()
thermStartup = True
thermPosOfVal = 0
thermTempString = ""
thermArray = [ 0, 1 ]
thermReadingComplete = False

# Global Variables for Bagel Oven
# This arduino number is 2
#ovenSerial = serial.Serial("COM10",9600)
#ovenSerial.flush()
ovenStartup = True
ovenPosOfVal = 0
ovenTempString = ""
ovenArray = [ 0, 1 ]
ovenReadingComplete = False


print("Ready to read!")

def readSerial(thisArduino, thisSerial, thisStartup, thisPosOfValue, thisTempString, thisArray, thisReadingComplete):    
    if (thisSerial.inWaiting() > 0):
        val = thisSerial.read()
        if (val == '\n'):
            if (thisStartup == True):
                thisStartup = False
            elif (thisStartup == False):
                thisArray [thisPosOfValue] = int(thisTempString)
                thisTempString = ""
                thisPosOfValue = 0
                thisReadingComplete = True
        elif (val == '\r'):
            thisReadingComplete = False
        elif (val == '?'):
            if (thisStartup == False):
                thisArray [thisPosOfValue] = int(thisTempString)
                thisTempString = ""
                thisPosOfValue += 1
                thisReadingComplete = False
        else:
            if (thisStartup == False):
                thisTempString += str(val)
                thisReadingComplete = False
        if(thisArduino==0):
            global pplStartup
            global pplPosOfVal
            global pplTempString
            global pplArray
            global pplReadingComplete
            pplStartup = thisStartup
            pplPosOfVal = thisPosOfValue
            pplTempString = thisTempString
            pplArray = thisArray
            pplReadingComplete = thisReadingComplete
        elif(thisArduino==1):
            global thermStartup
            global thermPosOfVal
            global thermTempString
            global thermArray
            global thermReadingComplete
            thermStartup = thisStartup
            thermPosOfVal = thisPosOfValue
            thermTempString = thisTempString
            thermArray = thisArray
            thermReadingComplete = thisReadingComplete
        elif(thisArduino==2):
            global ovenStartup
            global ovenPosOfVal
            global ovenTempString
            global ovenArray
            global ovenReadingComplete
            ovenStartup = thisStartup
            ovenPosOfVal = thisPosOfValue
            ovenTempString = thisTempString
            ovenArray = thisArray
            ovenReadingComplete = thisReadingComplete
    else:
        thisReadingComplete = False
        if(thisArduino==0):
            global pplReadingComplete
            pplReadingComplete = thisReadingComplete
        elif(thisArduino==1):
            global thermReadingComplete
            thermReadingComplete = thisReadingComplete
        elif(thisArduino==2):
            global ovenReadingComplete
            ovenReadingComplete = thisReadingComplete
            
def serialWrite():
    print("Ready to read!")

while True:
    try:
        readSerial(0, pplSerial, pplStartup, pplPosOfVal, pplTempString, pplArray, pplReadingComplete)
        if(pplReadingComplete):
            print(pplArray)
    except KeyboardInterrupt: 
        exit()
    
