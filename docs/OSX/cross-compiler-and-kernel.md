
CFLAGS="-march=armv6 -mfloat-abi=softfp -mfpu=vfp -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"
CXXFLAGS="-march=armv6 -mfloat-abi=softfp -mfpu=vfp -O2 -pipe -fstack-protector --param=ssp-buffer-size=4 -D_FORTIFY_SOURCE=2"


# Setup

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