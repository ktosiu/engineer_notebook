## Stop Safari re-opening windows

    defaults write com.apple.Safari ApplePersistenceIgnoreState YES
    defaults write com.apple.Preview ApplePersistenceIgnoreState YES
 
# Cross Compiling for Linux in OSX


CFLAGS="-march=armv6 -mfloat-abi=softfp -mfpu=vfp -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"
CXXFLAGS="-march=armv6 -mfloat-abi=softfp -mfpu=vfp -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"


## Setup

Much of this is taken from [twiq](http://www.rpiforum.net/forum/tutorials/article/16-a-raspberry-pi-emulated-environment-on-osx-lion/)

If you plan to use Linux, you can download compiler binaries [here](https://github.com/raspberrypi/firmware)
which will save you some work. I believe this compiler is an EABIHF compiler that has 
hardware floating point capability instead of the software floating point of EABI.

To set up an emulated environment of the Raspberry Pi software on OSX one will need:

1. An [ARM EABI Cross-Compiling Toolchain](https://github.com/jsnyder/arm-eabi-toolchain)
2. The [RPi Kernel](https://github.com/raspberrypi/linux).
3. The [RPi root filesystem](http://www.raspberrypi.org/downloads).
4. The Emulator ([QEMU](http://wiki.qemu.org/Main_Page)).
5. [Homebrew](https://github.com/mxcl/homebrew) installed
6. Apple's [Xcode](https://developer.apple.com/xcode/) and the command line tools 

## Using Crosstool-ng for Cross Compiler

You can also try [crosstool-ng](http://crosstool-ng.org/) explained by Chris Boot 
[here](http://www.bootc.net/archives/2012/05/26/how-to-build-a-cross-compiler-for-your-raspberry-pi/)
. 

    sudo apt-get install bison flex gperf makeinfo texinfo libtool automake 
    sudo apt-get install gawk libncurses5-dev subversion

## Alternate ARM Cross Compiler

First install the dependencies:

    brew install mpfr gmp libmpc libelf texinfo --use-llvm

Now mpfr has an issue with it, but the work around is to compile it with llvm.

Grab and compile the tool:

    mkdir ~/rpi
    mkdir ~/rpi/arm-cs-tools
    git clone https://github.com/jsnyder/arm-eabi-toolchain.git
    cd arm-eabi-toolchain
    PREFIX=$HOME/rpi/arm-cs-tools make install-cross
    make clean
    echo “export PATH=$HOME/rpi/arm-cs-tools/bin:$PATH” » ~/.bash_profile

---

## Linux Kernel (ARM)

The RPi Kernel Compilation

    mkdir ~/rpi/kernel
    cd ~/rpi/kernel
    git clone https://github.com/raspberrypi/linux.git
    cd linux

Unfortunately, at the time of this writing, the RPi kernel fails to build:

	size: file: arch/arm/boot/compressed/../../../../vmlinux is not an object file
	size: file: arch/arm/boot/compressed/../../../../vmlinux is not an object file
	size: file: arch/arm/boot/compressed/../../../../vmlinux is not an object file
	size: file: arch/arm/boot/compressed/../../../../vmlinux is not an object file
	  LD      arch/arm/boot/compressed/vmlinux
	arch/arm/boot/compressed/vmlinux.lds:77: undefined symbol `__OBJC' referenced in expression
	make[2]: *** [arch/arm/boot/compressed/vmlinux] Error 1
	make[1]: *** [arch/arm/boot/compressed/vmlinux] Error 2
	make[1]: Target `arch/arm/boot/zImage' not remade because of errors.
	make: *** [zImage] Error 2
	make: Target `_all' not remade because of errors.
    
Or you could grab Adafruit's kernel

    mkdir ~/rpi/kernel
    cd ~/rpi/kernel
    git clone https://github.com/adafruit/adafruit-raspberrypi-linux.git
    cd adafruit-raspberrypi-linux

Grab the config file and configure the kernel:

    cp arch/arm/configs/bcmrpi_cutdown_defconfig .config
    make ARCH=arm CROSS_COMPILE=~/rpi/arm-cs-tools/bin/arm-none-eabi- menuconfig

Save the configuration and let’s build the kernel afterwards. Note that the compilation 
should fail and complain about an <elf.h> inclusion in scripts/mod/mk_elfconfig. If it 
does, one must create the file:

    touch /usr/local/include/elf.h

Edit it and write the following:

    #include <libelf.h>

	#define R_386_NONE 0
	#define R_386_32 1
	#define R_386_PC32 2
	#define R_ARM_NONE 0
	#define R_ARM_PC24 1
	#define R_ARM_ABS32 2
	#define R_MIPS_NONE 0
	#define R_MIPS_16 1
	#define R_MIPS_32 2
	#define R_MIPS_REL32 3
	#define R_MIPS_26 4
	#define R_MIPS_HI16 5
	#define R_MIPS_LO16 6

and follow through the building process:

	make ARCH=arm CROSS_COMPILE=~/rpi/arm-cs-tools/bin/arm-none-eabi- -k

The image file is created and located as arch/arm/boot/zImage.

## The File System

You can grab one of several file systems from [RaspberryPi.org](http://www.raspberrypi.org/downloads)


## The Emulator

Due to a bug of a white screen hanging QEMU if compiled with llvm one must install the 
package apple-gcc42 from the homebrew’s dupes repository.

brew install homebrew/dupes/apple-gcc42 ???

And then compile and install qemu like:

	brew install qemu --use-gcc

Now we’re left with all we need to start the RPi distribution so let’s start it like:

	qemu-system-arm -M versatilepb -cpu arm1176 -hda debian6-19-04-2012.img -kernel zImage -append “root=/dev/sda2” -serial stdio -usbdevice tablet

and...

##Distcc [Raspbian]

sudo apt-get install distcc

sudo apt-get install distcc-pump [not tried]

export DISTCC_HOSTS='arch'

##Distcc [Arch Linux]

sudo pacman -S distcc

more ~/.distcc/hosts
arch

Modify /etc/conf.d/distccd with the following lines:

	PATH=/usr/local/x-tools/arm-unknown-linux-gnueabi/bin:$PATH
	DISTCC_ARGS="--user nobody --allow 192.168.1.0/24 --port 3632"

Not sure how useful the *port* switch is nor the *--user nobody*. It maybe necessary to change *user* to someone
 
**Warning: Arch Linux** /etc/rc.d/functions will reset PATH, make sure the /etc/conf.d/distccd gets called *after* /etc/rc.d/functions. You will have to modify /etc/rc.d/distccd to ensure this.

sudo /etc/rc.d/distccd start

Make sure distcc is working:

nmap -p 3632 arch

```bash
Starting Nmap 6.01 ( http://nmap.org ) at 2012-10-27 22:58 EDT
Nmap scan report for arch (127.0.0.1)
Host is up (0.00019s latency).
Other addresses for arch (not scanned): 127.0.0.1
PORT     STATE SERVICE
3632/tcp open  distccd

Nmap done: 1 IP address (1 host up) scanned in 0.06 seconds
```

###Terms

**Note:** The terminology used by the software can be a bit counterintuitive in that "the daemon" is the master and "the server(s)" are the slave PC(s) in a distcc cluster.

###distcc daemon [has source]
The PC or server that's running distcc to distribute the source code. The daemon itself will compile parts of the source code but will also send other parts to the hosts defined in DISTCC_HOSTS.

###distcc server [does compiling]
The PC or server compiling the source code it gets from the daemon. When it's done compiling, it sends back the object code (i.e. compiled source code) to the daemon, which in turn sends back some more source code (if there's any left to compile).

###Tips/Tricks

####Relocate $HOME/.distcc

By default, distcc creates $HOME/.distcc which stores transient relevant info as it serves up work for nodes to compile. Create a directory named .distcc in RAM such as /tmp and soft link to it in $HOME. This will avoid needless HDD read/writes and is particularly important for SSDs.

    $ mv $HOME/.distcc /tmp
    $ ln -s $HOME/.distcc /tmp/.distcc

One only needs to have /etc/rc.local re-create this directory on a reboot (the soft link will remain until it is manually removed like any other file):

    su -c "mkdir /tmp/.distcc" USERNAME


##Setup Cross Compile [Doesn't work]

Follow setting up distcc instructions on both an embedded computer (RaspberryPi) and a powerful computer (a virtual machine located on my Macbook)

Install linux cross compilers from ARM using on the virtual machine:

    sudo apt-get install gcc-arm-linux-gnueabihf
	sudo apt-get install g++-arm-linux-gnueabihf

Note that the search function doesn't seem to work with gcc-arm in the software GUI installer because of the dashes. Try using the commandline:

    sudo apt-cache search gcc-arm

## Test It Out

Log into a RaspberryPi and set the environment variable to:

	export DISTCC_HOSTS=192.168.1.11

Here, the computer 192.168.1.11 is a virtual machine running Ubuntu 12.10. My embedded raspberrypi computer will use this computer and its compiler for building.

Now make a simple project using cmake:

	cmake_minimum_required(VERSION 2.4.6)
	add_executable (test test.c)

Note you could have created test.cpp and done a c++ test instead. And a simple c file called test.c:

	#include<stdio.h>
	
	int main(){
		printf("hello ARM C\n");
		return 0;
	}

Now make a build directory and change into it and issue the following command:

	[kevin@raspberrypi build]$ CC="distcc arm-linux-gnueabihf-gcc" CXX="distcc arm-linux-gnueabihf-g++" cmake ..

Once that is done, you can do a "make" and the binary will get compiled. Make sure the binary is an ARM executable: 

	[kevin@raspberrypi build]$ file test
    test: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26,    BuildID[sha1]=0x2710e7f62bb42b0734650f13ab1e7921b73b139a, not stripped


**Note** this is the product of a natively compiled test.c:

	file test
	test: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26, BuildID[sha1]=0x4d3dbf9f1bde8ff79dc0faa0ae6ee9e337ddbb81, not stripped
  
