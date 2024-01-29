.. _ref_LinPEAS:

===================================================
LinPEAS – Linux Privilege Escalation Awesome Script
===================================================

.. index::
   single: LinPEAS
   single: Privilege Escalation Tools; LinPEAS

.. contents::
    :backlinks: top


####

    .. note:: 
        
        **Liens Web**

    * `LinPEAS - Github`_
    
.. _`LinPEAS - Github`: https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS

LinPEAS is an awesome script that searches for possible paths to escalate privileges on Linux/Unix
hosts. The script collects a lot of information from the system that may be useful to discover
privilege escalation vectors. LinPEAS collects information such as networking information, installed
software, processes, interesting files with misconfigured permissions and capabilities, and even
files with interesting content such as passwords. The LinPEAS script doesn’t have any dependencies
and runs on systems that support sh.

An interesting thing to note here is the legend printed at the top of the script output which
indicates the colors that are used to mark important output.

    .. image:: images/Linpeas-01.jpg
       :width: 500 px
       :align: center

It is important to pay special attention to the red and red/yellow text which mark privilege
escalation vectors and important things we must look at. According to the LinPEAS documentation it
should take about 2 minutes for the script to complete with default options.



####

--------
Weblinks
--------

.. target-notes::