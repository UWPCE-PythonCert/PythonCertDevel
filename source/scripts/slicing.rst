:orphan:

.. _script_slicing:

Slicing
=======

Python has a "secret power" beyond simple indexing as with arrays in any language, Python sequences support "slicing" -- pulling a chunk out of a sequence with one simple syntax.

Slicing is a real "power tool" of python -- it can allow very short code.

Slicing a sequence creates a new sequence with a range of objects from the
original sequence.

It also uses the indexing operator (``[]``), but with a twist.

``sequence[start:finish]`` returns all `sequence[i]` for which `start <= i < finish`

That's a fancy way to say that it's all the items from start to finish -- including start, but NOT including finish.

This also may be a bit unintuitive -- but it's very practical.

.. code-block:: ipython

    In [121]: s = "a bunch of words"
    In [122]: s[2]
    Out[122]: 'b'
    In [123]: s[6]
    Out[123]: 'h'
    In [124]: s[2:6]
    Out[124]: 'bunc'
    In [125]: s[2:7]
    Out[125]: 'bunch'

Helpful Hint
------------

It can really help if you think about slicing this way:

(write this out!)

Think of the indexes as pointing to the spaces between the items::

       a       b   u   n   c   h       o   f       w   o   r   d   s
     |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15

Slicing
-------

Python has some other slicing shortcuts...

You do not have to provide both ``start`` and ``finish``:

.. code-block:: ipython

    In [6]: s = "a bunch of words"
    In [7]: s[:5]
    Out[7]: 'a bun'
    In [8]: s[5:]
    Out[8]: 'ch of words'

Either ``0`` or ``len(s)`` will be assumed, respectively.

You can combine this with the negative index to get the end of a sequence:

.. code-block:: ipython

    In [4]: s = 'this_could_be_a_filename.txt'
    In [5]: s[:-4]
    Out[5]: 'this_could_be_a_filename'
    In [6]: s[-4:]
    Out[6]: '.txt'

**That** is a real-world example I use all the time.

Why start from zero?
--------------------

Python indexing feels 'weird' to some folks -- particularly those that don't come with a background in the C family of languages.

Why is the "first" item indexed with **zero**?

Why is the last item in the slice **not** included?

*Because* these lead to some nifty properties::

    len(seq[a:b]) == b-a

    seq[:b] + seq[b:] == seq

    len(seq[:b]) == b

    len(seq[-b:]) == b

There are very many fewer "off by one" errors as a result.

More on Slicing
---------------

Slicing takes a third argument: ``step`` which controls which items are
returned:

.. code-block:: ipython

    In [18]: a_tuple
    Out[18]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

    In [19]: a_tuple[0:15]
    Out[19]: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    In [20]: a_tuple[0:15:2]
    Out[20]: (0, 2, 4, 6, 8, 10, 12, 14)

    In [21]: a_tuple[0:15:3]
    Out[21]: (0, 3, 6, 9, 12)

    In [22]: a_tuple[::-1]
    Out[22]: (19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

very cool -- a negative step reverses the results!

Slicing vs. Indexing
--------------------

Though they share an operator, slicing and indexing have a few important
differences:

* Indexing will always return one single object (a scalar), whereas slicing will return a sequence of objects.

So if you start with, say, a list of numbers, indexing will return a single number.  Slicing, on the other hand, will return list of numbers -- even is that list only has one number in it -- or zero!

Note that strings are a bit of an exception -- there is no character type in Python -- so a single character is a string -- a sequence of length-1.

* Indexing past the end of a sequence will raise an error, slicing will not:

.. code-block:: ipython

    In [129]: s = "a bunch of words"
    In [130]: s[17]
    ----> 1 s[17]
    IndexError: string index out of range
    In [131]: s[10:20]
    Out[131]: ' words'
    In [132]: s[20:30]
    Out[132]: ''

(try it yourself....)
