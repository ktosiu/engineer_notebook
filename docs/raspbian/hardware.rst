Hardware
========

.. figure:: ../pics/rpi.png
   :width: 200px
	:align: center

Pinouts
-------

Depending on the version of the rpi you have, there are different
pinouts for the different versions. A great resource is
`Pinout <http://pi.gadgetoid.com/pinout>`__ to figur out what pin is
what.

.. figure:: ../pics/pinout.jpeg
   :width: 300px

Lights
------

The main indicators are the lights on the front corner of the board.
These are:

::

    OK (green): The board is active (blinks off when accessing the SD card)
    PWR (red): The board is successfully powered from USB
    FDX (green): Network is full-duplex
    LNK (green): The network cable is connected (blinks off when transferring data to/from the network)
    10M (yellow): Lit when the board is using a 100Mbps link, not lit when using a 10Mbps

i2c
---

First we need to load the drivers

::

    sudo modprobe i2c-dev
    sudo modprobe i2c-bcm2708

Now ``/dev/i2c-0`` and ``/dev/i2c-1`` should exist. Also, so see what is
on the i2c bus, install the ``i2c-tools`` using::

    sudo apt-get install i2c-tools

Now to explore the i2c bus try::

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

To have these load at boot, add them to ``/etc/modules``.

USB Camera
----------

To use the Logitech C270 camera you need to add your user (pi in this
case) to the video group:

::

    sudo usermod -a -G video pi

For other users, just change pi to the correct username. Then make sure
the driver is loaded:

::

    sudo modprobe uvcvideo

You can double check it works by grabbing an image:

::

    sudo apt-get install fswebcam

    fswebcam image.jpg

If an image appeared, then all is good.
