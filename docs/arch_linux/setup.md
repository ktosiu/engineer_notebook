# Install

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


## Update System

    pacman -Syu


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

