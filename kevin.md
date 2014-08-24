

# Dashboard

How to setup a kiosk to display [Dashing](http://dashing.io) widgets.

## Kiosk mode

### Auto Login

    sudo nano /etc/inittab

    1:2345:respawn:/sbin/getty 115200 tty1

and change to

    #1:2345:respawn:/sbin/getty 115200 tty1

Under that line add:

    1:2345:respawn:/bin/login -f pi tty1 </dev/tty1 >/dev/tty1 2>&1

### Auto StartX

    sudo nano /etc/rc.local

Scroll to the bottom and add the following above exit 0:

    su -l pi -c startx

where pi is the username you want to run X as.

**Note:** The previous method indicated that you should add startx to /etc/profile. The updated method is better, since it will cause startx to run only when necessary, and it will not launch the X server as root.

Additionally, you need to run dashing as root for nmap to work right so add this to `/etc/rc.local`:

    sudo /home/pi/dashing/home/start.bash &
    /usr/bin/espeak "booting now"

If you haven't updated everything yet do so now.

	sudo apt-get update
	sudo apt-get upgrade

Next install key software:

	sudo apt-get install chromium
	sudo apt-get install x11-xserver-utils unclutter

During testing:

    xinit /usr/bin/chromium --kiosk --incognito http://192.168.1.12:3030

Edit the X-Server to disable the screensaver and launch Google's chromium in kiosk mode without a desktop (saves resources).

	sudo nano /etc/xdg/lxsession/LXDE/autostart

	#@xscreensaver -no-splash
	@xset s off
	@xset -dpms
	@xset s noblank
	@unclutter -idle 0 # hide mouse
	@chromium --kiosk --incognito http://localhost:3030

Kiosk mode boots Chromium into full screen mode, by default. Incognito mode prevents a “Chrome did not shutdown cleanly” message from appearing on the top if the RaspberryPi loses power.

I also needed to modify /etc/lightdm/lightdm.conf. Add this line to the [SeatDefaults] section:

    sudo pico /etc/lightdm/lightdm.conf
    xserver-command=X -s 0 dpms


Rotate screen by editing `/boot/config.txt` and adding the line:

    display_rotate 1

where `1` is 90 deg clockwise and '3' is 270 deg clockwise rotation.

### Fixes

    error [1:1:1827694911:ERROR:nss_util.cc(692)] Failed to load NSS libraries.

    sudo ln -s /usr/lib/arm-linux-gnueabihf/nss/ /usr/lib/nss

## Ruby

    sudo apt-get ruby-dev libcurl4-openssl-dev nmap
    sudo gem install nokogiri htmlentities puma others?


# Issues

- in ruby scripts, the `ENV['variable']` doesn't seem to work. Not sure if it is a ruby 1.9.3 issue or not.
- the TV keeps going blank after a while. Could be a TV thing, auto shut off???
 
##I2C

Install some tools:

    sudo apt-get install python-smbus i2c-tools

Also make sure it is not blacklisted in `/etc/modprobe.d/raspi-blacklist.conf`. If the file doesn't exist, then you are fine. If the file does exist make sure the following are commented out using `#`.

    #blacklist spi-bcm2708
    #blacklist i2c-bcm2708

The Raspberry Pi designers swapped over I2C ports between board releases. Just remember: 512M Pi's use i2c port 1, 256M ones use i2c port 0!

    sudo i2cdetect -y 0


