.. _exercise_mailroom:

############################
Mailroom: A complete program
############################

Part 1
======

Using Python's basic data types and logic for a full program.

Goal:
-----

You work in the mail room at a local charity. Part of your job is to write
incredibly boring, repetitive emails thanking your donors for their generous
gifts. You are tired of doing this over and over again, so you've decided to
let Python help you out of a jam and do your work for you.

The program
-----------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each.

  You can store that data structure in the global namespace.

* The script should prompt the user (you) to choose from a menu of 3 actions:
  "Send a Thank You", "Create a Report" or "quit")

Sending a Thank You
-------------------

* If the user (you) selects 'Send a Thank You', prompt for a Full Name.

  * If the user types 'list', show them a list of the donor names and re-prompt
  * If the user types a name not in the list, add that name to the data structure and use it.
  * If the user types a name in the list, use it.
  * Once a name has been selected, prompt for a donation amount.
  * Turn the amount into a number -- it is OK at this point for the program to crash if someone types a bogus amount.
  * Once an amount has been given, add that amount to the donation history of
    the selected user.
  * Finally, use string formatting to compose an email thanking the donor for
    their generous donation. Print the email to the terminal and return to the
    original prompt.

It is fine (for now) to forget new donors once the script quits running.

Creating a Report
------------------

* If the user (you) selected "Create a Report", print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below)
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

Finally, use only functions and the basic Python data types you've learned
about so far. There is no need to go any farther than that for this assignment.

Intro Tutorial
--------------

Controlling Main Program Flow
..............................

One of the key components of the mailroom program is managing program flow and interacting with the user. Ideally main flow code should be cleanly separate from your feature code.

The best way to manage the program flow is to use a ``while True`` loop which means you will keep asking the user for input until user selects a feature or exits.

There are several ways to write your main program flow. Let's consider these two options:


.. code-block:: python

    def do_something():
        # do things

    def main():
        while True:
            do_something()

    main()




.. code-block:: python

    def do_something()
        # do things
        main()

    def main():
        do_something()

    main()


Can you see the advantages of one over the other?
In the first one, ``do_something`` is not aware of how the main works and as you add more features they shouldn't manage the main either.
The call stack will also keep getting deeper and deeper, which can make error stack traces hard to debug.
Another advantage is simpler code logic, and simpler code logic means less bugs!

Let's look at a simple program to utilize the while True loop and how we can handle user response:

.. code-block:: python

    import sys  # imports go at the top of the file


    fruits = ['Apples', 'Oranges', 'Pears']

    prompt = "\n".join(("Welcome to the fruit stand!",
              "Please choose from below options:",
              "1 - View fruits",
              "2 - Add a fruit",
              "3 - Remove a fruit",
              "4 - Exit",
              ">>> "))


    def view_fruits():
        print("\n".join(fruits))


    def add_fruit():
        new_fruit = input("Name of the fruit to add?").title()
        fruits.append(new_fruit)


    def remove_fruit():
        purge_fruit = input("Name of the fruit to remove?").title()
        if purge_fruit not in fruits:
            print("This fruit does not exist!")
        else:
            fruits.remove(purge_fruit)

    def exit_program():
        print("Bye!")
        sys.exit()  # exit the interactive script


    def main():
        while True:
            response = input(prompt)  # continuously collect user selection
            # now redirect to feature functions based on the user selection
            if response == "1":
                view_fruits()
            elif response == "2":
                add_fruit()
            elif response == "3":
                remove_fruit()
            elif response == "4":
                exit_program()
            else:
                print("Not a valid option!")


    if __name__ == "__main__":
        # don't forget this block to guard against your code running automatically if this module is imported
        main()



Choosing Data Structure
........................


So far we have learned about strings, tuples, and lists. We will apply data structures that we have learned in previous lessons to hold our mailroom donor information.
Choosing the right data structure is critical and our donor data structure will change in future lessons as we learn additional ones.

What goes into this decision? Here are a couple of things to consider:

* efficiency - we often need to look up data, are you able to efficiently look up the data you need?
* ease of use - is the code straightforward and simple for basic operations?
* features - does it do everything you need to do for your requirements?

Let's consider each data structure:

String would probably be able to do what we need feature wise but the code to implement would be quite complex and not very efficient.

A tuple would be an issue when adding donors since it is an immutable data structure.

A list would satisfy all of the needed features with a fairly simple code to implement. It makes the most sense to use a list for the main data structure, and actually we can have a combination of both tuples and a list.

Here is a potential data structure to consider:

.. code-block:: python

    donor_db = [("William Gates, III", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Mark Zuckerberg", [1663.23, 4300.87, 10432.0]),
            ]

Why choose tuples for inner donor record? Well another part of using the right data structure is also to reduce bugs - you are setting clear expectations that single donor entry only contains two items.

Submission
----------

As always, put the new file in your student directory in a ``session03``
directory, and add it to your clone early. Make frequent commits with
good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.

.. _exercise_mailroom_plus:


Part 2: Adding dicts and Files
==============================

**Wait to do this till after you've learned about dictionaries in a later lesson!**

use dicts where appropriate
---------------------------

You should have been able to do all of the above with the basic data types:

numbers, strings, lists and tuples.

But once you've learned about dictionaries, you may be able to re-write it a bit more simply and efficiently.

 * Update your mailroom program to:

  - Use dicts where appropriate

  - Convert your main donor data structure to be a dict.

  - See if you can use a dict to switch between the users selections.
    see :ref:`dict_as_switch` for what this means.

  - Try to use a dict and the ``.format()`` method to do the letter as one
    big template -- rather than building up a big string in parts.

Example:

.. code-block:: ipython

  In [3]: d
  Out[3]: {'first_name': 'Chris', 'last_name': 'Barker'}


  In [5]: "My name is {first_name} {last_name}".format(**d)
  Out[5]: 'My name is Chris Barker'

Don't worry too much about the "**" -- we'll get into the details later, but for now it means, more or less, pass this whole dict in as a bunch of keyword arguments.

Update mailroom with file writing.
----------------------------------

Write a full set of thank you letters to everyone as individual files on disk.

In the first version of mailroom, you generated a letter to someone who had just made a new donation, and printed it to the screen.

In this version, add a function (and a menu item to invoke it), that goes through all the donors in your donor data structure, generates a thank you letter, and writes it to disk as a text file.

Your main menu may look something like::

  Choose an action:

  1 - Send a Thank You
  2 - Create a Report
  3 - Send letters to everyone
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

Feel free to enhance it with some more information about past generosity, etc....

The idea is to require you to structure your code so that you can write the same letter to the screen or to disk (and thus anywhere else) and also exercise a bit of file writing. Remember to review the `with <http://www.diveintopython3.net/files.html#with>`_ statement as it is the preferred method when working with files.


.. _exercise_mailroom_exceptions:


Part 3: Adding Exceptions and Comprehensions
============================================

**After the lesson where you learn about Exceptions**.

Exceptions
----------

Now that you've learned about exception handling, you can update your code to handle errors better -- like when a user inputs bad data.

Comprehensions
--------------

Can you use comprehensions to clean up your code a bit?

.. _exercise_mailroom_testing:

Part 4: Adding Unit Tests
=========================

**After the lesson when you learn about Unit Testing**

Add a full suite of unit tests.

"Full suite" means all the code is tested. In practice, it's very hard to test the user interaction, but you can test everything else. Make sure that there is as little untested code in the user interaction portion of the program as possible -- hardly any logic.

This is a big step -- you may find that your code is hard to test. If that's the case, it's a good sign that you *should* refactor your code.

I like to say: "If it's hard to test, it's not well structured"

Put in the tests **before** you make the other changes below - that's much of the point of tests -- you can know that you haven't broken anything when you refactor!

Guidelines
-----------

Here are some suggestions on what should be refactored in your mailroom code.

As mentioned above, testing user interaction code is harder (code with ``print`` and ``input`` functions), these pieces require more advanced unit testing methodologies which will be revisited in future courses. So you should refactor your code where user interaction code has little business logic in there as possible, it should only deal with interacting with user either by asking them for input or printing out data. This is a good practice in general and we will come back to this concept in later lesson. This refactor will allow you to unit test functions with business logic.

Below, we will go over what components should be refactored so that we are able to unit test our mailroom - your code should improve and be better modularized if that's not the case then maybe your refactor approach should be re-visited.

For unit testing framework you should use `pytest <https://docs.pytest.org/en/latest/>`_, it has a simple interface and rich features.

You should have 3 main features so far:

* sending a thank you, which adds a new donor or updates existing donor info
* create a report
* send letters, which creates files


Send Thank You
...............

Even though every mailroom implementation will be unique, most likely this function will require significant refactor for most of you.
You can break up the code into components that handle user flow and data manipulation logic. Write your unit tests for data manipulation logic, that would include adding or updating donors and list donors functionality.


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

This one should require very little or no change to make it unit testable.
The unit test can assert that a file is created per donor entry (hint: ``os.path`` module) and file content contains text as expected.
