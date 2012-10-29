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
