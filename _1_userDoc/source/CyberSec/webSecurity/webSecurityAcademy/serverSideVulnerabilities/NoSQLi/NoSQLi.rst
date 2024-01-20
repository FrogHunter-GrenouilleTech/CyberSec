===============
NoSQL injection
===============

.. index::
   single: NoSQL injection
   single: Server-Side Vulnerabilities; NoSQL injection

.. contents::
    :depth: 3
    :backlinks: top


.. toctree::
   :maxdepth: 3

   NoSQLi_syntax/NoSQLi_syntax
   NoSQLi_operator/NoSQLi_operator

####

    .. image:: images/nosql-injection-graphic.svg
       :width: 500 px
       :align: center

 NoSQL injection is a vulnerability where an attacker is able to interfere with the queries that an
 application makes to a NoSQL database. NoSQL injection may enable an attacker to:

    * Bypass authentication or protection mechanisms.
    * Extract or edit data.
    * Cause a denial of service.
    * Execute code on the server.

NoSQL databases store and retrieve data in a format other than traditional SQL relational tables.
They use a wide range of query languages instead of a universal standard like SQL, and have fewer
relational constraints.

 There are two different types of NoSQL injection:

    * :ref:`Syntax Injection <ref_noSQLiSynt>` - This occurs when you can break the NoSQL query
      syntax, enabling you to inject your own payload. The methodology is similar to that used in
      SQL injection. However the nature of the attack varies significantly, as NoSQL databases use a
      range of query languages, types of query syntax, and different data structures.

    * :ref:`Operator injection <ref_noSQLiOper>` - This occurs when you can use NoSQL query
      operators to manipulate queries.



####

--------
Weblinks
--------

.. target-notes::