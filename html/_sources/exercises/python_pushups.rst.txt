.. _python_pushups:

##############
Python Pushups
##############

These are a couple exorcises to kick you off with Python

Task 1
======

Make sure you have a working development environment.

**Linux:** ::ref:`python_for_linux`

**OS-X:** ::ref:`python_for_mac`

**Windows:** ::ref:`python_for_windows`

The following commands should all run on the command line::

   python --version
   python -m pip --version
   ipython --version
   git --version

Task 2
======

Set Up a Great Dev Environment
------------------------------

Make sure you have the basics of command line usage down:

Work through the supplemental tutorials on setting up your
Command Line (::ref:`shell_customization`) for good development support.

Make sure you've got your editor set up productively -- at the *very* *very*
least, make sure it does Python indentation and syntax coloring well.

**Advanced Editor Setup:**

If you are using SublimeText, here are some notes to make it super-nifty:

:ref:`sublime_as_ide`

If you are using Atom, here are some more instructions:

:ref:`atom_as_ide`

At the end, your editor should support tab completion and pep8 and pyflakes (flake8)
linting.

If you are not using SublimeText, look for plugins that accomplish the same
goals for your own editor.  If none are available, please consider a change of
editor.


Task 3: Python Pushups
======================



To get a bit of exercise solving some puzzles with Python, work on the Python
exercises at "Coding Bat": http://codingbat.com/python

There are 8 sets of puzzles. Do as many as you can, but try to at least
get all the "Warmups" done.


Task 4: Explore Errors
======================

* Create a new directory in your working dir for the class::

  $ mkdir session01
  $ cd session01

* Add a new file to it called ``break_me.py``

* In the ``break_me.py`` file write four simple Python functions:

  * Each function, when called, should cause an exception to happen

  * Each function should result in one of the four most common exceptions you'll find.

  * for review: ``NameError``, ``TypeError``, ``SyntaxError``, ``AttributeError``

(hint -- the interpreter will quit when it hits a Exception -- so you can comment out all but the one you are testing at the moment)

  * Use the Python standard library reference on `Built In Exceptions <https://docs.python.org/3/library/exceptions.html>`_ as a
    reference

