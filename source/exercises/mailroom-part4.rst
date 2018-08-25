.. _exercise_mailroom_part4_testing:

Mailroom Part 4
=================

Add a full suite of unit tests.

"Full suite" means all the code is tested. In practice, it's very hard to test the user interaction, but you can test everything else. Make sure that there is as little untested code in the user interaction portion of the program as possible, hardly any logic.

This is a big step; you may find that your code is hard to test. If that's the case, it's a good sign that you *should* refactor your code.

I like to say: "If it's hard to test, it's not well structured."

Put in the tests **before** you make the other changes below. That's much of the point of tests. You can know that you haven't broken anything when you refactor!

Guidelines
----------

Here are some suggestions on what should be refactored in your mailroom code.

As mentioned above, testing user interaction code is harder (code with ``print`` and ``input`` functions), these pieces require more advanced unit testing methodologies which will be revisited in future courses. So you should refactor your code where user interaction code has little business logic in there as possible, it should only deal with interacting with user either by asking them for input or printing out data. This is a good practice in general and we will come back to this concept in later lesson. This refactor will allow you to unit test functions with business logic.

Below, we will go over what components should be refactored so that we are able to unit test our mailroom - your code should improve and be better modularized if that's not the case then maybe your refactor approach should be re-visited.

For unit testing framework you should use `pytest <https://docs.pytest.org/en/latest/>`_, it has a simple interface and rich features.

You should have 3 main features so far:

* Send a thank you, which adds a new donor or updates existing donor info.
* Create a report
* Send letters, which creates files


Send Thank You
...............

Even though every mailroom implementation will be unique, most likely this function will require a significant refactor for most of you.
You can break up the code into components that handle user flow and data manipulation logic. Your unit tests should test the data manipulation logic code: thank you text, adding or updating donors, and listing donors.


Create Report
.............

This function should only need slight modification. Split up user presentation (``print`` function calls) and data logic (actual creating of rows).
Your data logic function can either return the report string already formatted or return a list of formatted rows that can be joined and printed in the user presentation function.
Then you can write a unit test for your data logic function.

Example:

.. code-block:: python

    def display_report():
        for row in get_report():
            print(row)



Here you would write a unit test for ``get_report`` function.

Send Letters
............

This function should require very little or no change to make it unit-testable.
The unit test can assert that a file is created per donor entry (hint: ``os.path`` module), and that the file content contains text as expected.

Note that you should test the correct text being generated separately from the writing of file. That way you don't need to read the file to know it's correct. So the function that generates the text should be separate from the function that writes the file.

For example:

.. code-block:: python

    def get_letter_text(name):
        """Get letter text for file content"""
        return f"{name}, thanks a lot!"


    def test_get_letter_text():
        expected = "Frank, thanks a lot!"
        assert get_letter_text("Frank") == expected



