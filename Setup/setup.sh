#!/bin/bash


if [ -z "$3" ]; then
    echo "usage: sudo $0 linuxUsername githubUsername githubEmail"
    exit
fi

apt-get install git python python-serial python-tornado meld lamp-server^ arduino
su - $1
cd ~
git clone https://github.com/thebedroomlaboratory/MF2013.git
git config --global user.name "$2"
git config --global user.email "$3"
git config --global credential.helper cache
git config credential.helper 'cache --timeout=3600'
cd ~/sketchbook
ln -s ~/MF2013/ControlScripts/Arduino/serialWriteArduinoExamplePpl
ln -s ~/MF2013/ThermostatLightSensor/Thermostat
mkdir libraries
cd libraries/
ln -s ~/MF2013/ThermostatLightSensor/Thermostat/Adafruit_GFX
ln -s ~/MF2013/ThermostatLightSensor/Thermostat/Adafruit_PCD8544
