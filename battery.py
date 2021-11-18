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
		if percent < 10:
			notification.notify(
				title="Warning! Low battery info",
				message="Less than 10% charge, plug in now"
			)

		elif percent < 20:
			notification.notify( 
				title="Battery info",
				message="Less than 20% charge, plug in soon"
			)
