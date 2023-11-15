===========================
File Upload Vulnerabilities
===========================

.. index::
   single: File Upload Vulnerabilities
   single: Server-Side Vulnerabilities; File Upload Vulnerabilities

.. contents::
    :depth: 3
    :backlinks: top

####

-------------------------------------
What are file upload vulnerabilities?
-------------------------------------

File upload vulnerabilities are when a web server allows users to upload files to its filesystem
without sufficiently validating things like their name, type, contents, or size. Failing to
properly enforce restrictions on these could mean that even a basic image upload function can be
used to upload arbitrary and potentially dangerous files instead. This could even include
server-side script files that enable remote code execution.

In some cases, the act of uploading the file is in itself enough to cause damage. Other attacks may
involve a follow-up HTTP request for the file, typically to trigger its execution by the server.

####

-----------------------------------------
How do file upload vulnerabilities arise?
-----------------------------------------

Given the fairly obvious dangers, it's rare for websites in the wild to have no restrictions
whatsoever on which files users are allowed to upload. More commonly, developers implement what they
believe to be robust validation that is either inherently flawed or can be easily bypassed.

For example, they may attempt to blacklist dangerous file types, but fail to account for parsing
discrepancies when checking the file extensions. As with any blacklist, it's also easy to
accidentally omit more obscure file types that may still be dangerous.

In other cases, the website may attempt to check the file type by verifying properties that can be
easily manipulated by an attacker using tools like Burp Proxy or Repeater.

Ultimately, even robust validation measures may be applied inconsistently across the network of
hosts and directories that form the website, resulting in discrepancies that can be exploited.

####

----------------------------------------------------------
Exploiting unrestricted file uploads to deploy a web shell
----------------------------------------------------------

From a security perspective, the worst possible scenario is when a website allows you to upload
server-side scripts, such as PHP, Java, or Python files, and is also configured to execute them as
code. This makes it trivial to create your own web shell on the server.

    .. note:: 

        **Web Shell**
        
        A web shell is a malicious script that enables an attacker to execute arbitrary commands on
        a remote web server simply by sending HTTP requests to the right endpoint.

If you're able to successfully upload a web shell, you effectively have full control over the
server. This means you can read and write arbitrary files, exfiltrate sensitive data, even use the
server to pivot attacks against both internal infrastructure and other servers outside the network. 


    .. note:: 
        
        The following PHP one-liner could be used to read arbitrary files from the server's
        filesystem:
        
        .. code:: PHP
            :number-lines:
            :force:

             <?php echo file_get_contents('/path/to/target/file'); ?>

        Once uploaded, sending a request for this malicious file will return the target file's
        contents **in the response**.

    .. note:: 
        
        A more versatile web shell may look something like this:
        
        .. code:: PHP
            :number-lines:
            :force:

             <?php echo system($_GET['command']); ?>

        This script enables you to pass an arbitrary system command via a query parameter as follows:

        .. code:: HTTP
            :number-lines:
            :force:

             GET /example/exploit.php?command=id HTTP/1.1

Lab: Remote code execution via web shell upload
===============================================

    .. note:: 
        
        Creation of the file *"payload.php"* with the correct path we want to read from the server.
        
        .. image:: images/fileUploadPayload.png
           :width: 500 px
           :align: center

        The File is uploaded from the website. 

        .. image:: images/fileUploadWeb.png
           :width: 500 px
           :align: center

        Since there is no control of the file type, the website raise no error and let us to
        continue.

        .. image:: images/reponse2Upload.png
           :width: 500 px
           :align: center

        We can't see the data directly from the web site. But if we intercept the responce from
        *"BurpSuite"* or *"ZAP"*, we can see the correct answer.

        .. image:: images/response.png
           :width: 500 px
           :align: center

####

--------------------------------------------
Exploiting flawed validation of file uploads
--------------------------------------------

In the wild, it's unlikely that you'll find a website that has no protection against file upload
attacks like we saw in the previous lab. But just because defenses are in place, that doesn't mean
that they're robust. You can sometimes still exploit flaws in these mechanisms to obtain a web shell
for remote code execution.

Flawed file type validation
===========================

When submitting HTML forms, the browser typically sends the provided data in a POST request with
the content type application/x-www-form-url-encoded. This is fine for sending simple text like your
name or address. However, it isn't suitable for sending large amounts of binary data, such as an
entire image file or a PDF document. In this case, the content type multipart/form-data is preferred.

Consider a form containing fields for uploading an image, providing a description of it, and
entering your username. 


    .. note:: 
        
        Submitting such a form might result in a request that looks something like this:
        
        .. code:: HTTP
            :number-lines:
            :force:

             POST /images HTTP/1.1
             Host: normal-website.com
             Content-Length: 12345
             Content-Type: multipart/form-data; boundary=---------------------------012345678901234567890123456

             ---------------------------012345678901234567890123456
             Content-Disposition: form-data; name="image"; filename="example.jpg"
             Content-Type: image/jpeg

             [...binary content of example.jpg...]

             ---------------------------012345678901234567890123456
             Content-Disposition: form-data; name="description"

             This is an interesting description of my image.

             ---------------------------012345678901234567890123456
             Content-Disposition: form-data; name="username"

             wiener
             ---------------------------012345678901234567890123456--

As we can see, the message body is split into separate parts for each of the form's inputs. Each
part contains a Content-Disposition header, which provides some basic information about the input
field it relates to.

These individual parts may also contain their own Content-Type header, which tells the server the
**MIME type** of the data that was submitted using this input.

One way that websites may attempt to validate file uploads is to check that this input-specific
**Content-Type header** matches an expected MIME type. If the server is only expecting image files,
for example, it may only allow types like image/jpeg and image/png. 

    .. important:: 
        
        **implicitly trusted by the server**

        Problems can arise when the value of this header is implicitly trusted by the server.
        
        If no further validation is performed to check whether the contents of the file actually
        match the supposed MIME type, this defense can be easily bypassed using the repeater of 
        "BurpSuite" or "ZAP".

    .. note:: 
        
        **Uploading a File with th Wrong MIME type**

        When we upload a file with the wrong MIME type, we receve an HTTP/2 403 Forbiden responce.

        .. image:: images/uploadFileWrongMimeTypeReq.png
           :width: 500 px
           :align: center

        .. image:: images/uploadFileWrongMimeTypeRes.png
           :width: 500 px
           :align: center

        If we change only the MIME type and resend the request, the server will check only the
        validity of the MIME type without checking if the uploaded file type as the same as the
        MIME type.

        .. image:: images/uploadFileChangedMimeTypeReq.png
           :width: 500 px
           :align: center

        .. image:: images/uploadFileChangedMimeTypeRes.png
           :width: 500 px
           :align: center

        It is then possible to read the return of the php script.

        .. image:: images/uploadFileChangedMimeTypeResBrowserDevTools.png
           :width: 500 px
           :align: center

####

--------
Weblinks
--------

.. target-notes::