Git
===

What is Git?
------------

A "version control system"

Why Version Control?
--------------------

.. figure:: /_static/phd101212s.gif
   :class: fill
   :width: 45 %

   "Piled Higher and Deeper" by Jorge Cham

   www.phdcomics.com

   A history of everything everyone does to 'your' code

   A graph of "states" in which the code has existed

   That last one is a bit tricky, and is not necessary to understand right out of the gate. When you are ready, you can look at this supplement to gain a better understanding:

   :ref: https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/dev_environment/git_overview.html

Setting up git
--------------

You should have git installed on your machine and accessible from the command line. There will be a little bit of setup for git that you should only have to do once.

.. code-block:: bash

   $ git config --global user.name "Marie Curie"
   $ git config --global user.email "marie@radioactive.com"


Editor
------

* git needs an editor occasionally
* default is VI, which is not very intuitive to non-Unix Geeks
* Nano is simple, easy solution for Macs and Linux
* Nano no longer available for windows, use Sublime or Notepad++

For windows users:
 https://uwpce-pythoncert.github.io/PythonCertDevel/supplemental/installing/git_editor_windows.html

Once you have chosen/installed an editor, configure git to use it:

nano
``$ git config --global core.editor "nano -w"``

sublime (mac)
``$ git config --global core.editor "subl -n -w"``

sublime (win)
``$ git config --global core.editor "'c:/program files/sublime text 2/sublime_text.exe' -w"``

Notepad++ (Win)
``$ git config --global core.editor "'c:/program files (x86)/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"``

Repositories
------------

A repository is just a collection of files that 'belong together'.

Since ``git`` is a *distributed* versioning system, there is no **central**
repository that serves as the one to rule them all. This simply means that all repositories should look the same.

However, to keep things sane, there is generally one "central" repository chosen that users check with for changes, for us this is GitHub.

Working with Remotes
--------------------

With git, you work with *local* repositories and *remotes* that they are connected to.

.. rst-class:: build
.. container::

   Git uses shortcuts to address *remotes*. Cloned repositories get an *origin* shortcut for free:

   .. code-block:: bash

      $ git remote -v
      origin  https://github.com/UWPCE-PythonCert/IntroPython-2017.git (fetch)
      origin  https://github.com/UWPCE-PythonCert/IntroPython-2017.git (push)

   This shows that the local repo on my machine *originated* from the one in
   the UWPCE-PythonCert gitHub account (it shows up twice, because I there is
   a shortcut for both fetch from and push to this remote)

.. rst-class:: build
.. container::

    You can work on any project you wish to that has a public repository on Github. However, since you won't have permission to edit most projects directly, there is such a thing as *forking* a project.

    When you *fork* a repository, you make a copy of that repository in your own (Github) account.

    When you have made changes that you believe the rest of the community will want to adopt, you make a *pull request* to the original project. The maintainer(s) of that project than have the option of accepting your changes, in which case your changes will become part of that project.

    This is how we will be working in this class. When you want feedback on your work, you will make a *pull request* to the instructors.


Our class materials reside in a repository on *Github* in the *UWPCE-PythonCert* organization:

.. figure:: /_static/remotes_start.png
   :width: 50%
   :class: center


Note that we will be using a different repository for class assignments than the repository for the class materials (this repository).

It will be a repository that is created just for this class, and will be called IntroPython-*quarter*.

In examples below it is called IntroToPython, so replace that in your head with the name of this year's repository. :)

This new repository will include examples and we will add relevant materials (and exercise solutions) to it throughout the quarter.

There will be a folder called students at the top level, and everyone will create their own directory within it.

So, everyone will commit to this repository, and everyone will have access to everyone's code.

This will make it easier to collaborate.

We will do a live demo of setting up a machine for working with this repository now.

The first thing we have to do is on the Github website. We will create a fork of the class repository from the ``UWPCE-PythonCert`` account on GitHub into your personal account. Please create a gitHub account if you don't have one already.

.. figure:: /_static/remotes_fork.png
   :width: 50%
   :class: center

Everyone should now have a copy of the class repository in their account on the GitHub website.

The next step is to make a *clone* of your fork on your own computer, which means that **your fork** in github is the *origin* (Demo):

.. figure:: /_static/remotes_clone.png
   :width: 50%
   :class: center

We will now set up our individual folders and include a README in this folder.

