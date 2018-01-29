#!/usr/bin/env

"""
A couple nifty context managers
"""

class Raises:
    def __init__(self, *args):
        print("initializing:", args)
        self.exceptions = args

    def __enter__(self):
        """nothing to be done here."""
        print("in enter")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Here's where we check the exceptions """
        print("exiting:", exc_type)
        if exc_type in self.exceptions:
            # tests pass
            return True
        else:
            if exc_type is None:
                msg = "No error was raised -- expected one of {}".format(self.exceptions)
            else:
                msg = "{} raised -- expected {}".format(exc_type, self.exceptions)
            assert False, msg
