# Installing on Debian from SVN for Raspbian

*This document is modified from the originial [here](http://www.ros.org/wiki/ROSberryPi/Setting%20up%20ROS%20on%20RaspberryPi). I just added more details and made it more RPi specific.*

Install from SVN requires that you download and compile the source code on your own. The main supported version of Debian is version 6, "Squeeze", but it is possible that later versions are working. If you plan to use a newer version like "Wheezy" (version 7) or "Sid" (unstable), please see the bottom paragraph.

##Installation

###Setup

	sudo apt-get install build-essential python-yaml cmake subversion wget python-setuptools mercurial

Add *contrib* to your /etc/apt/sources.list for some packages.

	more /etc/apt/sources.list
	deb http://mirrordirector.raspbian.org/raspbian/ wheezy main contrib non-free rpi

If you have to add *contrib*, don't forget to do an "apt-get update" after this change to search for the new packages!

Install bootstrap dependencies:

	sudo apt-get install build-essential python-yaml cmake subversion wget python-setuptools mercurial git-core

Install core library dependencies (aka, 'ROS Base'):

	sudo apt-get install python-yaml libapr1-dev libaprutil1-dev  libbz2-dev python-dev libgtest-dev python-paramiko libboost-all-dev liblog4cxx10-dev pkg-config python-empy swig

You will need pip to install some python packages:

    sudo apt-get install python-pip

The Python "nose" package version 1.0 or later is required. If you are using Debian 6 (squeeze) or earlier, use pip to install it:

	sudo pip install nose

Otherwise, if you are using Debian 7 (wheezy) or later, use the Debian package:

	sudo apt-get install python-nose

Setup your environment, the assumption here is PRi is based off Debian Squeeze and you are using distcc to help cross compile:

	export ROS_OS_OVERRIDE=debian:wheezy
	export DISTCC_HOSTS=arch
	export CC="distcc arm-unknown-linux-gnueabi-gcc" 
	export CXX="distcc arm-unknown-linux-gnueabi-g++"

*Note:* even though I set my CC and CXX environment up to use the cross compiler, I will still append this to the compile commands below as a reminder.

*Note:* arch is my iMac (x86_64) desktop that my home router will resolve to something like 192.168.1.14. Change to the appropriate computer name or IP address. 

###rosdep failure

Right now, rosdep seems to fail on loading dependencies, so to make like easy add these:

* bullet: freeglut3-dev
* orocous_kdl: libeigen3-dev
* python_orocous_kdl: libcppunit-dev python-sip-dev
* camera_calibration_parsers: libyaml-cpp-dev
* kinect: libusb-1.0.0.-dev
* libfreenect: libxmu-dev libxi-dev

Basically just do:

	sudo apt-get install packages

where *packages* are the ones listed in the bulleted list above.

###rosinstall

The following steps requires two separate installation steps and will compile ROS-related code into two separate places/layers:

1. Download and install the underlying core ROS libraries and tools into /opt/ros/fuerte. While it is possible to install elsewhere (e.g. /usr), this is not well tested and you will encounter various problems along the way (e.g. having to change rosinstall files, having to manually install system dependencies, etc...). Please see REP 122: Filesystem Hiearchy Layout for more detailed documentation on how the installed files are placed.

2. Download and build some higher-level ROS libraries using rosmake in ~/ros.

##Layer 1: Install core libraries

The following instructions will create a system install of the core ROS libraries and tools. The installation is done using standard CMake/make tools, so experts can adjust to their liking.

ROS-Base: (Bare Bones) ROS package, build, and communication libraries.

	rosinstall --catkin ~/ros-underlay http://ros.org/rosinstalls/fuerte-ros-base.rosinstall

Build and install the underlay into /opt/ros/fuerte:

	cd ~/ros-underlay
	mkdir build
	cd build

Now, run cmake. The invocation depends on the platform you are on:

	CC="distcc arm-unknown-linux-gnueabi-gcc" CXX="distcc arm-unknown-linux-gnueabi-g++" cmake .. -DCMAKE_INSTALL_PREFIX=/opt/ros/fuerte

Note the compiler name after the CC and CXX might be slightly different. It depends on what you did and how you setup your cross compliler. 

Finally, build + install the code:

	make -j8
	sudo make install

Verify the installed environment:

	. /opt/ros/fuerte/setup.bash
	which roscore

You should see:

	/opt/ros/fuerte/bin/roscore

You can delete ~/ros-underlay now, if you wish. The ROS core libraries are now installed onto your system.

##Layer 2: Higher-level robotics libraries and tools

Now it's time to create the second layer, which contains your main robotics libraries (e.g. navigation) as well as visualization tools like rviz. You will build this layer using rosmake, but it is not installed.

There are many different libraries and tools in ROS. We provided four default configurations to get you started.

NOTE: The rosinstall installation files below assume that you've installed into /opt/ros/fuerte, so you will need to change them manually if you have a different install path.

Desktop-Full Install: ROS Full, rviz, robot-generic libraries, 2D/3D simulators, navigation and 2D/3D perception

	rosinstall ~/ros "http://packages.ros.org/cgi-bin/gen_rosinstall.py?rosdistro=fuerte&variant=desktop-full&overlay=no"

*NOTE:* the instructions above download all stacks inside the ~/ros folder. If you prefer a different location, simply change the ~/ros in the commands above.

*Note:* Not everything will install or compile, but that is not the point. 

Please reference [REP 113](http://ros.org/reps/rep-0000.html) for description of other available configurations.

###Environment Setup

Shell language:   Bash     Zsh    

You'll now need to update your environment. You can do this by typing:

	source ~/ros/setup.bash

It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched, which you can do with the command below:

	echo "source ~/ros/setup.bash" >> ~/.bashrc
	. ~/.bashrc

###Build Higher-level/tools (Layer 2)

First, initialize your rosdep. ROS Fuerte comes with rosdep 2. If you get a message that your default sources list exists, then don't worry as it means you've done this before.

	sudo rosdep init
	rosdep update

Now, use rosdep 2 to install system dependencies. Many of the system dependencies will install into /opt/ros/fuerte and will not be usable if you have changed the installation prefix.

	rosdep install -ay --os=debian:wheezy

Finally, build the ROS stacks using rosmake.

	CC="distcc arm-unknown-linux-gnueabi-gcc" CXX="distcc arm-unknown-linux-gnueabi-g++" rosmake -a

**Not completely compiled yet**