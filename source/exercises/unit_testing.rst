.. _exercise_unit_testing:

############################
Introduction To Unit Testing
############################

Preparation
-----------

In order to do unit testing, you need a framework in which to write and run your tests.
Earlier in this class, you've been adding "asserts" to your modules -- perhaps in the ``__name__ == "__main__"`` block.  These are, in fact a kind of unit test.
But as you build larger systems, you'll want a more structured way to write and run your tests.




Test Driven Development
-----------------------

Download this module:

:download:`walnut_party.py </examples/testing/walnut_party.py>`

(This is the adapted from the codingbat site: http://codingbat.com/prob/p195669)

and this test file:

:download:`test_walnut_party.py </examples/testing/test_walnut_party.py>`

Put them in the same directory, and make that directory your working directory.

Then try running the test file with pytest:

.. code-block:: bash

  $ pytest test_walnut_party

What you've done here is the first step in what is called:

  **Test Driven Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write the code that fixes these tests.

Let's do that next!

Test Driven development
-----------------------

Open:

``test_walnut_party.py``

and:

``walnut_party.py``

In your editor.

Now edit ``walnut_party.py``, and each time you make a change, run the tests again. Continue until all the tests pass.


Doing your own:
---------------

Pick another example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

* run something on the web site.
* write a few tests using the examples from the site.
* then write the function, and fix it 'till it passes the tests.

These tests should be in a file named ``test_something.py`` -- I usually name the test file the same as the module it tests,
with ``test_`` prepended.

.. note::
  Technically, you can name your test files anything you want. But there are two reasons to use standard naming conventions.
  One is that it is clear to anyone looking at the code what is and isn't a test module. The other is that pytest, and other testing systems, use `naming conventions <https://docs.pytest.org/en/latest/goodpractices.html#test-discovery>`_ to find your test files.
  If you name your test files: ``test_something.py`` then pytest will find them for you. And if you use the name of the module being tested:
  ``test_name_of_tested_module.py`` then it will be clear which test files belong to which modules.


Do at least two of these to get the hang of the process.

Also -- once you have the tests passing, look at your solution -- is there a way it could be refactored to be cleaner?

Give it a shot -- you'll know if it still works if the tests still pass!

