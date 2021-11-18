# MacOS battery notifier tool

I have noticed that MacOS does not have a good battery notification system. With iOS, it is easy with the help of the automation tool inside Shortcuts. So, I decided to make a low battery notification tool for MacOS, which should be helpful for the MacBooks that run on power and battery.

This tool runs a simple python file as daemon in the background. It checks for the battery level every 10 minutes, and sends a notification if the battery level is below 20% and again if it drops below 10%.

### Requirements:
- Python3
- python plyer library, for the MacOS system notification API 
- python psutil library, for getting the battery level and power source
- python pyobjus library, because for some reason, the program does not run without a separate pyobjus library.

### How to install
1. Open a terminal tab at the project repo and then paste the following lines.
2. `sudo cp battery.py /etc/` sudo is required to copy into the /etc/ folder. You can copy into any other folder and then update the folder path accordingly.
3. Edit the plist file with the path of the folder where you copied the python file. Skip this step if you copied to /etc/ folder.
4. `cp BatteryNotify.plist ~/Library/LaunchAgents/` This ensures that the daemon runs only for the current user, and not systemwide.
5. `launchctl load ~/Library/LaunchAgents/BatteryNotify.plist` which tells launchd to look into the plist file for execution details, and starts running in the background.

You can check if the daemon is running successfully by 
`launchctl list | grep BatteryNotify`
which should have exit code 0 for successful execution.

You can stop the daemon from running by 
`launchctl unload ~/Library/LaunchAgents/BatteryNotify.plist`
after which you can edit the plist config file or the python file.
