########################
Reviewing Students' Code
########################

One of the most important services the program provides is code review. While for the most part the students will know if they have solved the problem (i.e. their code works) there is a lot they can learn about clean style, robust logic, appropriate data structures, Pythonicity, etc.

And they can only learn that if their code is reviewed and critiqued.

Scoring Assignments
===================

Exactly how to score the exercises is up to the individual instructor. But we do need to provide some score, so there is a clear requirement to passing the class.

As the course is pass/fail, I don't think it's important to distinguish between decent, good, and excellent work. So I tend to give full credit for a good-faith effort at an exercise, and let the review be the feedback they need.

Reviewing Rubric
================

The following Rubric provides some guidelines as to what to critique of the students' code:

Logic issues:
-------------

 - Is the basic logic correct?
 - Will it handle edge cases properly?
 - Is it using appropriate data types?

Code structure
--------------
 - DRY?
 - Separation of concerns
 - Good OO design (when they get there and its appropriate)

Pythonicity:
------------

Is the code Pythonic?

 - looping through a sequence  rather than indexing
 - EAFTP Exception handling
 - iterating rather that making copies
 - no mutables in default arguments

Style Issues:
-------------

 - PEP 8 compliance
 - variable names:
    - meaningful names -- not "key", "value", "foo"
    - one letter names only for index variables etc.
    - verbs for functions and methods
    - nouns for objects
    - plural for sequences of objects / singular for single items


