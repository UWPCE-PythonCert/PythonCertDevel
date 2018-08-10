.. _exercise_trigrams:

=========================================
Kata Fourteen: Tom Swift Under Milk Wood
=========================================

Adapted from Dave Thomas's work:

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/


Trigrams
=========

Trigrams can be used to mutate text into new, surreal, forms. But what
heuristics do we apply to get a reasonable result?

The Problem
------------

As a boy, one of my treats was go to the shops on a Saturday and spend part
of my allowance on books; for a nine-year old, I had quite a collection of
Tom Swift and Hardy Boys. Wouldn’t it be great to be able to create
more and more of these classic books, to be able to generate a new Tom
Swift adventure on demand?


OK, perhaps not. But that won’t stop us trying. I coded up a quick
program to generate some swash-buckling scientific adventure on demand. It
came up with:

    ... it was in the wind that was what he thought was his companion. I
    think would be a good one and accordingly the ship their situation
    improved. Slowly so slowly that it beat the band! You’d think no one
    was a low voice. "Don’t take any of the elements and the
    inventors of the little Frenchman in the enclosed car or cabin completely
    fitted up in front of the gas in the house and wringing her hands.
    "I’m sure they’ll fall!"

    She looked up at them. He dug a mass of black vapor which it had
    refused to accept any. As for Mr. Swift as if it goes too high I’ll
    warn you and you can and swallow frequently. That will make the airship was
    shooting upward again and just before the raid wouldn’t have been
    instrumental in capturing the scoundrels right out of jail."


Stylistically, it’s Victor Appleton meets Dylan Thomas. Technically,
it’s all done with trigrams.

Trigram analysis is very simple. Look at each set of three adjacent words
in a document. Use the first two words of the set as a key, and remember
the fact that the third word followed that key. Once you’ve finished,
you know the list of individual words that can follow each two word
sequence in the document. For example, given the input::

  I wish I may I wish I might

You might generate::

    "I wish" => ["I", "I"]
    "wish I" => ["may", "might"]
    "may I"  => ["wish"]
    "I may"  => ["I"]


This says that the words "I wish" are twice followed by the word
"I", the words "wish I" are followed once by "may" and once by "might"
and so on.

To generate new text from this analysis, choose an arbitrary word pair as a
starting point. Use these to look up a random next word (using the table
above) and append this new word to the text so far. This now gives you a
new word pair at the end of the text, so look up a potential next word
based on these. Add this to the list, and so on. In the previous example,
we could start with "I may". The only possible next word is
"I", so now we have::

  I may I

The last two words are "may I", so the next word is
"wish". We then look up "I wish", and find our choice
is constrained to another "I".::

   I may I wish I


Now we look up "wish I", and find we have a choice. Let’s
choose "may"::

   I may I wish I may

Now we’re back where we started from, with "I may."
Following the same sequence, but choosing "might" this time, we
get::

   I may I wish I may I wish I might

At this point we stop, as no sequence starts "I might."


Given a short input text, the algorithm isn’t too interesting. Feed
it a book, however, and you give it more options, so the resulting output
can be surprising.

For this kata, try implementing a trigram algorithm that generates a couple
of hundred words of text using a book-sized file as input.
`Project Gutenberg <http://www.gutenberg.org/>`_ is a good source of online
books (Tom Swift and His Airship is `here <http://sailor.gutenberg.org/etext02/03tom10.txt>`_.)

Be warned that these files have DOS line endings (carriage return followed by
newline).


There is a copy of Sherlock Holmes right here:

:download:`sherlock.txt  <./sherlock.txt>`.

And a shorter copy for testing:

:download:`sherlock_small.txt  <./sherlock_small.txt>`.


Objectives
-----------

Kata’s are about trying something many times. In this one, what
we’re experimenting with is not just the code, but the heuristics of
processing the text. What do we do with punctuation? Paragraphs? Do we have
to implement backtracking if we chose a next word that turns out to be a
dead end?

I’ll fire the signal and the fun will commence...

Developing Your Solution
========================

This assignment has two parts: the key one is the trigrams exercise itself, but you also need to do some text processing to get a full book in shape for processing.

I suggest you write the trigrams part first -- it's more interesting :-)

trigrams
--------

Key to the trigrams problem is what data structure to use to hold the "trigrams themselves" -- what do we need here?

The text
........

First, you'll want a bit of text to try your code out on -- why not try the example here::

  I wish I may I wish I might

You need that in a python data structure somehow, so how about:

.. code-block:: python

    words = "I wish I may I wish I might".split()

which results in an (ordered) list of words::

  ['I', 'wish', 'I', 'may', 'I', 'wish', 'I', 'might']

Now you've got some words to play with. Once you think you've got it working, try a bit longer piece of text. But this will do for now, and it's small and simpile enough that you can immediately see if your code is working.

The trigrams structure
----------------------

From above, this is what you need to build up something like this::

    "I wish" => ["I", "I"]
    "wish I" => ["may", "might"]
    "may I"  => ["wish"]
    "I may"  => ["I"]

hmm -- in a way, that's almost pseudo code: You have a bunch of word pairs, and for each word pair, there are one or more works that follow it.

Those words look a lot like they are in a list, yes? Perfect -- it keeps order, and you can keep adding (appending) new words to it.

Each of those lists of words needs to be mapped to a particular pair. Each pair is unique -- it only shows up once (when that same pair is encountered again in the text, you add the follower to the list).

That sounds a a lot like a dictionary - the keys (word pairs) are unique, and map to a list of following words.

Now you have a choice -- the keys are a pair of words -- they can be represented as a string of two words with a space like so:

.. code-block:: python

    trigrams = {"I wish": ["I", "I"],
                "wish I": ["may", "might"],
                "may I": ["wish"],
                "I may": ["I"],
                }

But strings are not the only type that you can use as keys in a dict -- you can use any *immutable* type. Since the pairs of words are, well, a pair, it makes sense to store them in a tuple, keeping the individual words separate:

.. code-block:: python

    trigrams = {("I", "wish"): ["I", "I"],
                ("wish", "I"): ["may", "might"],
                ("may", "I"): ["wish"],
                ("I", "may"): ["I"],
                }

I like that better, but either one will work.

Building the Trigrams dict
..........................

So you've got a list of words, and you need to build up a dict like one of the above. Time to create a python file and put that in a function:

.. code-block:: python

  #!/usr/bin/env python3

  words = "I wish I may I wish I might".split()


  def build_trigrams(words):
      """
      build up the trigrams dict from the list of words

      returns a dict with:
         keys: word pairs
         values: list of followers
      """
      trigrams = {}

      # build up the dict here!

      return trigrams


  if __name__ == "__main__":
      trigrams = build_trigrams(words)
      print(trigrams)

So how do you actually build up that dict? That's kind of the point of the exercise, so I won't tell you that ... but here are some hints:

**Looping through the words**

Obviously you need to loop through all the words, so a for loop makes sense. However, this is a bit tricky -- usually in Python you loop through all the items in a list, and don't worry about the indexes:

   .. code-block:: python

     for item in a_list:
         ...

But in this case, we don't need to work with one word at a time, we need to work with three at a time (a pair of words, and the one that follows it).
So contrary to the usual practice, indexes can be helpful here:

   .. code-block:: python

     for i in len(words)-2: # why -2 ?
         pair = words[i:i + 2]
         follower = words[i + 2]

**Adding a pair to the dict:**

For each pair in the text, you need to add it to the dict. But:

- words[i:i + 2] is a list with two words in it -- can that be used as a key in a dict? IF not, how can you make a valid key out of it?

- As you loop through the text, you will collect pairs of words. Each time, a given pair may already be in the dict.

  - If the pair is not in the dict, you want to put it in the dict, with value being a list with the follower in it::

    ("may", "I"): ["wish"]

  - If the pair already is in the dict, then you want to add the follower to the list that's already there.

Note that the above suggests the basic logic -- it's almost pseudo-code. And that logic will work.  But it turns out that this is a common enough operation that python dicts have a method that lets you do that logic in one step -- can you find it?

You should now have code that will return a dict like we noted above::

   {("I", "wish"): ["I", "I"],
    ("wish", "I"): ["may", "might"],
    ("may", "I"): ["wish"],
    ("I", "may"): ["I"]}

Try it out on a longer bit of text (your choice) before you go any further.

Using the Trigrams dict
.......................

This is the fun part: once you have a mapping of word pairs to following words, you can build up some new "fake" text. Read above again to remind yourself of the procedure, but a couple hints:

- the "random" module is your friend here:

.. code-block:: python

  import random

  # returns a number between a and b (including a and b)
  random.randint(a, b)

  # pick a random item from a sequence
  random.choice(a_list)

- You need to start with the first word pair -- picking a random key from a dict is actually a bit tricky -- start with a known pair, and once you have the code working, you can figure out a better way.

- As you build up your text, you probably want to build it up in a list -- appending one word at a time -- you can join it together at the end.

- Remember that after adding a word, the next pair is the last two words in the text.

- What to do if you end up with a word pair that isn't in the original text?

- How to terminate? -- probably have a pre-defined length of text!

Once you have the basics working, try it on a longer piece of input text -- then think about making it fancy -- Can you make sentences? with capitalized first words, and punctuation? Anything else to make it more "real"?

Processing the Input Text
-------------------------

If you get a book from Project Gutenberg (or anywhere else), it will not be "clean" -- that is, it has header information, footer information, chapter headings, punctuation, what have you. So you'll need to clean it up somehow to get a simple list of words to use to build your trigrams.

The first part is pretty straightforward -- open the file and loop through the lines of text.

You may want to skip the header -- how would you do that??
hint -- there is a line that starts with::

  *** START OF THIS PROJECT GUTENBERG EBOOK

In the loop, you can process a single line of text.

 - calling ``.split()`` to break it into words.

Optional steps to cleaning up the text:

 - Strip out punctuation?
   - what about contractions? i.e. can't (vs a single quotation mark)

 - Remove capitalization?
   - what about "I"? And proper nouns?

Any other ideas your may have.

**Hints:**

The string methods are your friend here.

There are also handy constants in the ``string`` module: ``import string``

Check out the ``str.translate`` method -- it can make multiple replacements very fast.

Do get the full trigrams code working first -- then play with some of the fancier options.

Code Structure
--------------

Break your code down into a handful of separate functions. This way you can test each on its own, and it's easier to refactor one part without messing with the others.  For instance, your __main__ block might look something like:

.. code-block:: python

  if __name__ == "__main__":
      # get the filename from the command line
      try:
          filename = sys.argv[1]
      except IndexError:
          print("You must pass in a filename")
          sys.exit(1)

      in_data = read_in_data(filename)
      words = make_words(in_data)
      word_pairs = build_trigram(words)
      new_text = build_text(word_pairs)

      print(new_text)
