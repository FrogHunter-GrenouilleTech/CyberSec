====================
Output Data to files
====================

.. index::
   single: Nmap - Output Data
   single: Nmap; Nmap - Output Data

.. contents::
    :depth: 3
    :backlinks: top

####

-------------
Output format
-------------

:Liens_Web:
    * `Output to file`_

.. _`Output to file`: https://nmap.org/book/man-output.html

Nmap makes output available in five different formats.

    * The default is called **interactive output**, and it is sent to standard output (stdout) and
      has no associated command-line options.
    
    * **normal output**, which is similar to *interactive* except that it displays less
      runtime information and warnings since it is expected to be analyzed after the scan completes
      rather than interactively.

          .. note:: 
              
              **-oN**
              
              .. code:: shell
                  :number-lines:
                  :force:
      
                   -oN <filespec> (normal output)

    * **XML output** is one of the most important output types, as it can be converted to HTML,
      easily parsed by programs such as Nmap graphical user interfaces, or imported into databases.

            .. note:: 
                
                **-oX**
                
                .. code:: shell
                    :number-lines:
                    :force:
        
                     -oX <filespec> (XML output)

    * **grepable output** which includes most information for a target host on a single line.

          .. note:: 
              
              **-oG**
              
              .. code:: shell
                  :number-lines:
                  :force:
      
                   -oG <filespec> (grepable output)
    
    * **sCRiPt KiDDi3 0utPUt** for users who consider themselves. this output is not for serious
    work !

          .. note:: 
              
              **-oS**
              
              .. code:: shell
                  :number-lines:
                  :force:
      
                   -oS <filespec> (ScRipT KIdd|3 oUTpuT)

Multiple formats may be specified, but each format may only be specified once. For example, you may
wish to save normal output for your own review while saving XML of the same scan for programmatic
analysis. You might do this with the options **-oX** *myscan.xml* **-oN** *myscan.nmap*. 

As a convenience, you may specify **-oA <basename>** to store scan results in *normal*, *XML*, and
*grepable* formats at once. They are stored in **<basename>.nmap**, **<basename>.xml**, and
**<basename>.gnmap**, respectively. As with most programs, you can prefix the filenames with a
directory path, such as ~/nmaplogs/foocorp/ on Unix or c:\hacking\sco on Windows.

      .. note:: 
          
          **-oA**
          
          .. code:: shell
              :number-lines:
              :force:
  
               -oA <basename> (Output to all formats)

####

-------------------------------
Verbosity and debugging options
-------------------------------

Verbosity
=========

Increases the verbosity level, causing Nmap to print more information about the scan in progress.
Open ports are shown as they are found and completion time estimates are provided when Nmap thinks a
scan will take more than a few minutes. Use it twice or more for even greater verbosity: **-vv**, or
give a verbosity level directly, for example **-v3**.

      .. note:: 
          
          **-v**
          
          .. code:: shell
              :number-lines:
              :force:
  
              -v (Increase verbosity level) or -v<level> (Set verbosity level)

Debug Level
===========

Debugging output is useful when a bug is suspected in Nmap, or if you are simply confused as to what
Nmap is doing and why. As this feature is mostly intended for developers, debug lines aren't always
self-explanatory. You may get something like: Timeout vals: srtt: -1 rttvar: -1 to: 1000000 delta
14987 ==> srtt: 14987 rttvar: 14987 to: 100000. If you don't understand a line, your only recourses
are to ignore it, look it up in the source code, or request help from the development list
(nmap-dev). Some lines are self explanatory, but the messages become more obscure as the debug level
is increased.

####

--------
Weblinks
--------

.. target-notes::