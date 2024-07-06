================================================
Security Information and Event Management - SIEM
================================================

.. index::
   single: SIEM
   single: Blue Team; SIEM

.. contents::
    :depth: 3
    :backlinks: top

####

-------------
What is SIEM?
-------------

SIEM stands for Security Information and Event Management. It is a software solution that aggregates
and analyzes log data from various security devices and applications to identify threats, anomalies,
and risks in real-time. The core capabilities of SIEM include:

    * Log collection and normalization: Collects log data from different sources, parses the data,
      and converts it into a standard format.

    * Correlation analysis: Applies correlation rules to identify relationships between events
      across different data sources. This helps detect complex threats.

    * Alerting and notification: Triggers alerts and sends notifications when threats or anomalies
      are detected.

    * Reporting and dashboards: Provides various reports, graphs, and dashboards to visualize
      security data, trends, and key risk metrics. 

    * Retention and archiving: Stores log data for compliance and forensic analysis.

    * Threat intelligence integration: Incorporates data from threat feeds to detect known attack
      patterns and IOCs.

Some key benefits of using SIEM are faster threat detection, compliance, and centralized visibility
into security data. Leading SIEM solutions include Splunk, IBM QRadar, LogRhythm, AlienVault, etc.

####

-----------
SIGMA Rules
-----------

    .. note:: 
        
        **Liens Web**

        * `SIGMA detection Format`_
        * `Sigma - Generic Signature Format for SIEM Systems - GitHub`_
        * `Règles SIGMA: standardiser les détections quel que soit le SIEM`_
        
.. _`Règles SIGMA: standardiser les détections quel que soit le SIEM`: https://yogosha.com/fr/blog/regles-sigma/
.. _`Sigma - Generic Signature Format for SIEM Systems - GitHub`: https://github.com/SigmaHQ/sigma        
.. _`SIGMA detection Format`: https://sigmahq.io/

SIGMA rules are detection rules that can be used by SIEM solutions to detect suspicious activity and
potential threats. Here are some key points about SIGMA rules:

    * SIGMA stands for Security Information & Event Management Analytics. It is an open standard for
      describing detection rules.

    * SIGMA rules are written in YAML syntax. They contain fields like title, description, log
      source, detection logic etc.

    * The detection logic uses conditions to check events from log data. For example, checking
      process name, parent process, file path, registry keys etc. 

    * SIGMA rules help identify indicators of compromise and detect attack techniques based on
      MITRE ATT&CK framework.

    * There is a GitHub repository containing a collection of tested SIGMA rules for different use
      cases.

    * SIEM tools like Splunk, Elastic, IBM QRadar support importing and running SIGMA rules to
      monitor for suspicious activity.

    * Writing custom SIGMA rules allows organizations to detect threats specific to their
      environment.

    * Proper tuning is required to minimize false positives when applying SIGMA rules. They should
      be tested with real data.

In summary, SIGMA rules standardize detection logic to help SIEM solutions identify advanced threats
and targeted attacks.



####

--------
Weblinks
--------

.. target-notes::