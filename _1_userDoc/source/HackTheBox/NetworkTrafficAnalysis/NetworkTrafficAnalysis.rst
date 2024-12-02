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

--------------------
The Analysis Process
--------------------

Traffic Analysis is a **detailed examination of an event or process**, determining its origin and
impact, which can be used to trigger specific precautions and/or actions to support or prevent
future occurrences.

With network traffic, this means breaking down the data into understandable chunks, examining it for
anything that deviates from regular network traffic, for potentially malicious traffic such as
unauthorized remote communications from the internet over RDP, SSH, or Telnet, or unique instances
preceding network issues. While performing our analysis, we are also looking to see what the trends
look like within the traffic and determine if it matches a baseline of typical operational traffic.

Descriptive Analysis
====================

Descriptive analysis is an essential step in any data analysis. It serves to describe a data set
based on individual characteristics. It helps to detect possible errors in data collection and/or
outliers in the data set.

   .. note::

       #. What is the issue?
           * Suspected breach? Networking issue?
       
       #. Define our scope and the goal. (what are we looking for? which time period?)
           * Target: multiple hosts potentially downloading a malicious file from bad.example.com
           * When: within the last 48 hours + 2 hours from now.
           * Supporting info: filenames/types 'superbad.exe' 'new-crypto-miner.exe'

       #. Define our target(s) (net / host(s) / protocol)
           * Scope: 192.168.100.0/24 network, protocols used were HTTP and FTP.

Using our workflow, we will determine our issue, what we are looking for, when, and where to find
it. Descriptive analysis covers these critical concepts for our analysis.

Diagnostic Analysis
===================

Diagnostic analysis clarifies the causes, effects, and interactions of conditions. It provides
insights that are obtained through correlations and interpretation. Characteristic here is a
backward-looking view, as in the closely related descriptive analytics, with the subtle difference
that it tries to find reasons for events and developments.

   .. note::

    #. Capture network traffic
        * Plug into a link with access to the 192.168.100.0/24 network to capture live traffic to
          try and grab one of the executables in transfer. See if an admin can pull PCAP and/or
          netflow data from our SIEM for the historical data.

    #. Identification of required network traffic components (filtering)
        * Once we have traffic, filter out any packets not needed for this investigation to include;
          any traffic that matches our common baseline and keep anything relevant to the scope of
          the investigation. For example, HTTP and FTP from the subnet, anything transferring or
          containing a GET request for the suspected executable files.

    #. An understanding of captured network traffic
        * Once we have filtered out the noise, it is time to dig for our targets—filter on things
          like ftp-data to find any files transferred and reconstruct them. **For HTTP**, we can
          filter on **http.request.method == "GET"** to see any GET requests that match the
          filenames we are searching for. This can show us who has acquired the files and
          potentially other transfers internal to the network on the same protocols.

By capturing traffic around the source of our issue, clearing out any known good data, and then
taking the time to inspect and understand what is left, we can determine if it is the cause of our
problem. In doing so, we just performed diagnostic analysis. We are validating the cause of our
problems and examining the events surrounding them.

Predictive Analysis
===================

By evaluating historical and current data, predictive analysis creates a predictive model for future
probabilities. Based on the results of descriptive and diagnostic analyses, this method of data
analysis makes it possible to identify trends, detect deviations from expected values at an early
stage, and predict future occurrences as accurately as possible.

   .. note::

      #. Note-taking and mind mapping of the found results
          
          * Annotating everything we do, see, or find throughout the investigation is crucial.
            Ensure we are taking ample notes, including:
               
               * Timeframes we captured traffic during.
               * Suspicious hosts within the network.
               * Conversations containing the files in question. ( to include timestamps and packet
                 numbers)

      #. Summary of the analysis (what did we find?)

          * Finally, summarize what we have found explaining the relevant details so that superiors
            can decide to quarantine the affected hosts or perform more significant incident
            response.

          * Our analysis will affect decisions made, so it is essential to be as clear and concise
            as possible.

By performing an evaluation of the data we have found, comparing it to our baseline traffic, and
known bad data such as markers of infiltration or exploitation (like signatures for viruses and
other hacking tools), we are performing Predictive Analysis. In this process, we paint a clear
picture so that appropriate actions can be taken in response.

Prescriptive Analysis
=====================

Prescriptive analysis aims to narrow down what actions to take to eliminate or prevent a future
problem or trigger a specific activity or process. Using the results of our workflow, we can make
sound decisions as to what actions are required to solve the problem and prevent it from happening
again. To prescribe a solution is the culmination of this workflow.

Once done and the problem is solved, it is prudent to reflect on the entire process and develop
lessons learned. These lessons, when documented, will enable us to make our processes
stronger—document what was done correctly, what actions failed to help, and what could improve.

Often this process is not a once-and-done kind of thing. It is usually cyclic, and we will need to
rerun steps based on our analysis of the original capture to build a bigger picture. This could have
been a much larger attack than what is in the examples. Suppose a full-scale incident response is
deemed necessary. In that case, we may have to reanalyze the PCAP previously captured to look at
any conversations that involve the affected hosts within several minutes of the executable transfer
to ensure it did not spread over another route, as an example.

Key Components of an Effective Analysis
=======================================

   :Know your environment:

      There are several key components to perform traffic analysis effectively. First, know the
      environment. If we are unsure if a host belongs in the network, how can we determine if it is
      rogue or not? Keeping asset inventories and network maps is vital. These will aid in the
      analysis process.


   :Placement is Key:

      The placement of our host for capturing traffic is a critical thing. Closest to the source of
      the issue is the ideal placement of our capturing tool. If the traffic in question is coming
      from the internet, listening to the inbound links is a great way to see the complete picture.
      It is as close to the source as we, the administrators, can get. If the problem seems to be
      isolated to one host on our internal network, try placing the capture tools in the same
      segment as the problem host and see what traffic is happening within the segment.

   :Persistence:

      The issue will not always be easy to spot. It may not even be a frequent event on the network.
      For example, an attacker's Command and Control server reaching out to the victim's computers
      may only happen on a time interval of once every several hours, or even once a day or less.
      This means that if we did not catch it the first time around, it might be a while before it
      appears in our logs. Don't lose the drive to find the problem. It could mean the difference
      between stopping the attacker and a full-scale breach like a ransomware attack.

Analysis Approach
=================

   * **Start with standard protocols first** and work our way into the austere and specific only to
     the organization.

     Most attacks will come from the internet, so it has to access the internal net somehow. This
     means there will be traffic generated and logs written about it. HTTP/S, FTP, E-mail, and basic
     TCP and UDP traffic will be the most common things seen coming from the world. Start at these
     and clear out anything that is not necessary to the investigation. After these, check standard
     protocols that allow for communications between networks, such as SSH, RDP, or Telnet.
     
     When looking for these types of anomalies, be mindful of the security policy of the network.
     Does our organization's security plan and implementations allow for RDP sessions that are
     initiated outside the enterprise? What about the use of Telnet?

   * **Look for patterns.**

     Is a specific host or set of hosts checking in with something on the internet at the same time
     daily? This is a typical Command and Control profile setup that can easily be spotted by
     looking for patterns in our traffic data.

   * **Check anything host to host within our network.**

     In a standard setup, the user's hosts will rarely talk to each other. So be suspicious of any
     traffic that appears like this. Typically hosts will talk to infrastructure for IP address
     leases, DNS requests, enterprise services and to find its route out. We will also see hosts
     talking with local webservers, file shares, and other critical infrastructure for the
     environment to function like Domain controllers and authentication apps.

   * **Look for unique events.**

     Things like a host who usually visits a specific site ten times a day changing its pattern and
     only doing so once is curious.
     
     Seeing a different User-Agent string not matching our applications or hosts talking to a server
     out on the internet is also something to be concerned with.
     
     A random port only being bound once or twice on a host is also of note. This could be an
     opening for things like C2 callbacks, someone opening a port to do something non-standard, or
     an application showing abnormal behavior. In large environments, patterns are expected, so
     anything sticking out warrants a look.


####

--------
Weblinks
--------

.. target-notes::