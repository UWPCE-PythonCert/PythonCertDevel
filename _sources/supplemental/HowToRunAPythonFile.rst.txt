How to run a python file
========================

A file with python code in it is a 'module' or 'script'

(more on the distinction later on...)

It should be named with the ``.py`` extension: ``some_name.py``

To run it, you have a couple options:

1) call python on the command line, and pass in your module name

.. code-block:: bash

  $ python the_name_of_the_script.py

2) On \*nix (linux, OS-X, Windows bash), you can make the file "executable"::

       chmod +x the_file.py

   And make sur it has a "shebang" line at the top::

       #!/usr/bin/env python

   Then you can run it directly::

       ./the_file.py

3) run ``iPython``, and run it from within iPython with the ``run`` command

.. code-block:: ipython

  In [1]: run the_file.py

.. ifslides::

    .. rst-class:: centered

        [demo]
