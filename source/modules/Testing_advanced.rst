:orphan:

.. _advanced_testing:

*******
Testing
*******

Testing in Python

UWPCE Python certificate third quarter.

================
What is testing?
================

.. rst-class:: medium

    Code which runs your application in as close to a real environment as
    feasible and validates its behavior


Terminology of testing
----------------------

-  Unit tests
-  Integration tests
-  High level system tests
-  Acceptance tests
-  Black box / White box testing


"V" model and tests levels
--------------------------
.. image:: /_static/test_v_model.png

Unit testing
------------

-  Test smallest discrete units of source code
-  Tests should be independent of each other
-  Can separate tests from required resources through fixtures and
   mocking
-  Automatable
-  Integrates with development process

.. nextslide::

What should be tested?
----------------------

The percentage of code which gets run in a test is known as the
coverage.

100% coverage is an ideal to strive for. But the decision on when and
what to test should take into account the volatility of the project.

**NOTE** Even if every line of code is run during tests (100% coverage),
they may not be comprehensive! It is very hard to anticipate every wierd
input some code may get.


.. nextslide::

Unit-testing tools
------------------

-  unittest, the test framework that ships with Python. Port of Java jUnit

   http://docs.python.org/3/library/unittest.html

-  nose2, a test runner which integrates with unittest, making it nicer and easier

   http://nose2.readthedocs.org/en/latest/

   NOTE: it's not clear how well maintained nose2 is...

-  pytest, an alternative to unittest, which you should be pretty familiar with now

   http://pytest.org/latest/

-  mock, an object mocking library. Ships with Python 3.3+

   https://docs.python.org/dev/library/unittest.mock.html


About Unit-testing
------------------

1. Tests should be independent.
2. Tests do not run in order, which shouldn't matter, see point 1.
3. Test fixtures are available to do any setup/teardown needed for tests.
4. Test behavior not implementation
5. Mocking is available to fake stuff you may not want to run in your tests.

This all applies regardless of your test framework

unittest
--------

The unittest framework comes with the standard library

Unittest is ported from Java's jUnit -- it is therefor OO-heavy, and
requires a lot of boilerplate code.

Many projects built custom testing Frameworks on top of it -- e.g. Django

Therefor you will encounter it

So it's good to be familiar with it.

Key missing features:

 * A test runner

   - many people use nose or pytest to run unittest tests.

 * Parameterized tests

   - there are kludges and some third-party tools for this.


unittest.TestCase anatomy
-------------------------

* create a new subclass of ``unittest.TestCase``
* name test methods ``test_foo`` so the test runner finds them
* make calls to the ``self.assert*`` family of methods to validate results

.. code-block:: python

    import unittest
    class TestTest(unittest.TestCase):

        def setUp(self):
            self.x = 2

        def test_add(self):
            self.assertEqual(self.x+2, 4)

        def test_len(self):
            self.assertEqual(len('foo'), 3)

    if __name__ == '__main__':
        unittest.main()


Assert Methods
---------------

TestCase contains a number of methods named ``assert*`` which can be used
for validation, here are a few common ones:

.. code-block:: python

    assertEqual(first, second, msg=None)
    assertNotEqual(first, second, msg=None)
    assertTrue(expr, msg=None)
    assertFalse(expr, msg=None)
    assertIn(first, second)
    assertRaises(exc, fun, msg=None, *args, **kwargs)

See a full list at:

http://docs.python.org/3/library/unittest.html#assert-methods or

``dir(unittest.TestCase)`` or to get really fancy

.. code-block:: python

    [print(i) for i in dir(unittest.TestCase) if i.startswith('assert')]


==================
Running your tests
==================

.. rst-class:: medium

    How do you actually run your tests?


running tests in a single module
--------------------------------

Call unittest.main() right in your module

::

        if __name__ == "__main__":
            unittest.main()

  # or from the command line:
  python -m unittest test_my_module  # with or without .py on end
  python -m unittest test_my_module.TestClass  # particular class in a module
  python -m unittest test_my_module.TestClass.test_method  # particular test


If it gets cumbersome with many TestCases, organize the tests into a
test suite

Test Suites
-----------

Test suites group test cases into a single testable unit

::

    import unittest

    from calculator_test import TestCalculatorFunctions

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculatorFunctions)

    unittest.TextTestRunner(verbosity=2).run(suite)


Tests can also be organized into suites in the

``if __name__ == "__main__":``

block


pytest and Nose2
----------------

Nose2 is the new nose. Nose no longer maintained, and directs users to nose2.
But Nose2 is not all that well maintained either.

Both pytest and Nose2 are test runners: they autodiscover test cases

They will find tests for you so you can focus on writing tests, not
maintaining test suites

To find tests, pytest and nose look for modules (such as python files)
whose names start with ‘test’. In those modules, they will load tests
from all unittest.TestCase subclasses, as well as functions whose names
start with ‘test’.

So running your tests is as easy as

::

    $ pytest
    or
    $ nose2


http://nose2.readthedocs.org/en/latest/getting_started.html#running-tests

https://docs.pytest.org/en/latest/index.html

A number of projects use nose -- so you may encounter it, but we'll focus
on pytest for now.



Fixtures: Setting up your tests for success
-------------------------------------------

(or failure!)

Test fixtures are a fixed baseline for tests to run from consistently,
also known as test context.

Fixtures can be set up fresh before each test, once before each test
case, or before an entire test suite.

Fixtures in unittest
--------------------

unittest provides fixture support via these methods:

-  setUp / tearDown - these are run before and after each test method
-  setUpClass / tearDownClass - these are run before/after each TestCase
-  setUpModule / tearDownModule - run before/after each TestSuite
-  addCleanup / doCleanups - called after tearDown,
   in case a test throws an exception

Fixtures in pytest
------------------

pytest provides a fixture system that is powerful and flexible:

https://docs.pytest.org/en/latest/fixture.html#fixture

You use a decorator to create a fixture:

.. code-block:: python

    import pytest

    @pytest.fixture
    def smtp():
        import smtplib
        return smtplib.SMTP("smtp.gmail.com")

A fixture is simply a function that will get run when it it used, and
returns *something* that your tests need:

To use a fixture, you add it as a parameter to your test function:

.. code-block:: python

    def test_ehlo(smtp):
        response, msg = smtp.ehlo()
        assert response == 250
        assert 0 # for demo purposes

the parameter gets set to the value returned by the fixture function.
The fixture function is automatically run before each test.

Let's see this in action:

in: ``Examples\testing``::

    py.test -s -v pytest_fixtures.py

The ``-s`` tells pytest not to capture stdout -- so we can see print statements)

The ``-v`` is verbose mode -- so we can see a bit more what is going on.

"teardown"
----------

If your fixture needs to clean itself up after its done, this is known as
"teardown"

to accomplish this in pytest, you use "yield", rather than "return".

The teardowncode will run after the yield

.. code-block:: python

  @pytest.fixture()
  def smtp(request):
      smtp = smtplib.SMTP("smtp.gmail.com")
      yield smtp  # provide the fixture value
      print("teardown smtp")
      smtp.close()

See the example again for this...

=============================
Testing floating point values
=============================

.. rst-class:: left

    Why can't we just test if .5 == .5 ?

    .. code-block:: ipython

        In [1]: 3 * .15 == .45
        Out[1]: False

        In [2]: 3 * .15
        Out[2]: 0.44999999999999996

        In [3]: 3 * .15 * 10 / 10  == .45
        Out[3]: True

    There are an infinite number of floating point numbers, so they are
    stored as an approximation in computing hardware.

    https://docs.python.org/3/tutorial/floatingpoint.html

levels of precision of floating point
-------------------------------------

Floating point numbers are stored in `IEEE
754 <http://en.wikipedia.org/wiki/IEEE_floating_point>`__ 64-bit double
precision format, so 1 bit for the sign, 11 bits for the exponent, and
the remaining 52 for the fraction

So we can count on up to 16 digits of precision in decimal:

.. code-block:: ipython

    In [39]: len(str(2**52))
    Out[39]: 16

    In [40]: .1+.2
    Out[40]: 0.30000000000000004

    In [41]: len('3000000000000000')
    Out[41]: 16

    # with repeated operations, the errors eventually build up:
    # here's multiplying by '1' 10 million times:
    In [64]: x=1
    In [69]: for i in range(10000000): x *= (.1 + .2)/.3
    Out [69]: 1.000000002220446

assertAlmostEqual
-----------------

Verifies that two floating point values are close enough to each other.
Add a places keyword argument to specify the number of decimal places.

.. code-block:: python

    import unittest

    class TestAlmostEqual(unittest.TestCase):

        def setUp(self):
            pass

        def test_floating_point(self):
            self.assertEqual(3*.15, .45)

        def test_almost_equal(self):
            self.assertAlmostEqual(3*.15, .45, places=7)


What is close?
--------------

.. rst-class:: medium

    **Warning**

``assertAlmostEqual`` lets you specify *decimal places*,
i.e. the number of digits after the decimal point.

This works great for numbers that are about magnitude 1.0 (as above)

But what if you have numbers that are very large? (or small):

  - ``1.0e22``
  - ``1.0000000000001e22``

are they almost equal?

.. nextslide::

Remember that python floating point numbers store the exponent and up
to 16 decimal digits.

So those two are almost as close as you can get. But:

.. code-block:: ipython

    In [30]: x = 1e22

    In [31]: y = 1.0000000000001e22

    In [32]: '%g'%(y - x)
    Out[32]: '1.00034e+09'

They are different by about a billion!

In general, we don't want to compare floating point numbers to within a
certain number of decimal places.

Anyone remember "significant figures" from science classes?

``isclose()``
-------------

Python 3.5 introduced the isclose() function in the math module:

https://www.python.org/dev/peps/pep-0485/

.. code-block:: ipython

    In [39]: import math

    In [40]: x
    Out[40]: 1e+22

    In [41]: y
    Out[41]: 1.0000000000001e+22

    In [42]: math.isclose(x,y)
    Out[42]: True

So this works for any magnitude number.

.. nextslide::

.. code-block:: python

    is_close(a, b, *, rel_tol=1e-09, abs_tol=0.0) -> bool

    Determine whether two floating point numbers are close in value.

       rel_tol
           maximum difference for being considered "close", relative to the
           magnitude of the input values
        abs_tol
           maximum difference for being considered "close", regardless of the
           magnitude of the input values

    Return True if a is close in value to b, and False otherwise.

``rel_tol`` essentially specifies how many significant figures you want:
``1e-09`` is 9 significant figures: about half of what floats can store.

``abs_tol`` is required for comparisons to zero -- nothing is
"relatively close" to zero

Using ``isclose()`` with ``unittest``
-------------------------------------

Ideally, ``TestCase`` would have an ``assertIsClose`` method.
But you can use:

.. code-block:: python

    import unittest
    from math import isclose

    class TestAlmostEqual(unittest.TestCase):

        def test_floating_point(self):
            self.assertEqual(3*.15, .45)

        def test_almost_equal(self):
            self.assertTrue( isclose( 3*.15, .45, rel_tol=7) )

**NOTE** This is one of the key flaws with the unittest module: while
it can test anything with ``assertTrue`` and the like -- if there is no
nifty ``assert*`` method for your use-case, you lose the advantages of
the ``assert*`` methods.

What are those advantages? -- mostly a prettier printing of information
in the error::

  FAIL: test_floating_point (__main__.TestAlmostEqual)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/Users/Chris/PythonStuff/UWPCE/Py300-Spring2017/Examples/testing/test_floats.py", line 17, in test_floating_point
      self.assertEqual(3 * .15, .45)
  AssertionError: 0.44999999999999996 != 0.45

But when you use assertTrue::

  FAIL: test_isclose_tiny (__main__.TestAlmostEqual)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "/Users/Chris/PythonStuff/UWPCE/Py300-Spring2017/Examples/testing/test_floats.py", line 32, in test_isclose_tiny
      self.assertTrue(math.isclose(4 * .15e-30, .45e-30))
  AssertionError: False is not true

Not that helpful -- is it?

``pytest`` give you nice informative messages when tests fail -- without special asserts.


Parameterized Tests
--------------------

Often you want to run exactly the same tests, but with different outputs and inputs.

You can do this a really naive way, but putting multiple asserts into one test:

.. code-block:: python

  def test_multiply():
      assert multiply(2, 2) == 4
      assert multiply(2, -1) == -4
      assert multiply(-2, -3) == 6
      assert multiply(3, 0) == 0
      assert multiply(0, 3) == 0

If they all pass, fine, but if not, it will fail on the first one,
and you'll have no idea if the others pass.

Plus, it gets a bit tedious to write, particularly if the code is more
complex than a single function call.

You can write a separate test for each case:

.. code-block:: python

  def test_multiply_both_posative():
      assert multiply(2, 2) == 4

  def test_multiply_one_negative):
      assert multiply(2, -1) == -4

  def test_multiply_both_negative():
      assert multiply(-2, -3) == 6

  def test_multiply_second_zero():
      assert multiply(3, 0) == 0

  def test_multiply_first_zero():
      assert multiply(0, 3) == 0

But talk about tedious!!!

Unfortunately, ``unittest`` does not have a built-in way to solve this
problem. There are hacks to do it -- google them to find out how. Here is one:

http://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases

``pytest.mark.parametrize``
---------------------------

Pytest does provide a nifty way to do it:

https://docs.pytest.org/en/latest/parametrize.html#parametrize-basics

.. code-block:: python

  param_names = "arg1, arg2, result"
  params = [(2, 2, 4),
            (2, -1, -2),
            (-2, -2, 4),
            ]
  @pytest.mark.parametrize(param_names, params)
  def test_multiply(arg1, arg2, result):
      assert multiply(arg1, arg2) == result

I find this very, very, useful.

See ``Examples/teseting/calculator/test_calculator_pytest.py``

Code Coverage
-------------

"Coverage" is the fraction of your code that is run by your tests.
That is, how much code is "covered" by the tests.

It's usually reorted as a percentage of lines of code that were run.

If a line of code is *not* run in your tests -- you can be pretty
sure it hasn't been tested -- so how do you know it works?

So 100% coverage is a good goal (though harder to achieve than you might think!)

Keep in mind that 100% coverage does **NOT** mean that you code is fuly tested
-- you have no idea how many corner cases may not have been checked.

But it's a good start.

The coverage tool
-----------------

"Coverage.py" is a tool (written by Ned Batchelder) for checking code testing
coverage in python:

https://coverage.readthedocs.io/en/coverage-4.3.4/

It can be installed with ``pip``::

  python -m pip install coverage

To run coverage on your test suite:

::

    coverage run my_program.py arg1 arg2

This generates a .coverage file. To analyze it on the console:

::

    coverage report

Else generate an HTML report in the current directory:

::

    coverage html

To find out coverage across the standard library, add -L:

::

      -L, --pylib           Measure coverage even inside the Python installed
                            library, which isn't done by default.


branch coverage
---------------

consider the following code:

::

    x = False  # 1
    if x:      # 2
        print("in branch")  # 3
    print("out of branch")  # 4

We want to make sure the branch is being bypassed correctly in the False
case

Track which branch destinations were not visited with the --branch
option to run

::

    coverage run --branch myprog.py

http://nedbatchelder.com/code/coverage/branch.html

Using coverage with pytest
--------------------------

There is a plug-in for pytest that will run coverage for you when you run your tests:

::

    $ pip install pytest-cov
    # now it can be used
    $ py.test --cov test_file.py

https://pypi.python.org/pypi/pytest-cov

There are a number of ways to invoke it and get different reports:

To get a nifty html report::

  pytest --cov --cov-report html test_calculator_pytest.py


Doctests
--------

Tests placed in docstrings to demonstrate usage of a component to a
human in a machine testable way

.. code-block:: python

    def square(x):
        """
        Squares x.

        >>> square(2)
        4
        >>> square(-2)
        4
        """
        return x * x

::

        python -m doctest -v example.py

.. nextslide::

Now generate documentation, using epydoc for example:

::

        $ epydoc example.py


http://docs.python.org/3/library/doctest.html

http://www.python.org/dev/peps/pep-0257/

http://epydoc.sourceforge.net/

http://sphinx-doc.org/

http://www.doxygen.org


Test Driven Development (TDD)
-----------------------------

In TDD, the tests are written the meet the requirements before the code
exists.

Once the collection of tests passes, the requirement is considered met.

We don't always want to run the entire test suite. In order to run a
single test with pytest:

::

    pytest -k "test_divide"


Exercises
---------

-  Add unit tests for each method in calculator_functions.py
-  Add fixtures via setUp/tearDown methods and setUpClass/tearDownClass
   class methods. Are they behaving how you expect?

or

-  Use pytest fixtures instead.
-  Add additional unit tests for floating point calculations
-  Fix any failures in the code
-  Add doctests to calculator_functions.py



Now we've got the tools to really test
--------------------------------------

Consider the application in the examples/wikidef directory. Give the
command line utility a subject, and it will return a definition.

::

        ./define.py Robot


How can we test our application code without abusing (and waiting for)
Wikipedia?

Using Mock objects
------------------

Using Mock objects to test an application with service dependencies

Mock objects replace real objects in your code at runtime during test

This allows you to test code which calls these objects without having
their actual code run

Useful for testing objects which depend on unimplemented code, resources
which are expensive, or resources which are unavailable during test
execution

http://www.voidspace.org.uk/python/mock

Mocks
-----

The MagicMock class will keep track of calls to it so we can verify
that the class is being called correctly, without having to execute the
code underneath

::

        import mock

        mock_object = mock.MagicMock()
        mock_object.foo.return_value = "foo return"
        print(mock_object.foo.call_count)
        print(mock_object.foo())
        print(mock_object.foo.call_count)
        # raise an exception by assigning to the side_effect attribute
        mock_object.foo.side_effect = Exception
        mock_object.foo()


Easy mocking with mock.patch
----------------------------

patch acts as a function decorator, class decorator, or a context
manager

Inside the body of the function or with statement, the target is patched
with a new object. When the function/with statement exits the patch is
undone


Using patch
-----------

::

    # patch with a decorator
    @patch.object(Wikipedia, 'article')
    def test_article_success_decorator_mocked(self, mock_method):
        article = Definitions.article("Robot")
        mock_method.assert_called_once_with("Robot")

    # patch with a context manager
    def test_article_success_context_manager_mocked(self):
        with patch.object(Wikipedia, 'article') as mock_method:
            article = Definitions.article("Robot")
            mock_method.assert_called_once_with("Robot")


http://www.voidspace.org.uk/python/mock/patch.html


Exercise
--------

When define.py is given the name of a non-existent article, an exception
is thrown. This exception causes another exception to occur, and the whole thing
is not very readable. Why does this happen?

Use what you know about exceptions to throw a better exception, and
then add a new test that confirms this behavior. Use mock for your test, so you
are not hammering Wikipedia.

