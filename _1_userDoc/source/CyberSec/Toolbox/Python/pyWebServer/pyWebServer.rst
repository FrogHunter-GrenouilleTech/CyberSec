.. _ref_pyWebServer:

===================
Python - Web server
===================

.. index::
   single: Python - Web server
   single: Python; Python - Web server
   single: Web Server; Python - Web server
   single: File Transfer; Python - Web server

.. contents::
    :depth: 3
    :backlinks: top

####
    
Using the Python webserver is the safest, easiest and recommended way to serve exploits. In most
situations this method is sufficient and offers all the functionality required to compromise a
machines.
    
    .. note:: 
        
        **Python Web server**

            This module allows you to use a single command to create a web server to serve files and
            web pages.
        
        .. code:: shell
            :number-lines:
            :force:

                python3 -m http.server 80

        .. important:: 
            
            Providing a port number is optional, but if you don’t specify a port number the
            webserver will bind to port **8000** by default.

        .. image:: images/pythonWebServer.png
            :width: 540 px
            :align: center

    .. important:: 
        
        **Caution**
        
        SimpleHTTPServer : work only with Python2

    .. danger:: 
        
        **Take care of the scope of the web server**
        
        it is important to realize it serves the files in the directory from which it is started.
        For this reason, it’s important to be careful not to start the webserver in root directories
        (such as Linux root: ‘/’ or the root users home directory: ‘/root/’) or in directories
        containing files you don’t want to share.

The Python Web Server is also a good option for transfering a file from the compromized machine for
the data exfiltrating. However since Python is not installed by default on Windows Systems, the
Python Web server is, most of the time, the preferd way for the UX system.


####

--------
Weblinks
--------

.. target-notes::