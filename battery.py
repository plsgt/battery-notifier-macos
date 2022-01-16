#!/usr/bin/env python3

from plyer import notification 
import psutil

#returns a tuple
battery = psutil.sensors_battery()

plugged = battery.power_plugged
percent = battery.percent   

#description of code
if __name__=="__main__": 
	if not plugged:
		if percent < 30:
			notification.notify( 
				title="Battery info",
				message="Low charge, plug in soon"
			)
