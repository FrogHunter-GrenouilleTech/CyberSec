.. _ref_searchsploit:

============
Searchsploit
============

.. index::
   single: Searchsploit
   single: Tools; Searchsploit

.. contents::
    :depth: 3
    :backlinks: top

####

Searchsploit is a command-line search tool for exploit-db and incorporates all the exploits provided
by the exploit-db website. The tool is very easy to use and is included with Kali Linux and other
penetration testing distributions by default.

    .. image:: images/009-searchsploit-01.jpg
       :width: 500 px
       :align: center

####

-------------------
Update before usage
-------------------

    .. note:: 

        Since it is an offline search engine, you should update the DB before using it.
        
        .. code:: shell
            :number-lines:
            :force:

             sudo searchsploit -u


    .. note:: 
        
        Alternatively, you can also run the following command to just update Searchsploit because
        above command will update and install all exploitdb packages, including exploitdb-papers
        which is greater than 2GB in size.
        
        .. code:: shell
            :number-lines:
            :force:

             sudo apt-get install exploitdb

####

---------------
Exploit Storage
---------------

    .. danger:: 
        
       When using the local Searchsploit exploit files, it is recommended to always save a separate
       copy of the exploit file to another location so that you are not modifying the original file
       as you may need to revert to or reuse the original file later. 

       The original Exploit are stored in this path :

        .. code:: shell
            :number-lines:
            :force:

             /usr/share/exploitdb/exploits/

####

-------
Exemple
-------

    .. note:: 
        
        The command returns a list of known vulnerabilities.

        In the path column contain a hint for the targeted OS.

        We will see the exploit **linux/remote/16922.rb**. The exploit will be performed later
        through **Metasploit**.
        
        .. code:: shell
            :number-lines:
            :force:

             searchsploit unreal ircd

        .. image:: images/010-searchsploit-02.jpg
           :width: 500 px
           :align: center


    .. important:: 
        
        **Tips**
        
        You can use the **–-exclude= flag** to filter out unwanted results from your search.

        .. code:: shell
            :number-lines:
            :force:

             searchsploit unreal ircd --exclude="/dos/"

        ...

        We can also add the **-p** option to show the full path of the exploit script.

        .. code:: shell
            :number-lines:
            :force:

             searchsploit 35513 -p

    .. danger:: 
        
        **Don't work on the original file**

        Remember to work only to a copy of the Exploit File !


    .. note:: 
        
        We can then print the contents of the files to the terminal using the **cat** command by
        appending the Path from the Searchsploit output to the Searchsploit exploit directory:
        (Here we print the second file for Backdoor Command Execution 16922.rb)

        .. code:: shell
            :number-lines:
            :force:

             cat /usr/share/exploitdb/exploits/linux/remote/16922.rb

        .. image:: images/011-searchsploit-03.jpg
           :width: 500 px
           :align: center

####

--------
Weblinks
--------

.. target-notes::