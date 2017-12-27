.. _exercise_string_formatting:

##########################
String Formatting Exercise
##########################

Goal
====
In this excercise we will reinforce the important concepts of string formatting, so that these start to become second nature!

Procedure
=========
Being sure to follow all the steps described in Procedure at:

https://canvas.uw.edu/courses/1200526/assignments/3970003?module_item_id=7963708

but this time, creating a new file called stringf_lab.py in your student dir in the class repo.

When the empty script is available and runnable, complete the following tasks.


Task One
--------
* Write a format string that will take the tuple:

    ``( 2, 123.4567, 10000, 12345.67)``

    and produce:

    ``'file_002 :   123.46, 1.00e+04, 1.23e+04'``

1) The idea behind the "file_002" is that if you have a bunch of files that you want to name with numbers that can be sorted, you need to "pad" the numbers with zeros to get the right sort order.


**Example:**

.. code-block:: ipython

    In [10]: fnames = ['file1', 'file2', 'file10', 'file11']
    In [11]: fnames.sort()
    In [12]: fnames
    Out[12]: ['file1', 'file10', 'file11', 'file2']

That is probably not what you want. However:

.. code-block:: ipython

    In [1]: fnames = ['file001', 'file002', 'file010', 'file011']
    In [3]: sorted(fnames)
    Out[3]: ['file001', 'file002', 'file010', 'file011']

That works!

So you want to find a string formatting operator that will "pad" the number with zeros for you.

2) The second element is a floating point number. You should display it with 2 decimal places shown.

3) The third value is an integer, but could be any number. You should display it in scientific notation, with 2 decimal places shown.

4) The fourth value is a float with a lot of digits -- display it in scientific notation with 3 significant figures.

Task Two
--------
Dynamically Building up format strings
--------------------------------------

* Rewrite:

``"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)``

To take an arbitrary number of values.

Trick: You can pass in a tuple of values to a function with a ``*``:

.. code-block:: ipython

    In [52]: t = (1,2,3)

    In [53]: "the 3 numbers are: {:d}, {:d}, {:d}".format(*t)
    Out[53]: 'the 3 numbers are: 1, 2, 3'

The idea here is that you may have a tuple of three numbers, but might also have 4 or 5 or....

So you can dynamically build up the format string to accommodate the length of the tuple.

The string object has the ``format()`` method, so you can call it with a string that is bound to a name, not just a string literal. For example:

.. code-block:: ipython

    In [16]: form_string = "{:d}, {:d}"

    In [17]: nums = (34, 56)

    In [18]: fstring.format(*nums)
    Out[18]: '34, 56'

So how would you make a form_string that was the right length for an arbitrary tuple?


Put your code in a function that will return the final string like so:

.. code-block:: ipython

    In [20]: formatter((2,3,5))
    Out[20]: 'the 3 numbers are: 2, 3, 5'

    In [21]: formatter((2,3,5,7,9))
    Out[21]: 'the 5 numbers are: 2, 3, 5, 7, 9'

It will look like:

.. code-block:: python

  def formatter(in_tuple):
      do_something_here_to_make_a_format_string

      return form_string.format(in_tuple)


Task Three
----------

Task Four
---------


Tests
-----



Building up strings
===================


For reference:

The official reference docs:

https://docs.python.org/3/library/string.html#format-string-syntax

And a more human-readable intro:

https://pyformat.info/

And a nice "Cookbook":

https://mkaz.tech/python-string-format.html

