.. _ref_Meterpreter:

===========
Meterpreter
===========

.. index::
   single: Meterpreter
   single: Metasploit; Meterpreter

.. contents::
    :depth: 3
    :backlinks: top

####


------------------------
Meterpreter Presentation
------------------------

:Liens_Web:

    * `Security Wiki - Meterpreter`_

.. _`Security Wiki - Meterpreter`: https://doubleoctopus.com/security-wiki/threats-and-tools/meterpreter/

Meterpreter is a **Metasploit attack payload** that provides an interactive shell from which an
attacker can explore the target machine and execute code. Meterpreter is deployed using in-memory
DLL injection. As a result, Meterpreter resides entirely in memory and writes nothing to disk. No
new processes are created as Meterpreter injects itself into the compromised process, from which it
can migrate to other running processes. As a result, the forensic footprint of an attack is very
limited.

Meterpreter uses a reverse_tcp shell, which means it connects to a listener on the attacker’s machine.

####

--------
Weblinks
--------

.. target-notes::