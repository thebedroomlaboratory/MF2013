# Open-source program for interacting with three Arduinos
# in order to automatically control heating, lighting and
# cooking in the home.
# 
# Author: The Bedroom Laboratory, Copyright 2013
# License: Creative Commons

from time import sleep
from sys import exit
import serial
import dao
import logicControl
import SocketService
import threading
import sharedVariables

# Global Constants of Arduino numbers
PEOPLE = 0
THERMOSTAT = 1
OVEN = 2

# Global Variables for people counter stuff
# This arduino number is 0
#pplSerial = serial.Serial("COM5",9600)
#pplSerial = serial.Serial("/dev/ttyUSB0",9600)
pplSerial = serial.Serial("/dev/ttyACM0",9600)
pplSerial.flush()
pplStartup = True
pplPosOfVal = 0
pplTempString = ""
pplArray = [ 0, 1 ]
lastPpl = [ 0, 1]
pplReadingComplete = False

# Global Variables for Thermostat
# This arduino number is 1
thermSerial = serial.Serial("/dev/ttyACM1",9600)
thermSerial.flush()
thermStartup = True
thermPosOfVal = 0
thermTempString = ""
thermArray = [ 0, 0, 0, 0]
lastTherm = [ 0, 0, 0, 0]
thermReadingComplete = False

# Global Variables for Bagel Oven
# This arduino number is 2
#ovenSerial = serial.Serial("COM10",9600)
#ovenSerial.flush()
ovenStartup = True
ovenPosOfVal = 0
ovenTempString = ""
ovenArray = [ 0, 1 ]
lastOven = [ 0, 1]
ovenReadingComplete = False
bagelSetting=0

# Global array of tables
TABLES = ['people', 'temp', 'oven']

def readSerial(thisArduino, thisSerial, thisStartup, thisPosOfValue, thisTempString, thisArray, thisReadingComplete):	
	global pplStartup, pplPosOfVal, pplTempString, pplArray, pplReadingComplete, thermStartup, thermPosOfVal, thermTempString, thermArray, thermReadingComplete, ovenStartup, ovenPosOfVal, ovenTempString, ovenArray, ovenReadingComplete
	# Check if data is waiting to be read (asynchronous reading without blocking)						
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

def checkAndWrite():
	global lastPpl, lastTherm, lastOven
	# Manage heating
	if(logicControl.heating(lastPpl, lastTherm)):
		print("Heating On")
		thermSerial.write('1\n')
		thermSerial.flush()
	else:
		print("Heating Off")
		thermSerial.write('0\n')
		thermSerial.flush()
	# Manage lights
	if(logicControl.light(lastPpl, lastTherm)):
		print("Lights On")
		pplSerial.write('1\n')
		pplSerial.flush()
	else:
		print("Lights Off")
		pplSerial.write('0\n')
		pplSerial.flush()
	# Manage oven
	if(logicControl.bagel(lastOven)):
		print("Oven On")
		#ovenSerial.write('1\n')
		#ovenSerial.flush()
	else:
		print("Oven Off")
		#ovenSerial.write('0\n')
		#ovenSerial.flush()

if __name__ == "__main__":
	print("Home automation beginning...")
	# Connect to the database
	dao.connect()
	# Start Tornado Server in new Thread
	t = threading.Thread(target=SocketService.start_tornado)	
	t.start()
	while True:
		try:
			# Try Reading and parsing from People Counter
			readSerial(PEOPLE, pplSerial, pplStartup, pplPosOfVal, pplTempString, pplArray, pplReadingComplete)
			if(pplReadingComplete):
				lastPpl=pplArray
				# Save the read data to the database
				dao.insertRow(TABLES[PEOPLE], pplArray)
				# Perform control operation for all devices
				checkAndWrite()
				print(pplArray)
			# Try Reading and parsing from Thermostat
			readSerial(THERMOSTAT, thermSerial, thermStartup, thermPosOfVal, thermTempString, thermArray, thermReadingComplete)
			if(thermReadingComplete):
				lastTherm=thermArray
				# Save the read data to the database
				#dao.insertRow(TABLES[PEOPLE], thermArray)
				# Perform control operation for all devices
				checkAndWrite()
				print(thermArray)
		except KeyboardInterrupt:
			# Gracefully close all connections
			dao.disConnect()
			SocketService.stop_tornado()
			t.join()
			print("Program closing!")
			exit()
	
