Homework Session01
==================

Tasks and reading by next week


Task 1
------

Make sure you have a working development environment.

**Linux:** ::ref:`python_for_linux`

**OS-X:** ::ref:`python_for_mac`

**Windows:** ::ref:`python_for_windows`


Task 2
------

**Set Up a Great Dev Environment**

Make sure you have the basics of command line usage down:

Work through the supplemental tutorials on setting up your
Command Line (::ref:`shell_customization`) for good development support.

Make sure you've got your editor set up productively -- at the very very
least, make sure it does Python indentation and syntax coloring well.

.. nextslide::

**Advanced Editor Setup:**

If you are using SublimeText, here are some notes to make it super-nifty:

::ref:`sublime_as_ide`

At the end, your editor should support tab completion and pep8 and pyflakes
linting.

If you are not using SublimeText, look for plugins that accomplish the same
goals for your own editor.  If none are available, please consider a change of
editor.


Task 3
------

**Python Pushups**

To get a bit of exercise solving some puzzles with Python, work on the Python
exercises at "Coding Bat": http://codingbat.com/python

There are 8 sets of puzzles. Do as many as you can, but try to at least
get all the "Warmups" done.


Task 4
------

**Explore Errors**

* Create a new directory in your working dir for the class::

  $ mkdir session01
  $ cd session01

* Add a new file to it called ``break_me.py``

* In the ``break_me.py`` file write four simple Python functions:

  * Each function, when called, should cause an exception to happen

  * Each function should result in one of the four common exceptions from our
    lecture.

  * for review: ``NameError``, ``TypeError``, ``SyntaxError``, ``AttributeError``

(hint -- the interpreter will quit when it hits a Exception -- so you can comment out all but the one you are testing at the moment)

  * Use the Python standard library reference on `Built In Exceptions`_ as a
    reference

.. _Built In Exceptions: https://docs.python.org/3/library/exceptions.html


Reading, etc.
-------------

Every one of you has a different backgrond and learning style.

So take a bit of time to figure out which resource works for you.

:ref:`python_learning_resources` provides some options. Do look it over.

But here are few to get you started this week:

*Think Python:* Chapters 1–7 (http://greenteapress.com/thinkpython2/)

*Dive Into Python:* Chapters 1–2 (http://www.diveintopython3.net/)

*LPTHW:* ex. 1–10, 18-21 (http://learnpythonthehardway.org/book/)
  **NOTE:** LPTHW is python 2 -- you will need to add parentheses to all yoru print calls!

Or follow this excellent introductory tutorial:

http://pyvideo.org/video/1850/a-hands-on-introduction-to-python-for-beginning-p

(also python2 -- so same thing with the print function...)

You should be comfortable with working with variables, numbers, strings, and basic functions.

git
---

We'll be covering the basics of git next week - enough to use for this class. Please read one of these so you'll have a head start:

http://rogerdudler.github.io/git-guide/

or

https://try.github.io/levels/1/challenges/1


Next Class
----------

Next week, we will:

 * get set up with git
 * Some more basic Python
 * More on Functions
 * Boolean Expressions
 * Code Structure, Modules, and Namespaces

