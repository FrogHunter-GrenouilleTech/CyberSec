.. _ref_Gophish:

=======
Gophish
=======

.. index::
   single: Gophish
   single: Tools; Gophish
   single: Phishing; Gophish
   single: Mail Sending Tools; Gophish

.. contents::
    :depth: 3
    :backlinks: top

####


    .. note:: 
        
        **Liens Web**
        
            official website :
        
                * `Gophish Framework (official page)`_
                * `Gophish github`_

            tuto video :
                
                * `How To Setup GoPhish Phishing - Working 2023 using gmail - yt`_
                * `Tutoriel Gophish : créer sa campagne de phishing ! - yt`_

            Templates :

                * `GoPhish-Templates`_
                * `Phishing Templates`_
                * `Phishing Email Templates`_ 
                * `Phishing Templates - Landing page`_ 
                
            User Help :
                * `Adopter les bons réflexes face au phishing`_
                * `Conseils de prévention du phishing`_

            Misc :
        
                * `ngrok - web url genrator for localhost`_
                
                
.. _`Conseils de prévention du phishing`: https://www.kaspersky.fr/resource-center/preemptive-safety/phishing-prevention-tips
.. _`Adopter les bons réflexes face au phishing`: https://www.premiers-clics.fr/cours-informatique/protection-phishing-le-comportement-a-adopter/
.. _`Phishing Email Templates`: https://caniphish.com/free-phishing-test/phishing-email-templates
.. _`Phishing Templates - Landing page`: https://github.com/An0nUD4Y/blackeye/tree/master/sites
.. _`Tutoriel Gophish : créer sa campagne de phishing ! - yt`: https://www.youtube.com/watch?v=Tdpzi8M3Vtw
.. _`GoPhish-Templates`: https://github.com/FreeZeroDays/GoPhish-Templates/blob/master/Landing_Pages/O-Three-Sixty-Five_Landing_Page.html
.. _`How To Setup GoPhish Phishing - Working 2023 using gmail - yt`: https://www.youtube.com/watch?v=iRY9CVsCggg 
.. _`ngrok - web url genrator for localhost`: https://ngrok.com/
.. _`Gophish Framework (official page)`: https://getgophish.com/
.. _`Gophish github`: https://github.com/gophish/gophish
.. _`Phishing Templates`: https://github.com/criggs626/PhishingTemplates

####

------------------------------------------------
How to set up GoPhish to evade security controls
------------------------------------------------

    .. note:: 
        
        **Liens Web**

        * `Never had a bad day phishing. How to set up GoPhish to evade security controls.`_
        * `sneaky_gophish - Github`_
        
        .. _`sneaky_gophish - Github`: https://github.com/puzzlepeaches/sneaky_gophish

.. _`Never had a bad day phishing. How to set up GoPhish to evade security controls.`: https://www.sprocketsecurity.com/resources/never-had-a-bad-day-phishing-how-to-set-up-gophish-to-evade-security-controls

The article provides tips on configuring GoPhish to evade security controls and increase the
effectiveness of phishing campaigns. Key points:

    * Use valid SSL certificates to avoid warnings. Let's Encrypt is a good free option.

    * Configure email settings properly - use SMTP relay rather than SMTP server, authenticate with
      username/password rather than API key.

    * Make sure landing pages are reachable - use ngrok to tunnel traffic.

    * Fingerprint landing pages to mimic target sites and avoid detection.

    * Redirect to real sites after login to avoid suspicion.

    * Use realistic email templates - clone target emails/sites. 

    * Personalize emails with target details.

    * Test extensively and refine based on results.

        .. note:: 
            
            **Sneaky GoPhish Container**

            To run Gophish in Docker:
            
            .. code:: shell
                :number-lines:
                :force:
    
                 docker run -p 3333:3333 -p 8080:80 -v gophish-data:/gophish gophish/gophish
    
            This will start the Gophish web interface on port 3333 and the landing pages on
            port 8080, persisting data to a volume called gophish-data.

.. _`Gophish Docker`: https://hub.docker.com/r/gophish/gophish


####

--------
Weblinks
--------

.. target-notes::