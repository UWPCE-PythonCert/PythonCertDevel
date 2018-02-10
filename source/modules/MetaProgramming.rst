:orphan:

.. _metaprogramming:


################
Metaprogramming
################

NOTE: These notes are due for an updated -- stay tuned!

programs that write programs....

Metaprogramming
===============

.. rst-class:: left

  **Metaprogramming:**

  "Metaprogramming is a programming technique in which computer programs have the ability to treat programs as their data. It means that a program can be designed to read, generate, analyse or transform other programs, and even modify itself while running."

  -- ``https://en.wikipedia.org/wiki/Metaprogramming``

  In other words: A metaprogram is a program that writes (or maodifies) programs.

  As a dynamic language, Python is very well suited to metaprograming, as it allows objects to be modified at run time. It also provides excellent tools for **"Introspection"**:

  "The ability of a program to examine the type or properties of an object at runtime."


A class is just an object
-------------------------

A class is a first-class object:

Can be created at runtime

Passed as a parameter

Returned from a function

Assigned to a variable

(sound familiar from when we were talking about functions?)

This "everything is an object" is what allows full introspection and metaprogramming.

Introspection and manipulation tools
====================================

``getattr()`` and ``setattr()``
-------------------------------

these allow you to get and set attributes of an object by name:

.. code-block:: ipython

  In [1]: class Dummy():
     ...:     """A class with nothing in it"""
     ...:     pass
     ...:

  In [2]: obj = Dummy()

  In [3]: vars(obj)
  Out[3]: {}

  In [4]: setattr(obj, 'this', 54)

  In [5]: vars(obj)
  Out[5]: {'this': 54}

  In [6]: getattr(obj, 'this')
  Out[6]: 54

Let's play with this: (demo)

NOTE: Do attributes have to be python legal python names??

Namespaces are dictionaries!
============================




What's in a Class?
------------------

A class (and instance) object stores its attributes in a dictionary -- yes, a regular old python dict. You can access that dict with the ``__dict__`` attribute:

.. code-block:: ipython

  In [11]: class Simple():
      ...:     this = "a class attribute"
      ...:     def __init__(self):
      ...:         self.that = "an instance attribute"
      ...:

  In [12]: obj = Simple()

  In [13]: Simple.__dict__
  Out[13]:
  mappingproxy({'__dict__': <attribute '__dict__' of 'Simple' objects>,
                '__doc__': None,
                '__init__': <function __main__.Simple.__init__>,
                '__module__': '__main__',
                '__weakref__': <attribute '__weakref__' of 'Simple' objects>,
                'this': 'a class attribute'})

  In [15]: obj.__dict__
  Out[15]: {'that': 'an instance attribute'}


What class does this object belong to?
--------------------------------------

every object has a ``__class__`` attribute specifying what class the object belongs to:

.. code-block:: ipython

    In [16]: obj.__class__
    Out[16]: __main__.Simple

and that is the actuall class object:

.. code-block:: ipython

  In [17]: obj.__class__ is Simple
  Out[17]: True

metaclasses
===========

Creating a class from scratch
-----------------------------

.. code-block:: python

   >>> def create_a_class(**kw):
   ...    return type('CoolClass', (object,), dict(**kw))
   ...
   >>> cool_class = create_a_class(foo='nice', bar='sweet')
   >>> cool_class
   <class '__main__.CoolClass'>
   >>> cool_object = cool_class()
   >>> cool_object
   <__main__.CoolClass object at 0x10224e208>
   >>> cool_object.foo
   'nice'
   >>> cool_object.bar
   'sweet'


Equivalent to:
--------------

.. code-block:: python

   class CoolClass(object):
      foo = 'nice'
      bar = 'sweet'


But it was created at runtime, returned from a function and assigned to a variable.


http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example

"type" or "class"
-----------------

We talk about "classes", and yet we create them with ``type()``.

In python, "type" and "class" are essentially the same thing.

So why the two names?

History: in teheraly days of python, a "type" was a built-in object, and a "class" was an object crated with code.

type - class unifiation began in python 2.2:

``https://www.python.org/download/releases/2.2/descrintro/``

In python3, the unification is complete -- types *are* classes and vice-versa.


More on Classes
---------------

  Objects get created from classes. So what is the class of a class?

  The class of a Class is a metaclass

  The metaclass can be used to dynamically create a class

  The metaclass, being a class, also has a metaclass


What is a metaclass?
--------------------

-  A class is something that makes instances
-  A metaclass is something that makes classes
-  A metaclass is most commonly used as a class factory
-  Metaclasses allow you to do 'extra things' when creating a class,
   like registering the new class with some registry, adding methods
   dynamically, or even replace the class with something else entirely
-  Every object in Python has a metaclass
-  The default metaclass is ``type()``


``type()``
----------

With one argument, ``type()`` returns the type of the argument

With 3 arguments, ``type()`` returns a new class

.. code-block:: ipython

    type?
    Type:       type
    String Form: <type 'type'>
    Namespace:  Python builtin
    Docstring:
    type(object) -> the object's type
    type(name, bases, dict) -> a new type

    name: string name of the class
    bases: tuple of the parent classes
    dict: dict containing attribute names and values


using type() to build a class
-----------------------------

The ``class`` keyword is syntactic sugar, we can get by without it by
using type

.. code-block:: python

    class MyClass(object):
        x = 1

or

.. code-block:: python

    MyClass = type('MyClass', (), {'x': 1})

(``object`` is automatically a superclass)


Adding methods to a class built with ``type()``
-----------------------------------------------

Just define a function with the correct signature and add it to the attr
dictionary

.. code-block:: python

    def my_method(self):
        print("called my_method, x = %s" % self.x)

    MyClass = type('MyClass',(), {'x': 1, 'my_method': my_method})
    o = MyClass()
    o.my_method()


MyClass = type(name, bases, dct)

-  name: name of newly created class
-  bases: tuple of class's base classes
-  dct: class attribute mapping


What type is type?
------------------

.. code-block:: ipython

  In [30]: type(type)
  Out[30]: type


``metaclass``
---------------

Setting a class' metaclass:

.. code-block:: python

  class Foo(metaclass=MyMetaClass):
      pass


the class assigned to the ``metaclass`` keyword argument will be used to create the object class ``Foo``.

If the ``metaclass`` kwarg is not defined, it will use type to create the class.

Whatever is assigned to ``metaclass`` should be a callable with the
same signature as type()

**Python2 NOTE:**

In Python 2, instead of the keyword argument, a special class attribute: ``__metaclass__`` is used:

.. code-block:: python

    class Foo(object):
      __metaclass__ = MyMetaClass


Why use metaclasses?
--------------------

Useful when creating an API or framework

Whenever you need to manage object creation for one or more classes

For example, see ``Examples/metclasses/singleton.py``

Or consider the Django ORM:

.. code-block:: python

  class Person(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()

  person = Person(name='bob', age=35)
  print person.name

When the Person class is created, it is dynamically modified to
integrate with the database configured backend. Thus, different
configurations will lead to different class definitions. This is
abstracted from the user of the Model class.

.. nextslide::

Here is the Django Model metaclass:

https://github.com/django/django/blob/master/django/db/models/base.py#L77


__new__  vs  __init__ in Metaclasses
------------------------------------


``__new__`` is used when you want to control the creation of the class (object)

``__init__`` is used when you want to control the initiation of the class (object)

``__new__`` and ``__init__`` are both called when the module containing the class is imported for the first time.

``__call__`` is used when you want to control how a class (object) is called (instantiation)


.. nextslide::


.. code-block:: python

   class CoolMeta(type):
       def __new__(meta, name, bases, dct):
           print('Creating class', name)
           return super(CoolMeta, meta).__new__(meta, name, bases, dct)
       def __init__(cls, name, bases, dct):
     print('Initializing class', name)
     super(CoolMeta, cls).__init__(name, bases, dct)
       def __call__(cls, *args, **kw):
           print('Meta has been called')
     return type(cls, *args, **kw)

   class CoolClass(metaclass=CoolMeta):
       def __init__(self):
           print('And now my CoolClass exists')

   print('Actually instantiating now')
   foo = CoolClass()


Metaclass example
-----------------

Consider wanting a metaclass which mangles all attribute names to
provide uppercase and lower case attributes

.. code-block:: python

    class Foo(metaclass=NameMangler):
        x = 1

    f = Foo()
    print(f.X)
    print(f.x)


NameMangler
-----------

.. code-block:: python

  class NameMangler(type):

      def __new__(cls, clsname, bases, _dict):
          uppercase_attr = {}
          for name, val in _dict.items():
              if not name.startswith('__'):
                  uppercase_attr[name.upper()] = val
                  uppercase_attr[name] = val
              else:
                  uppercase_attr[name] = val

          return super().__new__(cls, clsname, bases, uppercase_attr)


  class Foo(metaclass=NameMangler):
      x = 1


Exercise: Working with NameMangler
----------------------------------

In the repository, find and run ``Examples/metaclasses/mangler.py``

Modify the NameMangler metaclass such that setting an attribute f.x also
sets f.xx

Now create a new metaclass, MangledSingleton, composed of the
NameMangler and Singleton classes in the ``Examples/metaclasses`` directory.

Assign it to the ``metaclass`` keyword argument of a new class and verify that it works.

Your code should look like this:

.. code-block:: python

    class MyClass(metaclass=MangledSingleton) # define this
        x = 1

    o1 = MyClass()
    o2 = MyClass()
    print(o1.X)
    assert id(o1) == id(o2)


The Singleton
-------------

One common use of metaclasses is to create a singleton. There is an example of this called singleton.py in the Examples directory. However, metaclasses are not the only way to create a singleton. It really depends on what you are trying to do with your singleton.


http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

class decorators?
-----------------

We touched last week a bit about class decorators:

.. code-block:: python

    @a_decorator
    class MyClass():
        ...

A decorator is a "callable" that returns a "callable" -- usually a modified
version of he one passed in.

Class objects are callable -- you call them when you instantiate a instance:

.. code-block:: python

   an_inst = MyClass()

So you can decorate a class as well as functions and methods.

In fact, you can do many of the same things that you can do with metaclasses:

When you decorate a class, you can cahnge it in some way, and then the
changed version replaces the one in the definiton.

This also happens at compile time, rather than run time, just like metaclasses.

class decorators were actually introduced AFTER metaclasses -- maybe they
are a clearer solution??


Json_save
---------

For a more involved (and useful!) example, see:

``Examples/metaclasses/Json_save``

It is a meta-class based system for saving and re-loading objects.

It works a bit like the ORMs.

It turns out that the metaclass part of the code is pretty simple and small.

But there is a lot of other nifty, magic with classes in there
-- so let's take a look.


Reference reading
-----------------

About metaclasses (Python 3):

.. rst-class:: small

  http://blog.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses

Python 2 (mostly the same):

What is a metaclass in Python?

.. rst-class:: small

  http://stackoverflow.com/a/6581949/747729

Python metaclasses by example:

.. rst-class:: small

  http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/

A Primer on Python Metaclasses:

.. rst-class:: small

  http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/

And some even more advanced tricks:

.. rst-class:: small

  http://blog.thedigitalcatonline.com/blog/2014/10/14/decorators-and-metaclasses

Notes on ``vars``:
------------------

Notes from python-ideas:

"""
I think you may have misunderstood the purpose of vars(). It isn't to be
a slightly different version of dir(), instead vars() should return the
object's namespace. Not a copy of the namespace, but the actual
namespace used by the object.

This is how vars() currently works:

py> class X:
...     pass
...
py> obj = X()
py> ns = vars(obj)
py> ns['spam'] = 999
py> obj.spam
999


If vars() can return a modified copy of the namespace, that will break
this functionality.


This is not always true, e.g. for classes vars() returns a mappingproxy.

From Doc:

"Objects such as modules and instances have an updateable ``__dict__`` attribute; however, other objects may have write restrictions on their __dict__ attributes (for example, classes use a types.MappingProxyType to prevent direct dictionary updates)."

https://docs.python.org/3.6/library/functions.html#vars

But you're right: it's misleading to return a RW mapping which is a fake namespace...

In the above examples you could just return a ``mappingproxy``.


If you want to support this feature you could use composition:

.. code-block::python

  class C:
     def __init__(self):
         self.publicns = {}  # or: self.proxyattr = MyProxyClass()
     def __vars__(self):
         return self.publicns  # or: return self.proxyattr.__dict__


This namespace will be updateable, and it let you distinguish between the namespace you want to expose to your clients without compromosing the real one.
Of course, the real one could always be accessible via __dict__ (if present).
"""
