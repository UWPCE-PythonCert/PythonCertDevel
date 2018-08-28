.. _exercise_mailroom:

############################
Mailroom: A complete program
############################


Part 1: Establishing The Data Structure (Lesson 3)
==================================================

**Using Python's basic data types and logic for a full program**

**Assignment Structure:**

This assignment is designed in three parts that will make use of your skills as you develop them during this course. You will complete and submit Part 1 for your homework in Lesson 3. You will continue to add functionality to your program in the following weeks, tackling and submitting Part 2 for Lesson 4,  Part 3 for Lesson 5, and Part 4 for Lesson 6. This progressive work will give you a strong foundation for success the final project, a Mailroom program using object-oriented programming (Lesson 9).


Program Goal:
-------------

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over and over again, so you've decided to
let Python help you out of a jam and do your work for you.


The program
-----------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each. You can store that data structure in the global namespace.

* The script should prompt the user (you) to choose from a menu of 3 actions:
  "Send a Thank You," "Create a Report," or "quit."

Sending a Thank You
-------------------

* If the user (you) selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt.
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Turn the amount into a number; it is OK at this point for the program to crash if someone types a bogus amount.
  * Once an amount has been given, add that amount to the donation history of
    the selected user.
  * Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

It is fine (for now) for the program not to store the names of the new donors that had been added, in other words, to forget new donors once the script quits running.

Creating a Report
-----------------

* If the user (you) selected "Create a Report," print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations, and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below).
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly.


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

Guidelines
----------

First, factor your script into separate functions. Each of the above
tasks can be accomplished by a series of steps.  Write discreet functions
that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive
programs are a classic use-case for the ``while`` loop.

Of course, ``input()`` will be useful here.

Put the functions you write into the script at the top.

Put your main interaction into an ``if __name__ == '__main__'`` block.

Finally, for Part 1 use only functions and the basic Python data types you've learned
about so far in Lessons 1-3. There is no need to go any farther than that for this assignment.

Submission
----------

As always, put the new file in your student directory in a ``session03``
directory, and add it to your clone early. Make frequent commits with
good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.

.. _exercise_mailroom_plus:


Part 2: Adding dicts and Files (Lesson 4)
=========================================

**Try this expansion after you've learned about dictionaries in Lesson 5**.

Use dicts where appropriate.
----------------------------

Part 1 of this assignment used these basic data types: numbers, strings, lists and tuples.

However, using dictionaries, covered in Lesson 4, will let you re-write your program a bit more simply and efficiently.

Update your mailroom program to:

  - Use dicts where appropriate.

  - See if you can use a dict to switch between the user's selections.

  - See if you can use a dict to switch between the users selections.
    see :ref:`dict_as_switch` for what this means.

  - Convert your main donor data structure to be a dict.
  
  - Try to use a dict and the ``.format()`` method to produce the letter as one
    big template, rather than building up a big string that produces the letter in parts.


Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the ``**``. We'll get into the details later, but for now it means, more or less, "pass this whole dict in as a bunch of keyword arguments."

Update mailroom with file writing.
----------------------------------

**Goal: Write a full set of letters to all donors to individual files on disk.**

In the first version of mailroom, you generated a letter to a donor who had just made a new donation, and printed it to the screen.

In this version of your program, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter for each donor, and writes each letter to disk as a text file.

Your main menu may look something like:

  Choose an action:

  1 - Send a Thank You to a single donor.
  2 - Create a Report.
  3 - Send letters to all donors.
  4 - Quit

The letters should each get a unique file name -- you can keep it really simple and just use the donor's name or add a date timestamp for additional uniqueness.

You want to avoid specifying a hardcoded file path when creating the files, for example don't to this:

.. code-block:: python

    open("/home/users/bob/dev/mailroom/thank_you.txt", "w")


Doing so will prevent other users from running the program as it will fail to find your path. Instead, you can create files in the current working directory or you can use a temporary directory.
To identify a temporary directory you can use a handy function like `tempfile.gettempdir() <https://docs.python.org/3/library/tempfile.html#tempfile.gettempdir/>`_ which is also OS agnostic (meaning it can handle temp directory differences between different operating systems).

After running the "send letters to everyone" option, you should see some new files in the directory -- there should be a file for each donor in the database, in this case 4.

After choosing action (3) above, I get these files::

  Jeff_Bezos.txt
  Mark_Zuckerberg.txt
  Paul_Allen.txt
  William_Gates_III.txt

(If you want to get really fancy, ask the user for a directory name to write to!)

An example file content looks like this::

  Dear Jeff Bezos,

          Thank you for your very kind donation of $877.33.

          It will be put to very good use.

                         Sincerely,
                            -The Team

Feel free to enhance your letter template with some more information about past generosity, etc....

The idea is to require you to structure your code so that you can write the same letter to the screen or to disk (and thus anywhere else) and also exercise a bit of file writing. Remember to review the `with <http://www.diveintopython3.net/files.html#with>`_ statement as it is the preferred method when working with files.


.. _exercise_mailroom_exceptions:


Part 3: Adding Exceptions and Comprehensions (Lesson 5)
=======================================================

**Tackle this expansion after you learn about exceptions in Lesson 5**.

Exceptions
----------

Now that you've learned about exception handling, you can update your code to handle errors better, such as when a user inputs bad data.


Comprehensions
--------------

Can you use comprehensions to clean up your code a bit?

.. _exercise_mailroom_testing:

Part 4: Adding Unit Tests  (Lesson 6)
=====================================

**Test your program after you learn about unit tests in Lesson 6**.

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
You can break up the code into components that handle user flow and data manipulation logic. Write your unit tests for data manipulation logic, including functionality for adding or updating donors, and for listing donors.


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

Note that you should test the correct text being generated separately from the writting the file. That way you don't need to read the file to know it's correct. So the function that generates the text should be separate from teh function that writes the file.




