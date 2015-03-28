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
 