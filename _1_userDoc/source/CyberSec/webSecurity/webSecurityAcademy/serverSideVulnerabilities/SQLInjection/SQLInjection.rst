.. _ref_sqli:

====================
SQL Injection (SQLi)
====================

.. index::
   single: SQL Injection
   single: Server-Side Vulnerabilities; SQL Injection

.. contents::
    :depth: 3
    :backlinks: top

####

-----------------------------
What is SQL injection (SQLi)?
-----------------------------

SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the
queries that an application makes to its database. This can allow an attacker to view data that they
are not normally able to retrieve. This might include data that belongs to other users, or any other
data that the application can access. In many cases, an attacker can modify or delete this data,
causing persistent changes to the application's content or behavior.

In some situations, an attacker can escalate a SQL injection attack to compromise the underlying
server or other back-end infrastructure. It can also enable them to perform denial-of-service
attacks.

####

-------------------------------------------
How to detect SQL injection vulnerabilities
-------------------------------------------

You can detect SQL injection manually using a systematic set of tests against every entry point in
the application. To do this, you would typically submit:

    * The single quote character **\'** and look for errors or other anomalies.

    * Some SQL-specific syntax that evaluates to the base (original) value of the entry point, and
      to a different value, and look for systematic differences in the application responses.
    
    * Boolean conditions such as **OR 1=1** and **OR 1=2**, and look for differences in the
      application's responses.

    * Payloads designed to trigger time delays when executed within a SQL query, and **look for 
      differences in the time taken to respond**.

    * OAST payloads designed to trigger an **out-of-band network interaction** when executed within
      a SQL query, and monitor any resulting interactions.

Alternatively, you can find the majority of SQL injection vulnerabilities quickly and reliably using
Burp Scanner.

####

----------------------
Retrieving hidden data
----------------------

Imagine a shopping application that displays products in different categories.


    .. note:: 
        
        When the user clicks on the **Gifts category**, their browser requests the URL:
        
        .. code:: URL
            :number-lines:
            :force:

             https://insecure-website.com/products?category=Gifts


        This causes the application to make a SQL query to retrieve details of the relevant products
        from the database:
        
        .. code:: SQL
            :number-lines:
            :force:

             SELECT * FROM products WHERE category = 'Gifts' AND released = 1


This SQL query asks the database to return:

    * all details (*)
    * from the products table
    * where the category is Gifts
    * and released is 1.

The restriction released = 1 is being used to hide products that are not released. We could assume
for unreleased products, released = 0.

The application doesn't implement any defenses against SQL injection attacks. 

    .. note:: 
        
        This means an attacker can construct the following attack, for example:
        
        .. code:: URL
            :number-lines:
            :force:

             https://insecure-website.com/products?category=Gifts'--
        
        This results in the SQL query:
        
        .. code:: SQL
            :number-lines:
            :force:

             SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1


Crucially, note that **--** is a comment indicator in SQL. This means that the rest of the query is
interpreted as a comment, effectively removing it. In this example, this means the query no longer
includes **AND released = 1**. As a result, all products are displayed, including those that are not
yet released.

    .. note:: 
        
        You can use a similar attack to cause the application to display all the products in any
        category, including categories that they don't know about:
        
        .. code:: URL
            :number-lines:
            :force:

             https://insecure-website.com/products?category=Gifts'+OR+1=1--
    .. note:: 
        
        This results in the SQL query:
        
        .. code:: SQL
            :number-lines:
            :force:

             SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1

The modified query returns all items where either the category is Gifts, or 1 is equal to 1. As 1=1
is always true, the query returns all items.



####

--------
Weblinks
--------

.. target-notes::