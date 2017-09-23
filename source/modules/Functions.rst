Functions
=========

We have seen some of the building blocks of programs such as basic data structures, conditional flow control statements like ``if`` and looping constructs such as ``while`` and ``for``. We can do quite a lot with these constructs alone.

Take a moment to think about what your programs will look like using only these constructs. If you are relatively new to programming this should be easy. If you've been around for awhile, you may need to forget some of what you already know for this thought experiment to work.

Using only the basic building blocks you start at the top of your program and work your way to the bottom. You likely create a few symbol definitions early on, perhaps set some of them based on command line inputs. From there you might have an ``if`` statement that conditionally executes some code block rather than some other code blok. Beyond that perhaps you iterate over a list with a ``for`` loop. Maybe you load data from a database into a list of tuples and iterate over those, printing to the console the interesting bits. At the end it might be nice to print 'Done!'

Think about this in its general form. Where does execution begin and where does it end? What happens if you find yourself repeating the same code, the same series of statments, in several ``while`` or ``for`` loops. What happens if you need to change the code in one of the loops, say in response to a change in the fields returned from your database, yet forget to make a change the corresponding code in all of the loops?

What we have without a higher level construct to help organize our code is closer to a script than a program. Scripts are common in the automation of systems level tasks, the type of programming used regularly by Systems Administrators and Devops Developers. To move beyond scripts we need functions.

Basic Function Definition
-------------------------

The basice form of a function is a ``def`` statment, followd by the name of the function ``addOne`` followed by an argument list ``(x)`` and finally a colon, ``:``. All of this is typically on the first line of the function definition. Then within the function are all of the statements and expressions that do the work of the function ``result = x + 1`` and finally a return value ``return result``.

.. code-block:: python

    def addOne(x):
    	result = x + 1
        return result

In simple cases such as this all of the work of the function can be done on the return line which eliminates a name ``result`` and makes the function easier to read.

.. code-block:: python

	def addOne(x):
		return x + 1

Arguments
---------

Functions can take more than a single argument.

.. code-block:: python

    def add(x, y):
    	return x + y

.. code-block:: python

    def add(x, y, z):
    	return x + y + z

Functions can have defaults values for arguments so that the caller can neglect to specify certain arguments yet get reasonable defaults.

.. code-block:: python

In [12]: def add(x, y=0, z=0):
    ...:     return x + y + z
    ...:

In [13]: add(3)
Out[13]: 3

In [14]: add(3, 2)
Out[14]: 5

In [15]: add(3, 2, 1)
Out[15]: 6




Return Values
-------------


Arity and Function Signatures
-----------------------------

Scope
-----


Related Topics
==============

Functions within Functions

