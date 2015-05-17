Networking
==========

Avahi - Multicast is kinda crap on my router
--------------------------------------------

Edit /etc/dhcpd.conf and comment out noipv4ll.

You can enable Avahi Daemon at startup with the following command:

::

    systemctl enable avahi-daemon.service

SSH
---

For the client edit /etc/ssh/ssh\_config remove protocol 1 since it is
deemed insecure and only use 2:

::

    Protocol 2 

For the server edit /etc/ssh/sshd\_config enable:

::

    AllowUsers user1 user2 (change to appropriate user names)
    PermitRooLogin no
    Banner /etc/issue

Then add it to the DAEMONS list in /etc/rc.conf, so it starts on boot:

\*\* Don't use rc.conf anymore!! \*\*

::

    DAEMONS=( .... sshd ....)

You can also start it immediately by:

::

    sudo rc.d start sshd

To see if it worked, type:

::

    ps -e | grep sshd

