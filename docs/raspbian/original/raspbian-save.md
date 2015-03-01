# Raspbian

[Raspbian](http://www.raspbian.org) is a Raspberry optimized version of Debian. The 
version installed here is based on Debian Wheezy.

	[kevin@raspberrypi ~]$ lscpu
	Architecture:          armv6l
    Byte Order:            Little Endian
	CPU(s):                1
	On-line CPU(s) list:   0
	Thread(s) per core:    1
	Core(s) per socket:    1
	Socket(s):             1

Note this output doesn't really tell you much other than it is ARMv6.

## Copying an image to the SD Card in Mac OS X

These commands and actions need to be performed from an account that has administrator 
privileges.

1. Download the image from a [mirror or torrent](http://www.raspberrypi.org/downloads).

2. Verify if the the hash key is the same (optional), in the terminal run:

    shasum ~/Downloads/debian6-19-04-2012.zip

3. Extract the image:

    unzip ~/Downloads/debian6-19-04-2012.zip

4. Attach the SD Card to the computer and identify the mount point

    df -h

Record the device name of the filesystem's partition, e.g. /dev/disk3s1

5. Unmount the partition so that you will be allowed to overwrite the disk, note that 
unmount is **NOT** the same as eject:

    sudo diskutil unmount /dev/disk3s1

Using the device name of the partition work out the raw device name for the entire disk, 
by omitting the final "s1" and replacing "disk" with "rdisk" (this is very important: 
you will lose all data on the hard drive on your computer if you get the wrong device 
name). Make sure the device name is the name of the whole SD card as described above, 
not just a partition of it (for example, rdisk3, not rdisk3s1. Similarly you might have 
another SD drive name/number like disk2 or disk4, etc. -- recheck by using the df -h 
command both before & after you insert your SD card reader into your Mac if you have 
any doubts!): e.g. /dev/disk3s1 => /dev/disk3

**Note:** Using rdisk3 might be faster than using disk3, need to look into this.

6. Write the image to the card with this command, using the raw disk device name from 
above (read carefully the above step, to be sure you use the correct rdisk# here!):

    sudo dd bs=1m if=~/archlinux-hf-2012-09-18.img of=/dev/disk3

If the above command report an error(dd: bs: illegal numeric value), please change bs=1M 
to bs=1m. 

Note that dd will not feedback any information until there is an error or it 
is finished, information will show and disk will re-mount when complete. However if you 
are curious as to the progresss - ctrl-T (SIGINFO, the status argument of your tty) will 
display some en-route statistics.

7. After the dd command finishes, eject the card:

    sudo diskutil eject /dev/disk3

8. Insert it in the raspberry pi, and have fun

## SSH Keys

To increase security, you can disable password logins and rely on ssh public keys. To do
this, take a look [here](https://wiki.archlinux.org/index.php/SSH_Keys) for details. Basic
steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA (1024 bit) both 
public and private keys. They will be stored in ~/.ssh with the public key having .pub 
appended to the end.

        ssh-keygen -t dsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"
    
    Note you can create a key for a different username if you change $(whoami) to the user name you want.

2. Copy the public key (.pub) to the server you will connect to:

        ssh-copy-id username@remote-server.org 

    This should update ~/.ssh/authorized_keys in the process. Also ensure the correct 
protections are on the file by:

        chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/ssh/sshd_config to disable password logins.

    PasswordAuthentication no
    ChallengeResponseAuthentication no

    
## Reconfiguring the Pi (speed and memory)

You can change the Pi's default settings for CPU MHz and memory split (between RAM and
GPU) using `raspi-config`. An alternate way is to simply edit the `/boot/config.txt`.

    [kevin@raspberrypi ~]$ more /proc/cpuinfo
    Processor	: ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS	: 795.44
    Features	: swp half thumb fastmult vfp edsp java tls 
    CPU implementer	: 0x41
    CPU architecture: 7
    CPU variant	: 0x0
    CPU part	: 0xb76
    CPU revision	: 7
    
    Hardware	: BCM2708
    Revision	: 0002
    Serial		: 000000008e0a5a17

    [kevin@raspberrypi ~]$ free -h
                 total       used       free     shared    buffers     cached
    Mem:          232M        57M       174M         0B        11M        28M
    -/+ buffers/cache:        18M       214M
    Swap:          99M         0B        99M

The output here shows overclocked to 800 MHz and the GPU given only 16 MB of RAM. Now
the CPU MHz will change dynamically based on load. So with no load, my 800 MHz system
will default to the original 700 MHz system. If you want to always be running at max
speed, put `force_turbo=1` in the `/boot/config.txt`.

    [kevin@raspberrypi ~]$ more /boot/config.txt 
    #uncomment to overclock the arm. 700 MHz is the default.
    arm_freq=800
    
    # for more options see http://elinux.org/RPi_config.txt
    gpu_mem=16     # can be 16, 64, 128 or 256
    core_freq=250
    sdram_freq=400
    over_voltage=0
    force_turbo=1

More info can be found [here](http://www.raspberrypi.org/documentation/configuration/config-txt.md).

## Determine Kernel version and upgrade

You can determine the current linux kernel version by:

    [kevin@raspberrypi tmp]$ more /proc/version
    Linux version 3.2.27+ (dc4@dc4-arm-01) (gcc version 4.7.2 20120731 (prerelease) 
    (crosstool-NG linaro-1.13.1+bzr2458 - Linaro GCC 2012.08) ) #250 PREEMPT Thu Oct
     18 19:03:02 BST 2012

or     

    [kevin@raspberrypi tmp]$ uname -a
    Linux raspberrypi 3.2.27+ #250 PREEMPT Thu Oct 18 19:03:02 BST 2012 armv6l GNU/Linux

In both cases, this is kernel version 3.2.27. Note that the *l* in `armv6l` refers to little endian.

Get and install [rpi-update](http://github.com/Hexxeh/rpi-update):

    sudo apt-get rpi-update

### Backup and Restore
Use the `dd` command to make a full backup of the image:

	dd if=/dev/sdx of=/path/to/image

or for compression:

	dd if=/dev/sdx | gzip > /path/to/image.gz

Where sdx is your SD card and the target could be ~/raspbian_wheezy_`date "+%Y%m%d_%T"`. 
This will save it to your home directory and append the current date and time on the end 
of the filename.

To restore the backup you reverse the commands:

	dd if=/path/to/image of=/dev/sdx

or when compressed:

	gzip -dc /path/to/image.gz | dd of=/dev/sdx 

## Raspi-Config

This is a simple [utility](http://www.raspberrypi.org/documentation/configuration/raspi-config.md) to reconfigure various things on the Pi. You can download it by:

    sudo apt-get raspi-config
	sudo raspi-config

Suggest selecting the advanced choice first so you can update raspi-config script first, just to make sure you have any bug fixes, 
then run the resize option. You can change:

* timezone (use internationalization option)
* hostname
* user password
* resize SD memory card
* configure sound through HDMI or 3.5 mm jack


## Sound

Sound is still experimental, but can be enabled in the current session by:

	sudo apt-get install alsa-utils
	sudo modprobe snd_bcm2835
	sudo aplay /usr/share/sounds/alsa/Front_Center.wav
 
To make the changes permanent for the next reboot, ensure the module is initialized on 
boot, add snd_bcm2835 to `/etc/modules`

Also make sure you are part of group audio:

	sudo gpasswd -a kevin audio

This will allow you to play audio commands without being root (via sudo). 

The audio output will be set to `automatic`, but can be changed:

	sudo amixer cset numid=3 n

where `n` is 0=auto, 1=headphones, or 2=hdmi.


## Software

Why have one program that does a few common sense things well when you can have multiple programs that do one or two things really badly!

| Program   | Description                                                    |
|-----------|----------------------------------------------------------------|
| apt-get   | install: `apt-get install <prgm>`                              |
|           | remove: `apt-get remove <prgm>` add `--purge` to remove configs|
| apt-cache | search for programs you can install: `apt-cache search <prgm>` |
| dpkg      | list programs you have installed: `dpkg -l`                    |

### Updates, Search, and List

	sudo apt-get update
	sudo apt-get upgrade

Now to just see the list of packages that would be upgraded:

	sudo apt-get upgrade -u

Now some packages will get `kept back` which seems to be some strange apt-get issue. To
update your system completely, do:

    sudo apt-get dist-upgrade

You can also search for software by:

    apt-cache showpkg [packagename]
    
Or list all packages installed on the computer by:

    dpkg -l

### Useful Software

* SSH (installed/enabled by default)
* Avahi (Bonjour for Linux)
* Netatalk (file sharing, Pi will appear in finder)

Install these with:

    sudo apt-get install avahi-daemon
    sudo apt-get install netatalk

### Python

You can use `pip` to install and keep python libraries up to date. Unfortunately `pip` is a horrible package manager, but it could be worse ... `apt-get` anyone? Some useful, undocumented commands:

    sudo pip list --outdated
    sudo pip install --upgrade

Why the idiots who run `pip` don't make useful commands like `pip upgrade` or `pip outdated` I don't know. Instead there are duplicate (stupid) commands like `pip freeze` which is the same as `pip list`.

## Lights

The main indicators are the lights on the front corner of the board. These are:

	OK (green): The board is active (blinks off when accessing the SD card)
	PWR (red): The board is successfully powered from USB
	FDX (green): Network is full-duplex
	LNK (green): The network cable is connected (blinks off when transferring data to/from the network)
	10M (yellow): Lit when the board is using a 100Mbps link, not lit when using a 10Mbps

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

## Error Messages
Yes, there are logs for everything.

If you connect a new device to the Pi then the module being loaded will show in dmesg. Eg;

	$ dmesg | tail 
	[16037.102139] Initializing USB Mass Storage driver...
	[16037.102299] scsi4 : usb-storage 2-2:1.0
	[16037.102422] usbcore: registered new interface driver usb-storage
	[16037.102425] USB Mass Storage support registered.

All other logs will have their place in /var/log/. Some important ones include:

/var/log/boot - For all boot messages, such as daemons starting.

/var/log/Xorg.0.log - All Xorg logs. Including any errors.

/var/log/errors.log - Any system error will also be logged here.

If you ssh into the running headless pi, then typing dmesg at the command prompt will do this for you

##WiFi

D-Link wireless N 150 (DWA-121) Pico USB adaptor install.

	[kevin@raspberrypi ~]$ lsusb
	Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
	Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp. 
	Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. 
	Bus 001 Device 004: ID 2001:3308 D-Link Corp. DWA-121 802.11n Wireless N 150 Pico Adapter [Realtek RTL8188CUS]

**Note:** If you don't see it, make sure it is the only USB device plugged in because it takes a lot of power. Otherwise attach to a powered USB hub and you should be fine.

###WPA2

First create a file with the following information, but substitute in the correct ssid and psk (with quotes around them) for your network.

	[kevin@raspberrypi ~]$ more /etc/wpa_supplicant/wpa_supplicant.conf 
	ctrl_interface=/var/run/wpa_supplicant
	ctrl_interface_group=0
	ap_scan=2
	
	network={
		ssid="wireless access point name in quotes"
		key_mgmt=WPA-PSK      
		proto=WPA2
		pairwise=CCMP TKIP
		group=CCMP TKIP
		psk="pass phrase in quotes"
	}

**Note:** The ssid is case sensitive!! 

###Network Setup

Next you will need to change your network interface for a static IP to:

	[kevin@raspberrypi ~]$ more /etc/network/interfaces 
	auto lo
	iface lo inet loopback
	
	# dynamic interface
	#iface eth0 inet dhcp 
	
	# static interface
	iface eth0 inet static
		address 192.168.1.120
		netmask 255.255.255.0
		gateway 192.168.1.1
	
	auto wlan0
	iface wlan0 inet static
		address 192.168.1.121
		wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
		netmask 255.255.255.0
		gateway 192.168.1.1

Note that the wifi interface (wlan0) points to the WPA config file from above. Also there is an example dynamic interface commented out (`iface eth0 inet dhcp`) to show you how to use DHCP. The `lo` is the loopback interface, eth0 is the wired interface, with the wlan0 being the wireless interface. Also, the lines with `auto` in them tell linux to automatically start those interfaces during the bootup process.

Or if you are fine with DHCP determining all your IP addresses:

	auto lo

	iface lo inet loopback
	iface eth0 inet dhcp

	allow-hotplug wlan0
	iface wlan0 inet manual
	wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet dhcp


Finally to get the wireless up and running, use `ifup` to get things started.

	[kevin@raspberrypi ~]$ sudo ifup wlan0
	ioctl[SIOCSIWAP]: Operation not permitted
	ioctl[SIOCSIWENCODEEXT]: Invalid argument
	ioctl[SIOCSIWENCODEEXT]: Invalid argument

These errors don't seem to effect the wifi adaptor. You can double check all is well by using `iwconfig`.

	[kevin@raspberrypi ~]$ iwconfig
	lo        no wireless extensions.
	
	wlan0     IEEE 802.11bgn  ESSID:"GC9J2"  Nickname:"<WIFI@REALTEK>"
	          Mode:Managed  Frequency:2.437 GHz  Access Point: 00:7F:28:05:4D:D9   
	          Bit Rate:150 Mb/s   Sensitivity:0/0  
	          Retry:off   RTS thr:off   Fragment thr:off
	          Power Management:off
	          Link Quality=100/100  Signal level=76/100  Noise level=0/100
	          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
	          Tx excessive retries:0  Invalid misc:0   Missed beacon:0
	
	eth0      no wireless extensions.

Looking at the wlan0 interface, it has a 150 Mb/s data rate (802.11n), and sees a signal strength of 76/100.

	[kevin@raspberrypi ~]$ ifconfig wlan0
	wlan0     Link encap:Ethernet  HWaddr fc:75:16:04:96:5f  
	          inet addr:192.168.1.121  Bcast:192.168.1.255  Mask:255.255.255.0
	          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
	          RX packets:59222 errors:0 dropped:63403 overruns:0 frame:0
	          TX packets:11365 errors:0 dropped:0 overruns:0 carrier:0
	          collisions:0 txqueuelen:1000 
	          RX bytes:92009000 (87.7 MiB)  TX bytes:1154992 (1.1 MiB)

Notice here a lot of dropped packets on the receive (RX).

# BitTorrent Sync

Use BitTorrent's [Sync](http://www.getsync.com) program to keep files on different computers up to date. You need to add the repository for `apt-get` to get the package from, first create the file.

    sudo nano /etc/apt/sources.list.d/btsync.list

Next, copy these lines into it:

    deb http://debian.yeasoft.net/btsync wheezy main contrib non-free
    deb-src http://debian.yeasoft.net/btsync wheezy main contrib non-free

Next, import the signing key:

	sudo gpg --keyserver pgp.mit.edu --recv-keys 6BF18B15
	sudo gpg --armor --export 6BF18B15 | sudo apt-key add -

Finally, update and install:

	sudo apt-get update
	sudo apt-get install btsync

## Uninstall 

To uninstall everything do:

	sudo apt-get --purge remove btsync btsync-common

If you just do `btsync` then it will leave stuff behind.

## Configure Sync

A configuration window will pop up during install, just take the defaults. Please **do not** select https or set a password for the web gui!!! You can re-run the installer anytime by:

	sudo dpkg-reconfigure btsync

The check the `status`, `start`, or `stop` with:

	sudo service btsync status

Finally, login into the webui at `computer_name:8888` to configure `btsync`.


# USB Camera

To use the Logitech C270 camera you need to add your user (pi in this case) to the video group:

    sudo usermod -a -G video pi

For other users, just change pi to the correct username. Then make sure the driver is loaded:

    sudo modprobe uvcvideo

You can double check it works by grabbing an image:

    sudo apt-get install fswebcam
    
    fswebcam image.jpg

If an image appeared, then all is good.

# External USB Drive

A goog resource is [here](http://devtidbits.com/2013/03/21/using-usb-external-hard-disk-flash-drives-with-to-your-raspberry-pi/)

## Setup

First connect the drive and find it:

	pi@calculon ~ $ sudo fdisk -l

	Disk /dev/mmcblk0: 15.9 GB, 15931539456 bytes
	4 heads, 16 sectors/track, 486192 cylinders, total 31116288 sectors
	Units = sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disk identifier: 0x000981cb

			Device Boot      Start         End      Blocks   Id  System
	/dev/mmcblk0p1            8192      122879       57344    c  W95 FAT32 (LBA)
	/dev/mmcblk0p2          122880    31116287    15496704   83  Linux

	WARNING: GPT (GUID Partition Table) detected on '/dev/sda'! The util fdisk doesn't support GPT. Use GNU Parted.


	Disk /dev/sda: 640.1 GB, 640135028736 bytes
	255 heads, 63 sectors/track, 77825 cylinders, total 1250263728 sectors
	Units = sectors of 1 * 512 = 512 bytes
	Sector size (logical/physical): 512 bytes / 512 bytes
	I/O size (minimum/optimal): 512 bytes / 512 bytes
	Disk identifier: 0x00000000

	   Device Boot      Start         End      Blocks   Id  System
	/dev/sda1               1  1250263727   625131863+  ee  GPT

Make a mount point and mount and/or unmount the drive.

	pi@calculon ~ $ sudo mkdir /mnt/usbdrive
	pi@calculon ~ $ sudo mount /dev/sda1 /mnt/usbdrive
	pi@calculon ~ $ sudo umount /dev/sda1 


## Formatting Disk

Starting with a USB hard drive 640GB formated in OSX's HSF+, I needed to change it to ext4:

	pi@calculon ~ $ sudo parted /dev/sda
	GNU Parted 2.3
	Using /dev/sda
	Welcome to GNU Parted! Type 'help' to view a list of commands.
	(parted) p                                                                
	Model: Maxtor OneTouch (scsi)
	Disk /dev/sda: 640GB
	Sector size (logical/physical): 512B/512B
	Partition Table: gpt

	Number  Start  End  Size  File system  Name  Flags

	(parted) mkpart primary ext4 1 640000                                     
	(parted) p                                                                
	Model: Maxtor OneTouch (scsi)
	Disk /dev/sda: 640GB
	Sector size (logical/physical): 512B/512B
	Partition Table: gpt

	Number  Start   End    Size   File system  Name     Flags
	 1      1049kB  640GB  640GB               primary

	(parted) quit                                                             
	Information: You may need to update /etc/fstab.

**Note** in the `mkpart` line, the start and stop locations are in MB.

	pi@calculon ~ $ sudo mkfs.ext4 /dev/sda1 -L Calculon
	mke2fs 1.42.5 (29-Jul-2012)
	Filesystem label=Calculon
	OS type: Linux
	Block size=4096 (log=2)
	Fragment size=4096 (log=2)
	Stride=0 blocks, Stripe width=0 blocks
	39067648 inodes, 156249856 blocks
	7812492 blocks (5.00%) reserved for the super user
	First data block=0
	Maximum filesystem blocks=0
	4769 block groups
	32768 blocks per group, 32768 fragments per group
	8192 inodes per group
	Superblock backups stored on blocks: 
		32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208, 
		4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968, 
		102400000

	Allocating group tables: done                            
	Writing inode tables: done                            
	Creating journal (32768 blocks): done
	Writing superblocks and filesystem accounting information: done    

Now mount the drive and double check it:

	pi@calculon ~ $ sudo mount /dev/sda1 /mnt/usbdrive
	pi@calculon ~ $ df -h
	Filesystem      Size  Used Avail Use% Mounted on
	rootfs           15G  3.7G   11G  27% /
	/dev/root        15G  3.7G   11G  27% /
	devtmpfs        112M     0  112M   0% /dev
	tmpfs            24M  240K   23M   2% /run
	tmpfs           5.0M     0  5.0M   0% /run/lock
	tmpfs            47M     0   47M   0% /run/shm
	/dev/mmcblk0p1   56M  9.8M   47M  18% /boot
	/dev/sda1       587G   70M  557G   1% /mnt/usbdrive

Fix permissions:

	pi@calculon ~ $ sudo chown pi:pi /mnt/usbdrive
	pi@calculon ~ $ sudo chmod 777 /mnt/usbdrive
	pi@calculon ~ $ sudo ls /mnt/usbdrive -alh
	total 24K
	drwxrwxrwx 3 pi   pi   4.0K Dec 14 20:45 .
	drwxr-xr-x 3 root root 4.0K Dec 14 18:24 ..
	drwx------ 2 root root  16K Dec 14 20:45 lost+found

## Automounting

Add the following to fstab so it mounts on boot.

	sudo nano /etc/fstab
	/dev/sda1 /mnt/usbdisk auto defaults,user 0 1

This sets the file system to `auto` and `user` enables write permissions for all users. The 0 is for debugging and 1 is for a file system check at boot.

## Making available to OSX

Make the following changes to the config file, adding the drive to netatalk.

	pi@calculon ~ $ sudo pico /etc/netatalk/AppleVolumes.default 
	# The line below sets some DEFAULT, starting with Netatalk 2.1.
	:DEFAULT: options:upriv,usedots

	# By default all users have access to their home directories.
	~/			"Home Directory"
	/mnt/usbdrive

	# End of File

There are also options to enable Time Machine support (see tm).

Then restart `netatalk`:

	pi@calculon ~ $ sudo /etc/init.d/netatalk stop
	Stopping Netatalk Daemons: afpd cnid_metad papd timelord atalkd.
	pi@calculon ~ $ sudo /etc/init.d/netatalk start
	Starting Netatalk services (this will take a while):  cnid_metad afpd.

---
<a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a><br />This work by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Kevin Walchko</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative Commons Attribution-ShareAlike 3.0 Unported License</a>.

---

<a href="http://raspberrypi.stackexchange.com/users/1677/kevin">
<img src="http://raspberrypi.stackexchange.com/users/flair/1677.png" width="208" height="58" alt="profile for kevin at Raspberry Pi, Q&amp;A for users and developers of hardware and software for Raspberry Pi" title="profile for kevin at Raspberry Pi, Q&amp;A for users and developers of hardware and software for Raspberry Pi">
</a>
