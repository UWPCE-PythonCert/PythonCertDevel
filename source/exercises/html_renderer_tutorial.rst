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

.. _render_tutorial_2_A:

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

Success!. WE now have three different tags.

.. note::
  Why the ``Html`` element? doesn't the ``Element`` class already use the "html" tag?
  Indeed it does -- but the goal of the ``Element`` class is to be a base class for the other tags, rather than being a particular element.
  Sometimes this is called an "abstract base class": a class that can't do anything by itself, but exists only to provide an interface (and partial functionality) for subclasses.
  But we wanted to be able to test that partial functionality, so we had to give it a tag to use in the initial tests.
  If you want to be pure about it -- you could use something like "abstract_tag" in the ``Element`` class to make it clear that it isn't supposed to be used alone.  And later on in the assignment, we'll be adding extra functionality to the ``Html`` element.

Making a subclass where the only thing you change is a single class attribute may seem a bit silly -- and indeed it is. If that were going to be the ONLY difference between all elements, There would be other ways to accomplish that task that would make more sense -- perhaps passing the tag in to the initializer, for instance. But have patience, as we proceed with the exercise, some element types will have more customization.

But another thing to keep in mind -- the fact that that is ALL we need to do to get a new type of element demonstrates the power of subclassing -- with that tiny change, we get a new element that we can add content to, and render to a file, etc. With virtually no repeated code.

.. _render_tutorial_2_B:

Part B:
.......

Now it gets more interesting, and challenging!

The goal is to be able to render nested elements, like so:

.. code-block:: html

    <html>
    <body>
    <p>
    a very small paragraph
    </p>
    <p>
    Another small paragraph.
    This one with multiple lines.
    </p>
    </body>
    </html>

This means that we need to be able to append not just text to an element, but also other elements.  The appending is easy -- the tricky bit is when you want to render those enclosed elements.

Let's take this bit by bit -- first with a test or two.
Uncomment ``test_subelement`` in the test file, and run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py .......F                                             [100%]

    =================================== FAILURES ===================================
    _______________________________ test_sub_element _______________________________

        def test_sub_element():
            """
            tests that you can add another element and still render properly
            """
            page = Html()
            page.append("some plain text.")
            page.append(P("A simple paragraph of text"))
            page.append("Some more plain text.")

    >       file_contents = render_result(page)

    test_html_render.py:163:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Html object at 0x1032f8438>
    out_file = <_io.StringIO object at 0x10325b5e8>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
    >           out_file.write(content)
    E           TypeError: string argument expected, got 'P'

    html_render.py:26: TypeError
    ====================== 1 failed, 7 passed in 0.11 seconds ======================

Again, the new test failed -- no surprise, we haven't written any new code yes. But do read the report carefully -- it did not fail on an assert -- but rather with a ``TypeError``.  The code itself raised an exception before it could produce results to test.

So now it's time to write the code -- look at where the exception was raised: line 26 in my code, inside the ``render()`` method. The line number will likely be different in your code, but it probably failed on the render method. Looking closer at the error::

    >           out_file.write(content)
    E           TypeError: string argument expected, got 'P'

It occurred in the file ``write`` method, complaining that it expected to be writing a string to the file, but it got a 'P' -- 'P' is the name of the paragraph element class. So we need a way to write an element to a file. How might we do that? Inside the element's render method, we need to render an element...

Well, elements already know how to render themselves -- this is what is meant by a recursive approach -- in the ``render`` method, we want to make use of the ``render`` method itself.

Looking at the signature of the render method::

.. code-block:: python

      def render(self, out_file):

it becomes clear -- we render an element by passing the output file to the element's render method. Here is what mine looks like now:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

So let's update our render by replacing that ``out_file.write()`` call with  a call to the content's ``render`` method:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            # out_file.write(content)
            content.render(out_file)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

And let's see what happens when we run the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py ..FFFFFF                                             [100%]

    =================================== FAILURES ===================================

    ... lots of failures here

    _______________________________ test_sub_element _______________________________

        def test_sub_element():
            """
            tests that you can add another element and still render properly
            """
            page = Html()
            page.append("some plain text.")
            page.append(P("A simple paragraph of text"))
            page.append("Some more plain text.")

    >       file_contents = render_result(page)

    test_html_render.py:163:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
    test_html_render.py:30: in render_result
        element.render(outfile)
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.Html object at 0x10b10dfd0>
    out_file = <_io.StringIO object at 0x10b123828>

        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>\n".format(self.tag))
                # out_file.write(content)
    >           content.render(out_file)
    E           AttributeError: 'str' object has no attribute 'render'

    html_render.py:27: AttributeError
    ====================== 6 failed, 2 passed in 0.12 seconds ======================

Whoaa! six failures! We really broke something! But that is a *good* thing -- it's the whole point of unit tests -- when you are making a change to address one issue, you know right away that you broke previously working code.

So let's see if we can fix these tests, while still allowing us to add the feature we intended to add.

Again -- look carefully at the error, and the solution might pop out at us::

    >           content.render(out_file)
    E           AttributeError: 'str' object has no attribute 'render'

Now we are trying to call a piece of content's ``render`` method, but we got a simple string, which does not *have* a ``render`` method.
This is the challenge of this part of teh excercise -- it's easy to render a string, and it's easy to render an element, but the content list could have either one -- so how do we switch between the two methods?

There are a number of approaches you can take. This is a good time to read the notes about this here: :ref:`notes_on_handling_duck_typing`.
You may want to try one of the more complex methods -- but for now, we're going to use the one that suggests itself from the error.

We need to know whether we want to call a ``render()`` method, or simply write the content to the file. How would we know which to do? Again, look at the error:
We tried to call the render() method of a piece of content, but got an ``AttributeError``. So the way to know whether we can call a render method is to try to call it -- if it works, great! If not, we can catch the exception, and do something else. In this case, the something else is to try to write the content directly to the file:

.. code-block:: python

    def render(self, out_file):
        # loop through the list of contents:
        for content in self.contents:
            out_file.write("<{}>\n".format(self.tag))
            try:
                content.render(out_file)
            except AttributeError:
                out_file.write(content)
            out_file.write("\n")
            out_file.write("</{}>\n".format(self.tag))

And run the tests again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 8 items

    test_html_render.py ........                                             [100%]

    =========================== 8 passed in 0.03 seconds ===========================

Yeah! all eight tests pass!  I hope you found that at least a little bit satisfying.  And pretty cool, really, only two extra lines of code. This is an application of the EAFP method: it's Easier to Ask Forgiveness than Permission. You simply try to do one thing, and if that raises the exception you expect, than do something else.

It's also taking advantage of Python's "Duck Typing" notice that we don't know if that piece of content is actually an ``Element`` object -- all we know is that it has a render() method that we can pass a file-like object to. Which is quite deliberate -- if some future user (that might be you) wants to write their own element type, that can do that -- and all it needs to do is define a render method.

So what are the downsides? Well, there are two:

1. When we successfully call the ``render`` method, we have no idea if it's actually done the right thing -- it could do anything -- if someone puts some completely unrelated object in the content list that happens to have a render method, this is not going to work -- but what are the odds of that?

2. This is the bigger one -- if the object *HAS* a render method, but that render method has something wrong with it, then it could conceivably raise an AttributeError itself -- but it would not be the Attribute Error we are expecting. The trick here is that this is very hard to debug.

However, we are saved by tests. If the render method works in all the other tests, It's not going to raise an AttributeError only in this case. Another reason to have a good test suite.


.. _render_tutorial_3:

Step 3:
-------

Now we are getting a little more interesting.

"Create a ``<head>`` element -- a simple subclass."

This is easy -- you know how to do that, yes?

But the training wheels are off -- you are going to need to write your own tests now.  So before you create the ``Head`` element class, write a test for it. You should be able to copy and paste one the previous tests, and just change the name of the class and the tag text. Remember to give it a new name, or it will simply replace the previous test.

I like to run the tests as soon as I make a new one -- if nothing else, I can make sure I have one more test!

OK, that should have been straightforward.  Now this part:

  Create a ``OneLineTag`` subclass of ``Element``:

  * It should override the render method, to render everything on one line -- for the simple tags, like::

      <title> PythonClass - Session 6 example </title>

Some html elements don't tend to have a lot content -- like the document title. So it makes sense to render them all on one line.  This is going to require a new render method.  Since there are multiple types of elements that should be rendered on one line, we want to create a base class for all one-line elements. It should subclass from Element, and override the render method with a new one, which will be pretty much the same as the main ``Element`` method, but without the newlines.

Before we do that though -- let's write a test for that!  as the ONeLIneTag class is a base class for actual elements that should be rendered on one line, we really don't need to write a test directly for it. We can write one for its first subclass: ``Title``. The title elements should be rendered something like this::

    <title> PythonClass - title example </title>

Which should be generated by code like this::

    Title("PythonClass - title example")

Take a look at one of the other tests to get ideas -- and maybe start with a copy and paste, and then change the names:

.. code-block:: python

    def test_title():
        e = Title("this is some text")
        e.append("and this is some more text")

        file_contents = render_result(e).strip()

        assert("this is some text") in file_contents
        assert("and this is some more text") in file_contents
        print(file_contents)
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")

That's not going to pass, as there is no ``Title`` class. But before we get that far -- what else do we need to change about this test?
For starters, this test is appending additional content.
That's not very likely for a title, is it? So let's get rid of that line.

.. code-block:: python

    def test_title():
        e = Title("This is a Title")

        file_contents = render_result(e).strip()

        assert("This is a Title") in file_contents
        print(file_contents)
        assert file_contents.startswith("<title>")
        assert file_contents.endswith("</title>")

So that's a bit cleaner.  But let's look at those asserts -- what are we testing for?  Looks like we're testing for the correct start and end tags, and that the content is there. That's a pretty good start, but it isn't checking for newlines at all.  In fact, all the previous tests would pass even if our render method did not have any newlines in it at all. Which is probably OK -- html does not require newlines.  You could go back and update the tests to check for the proper newlines, though later on, when we get to indenting, we'll be doing that anyway.

But for this element, we want to make sure that we don't have any newlines. So let's add an assert for that:

.. code-block:: python

    assert "\n" not in file_contents

You can run the tests now if you like -- it will fail due to there being no Title element. So let's make one now. Remember that we want to start with a ``OneLineTag`` element, and then subclass ``Title`` from that.

.. code-block:: python

    class OneLineTag(Element):
        pass


    class Title(OneLineTag):
        tag = "title"

The ``pass`` means "do nothing" -- but it is required to satisfy PYhton -- there needs to be *something* in the class definition.  So in this case, we have a ``OneLineTag`` class that is exactly the same as the Element class.  And a Title class that is the same except for the tag. Time to test again::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 10 items

    test_html_render.py .........F                                           [100%]

    =================================== FAILURES ===================================
    __________________________________ test_title __________________________________

        def test_title():
            e = Title("This is a Title")

            file_contents = render_result(e).strip()

            assert("This is a Title") in file_contents
            print(file_contents)
            assert file_contents.startswith("<title>")
            assert file_contents.endswith("</title>")
    >       assert "\n" not in file_contents
    E       AssertionError: assert '\n' not in '<title>\nThis is a Title\</title>'
    E         '\n' is contained here:
    E           <title>
    E         ? -------
    E           This is a Title
    E           </title>

    test_html_render.py:203: AssertionError
    ----------------------------- Captured stdout call -----------------------------
    <title>
    This is a Title
    </title>
    ====================== 1 failed, 9 passed in 0.12 seconds ======================

The title test failed on this assertion::

    >       assert "\n" not in file_contents

which is what we expected -- we haven't written a new render method yet.  But look at the end of the output -- where is says ``-- Captured stdout call --``.  That is showing you how the title element is being rendered -- with the newlines. That's there because there is a print in the test:

.. code-block:: python

  print(file_contents)

.. note::

  pytest is pretty slick with this. It "Captures" the output from print calls, etc, and then only shows them to you if a test fails.
  So you can sprinkle print calls into your tests, and it won't clutter the output -- you'll only see it when a test fails, which is when you need it.

This is a good exercise to go through -- if a new test fails, it lets you know that it is indeed working -- testing what it is supposed to test.

So how do we get this test to pass? We need a new render method for ``OneLineTag``.  For now, you can copy the render method from ``Element`` to ``OneLineTag``, and remove the newlines:

.. code-block:: python

    class OneLineTag(Element):
        def render(self, out_file):
            # loop through the list of contents:
            for content in self.contents:
                out_file.write("<{}>".format(self.tag))
                try:
                    content.render(out_file)
                except AttributeError:
                    out_file.write(content)
                out_file.write("</{}>\n".format(self.tag))

notice that I left the newline in at the end of the closing tag -- we do want a newline there, so the next element won't get rendered on the same line.  And the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 10 items

    test_html_render.py ..........                                           [100%]

    ========================== 10 passed in 0.03 seconds ===========================

We done good.  But wait! there *is* a newline at the end, and yet the assert: `assert "\n" not in file_contents` passed!  Why is that?

Take a look at the code in the tests that renders the element:

.. code-block:: python

    file_contents = render_result(e).strip()

It's calling ``.strip()`` on the rendered string.  That will remove all whitespace from both ends -- removing that last newline.

However, there is still some extra code in that ``render()`` method.  It's still looping through the contents and checking for an ``Element`` type. But for this, we hope that there will only be one piece of content, and it should not be an element. So we can make the render method simpler:

.. code-block:: python

    class OneLineTag(Element):
        def render(self, out_file):
            out_file.write("<{}>".format(self.tag))
            out_file.write(self.contents[0])
            out_file.write("</{}>\n".format(self.tag))

If you are nervous about people appending content that will then be ignored, you can override the append method, too:

.. code-block:: python

    def append(self, content):
        raise NotImplementedError

``NotImplementedError`` means just what it says -- this method is not implemented.  My tests still pass, but how do I test to make sure that I can't append to a OneLineTag? Let's try that:

.. code-block:: python

    def test_one_line_tag_append():
        """
        You should not be able to append content to a OneLineTag
        """
        e = OneLineTag("the initial content")
        e.append("some more content")

        file_contents = render_result(e).strip()
        print(file_contents)

and run the tests::

    test_html_render.py:199:
    _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    self = <html_render.OneLineTag object at 0x1020bb198>
    content = 'some more content'

        def append(self, content):
    >       raise NotImplementedError
    E       NotImplementedError

    html_render.py:57: NotImplementedError
    ===================== 1 failed, 10 passed in 0.09 seconds ======================

hmm -- it raised a NotImplementedError, whih is what we want -- but it is logging as a test failure.  An exception raised in a test is going to cause a failure -- but what we want is for the test to pass only *if* that exception is raised.
Fortunately, pytest has a utility to do just that. make sure there is an ``import pytest`` in your test file, and then add this code:

.. code-block:: python

    def test_one_line_tag_append():
        """
        You should not be able to append content to a OneLineTag
        """
        e = OneLineTag("the initial content")
        with pytest.raises(NotImplementedError):
            e.append("some more content")

that ``with`` is a "context manager" (kind of like the file open one). More on that later in the course, but what this means is that the test will pass if an only if the code inside that ``with`` block raised a ``NotImplementedError``.  If it raises something else, or it doesn't raise an exception at all -- then the test will fail.

OK -- I've got 11 tests passing now. How about you? Time for the next step.

.. _render_tutorial_4:

Step 4.
-------

Now we want to make our elements more feature-full -- supporting attributes to the tag.  First, a tiny bit of html (XML) reminder. elements can have both content and attributes.
(`html attributes <https://www.w3schools.com/html/html_attributes.asp>`_)
A full element might look like this:

<p id="warning" style="color:red">I am a paragraph</p>

each attribute is separated from the others by a space, and used the::

  attribute_name="attribute value"

form.

We need to add a few features to make this code work:
 * A way to pass the attributes to the ``Element.__init__``
 * A way to store the attributes
 * A way to render the attributes in the opening tag.

To pass the attributes in it would be nice to leverage smpiel keywork arguments like so:

.. code-block:: python

    Element("some text content", id="TheList", style="line-height:200%")

Remember test-driven development: let's write a test, and then we can make that code work. Here is my first simple test:

.. code-block:: python

    def test_attrs1():
        """
        test that attributes get rendered correctly
        """
        # create a P element with a couple attributes
        p = P("I am a paragraph", id="warning", style="color:red")
        # <p id="warning" style="color:red">I am a paragraph</p>

        file_contents = render_result(e).strip()
        print(file_contents)

        assert False

Note that I'm using the ``P`` element - I could use any element, as they all share the render method of the base class.  Note also that after creating the element, the test renders it, prints the result, and then has an ``assert False``. The ``assert False`` is a trick to assure that an incomplete test fails -- that way, we will see what's printed. And we want to be sure it fails because it doesn't yet test if the element is rendered correctly. Running the tests::

    $ pytest
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
    rootdir: /Users/Chris/Junk/lesson07, inifile:
    collected 12 items

    test_html_render.py ...........F                                         [100%]

    =================================== FAILURES ===================================
    _________________________________ test_attrs1 __________________________________

        def test_attrs1():
            """
            test that attributes get rendered correctly
            """
            # create a P element with a couple attributes
    >       p = P("I am a paragraph", id="warning", style="color:red")
    E       TypeError: __init__() got an unexpected keyword argument 'id'

    test_html_render.py:220: TypeError
    ===================== 1 failed, 11 passed in 0.15 seconds ======================












