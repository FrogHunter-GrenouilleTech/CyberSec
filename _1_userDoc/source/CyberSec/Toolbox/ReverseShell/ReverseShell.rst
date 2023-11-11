.. _ref_reverseShell:

=============
Reverse Shell
=============

.. index::
   single: Reverse Shell
   single: Tools; Reverse Shell

.. contents::
    :backlinks: top

.. toctree::
   :maxdepth: 3

   Hoaxshell/Hoaxshell

####

Reverse Shell

    .. note:: 
        
        **Liens Web**
        
        * `Reverse Shell Cheat Sheet`_
    
.. _`Reverse Shell Cheat Sheet`: https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet


-----------------------------------
How to Stabilized a reverse shell ?
-----------------------------------

    .. note:: 
        
        **Liens Web**
        
        * `Stabilizing the Shell`_
    
.. _`Stabilizing the Shell`: https://jasonturley.xyz/how-to-stabilize-a-reverse-shell/

    .. note:: 
        
        This command provide a clean shell but with :

            * no tab completion
            * no history
            * no [CTRL]-c
        
        .. code:: shell
            :number-lines:
            :force:

             python -c "import pty; pty.spawn('/bin/bash')"


####

--------
Weblinks
--------

.. target-notes::