Bluetooth
=========

.. figure:: ../pics/bluetooth.png
   :width: 200px

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
