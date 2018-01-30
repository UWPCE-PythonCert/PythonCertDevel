:orphan:

.. _pep8:


########################
Coding Style and Linting
########################

System Development with Python

- Maria McKinley

``mariak@mariakathryn.net``

pep-8
-----

Style Guide for Python

Defines a good baseline for your own local style guide

The 'rules' are just suggestions. From the document:

    most importantly: know when to be inconsistent -- sometimes the
    style guide just doesn't apply

important-pep-8-recommendations
-------------------------------

-  http://legacy.python.org/dev/peps/pep-0008/#tabs-or-spaces
-  Use 4 space indents. The tabs vs. spaces wars will likely never
   completely come to peaceful conclusion. But the Python community has
   standardized on 4 space indents. Unless you have compelling reasons
   not to, you should too.
-  Python 3 disallows mixing of tabs and spaces. With Python 2, you can
   run with the -tt flag which will force errors on mixed use of tabs
   and spaces.
-  Let your editor help you by having it insert 4 spaces for the tab
   key, turning on visible whitespace markers, and/or integrating a
   PEP-8 plugin

-  http://legacy.python.org/dev/peps/pep-0008/#maximum-line-length
-  Maximum line length of 79 characters
-  This is an easy one to let run away early. If 79 characters is too
   short, find a line length your team can agree on and stick to it as
   specified in PEP-8

pep-8-recommendations-continued
-------------------------------

-  http://legacy.python.org/dev/peps/pep-0008/#source-file-encoding
-  The default encoding in Python 2 is ASCII, in Python 3 it is UTF-8.
-  If you insert a non encodable character in a string literal, the
   interpreter will throw a SyntaxError when it reaches it.
-  To change the file encoding to UTF-8 for example, insert

   ::

       # coding: utf-8

   near the top of the file (see examples/encoding.py)


-  When comparing with singletons such as None, use "x is None", not "x == None". `Why? <http://jaredgrubb.blogspot.com/2009/04/python-is-none-vs-none.html>`__


naming-conventions
------------------

-  variables, attributes, and modules names should be lowercase, with
   words separated by underscores
-  class names should be CamelCase, aka StudlyCaps
-  constants should be ALL CAPS

argument-conventions
--------------------

-  instance methods should have a first argument called self
-  class methods should have a first argument called cls
-  There's nothing magic about these names. You don't have to use this
   convention, but not adopting it will likely confuse future readers

imports
-------

-  `imports <http://legacy.python.org/dev/peps/pep-0008/#imports>`__
   should be near the top of the file
-  imports should be grouped in the following order, separated by a
   blank line:

   #. standard library imports
   #. related third party imports
   #. local application/library specific imports

-  avoid wildcard imports to keep the namespace clean for both humans
   and automated tools


public and non-public class members
-----------------------------------

Python does not have a mechanism for restricting access to a variable or method, but it does have culture and convention.

The default is public. This works for most things.

If you do not want people to change your attribute or method, and especially if you do not want people to depend on this attribute or method always remaining the same, make it private by using a single underscore in front.

_my_private_method

If you are particularly paranoid:
A non-public attribute has two leading underscores and no trailing
underscores and triggers Python's name mangling.

__my_paranoid_method

tools-to-help
-------------

-  `pyflakes <https://pypi.python.org/pypi/pyflakes>`__ - searches for
   bugs, but without importing modules
-  `Pylint <http://www.pylint.org/>`__ - style guide, searches for bugs
-  `pycodestyle <https://pypi.python.org/pypi/pycodestyle>`__ - tests conformance to
   PEP-8
-  `flake8 <https://pypi.python.org/pypi/flake8>`__ combines pyflakes,
   pycodestyle, and mccabe, a code complexity analyzer


pylint
------

Interesting options:

::

    -d (msg ids), --disable=(msg ids)      Disable the messages identified in the messages table
    --generate-rcfile/--rcfile             Saves/restores a configuration

Poor code example examples/Listing1.py was adapted from `Doug
Hellman <http://doughellmann.com/2008/03/01/static-code-analizers-for-python.html>`__

What can you spot as an error, bad practice, or poor style?

Now let's see what pylint Listing1.py has to say


pyflakes
--------

Doesn't check style, just checks for functional errors, but does not run code.

Now let's see what pyflakes Listing1.py has to say

How much overlap with pylint?


pycodestyle
-----------

used to be called "pep8"

Only checks style

Interesting options:

::

    --statistics         count errors and warnings
    --count              print total number of errors and warnings to standard error and set exit code to 1 if total is not null

Now let's see what pycodestyle Listing1.py has to say

What's the overlap in pycodestyle's output versus the other two tools?

flake8
------

A tool which wraps pycodestyle, pyflakes, and mccabe

`mccabe <http://nedbatchelder.com/blog/200803/python_code_complexity_microtool.html>`__
is a "microtool" written by Ned Batchelder (author of coverage) for
assessing `Cyclomatic
Complexity <http://en.wikipedia.org/wiki/Cyclomatic_complexity>`__

Interesting options:

::

    --max-complexity=N    McCabe complexity threshold

Now let's see what flake8 Listing1.py has to say

What's the overlap in flake8 output versus the other tools?

analyzing-a-larger-codebase-in-the-wild
---------------------------------------

::

    cd $HOME/virtualenvs/uwpce/lib/python3.5/site-packages

    flake8 django

    pylint django

code-analysis-tool-battle-royale
--------------------------------

::

    pylint flake8
    flake8 pylint

analysis-tool-summary
---------------------

-  There is no magic bullet that guarantees functional, beautiful code
-  Some classes of programming errors can be found before runtime
-  With the PEP-8 tools, it is easy to let rules such as line length
   slip by
-  It's up to you to determine your thresholds
