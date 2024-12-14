====
CVSS
====

.. index::
   single: CVSS
   single: Report; CVSS

.. contents::
    :depth: 3
    :backlinks: top

####

    .. note:: 
        
        **Liens Web**

        * `Common Vulnerability Scoring System Version 4.`_
        * `Common Vulnerability Scoring System Version 4.0 Calculator`_
        
.. _`Common Vulnerability Scoring System Version 4.`: https://www.first.org/cvss/v4-0/
.. _`Common Vulnerability Scoring System Version 4.0 Calculator`: https://www.first.org/cvss/calculator/4.0

The Common Vulnerability Scoring System (CVSS) is an open framework for communicating the
characteristics and severity of software vulnerabilities. CVSS consists of four metric groups:

    .. note:: 
        
        ::Base::

            The Base group represents the intrinsic qualities of a vulnerability that are constant
            over time and across user environments.

        ::Threat::

            The Threat group reflects the characteristics of a vulnerability that change over time.

        ::Environmental::

            The Environmental group represents the characteristics of a vulnerability that are
            unique to a user's environment.
        
        ::Supplemental::
        
            Supplemental metrics do not modify the final score, and are used as additional insight
            into the characteristics of a vulnerability.

Base metric values are combined with default values that assume the highest severity for Threat and
Environmental metrics to produce a score ranging from 0 to 10. To further refine a resulting
severity score, Threat and Environmental metrics can then be amended based on applicable threat
intelligence and environmental considerations. A CVSS vector string consists of a compressed
textual representation of the values used to derive the score. 

####

--------
Weblinks
--------

.. target-notes::