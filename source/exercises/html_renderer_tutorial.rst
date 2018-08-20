.. _html_renderer_tutorial:

#######################################
Tutorial for the html render assignment
#######################################

If you are finding that you don't really know where to start with the html render assignemnt, this tutorial will walk you through the process.

However, you generally learn more if you figure things out for yourself. So I highly suggest that you give each step a try on your own first, before reading that step in this tutorial. Then, if you are really stuck -- follow the process here.

.. _render_tutorial_1:

Step 1:
-------

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

So that one simply tested that an ``Element`` class exists, and that you can pass in a string when you initialize it -- not a bad start, but it doesn't show that you can *do* anything with it.


.. code-block:: python

    def test_append():
        """
        This tests that you can append text

        It doesn't test if it works --
        that will be covered by the render test later
        """
        e = Element("this is some text")
        e.append("some more text")

And this one shows that you can call the ``append()`` method with some text -- nice, but again, it doesn't test if that appended text was used correctly. But it does show you got the API right.

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

    The ``Element`` class should have a class attribute for the tag name ("html" first)

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

OK, so we need a way to store the content -- both what gets passed in to the ``__init__`` and what gets added with the ``append method``.  We need a data structure that can hold an ordered list of things, and can be added to in the future -- sounds like a list to me. So let's create a list in __init__ and store it in ``self`` for use by the other methods:

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

.. rubric:: 1c.

From the assignment:

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

Darn -- something is wrong here. And this time it errored out before it even got results to test.  So look and see exactly what the error is. (pytest does a really nice job of showing you the errors)::

                  out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

So it failed when we tried to write to the file. We're trying to write a piece of content, and we got a "NoneType".  How in the world did a "NoneType" (which is the type of None) get in there?

Where does the ``self.contents`` list get created? In the ``__init__``. Let's do a little print debugging here. Add a print to the __init__:

.. code-block:: python

    def __init__(self, content=None):
        self.contents = [content]
        print("contents is:", self.contents)

And run the tests again::

    >           out_file.write(content)
    E           TypeError: string argument expected, got 'NoneType'

    html_render.py:24: TypeError
    ----------------------------- Captured stdout call -----------------------------
    contents is: [None]
    ====================== 1 failed, 3 passed in 0.06 seconds ======================


Same failure -- but pytest does a nice job of showing you what was printed (stdout) when a test fails. So in this case, at the end of the ``__init__`` method, the contents list looks like ``[None]`` -- a list with a single None object in it. No wonder it failed later when we tried to write that None to a file!

But why? -- well, looking at the __init__ -- it looks like content gets set to None by default:

    def __init__(self, content=None):

and then we put that in the ``self.contents`` list.  What do we want went content is None?  An empty list, so that we can add to it later.  So you need some code that checks for ``None`` (hint: use ``is None`` or ``is not None`` to check for ``None``), and only adds content to the list if it is not None.

I'll leave it as an exercise for the reader to figure out how to do that -- but make sure all tests are passing before you move on! And once the tests pass, you may want to remove that ``print()`` line.

.. _render_tutorial_2:

Step 2:
-------

OK, we have nice little class here -- it has a class attribute to store information about the tag -- information that's the same for all instances.

And we are storing a list of contents in "self" -- information that each instance needs its own copy of.

And we are using that data to render an element.

So we're ready to move on:

Part A
......

.. rubric:: Instructions:


"Create a couple subclasses of ``Element``, for each of ``<html>``, ``<body>``, and ``<p>`` tags. All you should have to do is override the ``tag`` class attribute (you may need to add a ``tag`` class attribute to the ``Element`` class first, if you haven't already)."

So this is very straightforward -- we have a class that represents an element -- and the only difference between basic elements is that they have a different tag. for example::

    <body>
    Some content.
    Some more content.
    </body>

and::

    <p>
    Some content.
    Some more content.
    </p>


The ``<body>`` tag is for the entire contents of an html page, and the ``<p>`` tag is for a paragraph.  But you can see that form of the tags is identical, so we don't have to change much to make classes for these tags. In fact, all we need to change is the ``tag`` class attribute.

Before we do that -- let's do some test-driven development. Uncomment the next few tests in ``test_html_render.py``: ``test_html``, ``test_body``, and ``test_p``, and run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 7 items

    test_html_render.py ....FFF                                              [100%]

    =================================== FAILURES ===================================
    __________________________________ test_html ___________________________________

        def test_html():
    >       e = Html("this is some text")
    E       NameError: name 'Html' is not defined

    test_html_render.py:117: NameError
    __________________________________ test_body ___________________________________

        def test_body():
    >       e = Body("this is some text")
    E       NameError: name 'Body' is not defined

    test_html_render.py:129: NameError
    ____________________________________ test_p ____________________________________

        def test_p():
    >       e = P("this is some text")
    E       NameError: name 'P' is not defined

    test_html_render.py:142: NameError
    ====================== 3 failed, 4 passed in 0.08 seconds ======================

So we have three failure -- of course we do -- we haven't written code yet!  Yes, this is pedantic, and there is no real reason to run tests you know are going to fail -- but there is a reason to *write* tests that you know are going to fail -- and you have to run them to know that you have written them correctly.

Now we can write the code for those three new element types. Try to do that yourself first, before you read on.

OK -- did you do something as simple as this?

.. code-block:: python

    class Body(Element):
        tag = 'body'

(and similarly for ``Html`` and ``P``)

That's it!  But what does that mean?  This line:

``class Body(Element):``

means: make a new subclass of the ``Element`` tag called "Body".

and this line:

``    tag = 'body'``

means:  set the "tag" class attribute to 'body'. Since this class attribute was set by the Element tag already -- this is called "overriding" the tag attribute.

The end result is that we now have a class that is exactly the same as the Element class, except with a different tag. Where is that attribute used? It is used in the ``render()`` method.

Let's  run the tests and see if this worked::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 7 items

    test_html_render.py .......                                              [100%]

    =========================== 7 passed in 0.02 seconds ===========================

Success!.

.. note::
  Why the ``Html`` element? doesn't the ``Element`` class already use the "html" tag?
  Indeed it does -- but the goal of the ``Element`` class is to be a base class for the other tags, rather than being a particular element.
  Sometimes this is called an "abstract base class": a class that can't do anything by itself, but exists only to provide an interface (and partial functionality) for subclasses.
  But we wanted to be able to test that partial functionality, so we had to give it a tag to use in the initial tests.
  If you want to be pure about it -- you could use something like "abstract_tag" in the ``Element`` class to make it clear that it isn't supposed to be used alone.  And later on in the assignment, we'll be adding extra functionality to the ``Html`` element.














