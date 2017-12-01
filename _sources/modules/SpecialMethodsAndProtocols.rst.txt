.. _special_methods:

###########################
Special Methods & Protocols
###########################


Special methods (also called *magic* methods) are the secret sauce to Python's Duck typing.

Defining the appropriate special methods in your classes is how you make your class act like standard classes.


What's in a Name?
-----------------

We've seen at least one special method so far::

    __init__

It's all in the double underscores...

Pronounced "dunder"


try: ``dir(2)``  or ``dir(list)``


Generally Useful Special Methods
--------------------------------

Most classes should at least have these special methods:

``object.__str__``:
  Called by the str() built-in function and by the print function to compute
  the *informal* string representation of an object.

``object.__repr__``:
  Called by the repr() built-in function to compute the *official* string representation of an object.

  Ideally: ``eval( repr(something) ) == something``

  This means that the "repr" is what you type to create the object. IN practice, this is impractical for complex objects... but it is still a more "formal" form.

  Note that is you don't define a ``__str__`` method, than the __repr__ will be used. And the base class (``object``) has a __repr__ defined, so every class automatically gets one -- but it's ugly :-)


Protocols
----------

The set of special methods needed to emulate a particular type of Python object is called a *protocol*.

Your classes can "become" like Python built-in classes by implementing the methods in a given protocol.

Remember, these are more *guidelines* than laws.  Implement what you need.


The Numerics Protocol
---------------------

Do you want your class to behave like a number? Implement these methods:

.. code-block:: python

    object.__add__(self, other)
    object.__sub__(self, other)
    object.__mul__(self, other)
    object.__matmul__(self, other)
    object.__truediv__(self, other)
    object.__floordiv__(self, other)
    object.__mod__(self, other)
    object.__divmod__(self, other)
    object.__pow__(self, other[, modulo])
    object.__lshift__(self, other)
    object.__rshift__(self, other)
    object.__and__(self, other)
    object.__xor__(self, other)
    object.__or__(self, other)

(or the fraction you actually need)


Operator Overloading
--------------------

Most of the previous examples map to "operators": ``+, - , *, //, /, %`` etc. This is often known as "operator overloading", as you are redefining what the operators mean for that specific type.

Note that you can define these operators to do ANYTHING you want -- but it is a really good idea to only define them to mean something that makes sense in the usual way.

One interesting exception to this rule is the ``pathlib.Path`` class, that has defined ``__truediv__`` to mean path concatenation:

..code-block:: ipython

    In [19]: import pathlib

    In [20]: p1 = pathlib.Path.cwd()

    In [21]: p1
    Out[21]: PosixPath('/Users/Chris/PythonStuff/UWPCE/PythonCertDevel')

    In [22]: p1 / "a_filename"
    Out[22]: PosixPath('/Users/Chris/PythonStuff/UWPCE/PythonCertDevel/a_filename')

While this is not division in any sense, the slash *is* used as a path separator -- so this does make intuitive sense.


The Container Protocol
----------------------

Want to make a container type? Here's what you need:

.. code-block:: python

    object.__len__(self)
    object.__getitem__(self, key)
    object.__setitem__(self, key, value)
    object.__delitem__(self, key)
    object.__iter__(self)
    object.__reversed__(self)
    object.__contains__(self, item)
    object.__index__(self)

``__len__`` is called when len(object) is called.

``__reversed__`` is called when reversed(object) is called.

``__contains__`` is called with ``in`` is used: ``something in object``

``__iter__`` is used for iteration -- called when in a for loop.

``__index__`` is used to convert the object into an integer for indexing. If you have a class that could reasonably be interpreted as in index, you should define this, and it can be used as in index. It should return an integer.  This was added to support multiple integer types for numpy.


An Example
----------

Each of these methods supports a common Python operation.

For example, to make '+' work with a sequence type in a vector-like fashion,
implement ``__add__``:

.. code-block:: python

    def __add__(self, v):
        """return the element-wise vector sum of self and v
        """
        assert len(self) == len(v)
        return vector([x1 + x2 for x1, x2 in zip(self, v)])


[a slightly more complete example may be seen here :download:`vector.py <../examples/object_oriented/vector.py>`]

Indexing and Slicing
--------------------

``__getitem__`` and ``set__item__`` are used when indexing:

``x = object[i]`` calls ``__getitem__``, and ``object[i] = something`` calls ``__setitem__``.

But indexing is pretty complex in python. There is simple indexing: ``object[i]``, but there is also slicing: ``object[i:j:skip]``

When you implement ``__getitem__(self, index)``, ``index`` will simply be the index if it's a simple index, but if it's slicing, it will be a ``slice`` object. Python also supports multiple slices:

``object[a:b,c:d]``

These are used in numpy to support multi-dimensional arrays, for instance.

In this case, a tuple of slice objects is passed in.

See: :download:`index_slicing.py<../examples/object_oriented/index_slicing.py>`


Protocols in Summary
--------------------

Use special methods when you want your class to act like a "standard" class in some way.

Look up the special methods you need and define them.

There's more to read about the details of implementing these methods:

* https://docs.python.org/3.6/reference/datamodel.html#special-method-names


Emulating Standard types
=========================

.. rst-class:: medium

  Making your classes behave like the built-ins

Callable classes
-----------------

We've been using functions a lot:

.. code-block:: python

    def my_fun(something):
        do_something
        ...
        return something

And then we can call it:

.. code-block:: python

    result = my_fun(some_arguments)

.. nextslide::

But what if we need to store some data to know how to evaluate that function?

Example: a function that computes a quadratic function:

.. math::

    y = a x^2 + bx + c

You could pass in a, b and c each time:

.. code-block:: python

    def quadratic(x, a, b, c):
        return a * x**2 + b * x + c

But what if you are using the same a, b, and c numerous times?

Or what if you need to pass this in to something
(like map) that requires a function that takes a single argument?

"Callables"
-----------

Various places in python expect a "callable" -- something that you can
call like a function:

.. code-block:: python

    a_result = something(some_arguments)

"something" in this case is often a function, but can be anything else
that is "callable".

What have we been introduced to recently that is "callable", but not a
function object?

Custom callable objects
------------------------

The trick is one of Python's "magic methods"

.. code-block:: python

    __call__(*args, **kwargs)

If you define a ``__call__`` method in your class, it will be used when
code "calls" an instance of your class:

.. code-block:: python

    class Callable:
        def __init__(self, .....)
            some_initilization
        def __call__(self, some_parameters)

Then you can do:

.. code-block:: python

    callable_instance = Callable(some_arguments)

    result = callable_instance(some_arguments)

Writing your own sequence type
------------------------------

Python has a handful of nifty sequence types built in:

 * lists
 * tuples
 * strings
 * ...

But what if you need a sequence that isn't built in?

A Sparse array
--------------

Example: Sparse Array

Sometimes we have data sets that are "sparse" -- i.e. most of the values are zero.

So you may not want to store a huge bunch of zeros.

But you do want the array to look like a regular old sequence.

So how do you do that?

The Sequence protocol
----------------------

You can make your class look like a regular python sequence by defining
the set of special methods you need:

https://docs.python.org/3/reference/datamodel.html#emulating-container-types

The key ones are:

+-------------------+-----------------------+
|  ``__len__``      | for ``len(sequence)`` |
+-------------------+-----------------------+
|  ``__getitem__``  | for  ``x = seq[i]``   |
+-------------------+-----------------------+
|  ``__setitem__``  | for ``seq[i] = x``    |
+-------------------+-----------------------+
|  ``__delitem__``  | for ``del seq[i]``    |
+-------------------+-----------------------+
|  ``__contains__`` | for ``x in seq``      |
+-------------------+-----------------------+

Callables:
----------

And Example of writing a callable class:

Write a class for a quadratic equation.

* The initializer for that class should take the parameters: ``a, b, c``

* It should store those parameters as attributes.

* The resulting instance should evaluate the function when called, and return the result:


.. code-block:: python

    my_quad = Quadratic(a=2, b=3, c=1)

    my_quad(0)

References
----------

Here is a good reference for magic methods:

http://minhhh.github.io/posts/a-guide-to-pythons-magic-methods

And with a bit more explanation:

https://www.python-course.eu/python3_magic_methods.php

