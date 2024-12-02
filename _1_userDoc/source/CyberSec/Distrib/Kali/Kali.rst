====
Kali
====

.. index::
   single: Kali
   single: Distrib; Kali

.. contents::
    :depth: 3
    :backlinks: top

####

----------
KALI Linux
----------

:Liens_Web:
      * `Kali Linux`_
      * `Download Kali`_
      * `Kali Docs`_
      * `Kali Tools`_

.. _`Kali Linux`: https://www.kali.org/
.. _`Download Kali`: https://www.kali.org/get-kali/#kali-platforms
.. _`Kali Docs`: https://www.kali.org/docs/
.. _`Kali Tools`: https://www.kali.org/tools/

Kali Linux is an open-source, Debian-based Linux distribution geared towards various information
security tasks, such as Penetration Testing, Security Research, Computer Forensics and Reverse
Engineering. This is the most used Distrib in cyber Security.

    .. danger:: 
        
        **Default creds**
        
            Login : kali
            Password : kali


Install and upgrade tools
-------------------------

On a new install of Kali, we need to update, upgrade and fix tools

:Liens_Web:
      * `git repository called “pimpmykali”`_
      
.. _`git repository called “pimpmykali”`: https://github.com/Dewalt-arch/pimpmykali


    .. warning:: 
        
        **Post Install**
        
        .. code:: shell
            :number-lines:
            :force:

            sudo apt update && apt install git
            cd /opt
            git clone https://github.com/Dewalt-arch/pimpmykali
            cd pimpmykali
            sudo ./pimpmykali.sh

####

--------
Weblinks
--------

.. target-notes::