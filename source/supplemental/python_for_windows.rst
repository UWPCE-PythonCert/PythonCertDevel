.. _python_for_windows:

****************************
Setting up Python on Windows
****************************

==================
Getting The Tools
==================

Python
-------

There are a number of python distributions available -- many designed for easier support of scientific programming:

- Anaconda
- Enthought Canopy
- Python(x,y)

But for core use, the installer from python.org is the way to go:

https://www.python.org/downloads/

You want the installer for Python 3.x -- probably 64 bit, though if you have a 32 bit system, you can get that. There is essentially no difference for the purposes of this course.

Double click and install.


Terminal
---------

If you are confident in your use of the "DOS Box" or "powershell", feel free to use one of those. However, your life may be easier if you install "Git Bash", as then you can follow unix-style terminal instructions exactly, and do not have to translate. Also, your instructors are more experienced with Bash.
From now on, if you hear the terms 'bash', 'shell' or 'terminal', know that this is the application that is being referred to.

When you install Git Bash, you are installing git (and a git gui) as well, thus killing two birds with one stone!

https://git-for-windows.github.io/

This is actually your best bet for running Python also -- If you use the Git Bash shell, you can use the same commands as Linux and OS-X users. Regardless of which shell you choose, you will need to add Python to your environment. It is possible that this was done during the installation of python. If you type 'which python' into your terminal, and get back the answer '/c/python34/python', then you are good to go, otherwise, follow the instructions here:

http://www.computerhope.com/issues/ch000549.htm

Based on the subversion of Python you will want to add something like:

``C:\Python36``

and

``C:\Python36\Scripts``

to ``PATH``


git
----

If you installed Git Bash, you will already have git, both usable in the terminal and as a gui, and can safely skip this section. If not, you still need a git client. You can use the above link and install git (it will install the bash shell as well, of course, but you can use your shell of choice instead).

There is also TortoiseGit:

https://code.google.com/p/tortoisegit/

which integrates git with the file manager. Feel free to use this if you already have an understanding of how git works, but for the purposes of learning, it may be better to use a command line client (git Bash above).

pip
---

``pip`` is the Python package installer. It is updated faster than python itself, so once you have python you want to get the latest version of pip working::

  $ python -m ensurepip --upgrade

It should download and install the latest ``pip``.

You can now use pip to install other packages.

iPython
--------

One extra package we are going to use in class is ``iPython``::

  $ pip install ipython[all]

You should now be able to run ``iPython`` from the git bash shell::

    $ ipython
    Python 3.6.2 (v3.6.2:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)]

    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.


(or from the DOS box or PowerShell prompt)

We will use this as our default python interpreter.
