Bluetooth
=========

.. image:: ../pics/bluetooth.png
	:scale: 20

Dongle
------

Make sure your bluetooth dongle is working:

::

    pi@calculon ~ $ lsusb
    Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp. 
    Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
    Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. 
    Bus 001 Device 004: ID 0a12:0001 Cambridge Silicon Radio, Ltd Bluetooth Dongle (HCI mode)
    Bus 001 Device 005: ID 0bc2:3312 Seagate RSS LLC 

Device 004 is my bluetooth dongle.

Audio
-----

References
`1 <http://blog.whatgeek.com.pt/2014/04/20/raspberry-pi-bluetooth-wireless-speaker/>`__
`2 <http://www.correderajorge.es/bluetooth-on-raspberry-audio-streaming/>`__

Get the bluetooth software:

::

    sudo apt-get install bluetooth bluez-utils bluez-alsa

Add ``pi`` to the user group:

::

    sudo gpasswd -a pi bluetooth

Start up bluetooth dongle:

::

    sudo hciconfig hci0 up

Scan for bluetooth devices

::

    pi@calculon ~ $ hcitool scan
    Scanning ...
        44:2A:60:D6:49:34   Dalek

If you need to figure out what your bluetooth hardware address is for
``hci0``:

::

    hcitool dev

Pair with device using
``bluetooth-agent --adapter hci0 <pin> <hardware_id>``:

::

    bluetooth-agent --adapter hci0 0000 00:11:67:8C:17:80

See if device is trusted or not:

::

    bluez-test-device trusted <hardware_id>

If it returns a ``0`` then it is not trusted and a ``1`` if it is
trusted. To make it trusted:

::

    bluez-test-device trusted <hardware_id> yes

Edit/create ``~/.asoundrc`` with:

::

    pcm.bluetooth {
                    type bluetooth
                    device <hardware_id>
    }

**Note:** You may have to copy this file and rename it to:
``/etc/asound.conf``

Edit ``/etc/bluetooth/audio.conf`` and add the following to the
``[General]`` section:

::

    Disable=Media
    Enable=Socket,Sink,Source

Restart bluetooth service with:

::

    sudo /etc/init.d/bluetooth restart

Audio Programs
--------------

::

    mplayer -ao alsa:device=bluetooth sound.mp3
    mpg321 -a bluetooth -g 15 sound.mp3

iBeacon
=======

I2C
---

Get software:

::

    sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev

Additionally, get:

::

    sudo apt-get install bluez bluez-tools python-bluez 

Check status of bluetooth

::

    $ hciconfig 
    hci0:   Type: BR/EDR  Bus: USB
    BD Address: 00:1A:7D:DA:71:13  ACL MTU: 310:10  SCO MTU: 64:8
    UP RUNNING 
    RX bytes:2401 acl:0 sco:0 events:119 errors:0
    TX bytes:2155 acl:0 sco:0 commands:119 errors:0

If it is already up and running, you can shut it down with:

::

    sudo tools/hciconfig hci0 down

Now turn it on:

::

    sudo tools/hciconfig hci0 up
    sudo tools/hciconfig hci0 leadv
    sudo tools/hciconfig hci0 noscan

Then send one of these commands:

::

    sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 E2 0A 39 F4 73 F5 4B C4 A1 2F 17 D1 AD 07 A9 61 00 00 00 00 C8 00
    sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 E2 C5 6D B5 DF FB 48 D2 B0 60 D0 F5 A7 10 96 E0 00 00 00 00 C8 00

Format

::

    hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 [UUID] [Major] [Minor] [Power]

where, Manufacturers Specific Data starts with FF and 4C 00 is for
Apple. The other stuff is:

::

    UUID: E2C56DB5-DFFB-48D2-B060-D0F5A71096E0
    Major: 00 00
    Minor: 00 00
    Power: C8

You should see it appear on a bluetooth finder `Locate
Beacon <https://itunes.apple.com/us/app/ibeacon-locate/id738709014>`__
by Radius Networks.

To stop transmission:

::

    sudo hciconfig hci0 noleadv

iBeacon Software
----------------

``git clone https://github.com/carsonmcdonald/bluez-ibeacon.git``

iBeacon-Scanner: ``git clone https://github.com/switchdoclabs/iBeacon-Scanner-.git``

BeaconAirPython: ``git clone https://github.com/switchdoclabs/BeaconAirPython.git``

I2C
===

``sudo apt-get install python-smbus sudo apt-get install i2c-tools``

::

	pi@bender ~ $ sudo i2cdetect -y 1 0 1 2 3 4 5 6 7 8 9 a b c d e f 00: --
	-- -- -- -- -- -- -- -- -- -- -- -- 10: -- -- -- -- -- -- -- -- 18 -- --
	-- -- -- 1e -- 20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 30:
	-- -- -- -- -- -- -- -- -- -- -- UU -- -- -- -- 40: -- -- -- -- -- -- --
	-- -- -- -- -- -- -- -- -- 50: -- -- -- -- -- -- -- -- -- -- -- -- -- --
	-- -- 60: -- -- -- -- -- -- -- -- -- 69 -- -- -- -- -- -- 70: -- -- --
	-- -- -- -- --

This shows what things are on the I2C bus: 0x18 (accelerometers), 0x1e
(forget?), and 0x69 (gyros).

Next, get Adafruit's python code:

``git clone https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git``
