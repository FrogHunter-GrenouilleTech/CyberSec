=============
Reverse Shell
=============

.. index::
   single: Reverse Shell
   single: Shell; Reverse Shell

.. contents::
    :depth: 3
    :backlinks: top

####

A Reverse Shell is the most common type of shell, as it is the quickest and easiest method to obtain
control over a compromised host. Once we identify a vulnerability on the remote host that allows
remote code execution, we can start a netcat listener on our machine that listens on a specific
port, say port 1234. With this listener in place, we can execute a reverse shell command that
connects the remote systems shell, i.e., Bash or PowerShell to our netcat listener, which gives us
a reverse connection over the remote system.

####

--------
Weblinks
--------

.. target-notes::