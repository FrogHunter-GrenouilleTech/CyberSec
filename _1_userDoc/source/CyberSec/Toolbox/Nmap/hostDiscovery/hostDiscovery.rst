==============
Host Discovery
==============

.. index::
   single: Host Discovery
   single: Nmap; Host Discovery

.. contents::
    :depth: 3
    :backlinks: top

####

:Liens_Web:
    * `Host Discovery`_

.. _`Host Discovery`: https://nmap.org/book/man-host-discovery.html

ping scan
=========

This option tells Nmap to perform host discovery only without any additional port scanning and
prints out details of any hosts that responded. When running Nmap with the -sn option it will run a
default scan involving an ICMP echo request, TCP SYN to port 443, TCP ACK to port 80, and an ICMP
timestamp request. This commande is making a lot of noise.

    .. note:: 
        
        **Ping Scan**
        
        .. code:: shell
            :number-lines:
            :force:

             nmap -sn 10.11.1.0/24

List Scan
=========

Print a list of target hosts, options for higher level functionality such as port scanning, OS
detection, or host discovery **cannot be combined** with this.

    .. note:: 
        
        **List Scan**
        
        .. code:: shell
            :number-lines:
            :force:

             nmap -sL 10.11.1.0/24


####

--------
Weblinks
--------

.. target-notes::