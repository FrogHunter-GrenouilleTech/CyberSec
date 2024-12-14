=======
Fuzzing
=======

.. index::
   single: Fuzzing
   single: Technics; Fuzzing

.. contents::
    :depth: 3
    :backlinks: top

####

The term fuzzing refers to a testing technique that sends various types of user input to a certain
interface to study how it would react. If we were fuzzing for SQL injection vulnerabilities, we
would be sending random special characters and seeing how the server would react. If we were fuzzing
for a buffer overflow, we would be sending long strings and incrementing their length to see if and
when the binary would break.

We usually utilize pre-defined wordlists of commonly used terms for each type of test for web
fuzzing to see if the webserver would accept them. This is done because web servers do not usually
provide a directory of all available links and domains (unless terribly configured), and so we would
have to check for various links and see which ones return pages. 

####

--------
Weblinks
--------

.. target-notes::