# rpi_auxFM
FM transmitter designed using markondej's fm_transmitter design. Connect to the device using bluetooth, and you're able to transmit using GPIO 4, or the gpclk pin on your rpi. 


!!!!!!!!!!!!!!
Make sure to follow markondej's guide for setting up the fm_transmitter library.


To setup bluetooth:

Add yourself into the user group: 

sudo usermod -a -G bluetooth <username>

Edit the config file to allow the device to be seen as a A2DP sink. (your phone will feed it audio instead of just pairing)

sudo nano /etc/bluetooth/main.conf
...
Class = 0x41C
...
DiscoverableTimeout = 0
...

Restart bluetooth, and the system:

sudo systemctl restart bluetooth
sudo reboot

Run these commands to setup bluetooth pairing: 

bluetoothctl
[bluetooth]# power on
Changing power on succeeded
[bluetooth]# discoverable on
Changing discoverable on succeeded
[CHG] Controller XX:XX:XX:XX:XX:XX Discoverable: yes
[bluetooth]# pairable on
Changing pairable on succeeded
[bluetooth]# agent on
Agent registered
[bluetooth]# default-agent
Default agent request successful
[bluetooth]# quit
Agent unregistered
[DEL] Controller XX:XX:XX:XX:XX:XX raspberrypi [default]

Once you do this, you'll be able to pair but not connect, you need to trust your address. 

bluetoothctl
[NEW] Controller XX:XX:XX:XX:XX:XX raspberrypi [default]
[NEW] Device YY:YY:YY:YY:YY:YY <your smartphone>
[bluetooth]# trust YY:YY:YY:YY:YY:YY
Changing YY:YY:YY:YY:YY:YY trust succeeded
[bluetooth]# quit
[DEL] Controller XX:XX:XX:XX:XX:XX raspberrypi [default]

Now you should be able to pair and play audio. If you'd like to make it run on startup instead of from CLI, I'd recommend editing the user's .bashrc file, otherwise you might run into some issues when running the script as sudo. 

Run the following commands to use the scripts: 

python3 bluetooth.py 

Or run the shell script: 

chmod +x run.sh 
./run.sh




