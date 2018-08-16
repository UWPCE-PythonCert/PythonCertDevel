.. _html_renderer_tutorial:

#######################################
Tutorial for the html render assignment
#######################################

If you are finding that you don't really know where to start with the html render assignemnt, this tutorial will walk you through the process.

However, you generally learn more if you figure things out for yourself. So I highly suggest that you give each step a try on your own first, before reading that step in this tutorial. Then, if you are really stuck -- follow the process here.

Step 1
------

Step one is a biggie -- that's 'cause you need a fair bit all working before you can actually have anything to test, really. But let's take it bit by bit.

First, we are doing test driven development, and we already have a test or two. So let's run those, and see what we get:

.. code-block:: bash

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 3 items

    test_html_render.py ..F                                                  [100%]

    =================================== FAILURES ===================================
    _____________________________ test_render_element ______________________________

        def test_render_element():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
            file_contents = render_result(e).strip()

            # making sure the content got in there.
    >       assert("this is some text") in file_contents
    E       AssertionError: assert 'this is some text' in 'just something as a place holder...'

    test_html_render.py:72: AssertionError
    ====================== 1 failed, 2 passed in 0.06 seconds ======================

Hey! that's pretty cool -- two tests are already passing! Let's take a quick look at those:

.. code-block:: python

    def test_init():
        """
        This only tests that it can be initialized with and without
        some content -- but it's a start
        """
        e = Element()

        e = Element("this is some text")

So that one simply tested that an Element class exists, and that you can pass in a string when you initialize it -- not a bad start, but it doesn't show that you can DO anything with it.


.. code-block:: python

    def test_append():
        """
        This tests that you can append text

        It doesn't test if it works --
        that will be covered by the render test later
        """
        e = Element("this is some text")
        e.append("some more text")

And this one shows that you can append some text -- nice, but again, it doesn't really do anything. But it does show you got the API right.

But this one failed:

.. code-block:: python

    def test_render_element():
        """
        Tests whether the Element can render two pieces of text
        So it is also testing that the append method works correctly.

        It is not testing whether indentation or line feeds are correct.
        """
        e = Element("this is some text")
        e.append("and this is some more text")

        # This uses the render_results utility above
        file_contents = render_result(e).strip()

        # making sure the content got in there.
        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents

        # make sure it's in the right order
        assert file_contents.index("this is") < file_contents.index("and this")

        # making sure the opening and closing tags are right.
        assert file_contents.startswith("<html>")
        assert file_contents.endswith("</html>")

OK -- this one really does something real -- it tries to render an html element -- which did NOT pass -- so it's time to put some real functionality in the Element class.

This is the code:

.. code-block:: python

    class Element(object):

        def __init__(self, content=None):
            pass

        def append(self, new_content):
            pass

        def render(self, out_file):
            out_file.write("just something as a place holder...")

Looking there, we can see why the tests did what they did -- we have the three key methods, but they don't actually do anything. But the ``render`` method is the only one that actually provides some results to test.

So back to the assignment:

    The Element class should a class attribute for the tag name ("html" first)

each html element has a different "tag", specifying what kind of element it is. so our class needs one of those. Why a class attribute? because each *instance* of each type (or class) of element will share the same tag.  And we don't want to store the tag in the render method, because then we couldn't reuse that render method for a different type of element.

So we need to add a tiny bit of code:

.. code-block:: python

    class Element(object):

        tag = "html"

        def __init__(self, content=None):
            pass

That's not much -- will the test pass now? Probably not, we aren't doing anything with the tag. But you can run it to see if you like. It's always good to run tests frequently to make sure you haven't inadvertently broken anything.





