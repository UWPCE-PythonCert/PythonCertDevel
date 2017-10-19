.. _dicts_and_sets:

#####################
Dictionaries and Sets
#####################

Dictionary
==========

Python calls it a ``dict``

Other languages call it:

  * dictionary
  * associative array
  * map
  * hash table
  * hash
  * key-value pair


Dictionary Constructors
-----------------------
.. code-block:: python

    >>> {'key1': 3, 'key2': 5}
    {'key1': 3, 'key2': 5}

    >>> dict([('key1', 3),('key2', 5)])
    {'key1': 3, 'key2': 5}

    >>> dict(key1=3, key2= 5)
    {'key1': 3, 'key2': 5}

    >>> d = {}
    >>> d['key1'] = 3
    >>> d['key2'] = 5
    >>> d
    {'key1': 3, 'key2': 5}

Dictionary Indexing
-------------------
::

    >>> d = {'name': 'Brian', 'score': 42}

    >>> d['score']
    42

    >>> d = {1: 'one', 0: 'zero'}

    >>> d[0]
    'zero'

    >>> d['non-existing key']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'non-existing key'


.. nextslide::

Keys can be any immutable:

  * number
  * string
  * tuple

.. code-block:: ipython

    In [325]: d[3] = 'string'
    In [326]: d[3.14] = 'pi'
    In [327]: d['pi'] = 3.14
    In [328]: d[ (1,2,3) ] = 'a tuple key'
    In [329]: d[ [1,2,3] ] = 'a list key'
       TypeError: unhashable type: 'list'


Actually -- any "hashable" type.


.. nextslide:: Hashing

Hash functions convert arbitrarily large data to a small proxy (usually int)

Always return the same proxy for the same input

MD5, SHA, etc

Dictionaries hash the key to an integer proxy and use it to find the key and value.

Key lookup is efficient because the hash function leads directly to a bucket with very few keys (often just one)

What would happen if the proxy changed after storing a key?

Hashability requires immutability

Key lookup is very efficient

Same average time regardless of size


.. nextslide:: Dictionary indexing


Note: Python name look-ups are implemented with dict -- it's highly optimized

Key to value:

 * lookup is one way

Value to key:

 * requires visiting the whole dict

If you need to check dict values often, create another dict or set

(up to you to keep them in sync)


Dictionary Ordering (not)
-------------------------


Dictionaries have no defined order

.. code-block:: ipython

    In [352]: d = {'one':1, 'two':2, 'three':3}
    In [353]: d
    Out[353]: {'one': 1, 'three': 3, 'two': 2}
    In [354]: d.keys()
    Out[354]: dict_keys(['three', 'two', 'one'])

Dictionary Iterating
--------------------

``for``  iterates over the keys

.. code-block:: ipython

    In [15]: d = {'name': 'Brian', 'score': 42}

    In [16]: for x in d:
        print(x)
       ....:
    score
    name


(note the different order...)

dict keys and values
--------------------

.. code-block:: ipython

    In [20]: d = {'name': 'Brian', 'score': 42}

    In [21]: d.keys()
    Out[21]: dict_keys(['score', 'name'])

    In [22]: d.values()
    Out[22]: dict_values([42, 'Brian'])

    In [23]: d.items()
    Out[23]: dict_items([('score', 42), ('name', 'Brian')])


dict keys and values
--------------------

Iterating on everything

.. code-block:: ipython

    In [26]: d = {'name': 'Brian', 'score': 42}

    In [27]: for k, v in d.items():
        print("%s: %s" % (k,v))
       ....:
    score: 42
    name: Brian


Dictionary Performance
-----------------------

  * indexing is fast and constant time: O(1)

  * ``x in s`` constant time: O(1)

  * visiting all is proportional to n: O(n)

  * inserting is constant time: O(1)

  * deleting is constant time: O(1)


 http://wiki.python.org/moin/TimeComplexity


Other dict operations:
----------------------

See them all here:

https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

Is it in there?

.. code-block:: ipython

  In [5]: d
  Out[5]: {'that': 7, 'this': 5}

  In [6]: 'that' in d
  Out[6]: True

  In [7]: 'this' not in d
  Out[7]: False

Containment is on the keys.

.. nextslide::

Getting something: (like indexing)

.. code-block:: ipython

  In [9]: d.get('this')
  Out[9]: 5

But you can specify a default

.. code-block:: ipython

  In [11]: d.get('something', 'a default')
  Out[11]: 'a default'

Never raises an Exception (default default is None)

.. nextslide::

iterating

.. code-block:: ipython

  In [13]: for item in d:
     ....:     print(item)
     ....:
  this
  that

which is equivalent to, but faster than:

.. code-block:: ipython

  In [15]: for key in d.keys():
      print(key)
     ....:
  this
  that

.. nextslide::

but to get values, must specify you want values:

.. code-block:: ipython

  In [16]: for val in d.values():
      print(val)
     ....:
  5
  7


.. nextslide::

"Popping": getting the value while removing it

pop out a particular key

.. code-block:: ipython

  In [19]: d.pop('this')
  Out[19]: 5

  In [20]: d
  Out[20]: {'that': 7}

pop out an arbitrary key, value pair

.. code-block:: ipython

  In [23]: d.popitem()
  Out[23]: ('that', 7)

  In [24]: d
  Out[24]: {}

.. nextslide::

This one is handy:

``setdefault(key[, default])``

gets the value if it's there, sets it if it's not

.. code-block:: ipython

  In [27]: d.setdefault('something', 'a value')
  Out[27]: 'a value'

  In [28]: d
  Out[28]: {'something': 'a value'}


.. nextslide::

Assignment maintains link to the original dict

.. code-block:: ipython

  In [47]: d
  Out[47]: {'something': 'a value'}

  In [48]: item_view = d

  In [49]: d['something else'] = 'another value'

  In [50]: item_view
  Out[50]: {'something': 'a value', 'something else': 'another value'}


.. nextslide::

Use explicit copy method to get a copy

.. code-block:: ipython

  In [51] item_copy = d.copy()

  In [52]: d['another thing'] = 'different value'

  In [53]: d
  Out[53]:
  {'another thing': 'different value',
   'something': 'a value',
   'something else': 'another value'}

   In [54]: item_copy
   Out[54]: {'something': 'a value', 'something else': 'another value'}


Sets
====

``set``  is an unordered collection of distinct values

Essentially a dict with only keys

Set Constructors

.. code-block:: ipython

    >>> set()
    set()

    >>> set([1, 2, 3])
    {1, 2, 3}

    >>> {1, 2, 3}
    {1, 2, 3}

    >>> s = set()

    >>> s.update([1, 2, 3])
    >>> s
    {1, 2, 3}


Set Properties
---------------

``Set``  members must be hashable

Like dictionary keys -- and for same reason (efficient lookup)

No indexing (unordered)

.. code-block:: ipython

    >>> s[1]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'set' object does not support indexing


Set Methods
-----------

.. code-block:: ipython

    >> s = set([1])
    >>> s.pop() # an arbitrary member
    1
    >>> s.pop()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'pop from an empty set'
    >>> s = set([1, 2, 3])
    >>> s.remove(2)
    >>> s.remove(2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 2

.. nextslide::

All the "set" operations from math class...

.. code-block:: python

    s.isdisjoint(other)

    s.issubset(other)

    s.union(other, ...)

    s.intersection(other, ...)

    s.difference(other, ...)

    s.symmetric_difference( other, ...)

Frozen Set
----------

Another kind of set: ``frozenset``

immutable -- for use as a key in a dict
(or another set...)

.. code-block:: python

    >>> fs = frozenset((3,8,5))
    >>> fs.add(9)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: 'frozenset' object has no attribute 'add'

A few added notes:
==================

The count() method
------------------

All Python sequences (including strings) have a ``count()`` method:

.. code-block:: ipython

    In [1]: s = "This is an arbitrary string"

    In [2]: s.count('t')
    Out[2]: 2

What if you want a case-insensitive count?

.. code-block:: ipython

    In [3]: s.lower().count('t')
    Out[3]: 3

set.update()
------------

If you want to add a bunch of stuff to a set, you can use update:

.. code-block:: ipython

    In [1]: s = set()

In [2]: s.update
Out[2]: <function set.update>

In [3]: s.update(['this', 'that'])

In [4]: s
Out[4]: {'that', 'this'}

In [5]: s.update(['this', 'thatthing'])

In [6]: s
Out[6]: {'that', 'thatthing', 'this'}

**NOTE:** It's VERY often the case that when you find yourself writing a trivial loop -- there is a way to do it with a built in method!



Sorting stuff in dictionaries:
-------------------------------

dicts aren't sorted, so what if you want to do something in a sorted way?

The "standard" way:

.. code-block:: python

  for key in sorted(d.keys()):
      ...

Another option:

.. code-block:: python

    collections.OrderedDict

Also other nifty stuff in the ``collections`` module:

https://docs.python.org/3.6/library/collections.html

**NOTE:** In Python 3.6, dicts were optimized in a way that happens to preserver order. But this is considered an implementation detail. Do not count on it! If you want order preserved, use OrderedDict.

