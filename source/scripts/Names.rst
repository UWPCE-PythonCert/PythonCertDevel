:orphan:

.. _script_names:


Names
=====

With Rick Riehle


Intro
-----

*  Variables

*  Mutability and copying

*  If you're coming from C or perhaps any statically compiled language, perhaps even regardless of your programming background, these next few topics may help prevent confusion and dispel some of Python's magic.


Variables, references or names?
-------------------------------

*  What are variables in Python?
*  They're not variables!
*  To try to figure out what they are, let's take a look under the hood.

$ ipython

dir()

*  There are already a few things in our workspace.  As an aside, perhaps it would be better to think of this as a namespace rather than as a workspace.  Why should become more clear as we move along.

x = 1
type(x)

int?

*  Is this helpful?  What are we really looking at here?  It looks like 'int' in addition to being a type is also a function.  Okay, good to know,  Let's look more directly at x.

dir(x)

*  Woah. Looks like a whole lotta stuff here in this namespace.  Many interesting dunders, but let's look at these things without leading underscores.

x.bit_length?
x.bit_length
x.bit_length()

x.conjugate?
x.conjugate()

x.__abs__?
x.__abs__()

*  Let's try __abs__() on a slightly more interesting value

y = -2
y.__abs__()

x
z = x
z
x == z
x is z

y
z = y
z
y == z
y is z
id(y)
id(z)

*  We've now been able to point z at x and then at y.  What does that make z?  Would you call it a varriable?  For that matter what are x and y?  Now that y is z and z is y, what happens if we delete y?

del(y)
y

z
id(z)

*  Variables?  Pointers?  References?  Names?  Symbols?  Identities?
*  When experienced coders are being careful about language they seem to generally prefer 'Names' or 'Symbols' to identify these things.
*  Notwithstanding the present deepdive into the issue, I'm not much for terminology.  In this case, however, to think of these objects as 'variables' can cause confusiton.

