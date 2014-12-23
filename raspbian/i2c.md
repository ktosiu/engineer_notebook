
## i2c

First we need to load the drivers

	sudo modprobe i2c-dev
	sudo modprobe i2c-bcm2708

Now `/dev/i2c-0` and `/dev/i2c-1` should exist. Also, so see what is on the i2c bus, install the `i2c-tools` using:

	sudo apt-get install i2c-tools

Now to explore the i2c bus try:

	[kevin@raspberrypi ~]$ sudo i2cdetect -y 1
	     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
	00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
	10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	70: -- -- -- -- -- -- -- --     

To have these load at boot, add them to `/etc/modules`.

