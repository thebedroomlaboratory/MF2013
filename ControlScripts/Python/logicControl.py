#!/usr/bin/python

# This script is used for all the control logic

import sharedVariables
# Global Constants of Arduino numbers
#PEOPLE = 0
#THERMOSTAT = 1
#OVEN = 2
HEAT_TIMEOUT=10
HEAT_THRESHOLD=1800
HEAT_FREEZING=500
heatOverrideTimer=0
heatSetting=0

LIGHT_TIMEOUT=10
LIGHT_THRESHOLD=150
lightOverrideTimer=0
lightSetting=0

bagelOverride=1
bagelOverrideTimer=0

def heating(pplArray, thermArray):
	# heating logic
	global HEAT_TIMEOUT, HEAT_THRESHOLD, HEAT_FREEZING, heatOverrideTimer, heatSetting
	if (sharedVariables.heatOverride):
		print("Turn on - override & start reset counter")
		heatOverrideTimer+=1
		heatSetting=True
		if (heatOverrideTimer>HEAT_TIMEOUT):
			heatOverrideTimer=0
			sharedVariables.heatOverride=False
	elif (thermArray[2]<HEAT_FREEZING):
		print("Turn on - freezing")
		heatSetting=True
	elif (thermArray[2]<HEAT_THRESHOLD) and (pplArray[0]>0):
		print("Turn on - cold & occupied")
		heatSetting=True
	else:
		print("Turn off")
		heatSetting=False
	return heatSetting

def light(pplArray, thermArray):
	# lighting logic
	global LIGHT_TIMEOUT, LIGHT_THRESHOLD, lightOverrideTimer, lightSetting
	if (sharedVariables.lightOverride):
		print("Lights on - override & start reset counter")
		lightOverrideTimer+=1
		lightSetting=True
		if (lightOverrideTimer>LIGHT_TIMEOUT):
			lightOverrideTimer=0
			sharedVariables.lightOverride=False
	elif (thermArray[1]<LIGHT_THRESHOLD) and (pplArray[0]>0):
		print("Lights on - dark & occupied")
		lightSetting=True
	else:
		print("Lights off")
		lightSetting=False
	return lightSetting

def bagel(ovenArray):
	# bagel oven logic
	global bagelOverrideTimer, bagelSetting
	if (sharedVariables.bagelOverride) and (not ovenArray[1]):
		print("Bagel Cooking")
		bagelSetting=True
		sharedVariables.bagelOverride=False
	else:
		bagelSetting=False
	return bagelSetting

