===========================
HTTP Requests and Responses
===========================

.. index::
   single: HTTP Requests and Responses
   single: HTTP; HTTP Requests and Responses

.. contents::
    :depth: 3
    :backlinks: top

####

HTTP communications mainly consist of an HTTP **request** and an HTTP **response**.

An HTTP request is made by the client (e.g. cURL/browser), and is processed by the server (e.g.
web server). The requests contain all of the details we require from the server, including the
resource (e.g. URL, path, parameters), any request data, headers or options we specify.

Once the server receives the HTTP request, it processes it and responds by sending the HTTP
response, which contains the response code and may contain the resource data if the requester has
access to it.

####

------------
HTTP Request
------------

    .. image:: images/raw_request.png
       :width: 600 px
       :align: center

The first line of any HTTP request contains three main fields **'separated by spaces'**:

    - **Method** - The method defines the action to be performed on the resource.

        ex: GET, POST, PUT, DELETE, etc.

    - **Path** - The path is the location of the resource we want to access.

        ex: /index.html, /images/logo.png, etc.

    - **Version** - The version of the HTTP protocol we are using.

        ex: HTTP/1.1

The next set of lines contain **HTTP header value pairs**, like Host, User-Agent, Cookie, and many
other possible headers.

These headers are used to specify various attributes of a request. **The headers are terminated with
a new line**, which is necessary for the server to validate the request. Finally, a request may end
with the request body and data.

    .. note:: 
        
        * **HTTP version 1.X** sends requests as clear-text, and **uses a new-line character to
          separate different fields and different requests**.

        
        * **HTTP version 2.X**, on the other hand, **sends requests as binary data `in a dictionary`
          form**.

####

-------------
HTTP Response
-------------

    .. image:: images/raw_response.png
       :width: 600 px
       :align: center

The first line of an HTTP response contains two fields separated by spaces. 

    - **Version** - The version of the HTTP protocol we are using.

        ex: HTTP/1.1

    - **Status Code** - The status code indicates the result of the request.

        ex: 200, 404, 500, etc.

Response codes are used to determine the request's status. After the first line, the response
lists its headers, similar to an HTTP request.

Finally, the response may end with a response body, which is separated by a new line after the
headers. The response body is usually defined as HTML code. However, it can also respond with
other code types such as JSON, website resources such as images, style sheets or scripts, or even
a document such as a PDF document hosted on the webserver.


####

--------
Weblinks
--------

.. target-notes::