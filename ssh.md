# 16 SSH Hacks

The original source for this work is [here](http://www.itworld.com/it-managementstrategy/261500/16-ultimate-openssh-hacks)

So you think you know OpenSSH inside and out? Test your chops against this hit parade of 
16 expert tips and tricks, from identifying monkey-in-the-middle attacks to road warrior 
security to attaching remote screen sessions. Follow the countdown to the all-time best 
OpenSSH command!

[Running SSH on a non-standard port](xhttp://www.itworld.com/nls_unixssh0500506)

## SSH tips #16-14:Detecting MITM attacks

When you log into a remote computer for the first time, you are asked if you want to 
accept the remote host's public key. Well how in the heck do you know if you should or 
not? If someone perpetrated a successful monkey-in-the-middle attack, and is presenting 
you with a fake key so they can hijack your session and steal all your secrets, how are 
you supposed to know? You can know, because when new key pairs are created they also 
create a unique fingerprint and randomart image:

    $ ssh-keygen -t rsa -C newserver -f .ssh/newkey
    
    Generating public/private rsa key pair.
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in .ssh/newkey.
    Your public key has been saved in .ssh/newkey.pub.
    The key fingerprint is:
    44:90:8c:62:6e:53:3b:d8:1a:67:34:2f:94:02:e4:87 newserver
    The key's randomart image is:
    +--[ RSA 2048]----+
    |oo   +.o.        |
    |. = B o.         |
    | E X +  .        |
    |  B B ..         |
    | . * o  S        |
    |  .              |
    |                 |
    |                 |
    |                 |
    +-----------------+

## SSH tip #16: Retrieve the fingerprint and randomart image of an SSH key

If you make a copy of this when you create new encryption keys, then you can fetch a 
key's fingerprint and randomart image anytime to compare and make sure they have not 
changed:

    $ ssh-keygen -lvf  keyname

## SSH tip #15: View all fingerprints and randomart images in known_hosts

And you can see all of them in your ~/.ssh/known_hosts file:

    $ ssh-keygen -lvf ~/.ssh/known_hosts

## SSH tip #14: Verify server keys

You can see the fingerprint and randomart for any computer you're logging into by 
configuring/etc/ssh/ssh_config on your client computer. Simply uncomment the VisualHostKey 
option and set it to yes:

VisualHostKey yes

Then login to any remote computer to test it:

    $ ssh user@host2
    Host key fingerprint is 66:a1:2a:23:4d:5c:8b:58:e7:ef:2f:e5:49:3b:3d:32
    +--[ECDSA  256]---+
    |                 |
    |                 |
    |  . o   .        |
    | + = . . .       |
    |. + o . S        |
    | o   o oo        |
    |. + . .+ +       |
    | . o .. E o      |
    |      .o.+ .     |
    +-----------------+
    
    user@host2's password: 

Obviously you need a secure method of getting verified copies of the fingerprint and 
randomart images for the computers you want to log into. Like a hand-delivered printed 
copy, encrypted email, the scp command, secure ftp, read over the telephone...The risk of 
a successful MITM attack is small, but if you can figure out a relatively painless 
verification method it's cheap insurance.

## SSH tip #13: Attach to a remote GNU screen session

You can attach a GNU screen session remotely over SSH; in this example we'll open a GNU 
screen session on host1, and connect to it from host2. First open and then detach a screen 
session on host1, named testscreen:

     host1 ~ $ screen -S testscreen

Then detach from your screen session with the keyboard combination Ctrl+a+d:

    [detached from 3829.testscreen]

You can verify that it's still there with this command:

    host1 ~ $ screen -ls

There is a screen on:

    3941.testscreen (03/18/2012 12:43:42 PM) (Detached)
    1 Socket in /var/run/screen/S-host1.

Then re-attach to your screen session from host2:

    host1 ~ $ ssh -t terry@uberpc screen -r testscreen

You don't have to name the screen session if there is only one.

##vSSH tip #12: Launch a remote screen session

What if you don't have a running screen session? No worries, because you can launch one 
remotely:

    host1 ~ $ ssh -t user@host2 /usr/bin/screen -xRR

## SSH tip #11: SSHFS is better than NFS

sshfs is better than NFS for a single user with multiple machines. I keep a herd of 
computers running because it's part of my job to always be testing stuff. I like having 
nice friendly herds of computers. Some people collect Elvis plates, I gather computers. 
At any rate opening files one at a time over an SSH session for editing is slow; with 
sshfs you can mount entire directories from remote computers. First create a directory to 
mount your sshfs share in:

    $ mkdir remote2

Then mount whatever remote directory you want like this:

    $ sshfs user@remote2:/home/user/documents remote2/

Now you can browse the remote directory just as though it were local, and read, copy, 
move, and edit files all you want. The neat thing about sshfs is all you need is sshd 
running on your remote machines, and thesshfs command installed on your client PCs.

## SSH tip #10: Log in and run a command in one step

You can log in and establish your SSH session and then run commands, but when you have a 
single command to run why not eliminate a step and do it with a single command? Suppose 
you want to power off a remote computer; you can log in and run the command in one step:

    carla@local:~$ ssh user@remotehost sudo poweroff

This works for any command or script. (The example assumes you have a sudo user set up 
with appropriate restrictions, because allowing a root login over SSH is considered an 
unsafe practice.) What if you want to run a long complex command, and don't want to type 
it out every time? One way is to put it in a Bash alias and use that. Another way is to 
put your long complex command in a text file and run it according to tip #9.

## SSH tip #9: Putting long commands in text files

Put your long command in a plain text file on your local PC, and then use it this way 
to log in and run it on the remote PC:

    carla@local:~$ ssh user@remotehost "`cat filename.txt`"

Mind that you use straight quotations marks and not fancy ones copied from a Web page, 
and back-ticks, not single apostrophes.

##vSSH tip #8: Copy public keys the easy way

The ssh-copy-id command is not as well-known as it should be, which is a shame because 
it is a great time-saver. This nifty command copies your public key to a remote host in 
the correct format, and to the correct directory. It even has a safety check that won't 
let you copy a private key by mistake. Specify which key you want to copy, like this:

    $ ssh-copy-id -i .ssh/id_rsa.pub user@remote

## SSH tip #7: Give SSH keys unique names

Speaking of key names, did you know you can name them anything you want? This helps when 
you're administering a number of remote computers, like this example which creates then 
private key web-admin and public key web-admin.pub:

    $ ssh-keygen -t rsa -f .ssh/web-admin

## SSH tip #6: Give SSH keys informative comments

Another useful way to label keys is with a comment:

    $ ssh-keygen -t rsa -C "downtown lan webserver" -f .ssh/web-admin

Then you can read your comment which is appended to the end of the public key.

## SSH tip #5: Read public key comments

    $ less .ssh/web-admin.pub
    
    ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1 
    
    [snip] KCLAqwTv8rhp downtown lan webserver

## SSH tip #4: Logging in with server-specific keys

Then when you log in, specify which key to use with the -i switch:

    $ ssh -i .ssh/web-admin.pub user@webserver

## SSH tip #3: Fast easy known_hosts key management

I love this one because it's a nice time-saver, and it keeps my ~/.ssh/known_hosts files 
tidy: using ssh-keygen to remove host keys from the ~/.ssh/known_hosts file. When the 
remote machine gets new SSH keys you'll get a warning, when you try to log in, that the 
key has changed. Using this is much faster than manually editing the file and counting 
down to the correct line to delete:

    $ ssh-keygen -R remote-hostname

Computers are supposed to make our lives easier, and it's ever so lovely when they do.

## SSH tip #2: SSH tunnel for road warriors

When you're at the mercy of hotel and coffee shop Internet, a nice secure SSH tunnel makes 
your online adventures safer. To make this work you need a server that you control to act 
as a central node for escaping from hotspot follies. I have a server set up at home to 
accept remote SSH logins, and then use an SSH tunnel to route traffic through it. This is 
useful for a lot of different tasks. For example I can use my normal email client to send 
email, instead of hassling with Web mail or changing SMTP server configuration, and all 
traffic between my laptop and home server is encrypted. First create the tunnel to your 
personal server:

    carla@hotel:~$ ssh -f carla@homeserver.com -L 9999:homeserver.com:25 -N

This binds port 9999 on your mobile machine to port 25 on your remote server. The remote 
port must be whatever you've configured your server to listen on. Then configure your mail 
client to use localhost:9999 as the SMTP server and you're in business. I use Kmail, which 
lets me configure multiple SMTP server accounts and then choose which one I want to use 
when I send messages, or simply change the default with a mouse click. You can adapt this 
for any kind of service that you normally use from your home base, and need access to when 
you're on the road.

## 1 Favorite SSH tip: Evading silly web restrictions

The wise assumption is that any public Internet is untrustworthy, so you can tunnel your 
Web surfing too. My #1 SSH tip gets you past untrustworthy networks that might have 
snoopers, and past any barriers to unfettered Web-surfing. Just like in tip #2 you need a 
server that you control to act as a secure relay; first setup an SSH tunnel to this server:

    carla@hotel:~$ ssh -D 9999 -C carla@homeserver.com

Then configure your Web browser to use port 9999 as a SOCKS 5 proxy. Figure 1 shows how 
this looks in Firefox.

Figure 1: Configuring Firefox to use your SSH tunnel as a SOCKS proxy.
An easy way to test this is on your home or business network. Set up the tunnel to a 
neighboring PC and surf some external Web sites. When this works go back and change the 
SOCKS port number to the wrong number. This should prevent your Web browser from 
connecting to any sites, and you'll know you set up your tunnel correctly.
How do you know which port numbers to use? Port numbers above 1024 do not require root 
privileges, so use these on your laptop or whatever you're using in your travels. Always 
check /etc/services first to find unassigned ports. The remote port you're binding to must 
be a port a server is listening on, and there has to be a path through your firewall to 
get to it.

To learn more try the excellent [Pro OpenSSH by Michael Stahnke]
(http://www.apress.com/networking/openssh/9781590594766), and my own [Linux 
Networking Cookbook](http://www.amazon.com/Linux-Networking-Cookbook-Carla-Schroder/dp/0596102488) 
has more on secure remote administration including SSH, OpenVPN, and 
remote graphical sessions, and configuring firewalls.



---



Dropbox on Raspberry Pi via SSHFS
POSTED BY MICHAEL ON JUL 10, 2012 IN RASPBERRY PI, TUTORIALS | 0 COMMENTS

http://mitchtech.net/category/tutorials/raspberry-pi/


This tutorial will demonstrate how to mount Dropbox (or any filesystem) over the network on the Raspberry Pi using SSHFS (Secure SHell FileSystem). For this procedure to work for your Dropbox share, you will need another machine somewhere that is running Dropbox, and is accessible to the Raspberry Pi via SSH.
Note: The following is not actually specific to the Raspberry Pi, nor to Dropbox. The tutorial generalizes for other systems and architectures that are not officially supported by Dropbox, as well as for mounting of other non Dropbox shares over the network.
How it works
SSH is a secure protocol for communicating between machines. SSHFS is a tool that uses SSH to enable mounting of a remote filesystem on a local machine; the network is (mostly) transparent to the user.
On the local computer where the SSHFS is mounted, the implementation makes use of the FUSE (Filesystem in Userspace) kernel module. The practical effect of this is that the end user can seamlessly interact with remote files being securely served over SSH just as if they were local files on his/her computer.
Installation (remote host)
The first step is to configure the remote host that the Raspberry Pi will connect to via SSH.  It will need to be running Dropbox, if you need to install it, follow the instructions for your respective OS here. If you are not yet a Dropbox user, and this has finally persuaded you to join, signup for Dropbox here.
Next, the remote machine will need to be running OpenSSH server. For Windows and Mac instructions on how to set up OpenSSH server, I recommend this tutorial on Lifehacker.  For Linux users, OpenSSH server is available in most every package manager. To install on Ubuntu, for example:
sudo apt-get install openssh-server
 
Installation (Raspberry Pi)
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

Automount Dropbox on boot
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
Reference: https://help.ubuntu.com/community/SSHFS
 