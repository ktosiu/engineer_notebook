Software
========

Debian Packaged Software
------------------------

Why have one program that does a few common sense things well when you
can have multiple programs that do one or two things really badly!

+-------------+-----------------------------------------------------------------------+
| Program     | Description                                                           |
+=============+=======================================================================+
| apt-get     | install: ``apt-get install <prgm>``                                   |
+-------------+-----------------------------------------------------------------------+
|             | remove: ``apt-get remove <prgm>`` add ``--purge`` to remove configs   |
+-------------+-----------------------------------------------------------------------+
|             | upgrade: ``apt-get upgrade <prgm>`` to get latest                     |
+-------------+-----------------------------------------------------------------------+
|             | update: ``apt-get update`` updates package databases                  |
+-------------+-----------------------------------------------------------------------+
| apt-cache   | search for programs you can install: ``apt-cache search <prgm>``      |
+-------------+-----------------------------------------------------------------------+
|             | info: ``apt-cache showpkg [packagename]`` displays package info       |
+-------------+-----------------------------------------------------------------------+
| dpkg        | list programs you have installed: ``dpkg -l``                         |
+-------------+-----------------------------------------------------------------------+

Updates, Search, and List
~~~~~~~~~~~~~~~~~~~~~~~~~

``apt-get`` is a horrible program and a beautiful example of how not to
design software. So if you want to know what packages are outdated, then
you need to install this package::

    sudo apt-get install apt-show-versions

Now to figure out what is outdated, do::

    apt-show-versions -u

Now some packages will get ``kept back`` which seems to be some strange
apt-get issue. To update your system completely, do::

    sudo apt-get dist-upgrade

Or list all packages installed on the computer by::

    dpkg -l

Raspbian
--------

There is a lot of junk automatically installed on Raspbian, use
``dpkg -l`` to see. Suggest removal via ``sudo apt-get remove <pkg>``:

-  isc-dhcp-server: Already have one on my network, don't need another
   running (it is on by default)
-  sonic-pi: a music programming environment aimed at new programmers
-  printer-driver-\*: don't print anything
-  hplip\*: HP printing stuff
-  cups cups-bsd cups-client cups-common cups-filters cups-ppdc:
   printing stuff
-  supercollider\*: real-time audio synthesis programming language
-  samba-common: Windoze stuff
-  sane-utils: scanner stuff
-  penguinspuzzle: game
-  ghostscript
