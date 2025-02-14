======
Crt.sh
======

.. index::
   single: Crt.sh
   single: Tools, Crt.sh
   single: Enumeration Tools, Crt.sh
   single: Domain Enumeration Tools, Crt.sh
   single: Web Reconnaissance - Passive; Crt.sh

.. contents::
    :depth: 3
    :backlinks: top

####

The site crt.sh helps in the search and analysis of SSL/TLS certificates. It allows:

   #. To identify the completeness of domain names that use TLS certificates for a given company, even if the transfer of domain names is prohibited on the DNS server.

   #. To consult the logs of detected certificates, providing details on all the certificates used as well as their validity date.

   #. To return a response in JSON format via the "output=json" parameter, which facilitates automation and integration into scripts.

   #. To be used as a data source for OSINT (Open Source Intelligence) activities, allowing for the quick identification of potentially vulnerable entry points of a company.

   #. To search for certificates issued for a specific domain, which can help discover lesser-known subdomains or potentially poorly protected resources.

In summary, crt.sh is a tool for in-depth analysis of SSL/TLS certificates.

###

-----------------------------
Using the API in command line
-----------------------------

    .. note:: 
        
         * **curl -s "https://crt.sh/?q=facebook.com&output=json"**: This command fetches the JSON output from crt.sh for certificates matching the domain facebook.com.
    
         * **jq -r '.[] | select(.name_value | contains("dev")) | .name_value'**: This part filters the JSON results, selecting only entries where the name_value field (which contains the domain or subdomain) includes the string "dev". The -r flag tells jq to output raw strings.
    
         * **sort -u**: This sorts the results alphabetically and removes duplicates.

        
        .. code:: bash
            :number-lines:
            :force:

             curl -s "https://crt.sh/?q=facebook.com&output=json" | jq -r '.[] | select(.name_value | contains("dev")) | .name_value' | sort -u

             *.dev.facebook.com
             *.newdev.facebook.com
             *.secure.dev.facebook.com
             dev.facebook.com
             devvm1958.ftw3.facebook.com
             facebook-amex-dev.facebook.com
             facebook-amex-sign-enc-dev.facebook.com
             newdev.facebook.com
             secure.dev.facebook.com





####

--------
Weblinks
--------

.. target-notes::