==============
Access Control
==============

.. index::
   single: Access Control
   single: Server-Side Vulnerabilities; Access Control

.. contents::
    :depth: 3
    :backlinks: top

####

-----------------------
What is access control?
-----------------------

Access control is the application of constraints on who or what is authorized to perform actions or
access resources. In the context of web applications, access control is dependent on authentication
and session management:

    * Authentication confirms that the user is who they say they are.
    * Session management identifies which subsequent HTTP requests are being made by that same user.
    * Access control determines whether the user is allowed to carry out the action that they are
      attempting to perform.

**Broken access controls** are common and often present a critical security vulnerability. Design
and management of access controls is a complex and dynamic problem that applies business,
organizational, and legal constraints to a technical implementation. Access control design decisions
have to be made by humans so the potential for errors is high.

    .. note:: 
        
        **Liens Web**

            * `Bypassing 403s like a PRO!`_
        
.. _`Bypassing 403s like a PRO!`: https://shrirangdiwakar.medium.com/bypassing-403s-like-a-pro-2-100-broken-access-control-66beef4afa8c

    .. image:: images/accessControl01.png
       :width: 500 px
       :align: center

####

-------------------------------
Horizontal privilege escalation
-------------------------------

Horizontal privilege escalation occurs if a user is able to gain access to resources belonging to
another user, instead of their own resources of that type. For example, if an employee can access
the records of other employees as well as their own, then this is horizontal privilege escalation.

Horizontal privilege escalation attacks may use similar types of exploit methods to **vertical**
**privilege escalation**.

    .. note:: 
        
        For example, a user might access their own account page using the following URL:
        
        .. code:: inputLanguage
            :number-lines:
            :force:

             https://insecure-website.com/myaccount?id=123


If an attacker modifies the id parameter value to that of another user, they might gain access to
another user's account page, and the associated data and functions.

    .. note::

        .. glossary::

           IDOR
        
                This is an example of an **Insecure Direct Object Reference (IDOR) vulnerability**.
                This type of vulnerability arises where user-controller parameter values are used to
                access resources or functions directly.

In some applications, the exploitable parameter does not have a predictable value. For example,
instead of an incrementing number, an application might use globally unique identifiers (GUIDs) to
identify users. This may prevent an attacker from guessing or predicting another user's identifier.
However, the GUIDs belonging to other users might be disclosed elsewhere in the application where
users are referenced, such as user messages or reviews.

####

-----------------------------
Vertical privilege escalation
-----------------------------

If a user can gain access to functionality that they are not permitted to access then this is 
**vertical privilege escalation**. For example, if a non-administrative user can gain access to an
admin page where they can delete user accounts, then this is vertical privilege escalation.

Unprotected functionality
=========================

At its most basic, vertical privilege escalation arises where an application does not enforce any
protection for sensitive functionality. For example, administrative functions might be linked from
an administrator's welcome page but not from a user's welcome page. However, a user might be able to
access the administrative functions by browsing to the relevant admin URL.

    .. note:: 
        
        For example, a website might host sensitive functionality at the following URL:
        
        .. code:: shell
            :number-lines:
            :force:

             https://insecure-website.com/admin

        This might be accessible by any user, not only administrative users who have a link to the
        functionality in their user interface.

    .. note:: 
        
        In some cases, the administrative URL might be disclosed in other locations, such as the robots.txt file:
        
        .. code:: url
            :number-lines:
            :force:

             https://insecure-website.com/robots.txt


    .. important:: 
        
        Even if the URL isn't disclosed anywhere, an attacker may be able to use a wordlist to
        brute-force the location of the sensitive functionality.

Unprotected functionality - Continued
=====================================

    .. note:: 
        
        In some cases, sensitive functionality is concealed by giving it a less predictable URL.
        This is an example of so-called "security by obscurity". However, hiding sensitive
        functionality does not provide effective access control because users might discover the
        obfuscated URL in a number of ways.

        Imagine an application that hosts administrative functions at the following URL:
        
        .. code:: html
            :number-lines:
            :force:

             <script>
	            var isAdmin = false;
	            if (isAdmin) {
	            	...
		            var adminPanelTag = document.createElement('a');
	            	adminPanelTag.setAttribute('https://insecure-website.com/administrator-panel-yb556');
	            	adminPanelTag.innerText = 'Admin panel';
	            	...
	            }
             </script>

        This script adds a link to the user's UI if they are an admin user. However, the script
        containing the URL is visible to all users regardless of their role.

####

--------------------------------------
Parameter-based access control methods
--------------------------------------

Some applications determine the user's access rights or role at login, and then store this
information in a user-controllable location. This could be:

    * A hidden field.
    * A cookie.
    * A preset query string parameter.

    .. note:: 
        
        The application makes access control decisions based on the submitted value. For example:
        
        .. code:: url
            :number-lines:
            :force:

             https://insecure-website.com/login/home.jsp?admin=true
             https://insecure-website.com/login/home.jsp?role=1

This approach is insecure because a user can modify the value and access functionality they're not 
authorized to, such as administrative functions. 

Exemple of a query string parameter
===================================

.. note:: 
    
    The GET request after a successfull authentication trought a previous POST request
    
    .. image:: images/accessControl02.png
        :width: 500 px
        :align: center


    A string query is showing to us that "Admin" has the Status "false" and the responce allow
    us to acces only to "/My-Account".
    
    .. image:: images/accessControl03.png
        :width: 500 px
        :align: center

.. note:: 
    
    By using a repeter throught a proxy like ":ref:`BurpSuite <ref_BurpSuite>`" or
    ":ref:`OWASP ZAP <ref_Owasp_Zap>`", it is possible to replace the value of the string query
    "Admin=false" by "Admin=true"
    
    .. image:: images/accessControl04.png
        :width: 500 px
        :align: center

    The response will now allow us to access to "/admin".
            
    .. image:: images/accessControl05.png
        :width: 500 px
        :align: center

Even if the response inside the proxy has a status "200 OK" and we can read that we have acces to
the Navigation Header "/admin" from the html response. We still have no access to "/admin" from the
browser.

.. note:: 
        
    We need to edit manualy the string value "Admin" insisde the storage "Cookie" accessible from
    the browser development tools (F12) :
        
    .. image:: images/accessControl06.png
       :width: 500 px
       :align: center
        
    ... And replace "false" by "true":

    .. image:: images/accessControl07.png
       :width: 500 px
       :align: center

    At this point, only the “Admin panel” menu will be accessible to us from the browser.

    .. image:: images/accessControl08.png
       :width: 500 px
       :align: center

####

--------
Weblinks
--------

.. target-notes::