Node.js
=======

.. figure:: ../pics/nodejs.png
   :width: 200px

Installing Node.js
------------------

The version in apt-get is old (at the time of this writing), `<http://node-arm.herokuapp.com/>`__ do:

::

    wget http://node-arm.herokuapp.com/node_latest_armhf.deb
    sudo dpkg -i node_latest_armhf.deb
	# Check installation
	node -v
	npm -v

Packages
--------

Nodejs uses Node Package Manager (npm) for add/removing packages. The
best way is to build a package.json file in your project and run
``npm install`` to get what you need. See these
`tutorials<https://docs.npmjs.com/>`__ for more info.
