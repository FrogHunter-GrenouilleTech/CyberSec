.. _ref_netCmd:

===========
Net Command
===========

.. index::
   single: Net Command
   single: Tools; Net Command
   single: Active Directory ; Active Directory - Enumeration
   single: Active Directory - Enumeration; Net Command
   single: Enumeration Tools; Net Command

.. contents::
    :depth: 3
    :backlinks: top

####

The Net command can be used to gather information from Active directory. This command must be run
with Administrator privileges.

Since the "domain" command must be run in a domain computer, it could be used directly from a
computer of the client or though a Reverse / Blind shell after initial access.

This set of command could be used for the pivoting. 

---------------------
List all the domain Users
---------------------

    .. note:: 
        
        .. code:: shell
            :number-lines:
            :force:

             net users /domain

####

--------------------------
List all the domain groups
--------------------------

    .. note:: 
        
        .. code:: shell
            :number-lines:
            :force:

             net groups /domain

####

-------------------------------------------------------
List all the member of the group "Domain Administrator"
-------------------------------------------------------

    .. note:: 
        
        .. code:: shell
            :number-lines:
            :force:

             net groups /domain "Admins du domaine"


####

--------
Weblinks
--------

.. target-notes::