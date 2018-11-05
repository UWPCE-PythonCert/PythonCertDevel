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

:download:`cigar_party.py </examples/testing/cigar_party.py>`

(This is the `"cigar party" <http://codingbat.com/prob/p195669>`_ problem from the codingbat site)

and this test file:

:download:`test_cigar_party.py </examples/testing/test_cigar_party.py>`

Put them in the same directory, and make that directory your working directory.

Then try running the test file with pytest:

.. code-block:: bash

  $ pytest test_cigar_party

What you've done here is the first step in what is called:

  **Test Driven Development**.

A bunch of tests exist, but the code to make them pass does not yet exist.

The red you see in the terminal when we run our tests is a goad to us to write the code that fixes these tests.

Let's do that next!

Test Driven development
-----------------------

Open:

``test_cigar_party.py``

and:

``cigar_party.py``

In your editor.

Now edit ``cigar_party.py``, and each time you make a change, run the tests again. Continue until all the tests pass.

Doing your own:
---------------

Pick another example from codingbat:

``http://codingbat.com``

Do a bit of test-driven development on it:

  * run something on the web site.
  * write a few tests using the examples from the site.

These tests should be in a file names ``test_something.py`` -- I usually name the test file the same as the module it tests,
with ``test_`` prepended.

  * then write the function, and fix it 'till it passes the tests.

Do at least two of these to get the hang of the process.

Also -- once you have the tests passing, look at your solution -- is there a way it could be refactored to be cleaner?
Give it a shot -- you'll know if it still works if the tests still pass!

