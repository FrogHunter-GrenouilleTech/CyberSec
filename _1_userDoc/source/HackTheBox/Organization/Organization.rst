============
Organization
============

.. index::
   single: Organization;
   single: Pentest; Organization;

.. contents::
    :depth: 3
    :backlinks: top

####

Organization plays a significant role in our penetration tests. It does not matter what type of
penetration test it is. Having a working environment that we can navigate almost blindly saves a
tremendous amount of time researching resources that we are already familiar with and have invested
our time learning. Once we have an extensive list of resources required for each assessment and
include installation, this results in a few hours of pure preparation.

####

-----------------------------------
Structuring the pentest environment
-----------------------------------

Corporate environments usually consist of heterogeneous networks (hosts/servers having different
Operating Systems). Therefore, it makes sense to organize hosts and servers based on their Operating
System. If we organize our structure according to penetration testing stages and the targets’
Operating System, then a sample folder structure could look as follows.

    .. image:: images/basicSampleFolder.png
       :width: 500 px
       :align: center

If we are specialized in specific penetration testing fields, we can reorganize the structure
according to these fields.

    .. image:: images/specilizedSampleFolder.png
       :width: 500 px
       :align: center

It is highly recommended to create your own folder structure. It is important to have a structure
that is easy to navigate and understand.

Proper organization helps us in both keeping track of everything and finding errors in our
processes. During our studies here, we will come across many different fields that we can use to
expand and enhance our understanding of the cybersecurity domain. Not only can we save the
cheatsheets or scripts provided here and there, but we can also keep notes regarding all phases of a
penetration test we will come across to ensure that no critical steps are missed in future
engagements. 

It is recommend to start with small structures, especially when entering the penetration testing
field. Organizing based on the Operating System is, therefore, more suitable for newcomers.

####

-----------
Note Taking
-----------

Note-taking is another essential part of our penetration testing because we accumulate a lot of
different information, results, and ideas that are difficult to remember all at once.

    .. note:: 
        
        **Five different main types of information that need to be noted down**

        #. Newly discovered information

        #. Ideas for further tests and processing

        #. Scan results

        #. Logging

        #. Screenshots


    :Discovering Information:

        The discovered informations are general information, such as new IP addresses, usernames,
        passwords, source code, etc., that we identified and are related to the penetration testing
        engagement and process.
       
        This is information that we can use against our target company. We often obtain such
        information through OSINT, active scans, and manual analysis of the given information
        resources and services.


    :Processing:

        We will receive a lot of different information during our penetration testing that will
        require us to adapt our approach.
        
        These results may give us ideas for subsequent steps we can take, and other vulnerabilities
        or misconfigurations may be forgotten or overlooked. Therefore, **we should get in the habit
        of noting down everything we see** that should be investigated as part of the assessment.


    :Results:

        The results we get after our scans and penetration testing steps are significant. With such
        a large amount of information in a short time, one can quickly feel overwhelmed. It is not
        easy at first to filter out the most critical pieces of information. This is something that
        will come with experience and practice. Only through practice, our eyes can be trained to
        recognize the essential small fragments of information. Nevertheless, we should keep all
        information and results not to miss something meaningful and because a piece of information
        may prove helpful later in the engagement. Besides, these results are also often used for
        documentation.


    :Logging:

        Logging is essential for both documentation and our protection. If third parties attack the
        company during our penetration test and damage occurs, we can prove that the damage did not
        result from our activities.


    :Screenshots:

        Screenshots serve as a momentary record and represent proof of results obtained, necessary
        for the Proof-Of-Concept and our documentation.


####

--------
Weblinks
--------

.. target-notes::