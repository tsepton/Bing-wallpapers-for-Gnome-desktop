# Bing-wallpapers-for-Gnome-screensaver
This is a simple script to set up the current Bing image of the day as your Gnome screensaver. 

## Installation
### Make it run every time you boot 
```Bash
chmod +x script.py
(crontab -l 2>/dev/null; echo "@reboot python3 /path/to/the/script.py") | crontab - 
```
