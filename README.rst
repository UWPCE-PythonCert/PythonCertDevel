=======================================
UWPCE Certificate In Python Programming
=======================================

This repository contains the source materials for the University of Washington Professional and Continuing Education Program Python Certification Program:

`Certificate in Python Programming <https://www.pce.uw.edu/certificates/python-programming>`_

These materials are available in html rendered version here:

https://uwpce-pythoncert.github.io/PythonCertDevel/

If you find any errors, typos, etc, or have suggestions, please feel free to raise an issue or submit a pull request to this repo.

Building These Documents
------------------------

These documents are written in `Restructured Text <http://docutils.sourceforge.net/rst.html>`_, and rendered with the `Sphinx Documentation system <http://www.sphinx-doc.org/>`_.

To build the docs, you need Python, Sphinx, and sphinx-rtd-theme::

  python3 -m pip install sphinx, sphinx-rtd-theme

Should do it.

Building the docs locally:
..........................

in the main dir, run::

  make html

The html docs will be generated in the ``build/html`` dir --
``build/html/index.html`` is the main page.

Building the docs for uploading to gh-pages
...........................................

The html docs are published by gitHub's gh-pages. This is accomplished by putting all the html in the ``gh-pages`` branch of the repo.

YOu can do that by hand, by copying any new html to the branch, but if you want to do it more often, it's easier to automate it.

There is a bash script that will do it for you: ``build_gh_pages.sh``.

It requires a bit of setup:

* make another clone of this repo "next to" the main clone (i.e. in the same dir), but name that clone: "PythonCertDevel.gh-pages".

* checkout the gh-pages branch in that clone::

    git checkout gh-pages

* it's a good idea to do a pull once to make sure you are up to date:

    git pull

* Once this is setup, you can run the build_gh_pages script from the name repo, and it should:

  - build the html docs
  - copy that build docs over to the other clone
  - add any new files to the gh-pages branch
  - commit the changes
  - push the changes to gitHub

Once run, the new version of the docs should be published on gitHub at:

https://uwpce-pythoncert.github.io/PythonCertDevel/

**NOTE:** ``build_gh_pages`` is a pretty hacky script with limited functionality -- in particular, it does not clear out any old files that have been removed. If you remove a page, it must be removed by hand from the gh-pages branch. PRs welcome.








