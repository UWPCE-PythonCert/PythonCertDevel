.. _files:

########################
File Reading and Writing
########################

Saving and loading data


Files
-----

Text Files

.. code-block:: python

    f = open('secrets.txt')
    secret_data = f.read()
    f.close()

``secret_data`` is a string

NOTE: these days, you probably need to use Unicode for text -- we'll get to that next week

.. nextslide::

Binary Files

.. code-block:: python

    f = open('secrets.bin', 'rb')
    secret_data = f.read()
    f.close()

``secret_data`` is a byte string

(with arbitrary bytes in it -- well, not arbitrary -- whatever is in the file.)

(See the ``struct``  module to unpack binary data )


.. nextslide::


File Opening Modes

.. code-block:: python

    f = open('secrets.txt', [mode])
    'r', 'w', 'a'
    'rb', 'wb', 'ab'
    r+, w+, a+
    r+b, w+b, a+b


These follow the Unix conventions, and aren't all that well documented
in the Python docs. But these BSD docs make it pretty clear:

http://www.manpagez.com/man/3/fopen/

**Gotcha** -- 'w' modes always clear the file

.. nextslide:: Text File Notes

Text is default

  * Newlines are translated: ``\r\n -> \n``
  *   -- reading and writing!
  * Use \*nix-style in your code: ``\n``


Gotcha:

  * no difference between text and binary on \*nix
  * breaks on Windows


File Reading
------------

Reading part of a file

.. code-block:: python

    header_size = 4096
    f = open('secrets.txt')
    secret_header = f.read(header_size)
    secret_rest = f.read()
    f.close()

.. nextslide::


Common Idioms

.. code-block:: python

    for line in open('secrets.txt'):
        print(line)

(the file object is an iterator!)

.. code-block:: python

    f = open('secrets.txt')
    while True:
        line = f.readline()
        if not line:
            break
        do_something_with_line()

.. nextslide::

We will learn more about the keyword with later, but for now, just understand
the syntax and the advantage over the try-finally block:

.. code-block:: python

 with open('workfile', 'r') as f:
     read_data = f.read()
 f.closed
 True


File Writing
------------

.. code-block:: python

    outfile = open('output.txt', 'w')
    for i in range(10):
        outfile.write("this is line: %i\n"%i)
    outfile.close()

    with open('output.txt', 'w'):
        for i in range(10):
           f.write("this is line: %i\n"%i)


File Methods
------------

Commonly Used Methods

.. code-block:: python

    f.read() f.readline()  f.readlines()

    f.write(str) f.writelines(seq)

    f.seek(offset)   f.tell() # for binary files, mostly

    f.close()

StringIO
--------

.. code-block:: python

    In [417]: import io
    In [420]: f = io.StringIO()
    In [421]: f.write("somestuff")
    In [422]: f.seek(0)
    In [423]: f.read()
    Out[423]: 'somestuff'
    Out[424]: stuff = f.getvalue()
    Out[425]: f.close()

(handy for testing file handling code...)

There is also cStringIO -- a bit faster.

.. code-block:: python

    from cStringIO import StringIO

=====================
Paths and Directories
=====================

Paths
-----

Paths are generally handled with simple strings (or Unicode strings)

Relative paths:

.. code-block:: python

    'secret.txt'
    './secret.txt'

Absolute paths:

.. code-block:: python

    '/home/chris/secret.txt'


Either work with ``open()`` , etc.

(working directory only makes sense with command-line programs...)

os module
----------

.. code-block:: python

    os.getcwd()
    os.chdir(path)
    os.path.abspath()
    os.path.relpath()


.. nextslide:: os.path module

.. code-block:: python

    os.path.split()
    os.path.splitext()
    os.path.basename()
    os.path.dirname()
    os.path.join()


(all platform independent)

.. nextslide:: directories

.. code-block:: python

    os.listdir()
    os.mkdir()
    os.walk()

(higher level stuff in ``shutil``  module)

pathlib
-------

``pathlib`` is a package for handling paths in an OO way:

http://pathlib.readthedocs.org/en/pep428/

All the stuff in os.path and more:

.. code-block:: ipython

    In [64]: import pathlib
    In [65]: pth = pathlib.Path('./')
    In [66]: pth.is_dir()
    Out[66]: True
    In [67]: pth.absolute()
    Out[67]: PosixPath('/Users/Chris/PythonStuff/UWPCE/IntroPython2015')
    In [68]: for f in pth.iterdir():
                 print(f)
    junk2.txt
    junkfile.txt
    ...

