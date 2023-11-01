=============================================
Fingerprinting services and operating systems
=============================================

.. index::
   single: Fingerprint
   single: Nmap; Fingerprint

.. contents::
    :depth: 3
    :backlinks: top

####

To identify services Nmap uses an extensive database of known services and their common ports.
Certain ports are reserved for particular services. Port 22, for example, is used for SSH and port
80 for HTTP webservers.

For penetration testing purposes and a vulnerability assessment we will also want to find out what
specific kind of software is running and listening on those ports.

Fingerprint services and OS version
===================================

The following command will use the Nmap port scan to detect the services and the OS.

    .. note:: 
        
        **Port and OS**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -sV -O [target IP address]

        .. image:: images/007-nmap-sv-O-01.jpg
           :width: 500 px
           :align: center

"Agressive" mode
================

The **-A** option in Nmap we can launch an aggressive scan against a target. The A stands for
‘Aggressive’ scan options and enables Fingerprint detection, OS detection, version detection,
script scanning and traceroute.

When using the aggressive option with Nmap it is important to consider that this scan option moves a
lot of packets by default and should be carefully used in combination with other options.

When the aggressive option is used together with the ‘all ports’ option (**-p-**) the scan may take
very long to complete but on the other hand it will provide you with a lot of information. It is
also important to run the aggressive scan with sudo when using a non-root account. Without sudo the
aggressive scan will skip the options that require more privileges such as OS detection.

Please note that this scan will also **generate a lot of network traffic and may crash unstable
services on the target host**. Another downside of aggressive scans (which include the service scans
(-sV)), is that target hosts or firewalls can sometimes block or limit the rate at which they can
run. Such rate-limiting mechanisms can delay a scan so drastically that it will never complete (or
at least not within a reasonable time). This behavior is regularly seen on Windows hosts.

So one recommended approach is to start by determining open ports using a less aggressive scan, such
as the SYN scan, and then to continue fingerprinting the services discovered using other scan types.

    .. note:: 
        
        **Agressive mode**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -A [target IP address]

        .. image:: images/008-nmap-a-01.jpg
           :width: 500 px
           :align: center

        .. image:: images/009-nmap-a-02.jpg
           :width: 500 px
           :align: center

####

--------
Weblinks
--------

.. target-notes::