=============================
Nmap Port Scanning Techniques
=============================

.. index::
   single: Nmap - Port Scanning
   single: Nmap; Nmap - Port Scanning

.. contents::
    :depth: 3
    :backlinks: top

####

:Liens_Web:
    * `Nmap - Port Scanning Techniques`_

.. _`Nmap - Port Scanning Techniques`: https://nmap.org/book/man-port-scanning-techniques.html

    .. image:: images/commonPorts.jpg
       :width: 500 px
       :align: center


Syn scan
========

SYN scan is the default and most popular scan option for good reasons. It can be performed quickly,
scanning thousands of ports per second on a fast network not hampered by restrictive firewalls. It
is also relatively unobtrusive and **stealthy** since it never completes TCP connections.

It is known as a ‘stealthy’ port scan because it does not complete the full TCP handshake and is
therefore less likely to be noticed.

    .. note:: 
        
        **Syn scan**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -sS [host or range IP]

TCP scan
========

TCP connect scan is the default TCP scan type when SYN scan is not an option. This is the case when
a user does not have raw packet privileges. Instead of writing raw packets as most other scan types
do, Nmap asks the underlying operating system to establish a connection with the target machine and
port by issuing the connect system call.

The problem with this type of scan is that it takes a lot more time to complete as more packets are
required to obtain information about the scanned ports. The SYN scan is generally much faster and
Nmap has more control over the SYN scan since it’s handled by Nmap instead of by the underlying
operating system. Therefore, the TCP connect port scan should not be used when the SYN scan is an
option, for example when you have root access on the machine running Nmap (this usually means the
root account or an account that is able to make use of sudo).

    .. note:: 
        
        **TCP scan**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -sT [host or range IP]

UDP scan
========

UDP services are very common. DNS, NTP and SNMP, for example, run over UDP on ports 53, 123 and
161/162 and checking for UDP services should always be included in a penetration test.

Scanning for UDP services is generally much slower and the techniques are different from those of
TCP. Vulnerable UDP services are quite common and may expose a lot of useful information about the
target host.

    .. note:: 
        
        **Title**
        
        .. code:: shell
            :number-lines:
            :force:

            sudo nmap -sU [target host]

Port ranges scanning
====================

By default, Nmap will only scan the 1.000 most common ports, but if you want to override the default
range you can set a custom range by using the **-p** option followed by a port range. The port range
can be specified in several formats the simplest of which would be to give the first port in the
range, a hyphen, and then the last port in the range.

You can also define multiple ports and/or ranges in a single command by separating them with a comma
sign.

If you want to scan all ports from 1 to 65.535 you have to use the **-p-** flag.

During a penetration test it is advisable to scan the full port range to detect any services running
on uncommon ports (including those common services that have been assigned different ports from
their defaults). However, please be aware that scanning the full port range can generate a lot of
traffic and might take a long time to complete when used in combination with specific options such
as a service scan.

    .. note:: 
        
        **ports 137 to 139 and port 445**
        
        .. code:: shell
            :number-lines:
            :force:

             nmap -p 137-139,445 [target host]

        .. image:: images/011-nmap-ranges-02.jpg
           :width: 500 px
           :align: center

We can also scan for the service names that are specified in the nmap-services. Instead of writing
out all the different NetBIOS services individually by name we can use a wildcard instead.

    .. note:: 
        
        **Port by its service name**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -p netbios*,microsoft-ds [target host]

NetBIOS also uses UDP ports which are not scanned unless we specify the UDP option. We can scan both
TCP and UDP in several ways. Let’s start by running an **UDP scan (-sU)** and a **TCP SYN scan
(-sS)** and specify the NetBIOS and Microsoft-ds port ranges as follows.

    .. note:: 
        
        **UDP + TCP scan**
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -sU -sS -p U:137-139,T:137-139,445 [target host]

        .. image:: images/013-nmap-ranges-04.jpg
           :width: 500 px
           :align: center

The same port range can also be specified by referencing the service name.

    .. note:: 
        
        .. code:: shell
            :number-lines:
            :force:

             sudo nmap -sU -sS -p netbios*,microsoft-ds [target host]



####

--------
Weblinks
--------

.. target-notes::