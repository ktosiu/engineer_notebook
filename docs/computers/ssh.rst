SSH 
========

.. figure:: ../pics/ssh.jpg
   :width: 200px

Summary of Useful Commands
--------------------------

=========== ======================================  ==========================
Command     Example                                 Use
=========== ======================================  ==========================
ssh         ssh kevin@thor.local                    login to a computer   
ssh-keygen  ssh-keygen                              generate an ssh key
ssh-keygen  ssh-keygen -lvf                         view the key finger print
ssh-copy-id ssh-copy-id kevin@loki.local            copy key to remote server
=========== ======================================  ==========================

Key Generation
---------------

To increase security, you can disable password logins and rely on ssh
public keys. To do this, take a look
`here <https://wiki.archlinux.org/index.php/SSH_Keys>`__ for details.
Basic steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA
   (1024 bit) both public and private keys. They will be stored in
   ``~/.ssh`` with the public key having .pub appended to the end. Two ways to 
   generate keys are shown below (pick one).

   ::

       ssh-keygen -t dsa -b 1024 -C "$(whoami)@$(hostname)-$(date)"
       ssh-keygen -t rsa -b 4096 -C "$(whoami)@$(hostname)-$(date)"

   Note you can create a key for a different username if you change
   $(whoami) to the user name you want. If no type is specified, the default is RSA
   2048 bits.
   
   ::
   
		[kevin@Tardis ~]$ ssh-keygen -C "test@$(hostname)-$(date)"
		Generating public/private rsa key pair.
		Enter file in which to save the key (/Users/kevin/.ssh/id_rsa): test
		Enter passphrase (empty for no passphrase): 
		Enter same passphrase again: 
		Your identification has been saved in test.
		Your public key has been saved in test.pub.
		The key fingerprint is:
		00:04:27:9d:7e:33:6f:65:1c:a5:e0:c3:82:5d:7b:92 test@Tardis.local-Tue Apr 21 22:29:40 MDT 2015
		The key's randomart image is:
		+--[ RSA 2048]----+
		|  o++.  o  ..    |
		|   oo+ + +..     |
		|   .. + E.o.     |
		|    . +o ++      |
		|     . +So       |
		|        o        |
		|       .         |
		|                 |
		|                 |
		+-----------------+


   Also note, it is advisable you create a strong pass phrase that you won't forget. However,
   I typically do not create one. But it does add an added level of protection.

2. Copy the public key (.pub) to the server you will connect to:

   ::

       ssh-copy-id username@remote-server.org 

   This will update ~/.ssh/authorized\_keys in the process. **Note:** ``ssh-copy-id``
   may need to be installed. Most Linux/Unix systems should have this, but for OSX do 
   ``brew install ssh-copy-id``. Also ensure the correct protections are on the file by:

   ::

       chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/ssh/sshd\_config to disable password logins.

   ::

       PasswordAuthentication no
       ChallengeResponseAuthentication no


SSH Key Finger Prints
---------------------

To view the finger print of a key:

::

    [kevin@Tardis ~]$ ssh-keygen -lvf ~/.ssh/id_rsa.pub
	2048 b1:58:41:c5:93:b3:bc:c7:34:5b:e8:be:bc:15:ff:55  kevin@tardis.local (RSA)
	+--[ RSA 2048]----+
	|       .oo..     |
	|         .=      |
	|        o. + .   |
	|       o oo + .  |
	|      . S  = +. E|
	|          . =  o.|
	|           o  . o|
	|           ...  o|
	|            +o  .|
	+-----------------+

This tells you the type of key (e.g., RSA or DSA), the bit size, what email/account it is
tied to, and a graphical representation of the key. In this case, the 2048 bits of my public 
RSA key.

