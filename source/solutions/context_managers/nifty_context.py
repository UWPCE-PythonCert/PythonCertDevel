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
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """ Here's where we check the exceptions """
        if exc_type in self.exceptions:
            # tests pass
            return True
        else:
            if exc_type is None:
                msg = "No error was raised -- expected one of {}".format(
                      [e.__name__ for e in self.exceptions])
            else:
                if len(self.exceptions) == 1:
                    msg = "{} raised -- expected {}".format(exc_type.__name__,
                           self.exceptions[0].__name__)
                else:
                    msg = "{} raised -- expected one of: {}".format(
                           exc_type.__name__,
                           [e.__name__ for e in self.exceptions])

            assert False, msg
