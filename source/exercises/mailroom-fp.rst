.. _exercise_mailroom_fp:


Mailroom - Functional
=====================

Making Mailroom Functional

A complete program
------------------

It was reasonable to build the simple MailRoom program using a single module, a simple data structure, and functions that manipulate that data structure. It was reasonable to refactor Mailroom around a class when it started to become unwieldy with all of the features we wanted to add to it.

Due to the success of Mailroom and the good PR it has generated with all its thank you letters, the donations are pouring in.  This has raised the attention of wealthy philanthropists who are willing to contribute matching funds.  Our problem now is to expand Mailroom so that it can run projections and account for matching funds offered by philanthropists.  Management is tremendously happy with us and has offered to support our expansion of Mailroom toward a distributed architecture capable of running calculations on matching funds across the donor database in parallel.

This is a good candidate for a functional programming approach.

Goal:
-----

1.  Add a new feature to Mailroom using map so that each donation on record can be doubled, tripled or indeed multiplied by any arbitrary factor based on the whims of philanthropists who would like to support our cause.

2.  Add a new feature to Mailroom using filter so that donations either above or below a specified dollar amount are included in the map operations of #1 above.

3.  Refactor the new features outlined in #1 and #2 above such that they can be used to run projections.  Imagine the following scenario.  You are an account manager out in the field meeting with philanthropists and talking with them about the many ways they might structure their matching contributions.  You would like a feature that could show them, based on past contributions, what their total contribution would become under differenc seenarios.  For instance, based on donations in the current database, show them (a) what their total contribution would come to in dollars if they were to double contributions under $100.  And then (b) show them what their total contribution would come to if they were to tripple contributions over $50.

Use map, filter and either sum or reduce to accomplish the goals above.

Submission
----------

As always, put the new file in your student directory in an appropraite  ``session??`` directory, and add it to your clone early. Make frequent commits with good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.
