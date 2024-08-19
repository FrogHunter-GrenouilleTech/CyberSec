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
        * `Cloudflare - HTTP Status Codes`_
        * `AWS - API Error Codes`_
        
.. _`HTTP response status codes`: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
.. _`Cloudflare - HTTP Status Codes`: https://developers.cloudflare.com/support/troubleshooting/http-status-codes/http-status-codes/
.. _`AWS - API Error Codes`: https://docs.aws.amazon.com/AmazonSimpleDB/latest/DeveloperGuide/APIError.html

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


Some of the most commonly seen examples from each of the above HTTP method types:

    - **200 OK** - Returned on a successful request, and the response body usually contains the
      requested resource.

    - **301 Moved Permanently** - Redirects the client to another URL. For example, redirecting the
      user to their dashboard after a successful login.

    - **302 Found** - Redirects the client to another URL. For example, redirecting the user to their
      dashboard after a successful login.

    - **400 Bad Request** - Returned on encountering malformed requests such as requests with missing
      line terminators.

    - **403 Forbidden** - Signifies that the client doesn't have appropriate access to the resource.
      It can also be returned when the server detects malicious input from the user.

    - **404 Not Found** - Returned when the client requests a resource that doesn't exist on the
      server.

    - **500 Internal Server Error** - Returned when the server cannot process the request.

    .. note:: 
        
        **Information**

       Apart from the standard HTTP codes, various servers and providers such as **Cloudflare** or
       **AWS** implement their own codes.


####

--------
Weblinks
--------

.. target-notes::