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

SSH Keys
~~~~~~~~

To increase security, you can disable password logins and rely on ssh
public keys. To do this, take a look
`here <https://wiki.archlinux.org/index.php/SSH_Keys>`__ for details.
Basic steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA
   (1024 bit) both public and private keys. They will be stored in
   ~/.ssh with the public key having .pub appended to the end.

   ::

       ssh-keygen -t dsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"

   Note you can create a key for a different username if you change
   $(whoami) to the user name you want.

2. Copy the public key (.pub) to the server you will connect to:

   ::

       ssh-copy-id username@remote-server.org 

   This should update ~/.ssh/authorized\_keys in the process. Also
   ensure the correct protections are on the file by:

   ::

       chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/sshd\_config to disable password logins.

   PasswordAuthentication no ChallengeResponseAuthentication no
