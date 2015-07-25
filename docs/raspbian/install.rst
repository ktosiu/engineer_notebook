Raspberry Pi (RPi)
===================

.. figure:: ../pics/rpi-org.png
   :width: 200px
	:align: center


Where to buy?
-------------

I always buy mine from `Adafruit <https://www.adafruit.com>`__, they
have tons of other great stuff at great prices. They also make make lots
of example code and drivers available for their products.

Install
--------

`Raspbian <http://www.raspbian.org>`__ is a Raspberry optimized version
of Debian. The version installed here is based on Debian Wheezy.

::

    [kevin@raspberrypi ~]$ lscpu
    Architecture:          armv6l
    Byte Order:            Little Endian
    CPU(s):                1
    On-line CPU(s) list:   0
    Thread(s) per core:    1
    Core(s) per socket:    1
    Socket(s):             1

Note this output doesn't really tell you much other than it is ARMv6.

Copying an image to the SD Card in Mac OS X
-------------------------------------------

.. figure:: ../pics/sd.jpg
   :width: 200px
   :alt: sd logo

These commands and actions need to be performed from an account that has
administrator privileges.

1. Download the image from a `mirror or
   torrent <http://www.raspberrypi.org/downloads>`__.

2. Verify if the the hash key is the same (optional), in the terminal
   run::

       shasum ~/Downloads/debian6-19-04-2012.zip

3. Extract the image::

       unzip ~/Downloads/debian6-19-04-2012.zip

4. Attach the SD Card to the computer and identify the mount point::

       df -h

   Record the device name of the filesystem's partition, e.g.
   ``/dev/disk3s1``

5. Unmount the partition so that you will be allowed to overwrite the
   disk, note that unmount is **NOT** the same as eject:

   ::

       sudo diskutil unmount /dev/disk3s1

   Using the device name of the partition work out the raw device name
   for the entire disk, by omitting the final "s1" and replacing "disk"
   with "rdisk" (this is very important: you will lose all data on the
   hard drive on your computer if you get the wrong device name). Make
   sure the device name is the name of the whole SD card as described
   above, not just a partition of it (for example, rdisk3, not rdisk3s1.
   Similarly you might have another SD drive name/number like disk2 or
   disk4, etc. -- recheck by using the df -h command both before & after
   you insert your SD card reader into your Mac if you have any
   doubts!): e.g. ``/dev/disk3s1`` => ``/dev/disk3``

   **Note:** Using rdisk3 might be faster than using disk3, need to look
   into this.

6. Write the image to the card with this command, using the raw disk
   device name from above (read carefully the above step, to be sure you
   use the correct rdisk# here!):

   ::

       sudo dd bs=1m if=~/rasbian.img of=/dev/rdisk3

   If the above command report an error(dd: bs: illegal numeric value),
   please change bs=1M to bs=1m.

   Note that dd will not feedback any information until there is an
   error or it is finished, information will show and disk will re-mount
   when complete. However if you are curious as to the progresss -
   ctrl-T (SIGINFO, the status argument of your tty) will display some
   en-route statistics.

7. After the dd command finishes, eject the card:

   ::

       sudo diskutil eject /dev/disk3

8. Insert it in the raspberry pi, and have fun

Configuration
--------------

Once you download and install Raspbian you have to configure it for it to be useful.

#. ``sudo raspi-config`` and change
    #. update ``raspi-config`` via the advanced option, update
    #. hostname
    #. memory split between GPU and RAM
    #. resize the file system to the size of your disk
    #. set correct timezone via the internationalization option
    #. turn on I2C interface
#. ``sudo apt-get update`` and then ``sudo apt-get upgrade``
#. ``sudo apt-get install apt-show-versions``
#. ``sudo easy_install pip`` then ``sudo pip install -U pip`` to get the latest pip version
#. ``sudo apt-get install rpi-update`` and then ``sudo rpi-update`` to update the kernel
#. Fix the pip paths so you don't have to use sudo (that is a security risk)
    #. ``sudo chown -R pi /usr/local``
    #. ``sudo chown -R pi /usr/lib/python2.7/dist-packages``
    #. ``sudo chown -R pi /usr/share/pyshare``
#. Fix the ``pip`` certificate warnings
    #. ``sudo apt-get install python-dev libffi-dev``
    #. ``pip install -U urllib3 certifi pyopenssl``
#. Find outdated python libraries with ``pip list --outdated`` then update them with ``pip install -U package_name``


SSH Login
---------

To increase security, you can disable password logins and rely on ssh
public keys. To do this, take a look
`here <https://wiki.archlinux.org/index.php/SSH_Keys>`__ for details.
Basic steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA
   (1024 bit) both public and private keys. They will be stored in
   ``~/.ssh`` with the public key having .pub appended to the end::

       ssh-keygen -C "$(whoami)@$(hostname)-$(date -I)"

   Note you can create a key for a different username if you change
   $(whoami) to the user name you want.

2. Copy the public key (.pub) to the server you will connect to::

       ssh-copy-id username@remote-server.org 

   This should update ~/.ssh/authorized\_keys in the process. Also
   ensure the correct protections are on the file by::

       chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/ssh/sshd\_config to disable password logins.

   ::

       PasswordAuthentication no
       ChallengeResponseAuthentication no

OSX
~~~~

On OSX install ``ssh-copy-id`` via ``brew`` and in a terminal window on OSX::

    ssh-copy-id pi@raspberry.local

Sound
-----

Double check sound works::

    aplay /usr/share/sounds/alsa/Front_Center.wav


/boot/config.txt
----------------

You can change the Pi's default settings for CPU MHz and memory split
(between RAM and GPU) using ``raspi-config``. An alternate way is to
simply edit the ``/boot/config.txt``.

::

    [kevin@raspberrypi ~]$ more /proc/cpuinfo
    Processor   : ARMv6-compatible processor rev 7 (v6l)
    BogoMIPS    : 795.44
    Features    : swp half thumb fastmult vfp edsp java tls
    CPU implementer : 0x41
    CPU architecture: 7
    CPU variant : 0x0
    CPU part    : 0xb76
    CPU revision    : 7

    Hardware    : BCM2708
    Revision    : 0002
    Serial      : 000000008e0a5a17

    [kevin@raspberrypi ~]$ free -h
                 total       used       free     shared    buffers     cached
    Mem:          232M        57M       174M         0B        11M        28M
    -/+ buffers/cache:        18M       214M
    Swap:          99M         0B        99M

The output here shows overclocked to 800 MHz and the GPU given only 16
MB of RAM. Now the CPU MHz will change dynamically based on load. So
with no load, my 800 MHz system will default to the original 700 MHz
system. If you want to always be running at max speed, put
``force_turbo=1`` in the ``/boot/config.txt``::

    [kevin@raspberrypi ~]$ more /boot/config.txt
    #uncomment to overclock the arm. 700 MHz is the default.
    arm_freq=800

    # for more options see http://elinux.org/RPi_config.txt
    gpu_mem=16     # can be 16, 64, 128 or 256
    core_freq=250
    sdram_freq=400
    over_voltage=0
    force_turbo=1

More info can be found
`here <http://www.raspberrypi.org/documentation/configuration/config-txt.md>`__.
