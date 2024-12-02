.. _ref_responder::


=========
Responder
=========

.. index::
   single: Responder
   single: Tools; Responder
   single: Windows toolkit; Responder
   single: Attack toolkit; Windows; Responder
   single: NTLM / NTLMv1 / NTLMv2; Responder
   single: Active Directory; Responder
   single: Network protocols; Responder
   single: SMB; Responder
   single: MSSQL; Responder
   single: Authentication servers; Responder
   single: DNS; Responder
   single: WPAD; Responder
   single: DHCP; Responder
   single: IPv4/IPv6; Responder
   single: DCE-RPC; Responder
   single: LLMNR; Responder
   single: NBT-NS; Responder
   single: MDNS; Responder

.. contents::
    :depth: 3
    :backlinks: top

####

    .. note:: 
        
        **Liens Web**

        * `Responder - github`_
        * `Responder - wiki`_
        
.. _`Responder - wiki`: https://github.com/lgandx/Responder/wiki
.. _`Responder - github`: https://github.com/lgandx/Responder

**Responder** is an attack toolkit abusing Windows proprietary protocols insecurities and aim at taking
complete control of active-directory environments.

This tool has several components:

    NBT-NS/LLMNR/MDNS poisoners

    Network traffic analyze mode

    Many rogue authentication servers

    Cross-protocol NTLMv1/2 Relay

    WPAD

    DHCP spoofer.

    Fast SMB scanner (Os version, null session, bootime, RDP open, smb1, signing, domain name)

    Weaponizing Responder.

Each of these components will be documented in this wiki.

Features
========

    * Dual IPv6/IPv4 stack.
    * Built-in SMB Auth server.
    * Built-in MSSQL Auth server.
    * Built-in HTTP Auth server.
    * Built-in HTTPS Auth server.
    * Built-in HTTP Auth server.
    * Built-in DCE-RPC Auth server.
    * Built-in FTP, POP3, IMAP, SMTP Auth servers.
    * Built-in DNS server.
    * Built-in WPAD Proxy Server.
    * Browser Listener
    * Icmp Redirect
    * Rogue DHCP
    * Analyze mode.





####

--------
Weblinks
--------

.. target-notes::