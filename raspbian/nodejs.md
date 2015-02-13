# Installing Node.js

The version in apt-get is old, do:

	wget http://nodejs.org/dist/v0.10.28/node-v0.10.28-linux-arm-pi.tar.gz
	tar -zxvf node-v0.10.28-linux-arm-pi.tar.gz 
	mkdir /opt/node
	chown pi:pi /opt/node
	mv node-v0.10.26-linux-arm-pi/* /opt/node
	ln -s /opt/node/bin/node /usr/local/bin/node
	ln -s /opt/node/bin/node /usr/bin/node
	ln -s /opt/node/bin/npm /usr/local/bin/npm
	ln -s /opt/node/bin/npm /usr/bin/npm

	sudo npm install -g http-server