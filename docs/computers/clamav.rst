Clamav
=======

`Clamav.net <http://www.clamav.net/>`__.

Install
--------

	brew clamav

Setup
------

Go to ``/usr/local/etc/clamav`` and modify clamd.conf freshclam.conf

Update virus definitions::

	freshclam

Use
----

::

	alias clamscan='clamscan -r -i --bell --move=/Users/`whoami`/viruses '

