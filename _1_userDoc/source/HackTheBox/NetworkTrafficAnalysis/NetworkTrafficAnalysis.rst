==============================
Network Traffic Analysis (NTA)
==============================

.. index::
   single: Network Traffic Analysis
   single: NTA
   single: Blue Team; Network Traffic Analysis
   single: Red Team; Network Traffic Analysis
   single: Blue Team; NTA
   single: Red Team; NTA

.. contents::
    :backlinks: top

.. toctree::
   :maxdepth: 3

   Child/Child

####

Network Traffic Analysis is a crucial cybersecurity practice that involves examining data flowing
through a network to identify potential threats, anomalies, and security incidents. It provides
valuable insights into network behavior, allowing security professionals to detect and respond to
malicious activities in real-time.

For SOC analysts, Network Traffic Analysis is an indispensable tool in their arsenal, enabling them
to monitor network communications, identify suspicious patterns, and investigate potential security
breaches. By analyzing network traffic, SOC analysts can detect various types of attacks, including
malware infections, data exfiltration attempts, and unauthorized access to sensitive resources. This
technique is particularly useful in intrusion detection and prevention, as it helps identify
indicators of compromise and potential attack vectors before they can cause significant damage.

Furthermore, Network Traffic Analysis plays a vital role in forensic investigations, allowing
analysts to reconstruct events, trace the origin of attacks, and gather evidence for incident
response and legal purposes. By providing a comprehensive view of network activities, it enables
security teams to maintain a proactive stance against evolving cyber threats and strengthen their
overall security posture.

####

----------
BPF Syntax
----------

    .. note:: 
        
        **Liens Web**

        * `Berkeley packet filters`_
        
.. _`Berkeley packet filters`: https://www.ibm.com/docs/en/qsip/7.4?topic=queries-berkeley-packet-filters


Many tools have their syntax and commands to utilize, but one that is shared among them is 
**Berkeley Packet Filter (BPF) syntax**. In essence, BPF is a technology that enables a raw
interface to read and write from the Data-Link layer. 

####

------------
NTA Workflow
------------

Traffic analysis is not an exact science. NTA can be a very dynamic process and is not a direct
loop. It is greatly influenced by what we are looking for (network errors vs. malicious actions) and
where we have visibility into our network. Performing traffic analysis can distill down to a few
basic tenants.


   #. Ingest Traffic

      Once we have decided on our placement, begin capturing traffic. Utilize capture filters if we
      already have an idea of what we are looking for.

   #. Reduce Noise by Filtering

      Capturing traffic of a link, especially one in a production environment, can be extremely
      noisy. Once we complete the initial capture, an attempt to filter out unnecessary traffic from
      our view can make analysis easier. (Broadcast and Multicast traffic, for example.)

   #. Analyze and Explore

      Now is the time to start carving out data pertinent to the issue we are chasing down. Look at
      specific hosts, protocols, even things as specific as flags set in the TCP header. The
      following questions will help us:

      * Is the traffic encrypted or plain text? Should it be?

      * Can we see users attempting to access resources to which they should not have access?

      * Are different hosts talking to each other that typically do not?

   #. Detect the Root Issue

      * Are we seeing any errors? Is a device not responding that should be?

      * Use our analysis to decide if what we see is benign or potentially malicious.

      * Other tools like IDS and IPS can come in handy at this point. They can run heuristics and
        signatures against the traffic to determine if anything within is potentially malicious.

   #. Fix and Monitor

      Fix and monitor is not a part of the loop but should be included in any workflow we perform.
      If we make a change or fix an issue, we should continue to monitor the source for a time to
      determine if the issue has been resolved.



####

--------
Weblinks
--------

.. target-notes::