RPI Tool Chain
-----------------------------------------

The Raspberry Pi Foundation is providing a ready-to-use toolchain on
their github repository. You can use it to save yourself some time.

To do so, you need to have git installed and to clone the repository ::

    > sudo apt-get install git-core
    > git clone https://github.com/raspberrypi/tools.git --depth=1
    > export PATH=$PATH:$HOME/tools/arm-bcm2708/gcc-linaro-arm-linux-gnueabihf-raspbian/bin

The "--depth=1" is here to tell git we only want the last revision, and
not the whole history to be cloned.

Create a new file named test.cpp and copy/paste the following code::

    #include <iostream>

    int main(void)
    {
        std::cout<<"Hello ARM world !\n";
        return 0;
    }

Then, enter the following commands::

    > arm-linux-gnueabihf-g++ test.cpp -o test
    > file test
    test: ELF 32-bit LSB executable, ARM, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26, BuildID[sha1]=0xfd72b5c6878433eb7f2296acceba9f648294a58c, not stripped

As you see, you can't execute this program on your PC. The file command
tells you that this executable is built for ARM processors.
