.. _setting_up_dev_environment:

###############################################
Setting Up A Development Environment For Python
###############################################

The following is the recommended setup for the UWPCE Python Certificate Program. It is not necessary to have exactly this same setup, but if you choose to use a different setup, we will be less able to support you if you need help.

Minimal Setup
=============

Although it is OK to use different tools, there are some requirements to successfully do the work the program requires:

1) cPython version 3.6.*
1) A way to edit python files (Programmers Text Editor)
1) A way to run your code -- command line, IDE, etc.
1) A way to use the "git" source code version control system

You can be successful in the program as long as you have the above. If you don't already have a setup that fulfills those requirements -- read on.

Platforms
---------

Python is a very platform independent system, it can run on all major Operating systems, including even micro controllers. It is most commonly used in production on Windows, Linux or OS-X systems.

For this program, we feel it is best for users to work in an environment in which they are comfortable, and which they will ultimately need to do production work.

We have included instructions for Windows, Linux and OS-X systems -- any of these are fine.

Python Itself
-------------

Python is a "byte compiled, interpreted" language. What this means to you is that you need a Python interpreter to run your Python code. It also means that that is all you need -- write some code, and run it with Python. That's it.

There are a number of different Python interpreters (or run-time environments) available:

- cPython
- PyPy
- Jython
- Iron Python
- MicroPython

These each have their own special uses for interaction with the Java VM or CLR, or running on micro controllers. But most production Python is run with the cPython interpreter, and most people mean cPython when they say "Python".

For this program, you will need cPython version 3.6, installed and running so that when you type "python" at your command line, it starts up.

cPython itself is available from a number of sources, or "distributions". We recommend the version available from python.org.

Python is also available as part of the Anaconda data analysis environment, as well as a few other sources. These Python distributions will work fine for this class, but when we get to advanced topics like virtual environments, there are some differences -- and you will be responsible for adapting to these differences.

Your Development Environment
============================

There are three basic elements to your environment when working with Python:

* The Command Line
* The Interpreter
* The Editor
* The source code revision control system

Some folks use an Integrated Development Environment (IDE), which combines some or all of these functions. For this class, we don't recommend using an IDE, because while it can makes some things easier, it also hides complication that is good to understand.

The Command Line (cli)
----------------------

Having some facility on the command line is important

Familiarity with basic use of the command line is a prerequisite for the program, so we won't cover this much in class. If you are not comfortable with the command line, please bone up on your own.

We have some resources here: :ref:`command_line_basics`

We suggest running through the **cli** tutorial at "learn code the hard way":

https://learnpythonthehardway.org/python3/appendixa.html

**Windows:**

Most of the demos in class, etc, will be done using the "bash" command line shell on OS-X. This is identical to the bash shell on Linux.

Windows provides the "DOS" command line, which is OK, but pretty old and limited, or "Power Shell" -- a more modern, powerful, flexible command shell.

If you are comfortable with either of these -- go for it.

If not, you can use the "git Bash" shell -- which is much like the bash shell on OS-X and Linux. Or, on Windows 10, look into the "bash shell for Windows" otherwise known as the "Linux subsystem for Windows" - - more info here: :ref:`windows_bash`

The Interpreter
---------------

Python comes with a built-in interpreter.

You see it when you type ``python`` at the command line:

.. code-block:: bash

  $ python
  Python 3.6.1 (v3.5.2:4def2a2901a5, Jun 26 2016, 10:47:25)
  [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>>

That last thing you see, ``>>>`` is the "Python prompt".

This is where you type code.


Python in the Interpreter
-------------------------

Try it out:

.. code-block:: python

    >>> print("hello world!")
    hello world!
    >>> 4 + 5
    9
    >>> 2 ** 8 - 1
    255
    >>> print ("one string" + " plus another")
    one string plus another
    >>>

.. nextslide:: Tools in the Interpreter

When you are in an interpreter, there are a number of tools available to
you.

There is a help system:

.. code-block:: python

    >>> help(str)
    Help on class str in module __builtin__:

    class str(basestring)
     |  str(object='') -> string
     |
     |  Return a nice string representation of the object.
     |  If the argument is a string, the return value is the same object.
     ...

You can type ``q`` to exit the help viewer.

.. nextslide:: Tools in the Interpreter

You can also use the ``dir`` builtin to find out about the attributes of a
given object:

.. code-block:: python

    >>> bob = "this is a string"
    >>> dir(bob)
    ['__add__', '__class__', '__contains__', '__delattr__',
     '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
     '__getitem__', '__getnewargs__', '__getslice__', '__gt__',
     ...
     'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines',
     'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill']
    >>> help(bob.rpartition)

This allows you quite a bit of latitude in exploring what Python is.

.. nextslide:: Advanced Interpreters

In addition to the built-in interpreter, there are several more advanced
interpreters available to you.

We'll be using one in this course called ``iPython``

More on this soon.


The Editor
----------

Typing code in an interpreter is great for exploring.

But for anything "real", you'll want to save the work you are doing in a more permanent
fashion.

This is where an Editor fits in.

.. nextslide:: Text Editors Only

Any good text editor will do.

MS Word is **not** a text editor.

Nor is *TextEdit* on a Mac.

``Notepad`` on Windows is a text editor -- but a crappy one.

You need a real "programmers text editor"

A text editor saves only what it shows you, with no special formatting
characters hidden behind the scenes.

.. nextslide:: Minimum Requirements

At a minimum, your editor should have:

.. rst-class:: build

* Syntax Colorization
* Automatic Indentation

In addition, great features to add include:

.. rst-class:: build

* Tab completion
* Code linting
* Jump-to-definition

Have an editor that does all this? Feel free to use it.

If not, we recommend ``SublimeText``:

http://www.sublimetext.com/

Use version 3.

http://uwpce-pythoncert.github.io/PythonResources/DevEnvironment/sublime_as_ide.html

"Atom" is another good open source option.

https://atom.io/

And, of course, vim or Emacs on Linux, if you are familiar with those.

Why No IDE?
-----------

An IDE does not give you much that you can't get with a good editor plus a good interpreter.

An IDE often weighs a great deal

Setting up IDEs to work with different projects can be challenging and time-consuming.

Particularly when you are first learning, you don't want too much done for you.


Why Not an IDE?
---------------

That said ...

You may want to go get the educational edition of PyCharm:

https://www.jetbrains.com/pycharm-edu/

Which is awesome.



.. toctree::
    :maxdepth: 2

    sublime_as_ide
    atom_as_ide
    command_line
    shell
    ipython
    windows_bash

    git_overview

    virtualenv

