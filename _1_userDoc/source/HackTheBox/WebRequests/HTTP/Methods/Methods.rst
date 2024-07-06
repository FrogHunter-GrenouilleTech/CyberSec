======================
HTTP Methods and Codes
======================


.. index::
   single: HTTP Methods and Codes
   single: HTTP; HTTP Methods and Codes

.. contents::
    :depth: 3
    :backlinks: top

####

HTTP supports multiple methods for accessing a ressource. Several request methods allow the browser
to send information, forms, or files to the server. These server methods are used to tell the server
how to process the request we send and how to reply.


---------------
Request Methods
---------------

    .. note:: 
        
        **Liens Web**

        * `HTTP request methods`_
        
.. _`HTTP request methods`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

Some of the most commonly used methods:

    - **GET** - Requests a specific resource. Additional data can be passed to the server via query
      strings in the URL (e.g. ?param=value).

    - **POST** - Sends data to the server. It can handle multiple types of input, such as text,
      PDFs, and other forms of binary data.
      
      This data is appended in the request body present after the headers. The POST method is
      commonly used when sending information (e.g. forms/logins) or uploading data to a website,
      such as images or documents.

    - **HEAD** - Requests the headers that would be returned if a GET request was made to the
      server. It doesn't return the request body and is usually made to check the response length
      before downloading resources.

    - **PUT** - Creates new resources on the server. Allowing this method without proper controls
      can lead to uploading malicious resources.

    - **DELETE** - Deletes an existing resource on the webserver. If not properly secured, can lead
      to Denial of Service (DoS) by deleting critical files on the web server.

    - **OPTIONS** - Returns information about the server, such as the methods accepted by it.

    - **PATCH** - Applies partial modifications to the resource at the specified location.

####

--------------
Response Codes
--------------

    .. note:: 
        
        **Liens Web**

        * `HTTP response status codes`_
        
.. _`HTTP response status codes`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

HTTP status codes are used to tell the client the status of their request. An HTTP server can return
five types of response codes:

    - **1XX** - Informational responses.
      Provides information and does not affect the processing of the request.

    - **2XX** - Successful responses.
      Returned when a request succeeds.

    - **3XX** - Redirection messages.
      Returned when the server redirects the client.

    - **4XX** - Client error responses.
      Signifies improper requests from the client. For example, requesting a resource that doesn't exist or requesting a bad format.

    - **5XX** - Server error responses.
      Signifies the server encountered an error while processing the request.




####

--------
Weblinks
--------

.. target-notes::