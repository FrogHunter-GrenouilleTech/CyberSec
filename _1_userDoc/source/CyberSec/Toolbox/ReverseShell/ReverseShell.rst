.. _ref_reverseShell:

=============
Reverse Shell
=============

.. index::
   single: Reverse Shell
   single: Tools; Reverse Shell

.. contents::
    :backlinks: top

####

    .. note:: 🔗 **Liens Web**
       :class: note
        
        * `Reverse Shell Cheat Sheet`_
    
.. _`Reverse Shell Cheat Sheet`: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

####

-------------
Reverse Shell
-------------

A **reverse shell**, also known as a connect-back shell, is a type of shell connection that
initiates from the compromised machine and connects back to a predetermined attacker-controlled
host. It is a common type of attack used by hackers to gain remote access to a system.

In a typical reverse shell attack, the attacker first exploits a vulnerability on the target machine
to gain a foothold. Once they have a foothold, they can then use a reverse shell to establish a
connection back to their own machine. This allows them to execute commands on the target machine as
if they were sitting at the keyboard.

Reverse shells can be used to steal data, install malware, or even take complete control of the
target machine. They are a powerful tool for attackers and can be difficult to defend against.

How does a reverse shell work?
==============================

A reverse shell works by establishing a TCP or UDP connection from the compromised machine to the
attacker's machine. The attacker then uses this connection to execute commands on the compromised
machine.

The two main types of reverse shells
====================================

    * **Bind shell:** The bind shell listens for incoming connections on a specific port **on the
      compromised machine**. When a connection is received, the bind shell executes commands sent
      from the attacker's machine.

    * **Reverse shell:** The reverse shell initiates a connection to a specific port **on the
      attacker's machine**. When the connection is established, the reverse shell executes commands
      sent from the attacker's machine.


####

-------------------------------------
How to protect against reverse shells
-------------------------------------

There are a number of things you can do to protect your systems from reverse shell attacks:

    * **Keep your software up to date:** Software updates often contain patches for known
      vulnerabilities that attackers can exploit.

    * **Use firewalls and intrusion detection systems (IDS):** Firewalls can block unauthorized
      incoming connections, while IDS can detect suspicious activity on your network.

    * **Educate your users about cybersecurity:** Users should be aware of the risks of clicking on
      links or opening attachments from unknown senders.

    * **Use strong passwords:** Strong passwords make it more difficult for attackers to guess your
      passwords and gain access to your systems.


####

--------------------------------
When a reverse shell is detected
--------------------------------

If you suspect that your system has been compromised by a reverse shell, there are a number of
things you can do:

    * **Isolate the compromised machine from the network:** This will prevent the attacker from
      further exploiting the system.

    * **Scan the compromised machine for malware:** Malware can be used to hide the presence of a
      reverse shell.

    * **Change your passwords:** This will help to prevent the attacker from accessing other systems.

    * **Report the incident to the authorities:** If you suspect that your system has been used to
      commit a crime, you should report the incident to the authorities.

By following these tips, you can help to protect your systems from reverse shell attacks.


####

--------------------------
Reverse shell as a payload
--------------------------

Since a reverse shell can be establish only after the exploitation of one or more vulnerability. We
need need to push the reverse shell, to the compromised computer, as a payload in the same time of
the exploitation of the vulnerability.

    .. note:: 🔗 **Liens Web**
       :class: note

        * `Reverse Shell Generator`_
        * `rcX - Shell Generator`_
        
.. _`rcX - Shell Generator`: https://rcxonline.cf/
.. _`Reverse Shell Generator`: https://www.revshells.com/


payload Generator
=================

    * :ref:`Hoaxshell <ref_hoaxshell>`

    * :ref:`MSFVenom <ref_msfvenom>`

Reverse shell Handler
=====================

    * :ref:`Netcat <ref_Netcat>`

    * :ref:`Pwncat <_ref_Pwncat>`

####

-----------------------------------
How to Stabilized a reverse shell ?
-----------------------------------

    .. admonition:: 🔗 **Liens Web**
       :class: note
        
        * `Stabilizing the Shell`_
    
.. _`Stabilizing the Shell`: https://jasonturley.xyz/how-to-stabilize-a-reverse-shell/

    .. admonition:: 💻 **Code Snipet**
       :class: note
        
        This command provide a clean shell but with :

            * no tab completion
            * no history
            * no [CTRL]-c
        
        .. code:: shell
           :number-lines:
           :force:

             python -c "import pty; pty.spawn('/bin/bash')"


        After we run this command, we will hit ctrl+z to background our shell and get back on our
        local terminal, and input the following stty command:

        .. code:: shell
           :number-lines:
           :force:

             www-data@remotehost$ ^Z

             FrogHunter95@htb[/htb]$ stty raw -echo
             FrogHunter95@htb[/htb]$ fg
             
             [Enter]
             [Enter]
             www-data@remotehost$


        We may notice that our shell does not cover the entire terminal. To fix this, we need to
        figure out a few variables. We can **open another terminal window on our system**, maximize
        the windows or use any size we want, and then input the following commands to get our
        variables:

        .. code:: shell
           :number-lines:
           :force:

             FrogHunter95@htb[/htb]$ echo $TERM

             xterm-256color

             FrogHunter95@htb[/htb]$ stty size

             67 318

        The first command showed us the **TERM variable**, and the second shows us the values for 
        **rows and columns**, respectively. Now that we have our variables, we can **go back to our
        netcat shell** and use the following command to correct them:
        
        .. code:: shell
           :number-lines:
           :force:

             www-data@remotehost$ export TERM=xterm-256color

             www-data@remotehost$ stty rows 67 columns 318

        Once we do that, we should have a netcat shell that uses the terminal's full features, just like an SSH connection.



####

--------
Weblinks
--------

.. target-notes::