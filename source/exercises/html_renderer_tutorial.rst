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

Back to the task at hand:

  The class should have an ``append`` method that can add another string to the content.

  ...

  So your class will need a way to store the content in a way that you can keep adding more to it.

OK, so we need a way to store the content -- both what gets passed in to the ``__init__`` and what gets added with the append method.  WE need a data structure that can hold an ordered list of things, and can be added to in the future -- sounds like a list to me. So let's create a list in __init__ and store it in ``self`` for use by the other methods:

.. code-block:: python

    def __init__(self, content=None):
        self.contents = [content]

    def append(self, new_content):
        self.contents.append(new_content)

OK -- let's run the tests and see if anything changed::

    >       assert("this is some text") in file_contents
    E       AssertionError: assert 'this is some text' in 'just something as a place holder...'

    test_html_render.py:72: AssertionError

nope -- still failed at the first assert in test_render. Which makes sense, we haven't done anything with the render method yet!

From the assignemnt:

  It should have a ``render(file_out)`` method that renders the tag and the strings in the content.

we have the render method -- but it's rending arbitrary text to the file -- not an html tag or contents. So let's add that. First let's add the contents, adding a newline in between to keep it readable.  Remember that there can be multiple pieces of content -- so we need to loop though the list:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write(content)
            out_file.write("\n")

And run the tests::

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
            assert("this is some text") in file_contents
            assert("and this is some more text") in file_contents

            # make sure it's in the right order
            assert file_contents.index("this is") < file_contents.index("and this")

            # making sure the opening and closing tags are right.
    >       assert file_contents.startswith("<html>")
    E       AssertionError: assert False
    E        +  where False = <built-in method startswith of str object at 0x10e23fcf0>('<html>')
    E        +    where <built-in method startswith of str object at 0x10e23fcf0> = 'this is some text\nand this is some more text'.startswith

    test_html_render.py:79: AssertionError
    ====================== 1 failed, 2 passed in 0.05 seconds ======================

Failed in test_render again -- but look carefully -- it didn't fail on the first assert! It failed on this line::

  assert file_contents.startswith("<html>")

which makes sense, we haven't rendered anything like that yet. So let's add that now. Recall that we want the results to look something like this:

.. code-block:: html

    <html>
    Some content.
    Some more content.
    </html>

In this case, the "html" part is stored in a class attribute. So how would you make that tag? Looks like a good place for string formatting::

  "<{}>".format(self.tag)

and

  "</{}>".format(self.tag)

So the method looks something like this:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

Now run the tests again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 3 items

    test_html_render.py ...                                                  [100%]

    =========================== 3 passed in 0.02 seconds ===========================

Whoo Hoo!  All tests pass! But wait, there's more -- comprehensive testing is difficult -- we tested that you could initialize the elemnt with one piece of content, and then add another.  But what if you initialized it with nothing, and then added some?  Uncomment the next test: ``test_render_element2`` -- and see what you get.

This is what I got with my code::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 4 items

    test_html_render.py ...F                                                 [100%]

    =================================== FAILURES ===================================
    _____________________________ test_render_element2 _____________________________

        def test_render_element2():
            """
            Tests whether the Element can render two pieces of text
            So it is also testing that the append method works correctly.

            It is not testing whether indentation or line feeds are correct.
            """
            e = Element()
            e.append("this is some text")
            e.append("and this is some more text")

            # This uses the render_results utility above
    >       file_contents = render_result(e).strip()

    test_html_render.py:95:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Element object at 0x10c4d5c88>
    out_file = <_io.StringIO object at 0x10c4881f8>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

    html_render.py:23: TypeError
    ====================== 1 failed, 3 passed in 0.08 seconds ======================

Darn -- something is wrong here.




