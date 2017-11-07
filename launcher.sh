#!/bin/sh
# can make this work by adding to crontab with $ sudo crontab -e
#       at the end of the file, add "@reboot /python/hellobox/launcher.sh"
# however that won't make it launch in a terminal window

# get it to launch in terminal window by adding the line
# @lxterminal --command /python/hellobox/launcher.sh
# to the file ~/.config/lxsession/LXDE-pi/autostart
# i.e. sudo nano ~/.config/lxsession/LXDE-pi/autostart

# navigate to the home directory, then this directory, then back home
echo started launcher
cd /python/hellobox

sleep 20  #  gives the pi time to get on the wifi

# sudo lxterminal -e 'python' 'hellobox.py'
# sudo lxterminal --command "sudo" "python" "hellobox.py"
# previous lines open it in terminal, but don't seem to work on startup.


sudo python hellobox.py


