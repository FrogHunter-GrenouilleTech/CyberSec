.. _ref_CrossLinked:

===========
CrossLinked
===========

.. index::
   single: CrossLinked
   single: LinkedIn; CrossLinked

.. contents::
    :backlinks: top

####

    .. note:: 
        
        **Liens Web**
        
        * `CrossLinked`_
        
        .. _`CrossLinked`: https://github.com/m8sec/CrossLinked

CrossLinked is a LinkedIn enumeration tool that uses search engine scraping to collect valid
employee names from an organization.

This technique provides accurate results without the use of API keys, credentials, or accessing
LinkedIn directly!

    .. note:: 
        
        **Usage exemple**

        For best results, use the company name as it appears on LinkedIn "Target Company" not the
        domain name.

        .. code:: shell
            :number-lines:
            :force:

             python3 crosslinked.py -f 'domain\{f}{last}' -t 15 -j 2 company_name

             # ...

             python3 crosslinked.py -f '{first}.{last}@domain.com' company_name

####

--------
Weblinks
--------

.. target-notes::