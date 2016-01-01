Node.js
=======

.. figure:: ../pics/nodejs.png
	:width: 200px
	:align: center

Installing Node.js
------------------

The version in apt-get is old (at the time of this writing), `<http://node-arm.herokuapp.com/>`__ do:

::

	wget http://node-arm.herokuapp.com/node_latest_armhf.deb
	sudo dpkg -i node_latest_armhf.deb
	
	# now sudo messed up some permisions, so we need to fix them
	sudo chown -R pi:pi /usr/local
	
	# Check to see if installation works
	node -v
	npm -v
	
	# now update to the latest version of node package manager (npm)
	npm upgrade -g

Packages
--------

Nodejs uses Node Package Manager (npm) for add/removing packages. The
best way is to build a package.json file in your project and run
``npm install`` to get what you need. See these
`tutorials<https://docs.npmjs.com/>`__ for more info.


============================== =======================================================
Command Cheatsheet             Description
============================== =======================================================
adduser                        Create a user account on npmjs.com
cache clean                    Clean up old packages in the cache
config list                    List config settings
config get prefix              Get path to global location
config set prefix=$HOME/.node  Set the global location
init                           Create a new ``package.json`` file
install [-g|--global]          Install packages locally or to the global location
install <pgk> --save           Install package and save it to ``package.json``
list [-g|--global]             List packages locally or globally
list --depth=0                 List packages, but only print top level
outdated [-g|--global]         Check for outdated packages
uninstall [-g|--global]        Uninstall packages locally or from the global location
update [-g|--global]           Update packages locally or globally
search <pkg>                   Search npmjs.com for a package
============================== =======================================================