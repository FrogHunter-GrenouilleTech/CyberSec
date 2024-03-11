.. _ref_unixPrivescCheck:

==================
Unix-Privesc-Check
==================

.. index::
   single: Unix-Privesc-Check
   single: Privilege Escalation Tools; Unix-Privesc-Check

.. contents::
    :depth: 3
    :backlinks: top

####

------------------
unix-privesc-check
------------------

    .. note:: 
        
        **Liens Web**

        * `pentestmonkey - unix-privesc-check`_
        
.. _`pentestmonkey - unix-privesc-check`: https://pentestmonkey.net/tools/audit/unix-privesc-check


**Unix-privesc-checker** is a script that runs on Unix systems (tested on Solaris 9,
HPUX 11, Various Linuxes, FreeBSD 6.2).  It tries to find misconfigurations that could allow local
unprivilged users to escalate privileges to other users or to access local apps (e.g. databases).

It is written as a single shell script so it can be easily uploaded and run (as opposed to
un-tarred, compiled and installed).  It can run either as a normal user or as root (obviously it
does a better job when running as root because it can read more files).


####

--------
Weblinks
--------

.. target-notes::