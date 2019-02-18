
.. _unit_testing:

############
Unit Testing
############

You've already seen a very basic testing strategy.

You've written some tests using that strategy.

These tests were pretty basic, and a bit awkward in places (testing error
conditions in particular).

    **It gets better**

Test Frameworks
---------------

So far our tests have been limited to code in an ``if __name__ == "__main__":``
block.


* They are run only when the file is executed
* They are always run when the file is executed
* You can't do anything else when the file is executed without running tests.


    This is not optimal.

    Python provides testing systems to help.


Standard Library: ``unittest``
------------------------------

The original testing system in Python.

``import unittest``

More or less a port of `JUnit <https://junit.org>`_ from Java

A bit verbose: you have to write classes & methods (And we haven't covered that yet!)

But here's a bit of an introduction, as you will see this in others' code.

And seeing how verbose it can be will help you appreciate other options.


Using ``unittest``
------------------

To use ``unittest``, you need to write subclasses of the ``unittest.TestCase`` class:

.. code-block:: python

    # in test.py
    import unittest

    class MyTests(unittest.TestCase):

        def test_tautology(self):
            self.assertEqual(1, 1)

Then you run the tests by using the ``main`` function from the ``unittest``
module:

.. code-block:: python

    # in test.py
    if __name__ == '__main__':
        unittest.main()


Testing Your Code
-----------------

This way, you can write your code in one file and test it from another:

in ``my_mod.py``:

.. code-block:: python

    def my_func(val1, val2):
        return val1 * val2

in ``test_my_mod.py``:

.. code-block:: python

    import unittest
    from my_mod import my_func


    class MyFuncTestCase(unittest.TestCase):
        def test_my_func(self):
            test_vals = (2, 3)
            expected = test_vals[0] * test_vals[1]
            actual = my_func(*test_vals)
            self.assertEqual(expected, actual)

    if __name__ == '__main__':
        unittest.main()


Advantages of ``unittest``
--------------------------

The ``unittest`` module is pretty full featured

It comes with the standard Python distribution, no installation required.

It provides a wide variety of assertions for testing all sorts of situations.

It allows for a setup and tear down workflow both before and after all tests and before and after each test.

It's well known and well understood.


Disadvantages of ``unittest``
-----------------------------

It's Object Oriented, and quite "heavyweight".

  - modeled after Java's ``JUnit`` and it shows...

It uses the framework design pattern, so knowing how to use the features means learning what to override.

Needing to override means you have to be cautious.

Test discovery is both inflexible and brittle.

And there is no built-in parameterized testing.


Other Options
-------------

There are several other options for running tests in Python.

* **Nose2**: https://github.com/nose-devs/nose2

* **pytest**: http://pytest.org/latest/

* ... (many frameworks supply their own test runners: e.g. django)

Nose was the most common test runner when I first started learning testing, but it has been in maintenance mode for a while. Even the nose2 site recommends that you consider pytest.

pytest has become the defacto standard test runner for those that want a more "pythonic" test framework.

pytest is very capable and widely used.

For a great description of the strengths of pytest, see:

`The Cleaning Hand of Pytest <https://blog.daftcode.pl/the-cleaning-hand-of-pytest-28f434f4b684>`_

So we will use pytest for the rest of this class.

Installing ``pytest``
---------------------

The first step is to install the package:

.. code-block:: bash

    $ python3 -m pip install pytest

Once this is complete, you should have a ``pytest`` command you can run
at the command line:

.. code-block:: bash

    $ pytest

If you have any tests in your repository, that command will find and run them (If you have followed the proper naming conventions).

    **Do you?**

Pre-existing Tests
------------------

Let's take a look at some examples.

Create a directory to try this out, and download:

:download:`test_random_unitest.py <../examples/testing/test_random_unitest.py>`

In the directory you created for that file, run:

.. code-block:: bash

  $ pytest

It should find that test file and run it.

You can also run pytest on a particular test file:

.. code-block:: bash

  $ pytest test_random_unitest.py

The results you should have seen when you ran ``pytest`` above come
partly from these files.

Take a few minutes to look these files over.

``test_random_unitest.py`` contains the tests for some of the functions in the built in``random`` module. You really don't need to test Python's built in modules -- they are already tested! This is just to demonstrate the process.


What is Happening Here?
-----------------------

You should have gotten results that look something like this:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.10.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/temp/test_temp, inifile:
    plugins: cov-2.6.0
    collected 3 items

    test_random_unitest.py ...                                               [100%]

    =========================== 3 passed in 0.06 seconds ===========================


When you run the ``pytest`` command, ``pytest`` starts in your current
working directory and searches the file system for things that might be tests.

It follows some simple rules:

* Any python file that starts with ``test_`` or ``_test`` is imported.

* Any functions in them that start with ``test_`` are run as tests.

* Any classes that start with ``Test`` are treated similarly, with methods that begin with ``test_`` treated as tests.

( don't worry about "classes" part just yet ;-) )

* Any ``unittest`` test cases are run.

pytest
------

This test running framework is simple, flexible and configurable.

Read the documentation for more information:

http://pytest.org/latest/getting-started.html#getstarted

It will run ``unittest`` tests for you, so can be used as a test runner.

But in addition to finding and running tests, it makes writing tests simple, and provides a bunch of nifty utilities to support more complex testing.

Now download this file:

:download:`test_random_pytest.py <../examples/testing/test_random_pytest.py>`

And run pytest again:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.10.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/temp/test_temp, inifile:
    plugins: cov-2.6.0
    collected 8 items

    test_random_pytest.py .....                                              [ 62%]
    test_random_unitest.py ...                                               [100%]

    =========================== 8 passed in 0.07 seconds ===========================

Note that it ran the tests in both the test files.

Take a look at ``test_random_pytest.py`` -- It is essentially the same tests -- but written in native pytest style -- simple test functions.

pytest tests
------------

The beauty of pytest is that it takes advantage of Python's dynamic nature -- you don't need to use any particular structure to write tests.

Any function named appropriately is a test.

If the function doesn't raise an error or an assertion, the test passes. It's that simple.

Let's take a look at ``test_random_pytest.py`` to see how this works.

.. code-block:: python

    import random
    import pytest

The ``random module is imported becasue that's what we are testing``.
``pytest`` only needs to be imported if you are using its utilities -- more on this in a moment.

.. code-block:: python

    seq = list(range(10))

Here we create a simple little sequence to use for testing. We put it in the global namespace so other functions can access it.

Now the first test -- simply by naming it ``test_something``, pytest will run it as a test:

.. code-block:: python

    def test_shuffle():
        """
        Make sure the shuffled sequence does not lose any elements
        """
        seq2 = seq[:]  # make a copy so the main one won't get changed
        seq2.sort()
        random.shuffle(seq2)
        seq2.sort()  # If you comment this out, it will fail, so you can see output
        print("seq2:", seq2)  # only see output if it fails
        assert seq2 == list(range(10))

This test is designed to make sure that random.shuffle only re-arranges the items, but doesn't add or lose any.
First a copy of the global sequence is made -- you want to make sure that tests don't change the status of anything global.




    def test_shuffle_immutable():
        with pytest.raises(TypeError):
            random.shuffle((1, 2, 3))


    def test_choice():
        element = random.choice(seq)
        assert (element in seq)


    def test_sample():
        for element in random.sample(seq, 5):
            assert element in seq


    def test_sample_too_large():
        with pytest.raises(ValueError):
            random.sample(seq, 20)








Test Driven Development
-----------------------

Test Driven Development or "TDD", is a development process where you write tests to assure that your code works, *before* you write the actual code.

This is a very powerful approach, as it forces you to think carefully about exactly what your code should do before you start to write it. It also means that you know when you code is working, and you can refactor it in the future will assurance that you haven't broken it.

Give this exercise a try to get the idea:

:ref:`exercise_unit_testing`
