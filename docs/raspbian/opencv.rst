OpenCV
============

.. figure:: ../pics/opencv.png
   :width: 200px
   :align: center

Determine Kernel version and upgrade
------------------------------------

::

	sudo apt-get install build-essential cmake cmake-curses-gui pkg-config libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libtiff4-dev libtiff4 libtiffxx0c2 libtiff-tools libeigen3-dev
	sudo apt-get install libjpeg8 libjpeg8-dev libjpeg8-dbg libjpeg-progs ffmpeg libavcodec-dev libavcodec53 libavformat53 libavformat-dev libxine1-ffmpeg libxine-dev libxine1-bin libunicap2 libunicap2-dev swig libv4l-0 libv4l-dev python-numpy libpython2.6 python-dev python2.6-dev libgtk2.0-dev
				
	git clone https://github.com/Itseez/opencv.git
	cd opencv/
	git checkout tags/3.0.0
	mkdir build
	cd build/
	cmake ../
	make
	sudo make install
	sudo ldconfig

If you have a RPi2, suggest also using libtbb to take advantage of multicore.


