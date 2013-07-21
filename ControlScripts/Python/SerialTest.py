# Script which reads and prints all of the data received over
# USB from the Arduino

from time import sleep
from sys import exit
import serial
import dao

print("Setting up variables and USB serial connections")


# Global Constants of Arduino numbers
PEOPLE = 0
THERMOSTAT = 1
OVEN = 2

# Global Variables for people counter stuff
# This arduino number is 0
#pplSerial = serial.Serial("COM5",9600)
pplSerial = serial.Serial("/dev/ttyUSB0",9600)
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

# Global array of tables
TABLES = ['people', 'temp', 'oven']


print("Ready to read!")

def readSerial(thisArduino, thisSerial, thisStartup, thisPosOfValue, thisTempString, thisArray, thisReadingComplete):    
    global pplStartup, pplPosOfVal, pplTempString, pplArray, pplReadingComplete, thermStartup, thermPosOfVal, thermTempString, thermArray, thermReadingComplete, ovenStartup, ovenPosOfVal, ovenTempString, ovenArray, ovenReadingComplete

                        
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
        if(thisArduino==PEOPLE):
            pplStartup = thisStartup
            pplPosOfVal = thisPosOfValue
            pplTempString = thisTempString
            pplArray = thisArray
            pplReadingComplete = thisReadingComplete
        elif(thisArduino==THERMOSTAT):
            thermStartup = thisStartup
            thermPosOfVal = thisPosOfValue
            thermTempString = thisTempString
            thermArray = thisArray
            thermReadingComplete = thisReadingComplete
        elif(thisArduino==OVEN):
            ovenStartup = thisStartup
            ovenPosOfVal = thisPosOfValue
            ovenTempString = thisTempString
            ovenArray = thisArray
            ovenReadingComplete = thisReadingComplete
    else:
        thisReadingComplete = False
        if(thisArduino==0):
            pplReadingComplete = thisReadingComplete
        elif(thisArduino==1):
            thermReadingComplete = thisReadingComplete
        elif(thisArduino==2):
            ovenReadingComplete = thisReadingComplete
            
# Connect to the database
dao.connect()


def serialWrite():
    print("Ready to read!")

while True:
    try:
        readSerial(PEOPLE, pplSerial, pplStartup, pplPosOfVal, pplTempString, pplArray, pplReadingComplete)
        if(pplReadingComplete):
            # Presist the read data to the database
            dao.insertRow(TABLES[PEOPLE], pplArray)
            print(pplArray)
    except KeyboardInterrupt: 
        dao.disConnect()
        exit()        
    
