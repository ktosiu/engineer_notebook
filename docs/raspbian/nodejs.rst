Node.js
=======

.. figure:: ./pics/nodejs.png
   :alt: nodejs logo

   nodejs logo

Installing Node.js
------------------

The version in apt-get is old (at the time of this writing), do:

::

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

Packages
--------

Nodejs uses Node Package Manager (npm) for add/removing packages. The
best way is to build a package.json file in your project and run
``npm install`` to get what you need. See these
[tutorials(https://docs.npmjs.com/) for more info.
