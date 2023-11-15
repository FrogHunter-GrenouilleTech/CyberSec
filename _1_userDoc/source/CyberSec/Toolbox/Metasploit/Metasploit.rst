.. _ref_Metasploit:

==========
Metasploit
==========

.. index::
   single: Metasploit
   single: Tools; Metasploit
   single: Red Team Tools; Metasploit

.. contents::
    :backlinks: top

.. toctree::
   :maxdepth: 2

   Meterpreter/Meterpreter
   Msfvenom/Msfvenom

####

    .. note:: 
        
        **Liens Web**
        
         * `Metasploit Framework – A Beginner’s Guide`_
         * `Metasploit Documentation`_
         
.. _`Metasploit Documentation`: https://docs.metasploit.com/
.. _`Metasploit Framework – A Beginner’s Guide`: https://kalilinuxtutorials.com/metasploit-framework/

-----------------------
Define a RHOST globally
-----------------------

    .. note:: 
        
        From the **msfconsole** :
        
        .. code:: shell
            :number-lines:
            :force:

             # setg RHOSTS [Remote_host_IP]

             setg RHOSTS 10.11.1.250

        To see the value of the variable RHOSTS :
        
        .. code:: shell
            :number-lines:
            :force:

             get RHOSTS


####

--------
Weblinks
--------

.. target-notes::