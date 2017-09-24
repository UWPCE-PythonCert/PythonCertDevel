Functions
=========

We have seen some of the building blocks of programs such as basic data structures, conditional flow control statements like ``if`` and looping constructs such as ``while`` and ``for``. We can do quite a lot with these constructs alone.

Take a moment to think about what your programs will look like using only these constructs. If you are relatively new to programming this should be easy. If you've been around for awhile, you may need to forget some of what you already know for this thought experiment to work.

Using only the basic building blocks you start at the top of your program and work your way to the bottom. You likely define a few variables early on. From there you might have an ``if`` statement that conditionally executes some code block rather than some other code block. Beyond that perhaps you iterate over a list with a ``for`` loop. Maybe you load data from a database into a list of tuples and iterate over those, printing to the console the interesting bits. At the end it might be nice to print 'Done!'

Think about this in its general form. Where does execution begin and where does it end? What happens if you find yourself repeating the same code, the same series of statments, in several ``while`` or ``for`` loops. What happens if you need to change the code in one of the loops, say in response to a change in the fields returned from your database, yet forget to change the corresponding code in all of the loops?

Without a higher level construct to help organize our code it will be closer to a script than a program. Scripts are common in the automation of systems-level tasks, the type of programming used regularly by Systems Administrators and Devops Developers. To move beyond scripts we need functions.

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

Functions can have default values for arguments so that the caller can neglect to specify certain arguments and yet get reasonable defaults.

.. code-block:: ipython

	In [12]: def add(x, y=0, z=0):
	    ...:     return x + y + z
	    ...:

	In [13]: add(3)
	Out[13]: 3

	In [14]: add(3, 2)
	Out[14]: 5

	In [15]: add(3, 2, 1)
	Out[15]: 6

We snuck in an interesting and usefule feature of functions in Python: key word arguments which are often called kwargs for short. The second and third arguments to our function above have names. The first named or key word argument is ``y`` and the second is ``z``. This allows the caller to specify them by name rather than by position so that they can be called in any order. For instance, ``z`` can be specified before ``y``.

.. code-block:: ipython

	In [16]: add(0, z=1, y=2)
	Out[16]: 3

Kwargs also allow the caller to skip unneeded arguments and rely instead on their defaults.

.. code-block:: ipython

	In [17]: add(0, z=1)
	Out[17]: 1

Note however, that positional arguments cannot be skipped. In this simple case we have only one positional argument ``x`` which Python will not permit us to ignore.

.. code-block:: ipython

    In [18]: add(y=2, z=3)
    -------------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call     last)
    <ipython-input-18-5b53a9942d6b> in <module>()
    ----> 1 add(y=2, z=3)

    TypeError: add() missing 1 required positional argument: 'x'

Functions can also take zero arguments and return nothing.

.. code-block:: ipython

    def sayHello():
        print("Hello")

Scope
-----

Related Topics
==============

Functions within Functions

