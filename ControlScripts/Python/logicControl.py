#!/usr/bin/python

# This script is used for all the control logic

# Global Constants of Arduino numbers
#PEOPLE = 0
#THERMOSTAT = 1
#OVEN = 2
HEAT_TIMEOUT=10
HEAT_THRESHOLD=1800
HEAT_FREEZING=500
heatOverride=1
heatOverrideTimer=0
heatSetting=0

LIGHT_TIMEOUT=10
LIGHT_THRESHOLD=150
lightOverride=1
lightOverrideTimer=0
lightSetting=0

bagelOverride=1
bagelOverrideTimer=0
bagelSetting=0

def heating(pplArray, thermArray):
	# heating logic
	global HEAT_TIMEOUT, HEAT_THRESHOLD, HEAT_FREEZING, heatOverride, heatOverrideTimer, heatSetting
	if (heatOverride):
		print("Turn on - override & start reset counter")
		heatOverrideTimer+=1
		heatSetting=True
		if (heatOverrideTimer>HEAT_TIMEOUT):
			heatOverrideTimer=0
			heatOverride=False
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
	global LIGHT_TIMEOUT, LIGHT_THRESHOLD, lightOverride, lightOverrideTimer, lightSetting
	if (lightOverride):
		print("Lights on - override & start reset counter")
		lightOverrideTimer+=1
		lightSetting=True
		if (lightOverrideTimer>LIGHT_TIMEOUT):
			lightOverrideTimer=0
			lightOverride=False
	elif (thermArray[1]<LIGHT_THRESHOLD) and (pplArray[0]>0):
		print("Lights on - dark & occupied")
		lightSetting=True
	else:
		print("Lights off")
		lightSetting=False
	return lightSetting

def bagel(ovenArray):
	global bagelOverride, bagelOverrideTimer, bagelSetting
	if (bagelOverride) and (not ovenArray[1]):
		print("Bagel Cooking")
		bagelSetting=True
	else:
		bagelSetting=False
	return bagelSetting

