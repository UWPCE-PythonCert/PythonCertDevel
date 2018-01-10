.. _exercise_mailroom_package:

Mailroom -- as a Python Package
===============================

The mailroom program, particularly the Object Oriented version, is a pretty complete system -- if you wanted to make it available for others to test snd run, making a "proper" python package is a great idea.

Code Structure
--------------

Start with an Object Oriented mailroom.

It should already be structured with the "logic" code distinct from the user interface (yes, a command line *is* a user interface). But you may have it all in one file. This isn't *too* bad for such a small program, but as a program grows, you really want to keep things separate, in a well organized package.

The first step is to re-structure your code into separate files:

 - one (or more) for the logic code (the Donor and DonorDB classes)
 - one for the user-interface code
 - one (or more) for tests.

Then you are going to want a top-level script file that does little but import the ui code and run a ``main()`` function.

Put all these in a python package structure, something like this::

  mailroom
      setup.py
      mailroom\
          __init__.py
          model.py
          ui
          tests\
              test_model.py
              test_ui.py
      scripts
          mailroom.py

You will need to import the logic code from model.py in the ui code in order to use it. You can wait until you learn about mocking to write the code in test_ui.py









