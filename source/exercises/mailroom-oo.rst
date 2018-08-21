.. _exercise_mailroom_oo:

Mailroom - Object Oriented
==========================

Making Mailroom Object Oriented.

Goal:
-----

Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

:ref:`exercise_mailroom`

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a
single module, a simple data structure, and functions that manipulate
that data structure.

But if one were to expand the program with additional functionality, it
would start to get a bit unwieldy and hard to maintain.

So it's a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidelines for good code structure:


1) Encapsulation: you have a data structure that holds your data, and you have functions that manipulate that data -- you want them "bundled up" in a neat package so that data and methods that work on that data are within one unit. The rest of the code doesn't need to know about the data structure you are using.

2) Separation of Concerns: The user interaction code should be cleanly separated from the data handling code.

   https://en.wikipedia.org/wiki/Separation_of_concerns

   There should be no ``input`` functions in the classes that hold the data!

3) As always: **DRY** -- Don't Repeat Yourself -- anywhere you see repeated code -- refactor it!


The Program
-----------

See: :ref:`exercise_mailroom` to remind yourself what the program needs to do.


Suggestions
-----------

One of the hardest parts of OO design (particularly in Python) is to know how "low" to go with the classes and data structures. In particular, you might have a bit of data collected together (say, a donor's name and donation history), This can be a simple tuple with a few items in it, it can be a dict with those same data available as ``key:value`` pairs, or it can be a class, with class attributes (and maybe methods).

There are no hard and fast rules, but here are some guidelines:

For this assignment it's OK to go with simple tuples. However, in order for the code to be more flexible in the future, if new "fields" were added to the donor object, it's probably better to use a more structured type, so you don't have to worry about changing the order or number of fields.

So now you have to think about using a dict or class? Again for flexibility, I think a dict is a bit easier -- you can add fields to it very easily. However, with a class, you can build some functionality in there, too. This is where encapsulation comes in -- for instance, one thing you might want to do is get the total of all donations a donor has made in the past. If you add a method to compute that (or a property!), then the rest of the code doesn't need to know how the donations are stored.

Consider ``data[0]`` vs ``data["first_name"]`` vs ``data.first_name`` -- which one is more readable? Keep in mind that another benefit of using OO for data encapsulation is ability of modern IDE to provide auto-completion, which reduces number of bugs and helps to produce code faster.

Below are more detailed suggestions on breaking down your existing code into multiple modules that will be part of a single mailroom program.


Modules vs Classes
...................

You may organize your code up to your preference and you can keep it simple by having all of the code in a single file.

Optionally, you could organize your code into modules which helps to keep code organized and re-usable.

What is a module? Module is a python file that can be imported in other files.
Modules can contain functions, classes, and even variables (constants).

Here is an example file structure for ``mailroom_oo`` package:

.. code-block:: bash

  └── mailroom_oo
     ├── __init__.py
     ├── cli_main.py
     ├── donor_models.py
     └── test_mailroom_oo.py


``donor_models.py`` can contain ``Donor`` and ``DonorCollection`` classes

``cli_main.py`` would include all of your user interaction functions and main program flow

Note that ``__init__.py`` is an empty file that tells Python that this directory should be treated as a package so that you can import modules.

Donor Class
...........

**Class responsible for donor data encapsulation**

This will hold all the information about a single donor, and have attributes, properties, and methods to provide access to the donor specific information that is needed.
Remember that if you are writing code that only accesses information about a single donor then it should most likely live in this class.

DonorCollection Class
.....................

**Class responsible for donor collection data encapsulation**

This will hold all of the donor objects, but also methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would have that too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.


Command Line Interface
.......................

Module responsible for main program flow (CLI - Command Line Interface).

Let's call this module ``cli_main.py`` to represent the entry point for the mailroom program. This module will be using above classes we defined: ``Donor`` and ``DonorCollection``; it will also handle interaction with the user via the ``input`` function calls to gather user input and to provide the output to the console.

What should go into this module?

* the main "switch dictionary" to map user selection to the program features; in general, you will have a method for each of the mailroom functions.
* ``input`` function calls to gather user input.
* ``print`` statements to print to console.

.. note::  Technically console print statement don't belong in your data classes, however for some features like send letters instead of "sending" we are simply printing so it is ok for this feature to reside in the data class. But do keep it to a minimum -- i.e. the data class methods return a string, and the UI code does the printing.


Why is this separation so important?

The idea here is that we should be able to fairly easy replace this CLI program with a different type of interface like a GUI (Graphical User Interface) as an example and not having to make any changes to our data classes.
The only thing that would need to change with a potential GUI feature is implementing actual gui elements to use those same classes.

Test Driven Development
-----------------------

At this point we have done a great job refactoring the more complex code out of data holding classes and we are left with simple classes that are more straightforward to unit test. As you build your classes update the tests you already have to the logic code to the new API. Ideally, update the tests first, then the code.

The ``Donor`` and ``DonorCollection`` classes should now have close to 100 percent code coverage.

For the moment, don't worry about testing most of the command line interface code. That requires simulating use input, which is an advanced testing topic. But you can (hopefully) see some of the benefits of separating the user-interaction code from the logic code -- your logic code is much easier to test with no user-interaction involved.



