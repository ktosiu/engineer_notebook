Create a Local Repository
==========================

http://linuxconfig.org/easy-way-to-create-a-debian-package-and-local-package-repository

Get Software
-------------

apt-get install build-essential node

Create Debian Package
----------------------

mkdir package
cd package
mkdir DEBIAN
mkdir usr/local/bin
cp /path/to/executable usr/local/bin
pico DEBIAN/control

Package: package
Version: 1.0
Section: custom
Priority: optional
Architecture: all
Essential: no
Installed-Size: 1024
Maintainer: package.org
Description: This package does awesome things!

cd ..
dpkg-deb --build package
ls
mv package.deb package-1.0_arm7.deb

Create Local Repository
------------------------

apt-get install node

cd /var/www
mkdir debian
cp /path/to/package-1.0_arm7.deb /var/www/debian

dpkg-scanpackages debian /dev/null | gzip -9c > debian/Packages.gz

Update apt/source
~~~~~~~~~~~~~~~~~~

echo "deb http://10.1.1.4 debian/" >> /etc/apt/sources.list