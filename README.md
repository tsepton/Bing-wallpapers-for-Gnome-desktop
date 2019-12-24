# Bing-wallpapers-for-Gnome-screensaver
This is a simple script to set up the current Bing image of the day as your Gnome screensaver.

## Installation
### Make it run every 6 hours
```Bash
(crontab -l 2>/dev/null; echo "0 */6 * * * python3 /path/to/the/script.py") | crontab -
```
