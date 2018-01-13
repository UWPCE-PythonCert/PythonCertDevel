#!/usr/bin/env python

"""
a re-implementation of the built-in range object

Not that there is any reason to do so, but it is a good
exercise in understanding the iterator protocol
"""

from operator import index

class range2:
    def __init__(self, start, stop=None, step=None):
        # some logic to handle the optional interface
        if stop is None and step is None:
            self.stop = index(start)
            self.start = 0
            self.step = 1
        elif step is None:
            self.start = index(start)
            self.stop = index(stop)
            self.step = 1
        else:
            self.start = index(start)
            self.stop = index(stop)
            self.step = index(step)
        if step == 0:
            raise ValueError("range() arg 3 must not be zero")

    def __iter__(self):
        # reset when __iter__ is called
        print("iter called", self.start, self.stop, self.step)
        if self.step < 0:
            self.current = self.start - self.step
        else:
            self.current = self.start - self.step
        print(self.current)
        return self

    def __next__(self):
        self.current += self.step

        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        else:
            return self.current


