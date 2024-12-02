=======
MailHog
=======

.. index::
   single: MailHog
   single: Tools; MailHog
   single: Mail Sending Tools; MailHog

.. contents::
    :depth: 3
    :backlinks: top

####

-------
MailHog
-------

    .. note:: 
        
        **Liens Web**

        * `MailHog - github`_
        * `MailHog - docker`_
        * `Deploying MailHog`_
        
.. _`Deploying MailHog`: https://github.com/mailhog/MailHog/blob/master/docs/DEPLOY.md
.. _`MailHog - docker`: https://registry.hub.docker.com/r/mailhog/mailhog/
.. _`MailHog - github`: https://github.com/mailhog/MailHog

MailHog is an **email testing tool** that catches emails sent from your local machine without
sending them to the intended recipient. It provides a web interface to view and test emails captured.

    .. note:: 
        
        **Key features**

            * Catches outgoing email for testing instead of sending to recipient
            * Web interface to view and test captured emails
            * Open source tool written in Go
            * Available as executable binary or Docker image
            * Useful for testing email in development environments

how to use MailHog with GoPhish ?
=================================

    .. note:: 
        
        use MailHog with GoPhish for testing phishing emails:

            #. Install MailHog on the same server as GoPhish.

            #. Configure GoPhish to use MailHog as the SMTP server.

                * Edit config.json in the GoPhish root folder
                * Set the SMTP host to the IP address of the server running MailHog

            .. code:: json
                :number-lines:
                :force:

                "smtp_host": "localhost", 
                "smtp_port": 1025,
                "smtp_user": "",
                "smtp_pass": ""

            #. Start MailHog so it is running on port 1025.

            #. Start GoPhish and it will now send emails to MailHog instead of an external SMTP server.

            #. View and test the phishing emails in the MailHog UI at http://server-ip:8025.

        This allows you to test the phishing emails locally without sending them externally.
        You can inspect the contents, headers, links etc to verify they are as expected.

            #. Optionally forward emails from MailHog to real inboxes by configuring the SMTP
               relay in MailHog to send to an external SMTP server.

        So in summary, using MailHog with GoPhish provides a convenient way to test and debug
        phishing emails locally before sending real phishing campaigns. The integration
        is seamless.








####

--------
Weblinks
--------

.. target-notes::