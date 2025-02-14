.. _ref_Whois:

=====
Whois
=====

.. index::
   single: Whois
   single: Tools; Whois
   single: Passive information gathering; Whois

.. contents::
    :depth: 3
    :backlinks: top

####

----------
Definition
----------

**Whois** is a query and response protocol used for querying databases that store the registered
users or assignees of a domain name or an IP address block. It is commonly used for network
troubleshooting and for gathering information about domain ownership, registration details, and
contact information.

.. note::

    Each WHOIS record typically includes the following information:

        * Domain name: The domain name for which the record is being queried. (e.g., example.com)
        * Registar: The registrar responsible for the domain name registration. (e.g., GoDaddy)
        * Registrant Contact: The contact information of the domain owner.
        * Administrative Contact: The person responsible for managing the domain.
        * Technical Contact: The person handling technical issues related to the domain.
        * Creation and Expiration Dates: The date when the domain was registered and when it will expire.
        * Name Servers: The name servers responsible for hosting the domain's DNS records.

####

-------------------
WHOIS for Web Recon
-------------------

    * **Identifying Key Personnel**: WHOIS records often include contact information for the domain
      owner, such as email and phone numbers. This information can be valuable for identifying key
      personnel within an organization. It can be leveraged for social engineering attacks or to
      identify potential targets for phishing campaigns.

    * **Discovering Network Infrastructure**: Technical details like name servers and IP addresses
      provide clues about the target's network infrastructure. This can help penetration testers
      identify potential entry points or misconfigurations.

    * **Historical Data Analysis**: Accessing historical WHOIS records can reveal changes in 
      ownership, contact information, or technical details over time. This can be useful for
      tracking the evolution of the target's digital presence.



####

--------
Weblinks
--------

.. target-notes::