.. _exercise_mailroom_oo:

Mailroom Object Oriented
========================

Making Mailroom Object Oriented

[NOTE: needs updating!!]


Goal:
-----

Refactor the mailroom program using classes to help organize the code.

The goal here is the same as the earlier mailroom:

:ref:`exercise_mailroom`

But this time, we want to use an OO approach to better structure the code to make it more extensible.

It was quite reasonable to build the simple MailRoom program using a
single module, a simple data structure, and functions that manipulate
that data structure.

But if one were to expand the program with additional functionality, it
would start to get a bit unwieldy and hard to maintain.

So it's a pretty good candidate for an object-oriented approach.

As you design appropriate classes, keep in mind that there are three goals:

1) encapsulation: you have a data structure that holds your data, and you have methods that manipulate that data -- you want them "bundled up" in a neat package, so that the rest of the code doesn't need to know about the data structure you are using.

2) separation of concerns: the user interaction code should be cleanly separteed from the data handling code.

3) As always: **DRY** -- Don't repeat yourself -- anywhere you see repeated code -- refactor it!

The program (reminder..)
------------------------

Write a small command-line script called ``mailroom.py``. This script should be executable. The script should accomplish the following goals:

* It should have a data structure that holds a list of your donors and a
  history of the amounts they have donated. This structure should be populated
  at first with at least five donors, with between 1 and 3 donations each

* The script should prompt the user (you) to choose from a menu of 3 actions:
  'Send a Thank You' or 'Create a Report' or 'quit')

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

**It is fine to forget new donors once the script quits running.**

Creating a Report
-----------------

* If the user (you) selected 'Create a Report' print a list of your donors,
  sorted by total historical donation amount.

  - Include Donor Name, total donated, number of donations and average donation amount as values in each row. You do not need to print out all their donations, just the summary info.
  - Using string formatting, format the output rows as nicely as possible.  The end result should be tabular (values in each column should align with those above and below)
  - After printing this report, return to the original prompt.

* At any point, the user should be able to quit their current task and return
  to the original prompt.

* From the original prompt, the user should be able to quit the script cleanly


Your report should look something like this::

    Donor Name                | Total Given | Num Gifts | Average Gift
    ------------------------------------------------------------------
    William Gates, III         $  653784.49           2  $   326892.24
    Mark Zuckerberg            $   16396.10           3  $     5465.37
    Jeff Bezos                 $     877.33           1  $      877.33
    Paul Allen                 $     708.42           3  $      236.14

Guidelines
----------

