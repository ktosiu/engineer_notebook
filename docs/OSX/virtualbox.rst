Virtualbox
==========

Raspberry Pi VM Setup
=====================

This HOWTO follows the work by `Russell
Davis <http://russelldavis.org>`__ for setting up a cross compiling
environment for the Raspberry Pi. I have modified his instructions to
make them more ROS specific.

If you don't already have Virtualbox and the Extension pack installed
then you'll need to download it from
https://www.virtualbox.org/wiki/Downloads, choosing the correct one for
your platform and also download the Extension Pack from the same page if
you haven't already installed it. Once you have downloaded and installed
Virtualbox+Extension pack for your platform move on to step 2.

1. You can download the Ubuntu iso from the `Ubuntu
   website <http://www.ubuntu.com/download/ubuntu/download>`__

2. Once you have the Ubuntu iso downloaded, start Virtualbox and create
   a new Virtual machine by clicking the New button. Virtualbox will
   then start the Virtual Machine Wizard. Give your VM a name. I suggest
   something like RaspberryPi Development. Choose Linux & Ubuntu from
   the dropdowns (or if you are not going to use Ubuntu as the guest os
   then select whichever distro you are going to use). It should look
   something like this

3. Choose the amount of memory to allocate to the VM, give it 1 or 2 GB
   of ram.

4. Create a virtual harddisk and choose VDI which will be dynamically
   allocated. Make it at least 8GB to hold everything. The harddisk will
   resize dynamically.

5. Click the Create button. You will then be returned to the main
   Virtualbox screen with the VM you have just created highlighted click
   the Settings button.

6. Now open up the setting for the VM you just created. The only setting
   you MUST change:

-  storage
-  networking
-  video

7. Go to the storage tab and click the little CD icon. Add the iso you
   downloaded earlier from Ubuntu. This will only effect this boot
   cycle. After you install Linux, the disk image will automatically be
   removed.

8. Go to the networking tab and ensure NAT is selected so you can see
   the interweb. This will also allow you to install updates and 3rd pa

9. Go to the video tab and sensure 3D acceleration is turned off and
   there is enough video memory for your VM ... I selected 32 MB.

Install Linux
=============

Now hit start on the Virtualbox screen and install Linux.

If you this error message:

::

    piix4_smbus 0000.00.07.0: SMBus base address uninitialized - upgrade bios or use force_addr=0xaddr

Fix based on work by `Karl Foley <http://finster.co.uk>`__, in a
terminal type:

::

    sudo vi /etc/modprobe.d/blacklist.conf

Add the line blacklist i2c\_piix4 to the end of the file and save

::

    sudo update-initramfs -u -k all
    sudo reboot

Also make sure you have the development tools installed

::

    sudo apt-get install build-essential

Also to reduce the size of the install, I uninstalled office, game, and
other unneeded software.

Bonjour
-------

see kinect/README.md

SSH Server
----------

see kinect/README.md

VM Commands
===========

VBoxHeadless --startvm vb\_ros

VBoxManage controlvm vb\_ros poweroff \| pause \| reset

Networking
----------

In order for your vm to see the internet and other attached vm and
computers, you must use a bridged connection. However on **OSX** the
bridged network doesn't work if you are using a wireless connection
(airport). A real wired connection works fine in OSX (10.8.2 tested).
