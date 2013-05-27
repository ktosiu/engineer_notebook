# Arch Linux install

# Basic Install Process

Don't follow the install instructions, they suck. Instead, look at the 
[Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners%27_Guide) 
on the wiki.

## Virtualbox Guest

Follow these [instructions](https://wiki.archlinux.org/index.php/Arch_Linux_VirtualBox_Guest#Arch_Linux_guests)
for the install.

1. Install this package:

    pacman -S virtualbox-guest-utils

2. Create the module file /etc/modules-load/virtualbox.conf

    vboxguest
    vboxsf
    vboxvideo

# Post-Install Packages

    pacman -S package

Useful packages:

* distcc
* sudo - edit /etc/sudoers, uncomment wheel group
* avahi and nss-mdns
* openssh
* virtualbox-guest-utils

## Avahi - Multicast is kinda crap on version router

Edit /etc/dhcpd.conf and comment out noipv4ll.

You can enable Avahi Daemon at startup with the following command:

    systemctl enable avahi-daemon.service

## SSH

For the client edit /etc/ssh/ssh_config remove protocol 1 since it is deemed insecure and only use 2:

    Protocol 2 

For the server edit /etc/ssh/sshd_config enable:

    AllowUsers user1 user2 (change to appropriate user names)
    PermitRooLogin no
    Banner /etc/issue

Then add it to the DAEMONS list in /etc/rc.conf, so it starts on boot:

** Don't use rc.conf anymore!! **

    DAEMONS=( .... sshd ....)

You can also start it immediately by:

    sudo rc.d start sshd

To see if it worked, type:

    ps -e | grep sshd

### SSH Keys

To increase security, you can disable password logins and rely on ssh public keys. To do
this, take a look [here](https://wiki.archlinux.org/index.php/SSH_Keys) for details. Basic
steps are:

1. Generate an ssh key pair using either RSA (2048-4096 bit) or DSA (1024 bit) both 
public and private keys. They will be stored in ~/.ssh with the public key having .pub 
appended to the end.

        ssh-keygen -t dsa -b 1024 -C "$(whoami)@$(hostname)-$(date -I)"
    
    Note you can create a key for a different username if you change $(whoami) to the user name you want.

2. Copy the public key (.pub) to the server you will connect to:

        ssh-copy-id username@remote-server.org 

    This should update ~/.ssh/authorized_keys in the process. Also ensure the correct 
protections are on the file by:

        chmod 600 ~/.ssh/authorized_keys

3. Edit /etc/sshd_config to disable password logins.

    PasswordAuthentication no
    ChallengeResponseAuthentication no

## Update System

    pacman -Syu

# Copying an image to the SD Card in Mac OS X

These commands and actions need to be performed from an account that has administrator 
privileges.

1. Download the image from a [mirror or torrent](http://www.raspberrypi.org/downloads).

2. Verify if the the hash key is the same (optional), in the terminal run:

    shasum ~/Downloads/debian6-19-04-2012.zip

3. Extract the image:

    unzip ~/Downloads/debian6-19-04-2012.zip

4. Attach the SD Card to the computer and identify the mount point

    df -h

Record the device name of the filesystem's partition, e.g. /dev/disk3s1

5. Unmount the partition so that you will be allowed to overwrite the disk, note that 
unmount is **NOT** the same as eject:

    sudo diskutil unmount /dev/disk3s1

Using the device name of the partition work out the raw device name for the entire disk, 
by omitting the final "s1" and replacing "disk" with "rdisk" (this is very important: 
you will lose all data on the hard drive on your computer if you get the wrong device 
name). Make sure the device name is the name of the whole SD card as described above, 
not just a partition of it (for example, rdisk3, not rdisk3s1. Similarly you might have 
another SD drive name/number like rdisk2 or rdisk4, etc. -- recheck by using the df -h 
command both before & after you insert your SD card reader into your Mac if you have 
any doubts!): e.g. /dev/disk3s1 => /dev/rdisk3

6. Write the image to the card with this command, using the raw disk device name from 
above (read carefully the above step, to be sure you use the correct rdisk# here!):

    sudo dd bs=1m if=~/archlinux-hf-2012-09-18.img of=/dev/rdisk3

If the above command report an error(dd: bs: illegal numeric value), please change bs=1M 
to bs=1m. 

Note that dd will not feedback any information until there is an error or it 
is finished, information will show and disk will re-mount when complete. However if you 
are curious as to the progresss - ctrl-T (SIGINFO, the status argument of your tty) will 
display some en-route statistics.

7. After the dd command finishes, eject the card:

    sudo diskutil eject /dev/rdisk3

8. Insert it in the raspberry pi, and have fun

## Fonts

Fontconfig configuration is done via /etc/fonts/conf.avail and conf.d.
Read /etc/fonts/conf.d/README for more information.

Configuration via /etc/fonts/local.conf is still possible,
but is no longer recommended for options available in conf.avail.

Main systemwide configuration should be done by symlinks
(especially for autohinting, sub-pixel and lcdfilter):

cd /etc/fonts/conf.d
ln -s ../conf.avail/XX-foo.conf

Check also https://wiki.archlinux.org/index.php/Font_Configuration
and https://wiki.archlinux.org/index.php/Fonts.


---



#Dropbox on Raspberry Pi via SSHFS
**POSTED BY MICHAEL ON JUL 10, 2012 IN RASPBERRY PI, TUTORIALS**

[Original Post Here](http://mitchtech.net/category/tutorials/raspberry-pi/)


This tutorial will demonstrate how to mount Dropbox (or any filesystem) over the network on the Raspberry Pi using SSHFS (Secure SHell FileSystem). For this procedure to work for your Dropbox share, you will need another machine somewhere that is running Dropbox, and is accessible to the Raspberry Pi via SSH.
Note: The following is not actually specific to the Raspberry Pi, nor to Dropbox. The tutorial generalizes for other systems and architectures that are not officially supported by Dropbox, as well as for mounting of other non Dropbox shares over the network.

##How it works

SSH is a secure protocol for communicating between machines. SSHFS is a tool that uses SSH to enable mounting of a remote filesystem on a local machine; the network is (mostly) transparent to the user.

On the local computer where the SSHFS is mounted, the implementation makes use of the FUSE (Filesystem in Userspace) kernel module. The practical effect of this is that the end user can seamlessly interact with remote files being securely served over SSH just as if they were local files on his/her computer.

##Installation (remote host)

The first step is to configure the remote host that the Raspberry Pi will connect to via SSH.  It will need to be running Dropbox, if you need to install it, follow the instructions for your respective OS here. If you are not yet a Dropbox user, and this has finally persuaded you to join, signup for Dropbox here.
Next, the remote machine will need to be running OpenSSH server. For Windows and Mac instructions on how to set up OpenSSH server, I recommend this tutorial on Lifehacker.  For Linux users, OpenSSH server is available in most every package manager. To install on Ubuntu, for example:

    sudo apt-get install openssh-server
 
##Installation (Raspberry Pi)

Now that the remote host is configured, you can setup the mount on the Pi.  This first requires installation of the sshfs package.  Open a terminal on the Pi and install it like this:

    sudo apt-get install sshfs

Then add the user pi to the FUSE users group:

    sudo gpasswd -a pi fuse

Once added to the fuse group, log out and log back in again for the change to take effect. Next, create a directory to mount Dropbox (or other remote share)

    mkdir ~/Dropbox

Now use sshfs to mount the remote share on the newly created mountpoint. Be sure to change the user@remote-host and path to Dropbox to match your own settings:

    sshfs -o idmap=user user@remote-host:/home/user/Dropbox ~/Dropbox

For example, connecting to another machine on your local network will look something like this:

    sshfs -o idmap=user michael@192.168.1.100:/home/michael/Dropbox ~/Dropbox

The idmap=user option ensures that files owned by the remote user are owned by the local user. If you don’t use idmap=user, files in the mounted directory might appear to be owned by someone else, because your computer and the remote computer have different ideas about the numeric user ID associated with each user name. idmap=user will not translate UIDs for other users.
That’s all there is to it! To unmount,

    fusermount -u ~/Dropbox

##Automount Dropbox on boot
To configure the Dropbox SSHFS to automatically mount at startup, we first need to enable SSH keyless remote login.  The first part of this task is to generate an RSA crypto key so we can securely login to the remote machine running Dropbox without entering a password.  In a terminal on the Pi, run:

    ssh-keygen -t rsa

Hit enter three times when prompted, accepting the default settings for the RSA ssh keys. Now copy the public part of the key to the remote host using the ssh-copy-id command:

    ssh-copy-id -i ~/.ssh/id_rsa.pub user@remote-host

You will be prompted for the password on the remote one last time. Once entered, terminal output will confim the key was added sucessfully.

Now that you can login remotely without password, the final task is to configure the share to automatically mount on startup. There are a few ways this could be accomplished, I decided to use cron for the task. Open the global crontab for editing:

    sudo crontab -e

And add a line to the end like this:

    @reboot sshfs user@remote-host:/home/user/Dropbox /home/pi/Dropbox

Then press CTRL and X to exit the editor, then Y to confirm the changes (if using nano, the default text editior).
That’s it! Reboot the Pi, and your Dropbox share will mount automatically on startup.

Another method to accomplish this task would be to add a line to /etc/fstab to automatically mount the Dropbox SSHFS share.

[Reference](https://help.ubuntu.com/community/SSHFS)
 