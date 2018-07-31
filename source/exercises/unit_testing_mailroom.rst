.. _exercise_unit_testing_mailroom:

############################
Unit Testing Mailroom
############################


Side Effects
-----------------------

Explain how side effects work


Let's write some tests using side-effects for the simple function below:

.. code-block:: python

    def get_user_answer():
        while True:
            response = input("Do you like fruits?")
            if response.lower() in ("yes", "y"):
                return True
            elif response.lower() in ("no", "n"):
                return False


Let's observe this test:

.. code-block:: python

    import pytest
    import mock

    @mock.patch("builtins.input", side_effect=["invalid"])
    def test_get_user_answer(*mocks):
        actual = get_user_answer()


Some of the interesting things here:

We are using a ``mock`` library to overwrite the built-in functionality of the ``input`` function.
We do this by telling ``patch`` the exact path to that function, in this case it is ``builtins.input``.

side_effect param allows to specify the side-effects of this fake function, meaning all possible return values.
In most cases we can use a simple ``return_value`` param, however since we have a while True loop the ``input`` function has a possibility to be called multiple times.


If we run ``pytest test_user_input.py`` (create new file and copy the function and test into this new file), you should get a StopIteration exception output similar to this:

.. code-block:: bash


                if not _callable(effect):
    >               result = next(effect)
    E               StopIteration

    /usr/local/lib/python3.6/site-packages/mock/mock.py:1121: StopIteration

What happens here? Side effect expects to continue to receive mocked output values for ``input`` function return.
Since our function continues to loop and call input until valid values like "yes", "y" etc are received, side-effect will continue to grab values from side-effect list.
StopIteration exception is raised on second while loop iteration because there are no more values available after "invalid" is grabbed.


Let's fix our test and provide some valid values to the side-effect list:

.. code-block:: python

    @mock.patch("builtins.input", side_effect=["invalid", "NO"])
    def test_get_user_answer(*mocks):
        assert get_user_answer() is False


Our test is now passing because we have provided an input that terminates the function ("NO" input).


PLACEHOLDER: side-effects with exception.


You should now be able to successfully write tests for functions that use ``input`` functionality.

Capture print output
-----------------------
