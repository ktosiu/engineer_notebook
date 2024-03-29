Computer Monitoring
===================

+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Program     | Usefulness   | Description                                                                                                                                            |
+=============+==============+========================================================================================================================================================+
| iftop       | great        | Monitor inbound and outbound IP traffic of the host computer                                                                                           |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| netstat     | good         | Monitor incoming/outgoing network packets, ``netstat -a``                                                                                              |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| lsof        | low          | List of open files (e.g., disk files, network sockets, pipes, devices, and processes) and processes                                                    |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| htop        | great        | Like ``top`` but much more user friendly                                                                                                               |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| iptraf      | good         | Network monitoring                                                                                                                                     |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| btscanner   | low          | Bluetooth scanner                                                                                                                                      |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| darkstat    | great        | Network traffic analyzer with web interface, ``darkstat -i en0 -p 8080``, point browser to `localhost:8080 <http://localhost:8080>`__ to see results   |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| nmap        | good         | Network mapper                                                                                                                                         |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| p0f         | low          | Passive OS finger printing tool                                                                                                                        |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| wireshark   | great        | Network traffic analyzer                                                                                                                               |
+-------------+--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

Other useful
`tools <http://hack-tools.blackploit.com/2014/07/pwnpi-pen-test-drop-box-distro-for.html>`__
for your network.

Tools
-----

Install::

	sudo apt-get nmap
    sudo apt-get install tshark libcap-dev snmp-mibs-downloader
    pip install scapy pcapy



