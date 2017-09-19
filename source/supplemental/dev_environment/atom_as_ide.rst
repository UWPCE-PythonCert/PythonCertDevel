.. _atom_as_ide:

**************************************************
Turning Atom Into a Lightweight Python IDE
**************************************************

Atom is the self-proclaimed "hackable text editor for the 21st Century." It has a nice
modern interface, and is highly customizable yet can also be used productively
with minimal setup and configuration.


Requirements
============

Any IDE should ease your development experience by providing the following:

* It should provide excellent, configurable syntax colorization.
* It should allow for robust tab completion.
* It should offer the ability to jump to the definition of symbols in other files.
* It should perform automatic code linting to help avoid silly mistakes.
* It should be able to interact with a Python interpreter such that when debugging, the editor will follow along with the debugger.

Atom does all this and more, but some functionality requires you to select and install packages.


Which Version?
==============

The latest version is the best version. Atom is regularly maintained, so the latest
version will have the latest bug fixes and updates. On the Atom website, click the big red button_ to
download, then run the executable to install.

.. _button: https://atom.io/

If you already have Atom installed, but want to check for a newer version, go to
Help --> Check for Update.


Basic Settings
==============

Atom can be used out of the box with no setup as a simple text editor. It automatically
recognizes file types and helpfully highlights text accordingly. To use in this manner,
write your Python files in Atom, then run them in your Python command prompt.


Extending the Editor
====================

Atom has great documentation_ on how to hack and configure it. Read the Flight Manual_ for tons of information on
everything you can do. You can also watch a Getting Started video_.

.. _documentation: https://atom.io/docs
.. _Manual: http://flight-manual.atom.io/
.. _video: https://www.youtube.com/watch?v=U5POoGSrtGg

In general, you can extend Atom by installing packages, and then accessing their functionality from the Packages drop-down menu. Keyboard shortcuts are specified in the packages menus if available.


Useful Packages
==============

Running Scripts
---------------

To run scripts within Atom, you will need to install the Script_ package. The Script package supports a ton of languages, including Python.

.. _Script: https://atom.io/packages/script

To run a Python script with the Script package....

Autocompletion
--------------

By default, Atom knows which Python packages you have imported, variables you have created
and so on. Autocomplete_ ships with Atom and requires no setup.

.. _Autocomplete: http://flight-manual.atom.io/using-atom/sections/autocomplete/

Code Linting
------------

To get code linting functionality in Atom, you will need to install the atom-lint_ package.

.. _atom-lint: https://atom.io/packages/atom-lint

White Space Management
----------------------

Atom knows when you are writing Python and helps you out by dealing with spaces and tabs
in the same way. When in a Python file, if you type 4 spaces, then hit delete, you are
taken back a tab.

The Whitespace_ package ships with Atom and requires no setup. Under the Packages --> Whitespace menu,
you will find tools to turn all tabs into spaces, all spaces into tabs, among other whitespace-related options.

.. _Whitespace: https://atom.io/packages/whitespace

Follow-Along
------------

To use a Python debugger in Atom, you will need to install the python-debugger_ package. Once installed, turn on the debugger by going to Packages --> python-debugger --> Toggle.

.. _python-debugger: https://atom.io/packages/python-debugger
