 #!/bin/sh
# launcher.sh
# navigate to the home directory, then this directory, then back home

cd /
cd python/hellobox
sleep 20   #  gives the pi time to get on the wifi
sudo python hellobox.py
cd /
