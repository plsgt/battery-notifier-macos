#!/usr/bin/env python3

from plyer import notification 
import psutil

#returns a tuple
battery = psutil.sensors_battery()

plugged = battery.power_plugged
percent = battery.percent   

charging = False
charged = False

#description of code
if __name__=="__main__": 
	if not plugged:
		if percent < 30:
			notification.notify( 
				title="Battery info",
				message="Low charge, plug in soon"
			)
	else:
		if percent < 100:
			charging = True
		if percent == 100:
			charged = True
			if (charging and charged):
				notification.notify( 
				title="Battery info",
				message="Battery fully charged"
			)
			charging = False