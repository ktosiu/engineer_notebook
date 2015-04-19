Other
-----

Install these additional tools

::

    sudo apt-get install libsdl1.2-dev libncurses5 libncurses5-dev
    sudo apt-get install autoconf fakeroot realpath
    sudo apt-get install git-core wget

Install Scratchbox2
===================

Alternate
---------

Instead of building scratchbox2 and qemu from source, you can install it
form apt-get. However, I can't find qemu exactly ... there seems to be
other options.

::

    sudo apt-get install scratechbox2 sbrsh qemu-user

Not sure I need sbrsh ... could delete it.

--------------

Scratchbox2 building
--------------------

Installing in subdirectories in the user's home directory makes it easy
to keep things organised. It makes things almost idiotproof when you
want to upgrade the ARM toolchain, scratchbox2, qemu or change the seed
rootfs etc. as it's pretty much just rename the old directory, create a
new directory and if neccessary rerun sb2-init.

Open a terminal and create a directory for temporary use.

::

    mkdir hold
    cd hold

Download scratchbox2 and qemu from their respective git repositories

::

    git clone git://gitorious.org/scratchbox2/scratchbox2.git
    git clone git://git.qemu.org/qemu.git

Download the codesourcery ARM toolchain. I have been using the 2011.03
version successfully and I believe it was the last released version
before codesourcery was bought by Mentor Graphics who seem to have
closed sourced the more recent releases of the toolchain.

::

    wget https://sourcery.mentor.com/sgpp/lite/arm/portal/...

Then download an ARM rootfs. You have several options, you can download
the `Official <http://www.raspberrypi.org/downloads>`__ RaspberryPi or
try
`Adafruit's <http://learn.adafruit.com/adafruit-raspberry-pi-educational-linux-distro/occidentalis-v0-dot-2>`__.
Adafruit's version includes things like I2C, SPI, and other drivers
useful for hacking. Grab one of these distributions using **ONE** of the
following wget commands:

::

    wget ...
    wget ...

Now create some more directories:

::

    mkdir ../raspberry_pi_dev
    mkdir ../raspberry_pi_dev/qemu
    mkdir ../raspberry_pi_dev/scratchbox2
    mkdir ../raspberry_pi_dev/rootfs

Untar the rootfs using sudo. A normal user cannot create some file
system components when untarring a tarred rootfs so sudo is used.

::

    sudo tar xjvpf rootfs*.tar.bz2 -C ../raspberry_pi_dev/rootfs

Extract the codesourcery ARM toolchain into the
raspberry\_pi\_development directory.

::

    tar xjvpf arm-2011.03*tar.bz2 -C ../raspberry_pi_dev

Do a directory listing of the raspberry\_pi\_development directory and
it will look like the image below.

???

Change into the scratchbox2 directory and run the autogen.sh script and
make.

::

    cd scratchbox2
    ./autogen.sh
    make install prefix=$HOME/raspberry_pi_dev/scratchbox2

Scratchbox2 is now installed and we now need to build qemu so cd to the
qemu directory

::

    cd ../qemu

To use scratchbox2 you only need to build qemu usermode for ARM,
however, I find it useful to also build the ARM system emulation as well
(I use the qemu full system emulation for some little hacks and tricks
that are beyond the scope of this howto but I will write them up at a
later date along with how to use scratchbox2 with real hardware once I
have the process down pat & actually have a real Raspberry Pi to test
on).

::

    ./configure --prefix=$HOME/raspberry_pi_dev/qemu --target-list=arm-linux-user,arm-softmmu
    make && make install

Now that scratchbox2, the toolchain, qemu and the seed rootfs are
installed we just have a few more steps before we can actually use the
VM for compiling software. First of all we need to add the scratchbox2
and qemu bin directories to our PATH environment variable. You can do
this as a single export statement but so it's clear i'll do it as two.

::

    export PATH=$HOME/raspberry_pi_dev/scratchbox2/bin:$PATH
    export PATH=$HOME/raspberry_pi_dev/qemu/bin:$PATH

You will also want to add the previous two lines to your /etc/bashrc
file.

change to the rootfs directory

::

    cd raspberry_pi_dev/rootfs

before we can use the seed rootfs inside scratchbox2 we need to change
the owner, group and permissions so that it is read/writable by our
non-root account.

::

    sudo chown -R USER_NAME *
    sudo chgrp -R GRP_NAME *
    chmod -R 777 *

where **USER\_NAME** is your user login name and **GRP\_NAME** can be
any group, but you could also your own group.

There is just one more thing to do before we can start using
scratchbox2. We need to initialize it. While inside the the seed rootfs
directory. In this case rootfs

::

    sb2-init USER_NAME $HOME/raspberry_pi_dev/arm-2011.03/bin/arm-none-linux-gnueabi-gcc

sb2-init actually has a lot of options you can use but in most cases
they just complicate matters and for our needs the above command line is
good enough. What it actually means is configure scratchbox2 to create a
target called raspberry and use the toolchain binaries that we have
installed in $HOME/raspberry\_pi\_dev/arm-2011.03/bin

As you get more familar with scratchbox2 you might want to experiment
with things such as having multiple targets with a single scratchbox2
installation etc.

After a short wait your screen will look something like this

???

You are now ready to start using scratchbox2 to compile software.
However, I do a few more things just to make life easier that you might
also want to do. I create a directory called $HOME/build, install an ssh
server and apache2 and put a symlink of the build directory in the
apache2 directory tree. This allows me to keep all my ARM binaries an
source seperate from anything else and lets me get them out of the VM
easily although I could also use shared folders but I prefer using a
webserver as then any machine on my network can access them. I got a bit
bored doing the screenshots and cutting out the relevant parts so here
is a video of me doing this final bit of setup

???

If you have got this far you are now ready to start building software
for the Raspberry Pi. As a test I create a C hello world program and
check that it compiles and runs both in the host os and also inside
scratchbox2 and if that works then I check that the seed rootfs's
package manager works. If both do then i'll start using the vm. Again
because I am bored with doing screenshots here is a short video of that
process.

???
