#!/usr/bin/env python

"""
Simple iterator example

This is a solution to an class-based iterator that
simulates the range() built in.

The range() API:

range(stop) -> range object

range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).

NOTE: this is a bit of an tricky API:

With one argument, the value is the "stop" value

With two or three arguments, the first value is "start", and the second "stop"

That isn't really relevent to the iterator issue, but still a good thing to know about.

"""

import pytest


class MyRange(object):
    """
    About as simple an iterator as you can get:

    returns the sequence of numbers from zero to 4
    ( like range(4) )
    """
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("MyRange() arg 3 must not be zero")
        if stop is None:
            stop = start
            start = 0
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        # reset on re-iterating
        self.current = self.start - self.step
        return self

    def __next__(self):
        try:
            self.current += self.step
        except AttributeError:
            raise TypeError('MyRange object is not an iterator -- it is an "iterable"\n'
                            'That is, iter() needs to be called on it to obtain an iterator')
        if self.step > 0:
            if self.current < self.stop:
                return self.current
            else:
                raise StopIteration
        else:
            if self.current > self.stop:
                return self.current
            else:
                raise StopIteration

    def __len__(self):
        """
        define length, so it will look more like range()
        """
        l = (self.stop - self.start) // self.step
        return l if l > 0 else 0

# putting the tests in teh same module
# usually one would putthe tests in a separate module, but this is small enough

# they can be run with pytest:
# $ pytest iterator_solution.py

# whilethe most common way to use an iterator is a for loop, you can also pass an
# iterator to many other funcitons, such as the list() constructor
#
# list() is used in the tests, as it's a lot easier to test if you get the list
# expected than if a for loop ran correctly.
#
# in this case, we can compare to what hte built-in range does...


@pytest.mark.parametrize('stop', [3, 10, 0])
def test_just_stop(stop):
    """
    The MyRange object should produce a list that's the right length
    and have all integers in it.
    """

    assert list(MyRange(stop)) == list(range(stop))


def test_renter():
    """
    iterating part way through, and then again should reset the iterator
    """

    r = MyRange(10)
    for i in r:
        if i > 5:
            break

    assert list(r) == list(range(10))


def test_start_stop():
    """
    what if there is a start an a stop value?
    """

    assert list(MyRange(2, 10)) == list(range(2, 10))


# this generates tests for a bunch of possible values
@pytest.mark.parametrize("start, stop, step",
                         [(0, 10, 1),
                          (3, 10, 2),
                          (10, 20, 2),  # should return zero-length iteratorable
                          # (0, 10, -1),
                          ])
def test_start_stop_step(start, stop, step):
    """
    What if there is a start, stop and step value?
    """
    assert list(MyRange(start, stop, step)) == list(range(start, stop, step))


@pytest.mark.parametrize("start, stop, step", [(10, 0, -1),
                                               (10, 2, -2),
                                               (2, 10, -3),
                                               ])
def test_negative_step(start, stop, step):
    """
    negative step should iterate backwards
    """
    assert list(MyRange(start, stop, step)) == list(range(start, stop, step))


def test_zero_step():
    """
    range() raises a value error for a zero step

    MyRange should to.
    """
    with pytest.raises(ValueError):
        MyRange(2, 10, 0)


@pytest.mark.parametrize("start, stop, step", [(10, 0, -1),
                                               (10, 2, -2),
                                               (2, 10, -3),
                                               (4, 4, 1),
                                               (10, 5, 1),
                                               ])
def test_length(start, stop, step):
    """
    Despite not storing all the numbers, range() does support len()
    """
    assert len(MyRange(10)) == 10

    assert len(MyRange(5, 4)) == 0
    assert len(MyRange(start, stop, step)) == len(range(start, stop, step))
