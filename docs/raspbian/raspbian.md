# Raspbian

There is a lot of junk automatically installed on Raspbian, use `dpkg -l` to see. Suggest removal via `sudo apt-get remove <pkg>`:

* isc-dhcp-server: Already have one on my network, don't need another running (it is on by default)
* sonic-pi: a music programming environment aimed at new programmers
* printer-driver-*: don't print anything
* hplip*: HP printing stuff
* cups cups-bsd cups-client cups-common cups-filters cups-ppdc: printing stuff
* supercollider*: real-time audio synthesis programming language
* samba-common: Windoze stuff
* sane-utils: scanner stuff
* penguinspuzzle: game
* ghostscript
* 
