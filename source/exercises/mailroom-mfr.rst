.. _exercise_mailroom_map_filter_reduce:

Mailroom - Map Filter Reduce
============================

Making Mailroom Functional

A complete program
------------------

It was reasonable to build the simple MailRoom program using a single module, a simple data structure, and functions that manipulate that data structure. It was reasonable to refactor Mailroom around a class when it started to become unwieldy with all of the features we needed to add to it.

Due to the success of Mailroom and the good PR it has generated with all its Thank You letters, the donations are pouring in. Moreover this has raised the attention of wealthy philanthropists who are willing to contribute matching funds. Our problem now is to expand Mailroom so that it can quickly account for the matching funds being offered by philanthropists. Management is tremendously happy with us and has offered to support our expansion of Mailroom toward a distributed architecture capable of running calculations on matching funds across the donor database in parallel.

And that is a pretty good candidate for a functional programming approach.

Goal:
-----

Refactor Mailroom using map so that each donation on record can be doubled, tripled or indeed multiplied by any arbitrary factor based on the whims of philanthropists who would like to support our cause.

The program
-----------

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

Submission
----------

As always, put the new file in your student directory in an appropraite  ``session??`` directory, and add it to your clone early. Make frequent commits with good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.
