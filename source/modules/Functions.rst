Functions
=========

We have seen some of the building blocks of programs such as basic data structures, conditional flow control statements like ``if`` and looping constructs such as ``while`` and ``for``. We can do quite a lot with these constructs alone.

Take a moment to think about what your programs will look like using only these constructs. If you are relatively new to programming this should be easy. If you've been around for awhile, you may need to forget some of what you already know for this thought experiment to work.

Using only the basic building blocks you start at the top of your program and work your way to the bottom. You likely create a few symbol definitions early on, perhaps set some of them based on command line inputs. From there you might have an ``if`` statement that conditionally executes some code block rather than some other code blok. Beyond that perhaps you iterate over a list with a ``for`` loop. Maybe you load data from a database into a list of tuples and iterate over those, printing to the console the interesting bits. At the end it might be nice to print 'Done!'

Think about this in its general form. Where does execution begin and where does it end? What happens if you find yourself repeating the same code, the same series of statments, in several ``while`` or ``for`` loops. What happens if you need to change the code in one of the loops, say in response to a change in the fields returned from your database, yet forget to make a change the corresponding code in all of the loops?





.. code-block:: python

	''' docstring placeholder '''
	pass

.. code-block:: python

    def addOne(x):
        return x + 1


.. code-block:: python

    def add(x, y):
    	return x + y


Arguments
---------


Return Values
-------------


Arity and Function Signatures
-----------------------------

Scope
-----



