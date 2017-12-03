#!/usr/bin/env python3

"""
test code for the object_canvas
"""
import os

import object_canvas as oc

def test_init():
    canvas = oc.ObjectCanvas()

    assert canvas


def test_polyline():
    """
    can we draw a polyline?
    """
    canvas = oc.ObjectCanvas()
    points = ((10, 10),  # this should be a triangle
              (10, 400),
              (400, 10),
              (10, 10),
              )

    pl = oc.PolyLine(points)
    canvas.add_object(pl)
    canvas.render("junk.png")

    assert os.path.isfile("junk.png")
    assert False

