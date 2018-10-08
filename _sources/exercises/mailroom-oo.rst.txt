.. _exercise_mailroom_oo:

Mailroom - Object Oriented
==========================

Making Mailroom Object Oriented.

Goal: Refactor the mailroom program using classes to help organize the code.

The functionality is the same as the earlier mailroom:

:ref:`exercise_mailroom_part1`

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple mailroom program using a
single module, a simple data structure, and functions that manipulate
that data structure.

But if one were to expand the program with additional functionality, it
would start to get a bit unwieldy and hard to maintain. So it's a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind these three guidelines for good code structure:


1) Encapsulation: You have a data structure that holds your data, and functions that manipulate that data; you want data and methods "bundled up" in a neat package so that they that work on that data are within one unit. The rest of the code doesn't need to know about the data structure you are using.

2) Separation of Concerns: The user-interaction code should be cleanly separated from the data handling code.

   https://en.wikipedia.org/wiki/Separation_of_concerns

   There should be no ``input`` functions in the classes that hold the data!

3) As always: **DRY** (Don't Repeat Yourself): Anywhere you see repeated code; refactor it!


The Program
-----------

See: :ref:`exercise_mailroom_part1` to remind yourself what the program needs to do.


Suggestions
-----------

One of the hardest parts of OO design (particularly in Python) is to know how "low" to go with the classes and data structures. In particular, you might have a bit of data collected together (say, a donor's name and donation history). This can be a simple tuple with a few items in it; a dict with those same data available as ``key:value`` pairs; or a class, with class attributes (and, possibly, methods).

There are no hard and fast rules, but here are some guidelines:

For this assignment it's OK to go with simple tuples. However, in order for the code to be more flexible in the future, for example, if new "fields" were added to the donor object, it's probably better to use a more structured data type, so you don't have to worry about changing the order or number of fields.

So now you have to think about using a dict or class. Again for flexibility, I think a dict is a bit easier; you can add fields to it very easily. However, with a class, you can build some functionality in there, too. This is where encapsulation comes in. For instance, one thing you might want to do is get the total of all donations a donor has made in the past. If you add a method to compute that (or a property!), then the rest of the code doesn't need to know how the donations are stored.

Consider ``data[0]`` vs ``data["first_name"]`` vs ``data.first_name``. Which one is more readable? Keep in mind that another benefit of using OO for data encapsulation is ability of modern IDE to provide auto-completion, which reduces number of bugs and helps to produce code faster.

Below are more detailed suggestions on breaking down your existing code into multiple modules that will be part of a single mailroom program.


Modules vs. Classes
...................

You may organize your code to your preference and keep it simple by having all of the code in a single file.

Optionally, you could organize your code into modules, which helps to keep code organized and re-usable.

What is a module? A module is a python file that can be imported in other files.
Modules can contain functions, classes, and even variables (constants).

Here is an example file structure for ``mailroom_oo`` package that contains 3 modules:

.. code-block:: bash

  └── mailroom_oo
     ├── __init__.py
     ├── cli_main.py
     ├── donor_models.py
     └── test_mailroom_oo.py


The module ``donor_models.py`` can contain the ``Donor`` and ``DonorCollection`` classes.

The module ``cli_main.py`` would include all of your user interaction functions and main program flow.

Note that ``__init__.py`` is an empty file that tells Python that this directory should be treated as a package so that you can import modules.

Donor Class
...........

**Class responsible for donor data encapsulation**

This class will hold all the information about a single donor, and have attributes, properties, and methods to provide access to the donor-specific information that is needed.
Remember, if you are writing code that only accesses information about a single donor, then it should most likely live in this class.

DonorCollection Class
.....................

**Class responsible for donor collection data encapsulation**

This class will hold all of the donor objects, as well as methods to add a new donor, search for a given donor, etc. If you want a way to save and re-load your data, this class would hold that method, too.

Your class for the collection of donors will also hold the code that generates reports about multiple donors.


Command Line Interface
.......................

**Module responsible for main program flow (CLI - Command Line Interface)**

Let's call this module ``cli_main.py`` to represent the entry point for the mailroom program. This module will be using the classes we defined: ``Donor`` and ``DonorCollection``. It will also handle interaction with the user via the ``input`` function calls that gather user input and to provide the output to the console.

What should go into this module?

* main "switch dictionary" to map user selection to the program features; in general, you will have a method for each of the mailroom functions.
* ``input`` function calls to gather user input
* ``print`` statements to print to console

.. note::  Technically, console print statements don't belong in your data classes. However, for some features of this program, such as "send letters," we are simply printing instead of "sending," so it is ok for this feature to reside in the data class. But do keep integration of console print statements with data classes to a minimum. Ideally, the data class methods return a string, and the UI code does the printing.


Why is this separation of data and method so important?

The idea here is that we should be able to fairly easy replace this CLI program with a different type of interface,
such as a GUI (Graphical User Interface), without having to make any changes to our data classes.
If that was the case, then you would implement the GUI elements and use your data classes the same way as they are used in CLI.


Test-Driven Development
-----------------------

At this point we have done a great job refactoring the more complex code out of data-holding classes and we are left with simple classes that are more straightforward to unit test. As you build your classes, update the tests you already have to the logic code to the new API. Ideally, update the tests first, then the code.

The ``Donor`` and ``DonorCollection`` classes should now have close to 100 percent code coverage.

For the moment, don't worry about testing most of the command line interface code. That requires simulating use input, which is an advanced testing topic. But you can (hopefully) see some of the benefits of separating the user-interaction code from the logic code; your logic code is much easier to test with no user-interaction involved.



