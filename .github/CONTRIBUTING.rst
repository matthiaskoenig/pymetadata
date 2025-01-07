============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Report Bugs
===========

Report bugs at https://github.com/matthiaskoenig/pymetadata/issues.

If you are reporting a bug, please follow the template guide lines. The more
detailed your report, the easier and thus faster we can help you.

Fix Bugs
========

Look through the GitHub issues for bugs.

Implement Features
==================

Look through the GitHub issues for features.

Write Documentation
===================

pymetadata could always use more documentation, whether as part of the official
documentation, in docstrings, or even on the web in blog posts, articles, and
such.

Submit Feedback
===============

The best way to send feedback is to file an issue at
https://github.com/matthiaskoenig/pymetadata/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are
  welcome :)

Get Started!
============

Ready to contribute? Here's how to set up pymetadata for local development.

1. Fork the https://github.com/matthiaskoenig/pymetadata repository on GitHub. If you
   have never done this before, `follow the official guide
   <https://guides.github.com/activities/forking/>`_
2. Clone your fork locally as described in the same guide.
3. Install your local copy into a a Python virtual environment. We recommend using ``uv`` for
   managing the environments

   .. code-block:: console

        # install dependencies
        uv sync
        # install dev dependencies
        uv pip install -r pyproject.toml --extra dev
        # install tox-uv support
        uv tool install tox --with tox-uv


4. Create a branch for local development using the ``develop`` branch as a
   starting point.

   .. code-block:: console

       git checkout devel
       git checkout -b fix-name-of-your-bugfix

   Now you can make your changes locally.

5. When making changes locally, it is helpful to ``git commit`` your work
   regularly. On one hand to save your work and on the other hand, the smaller
   the steps, the easier it is to review your work later.

   .. code-block:: console

       git add .
       git commit -m "fix: Your summary of changes"

6. When you're done making changes, check that your changes pass our test suite.
   This is all included with tox

   .. code-block:: console

       tox run-parallel


7. Push your branch to GitHub.

   .. code-block:: console

       git push origin fix-name-of-your-bugfix

8. Open the link displayed in the message when pushing your new branch in order
   to submit a pull request. Please follow the template presented to you in the
   web interface to complete your pull request.

For larger features that you want to work on collaboratively with other pymetadata
team members, you may consider to first request to join the pymetadata developers
team to get write access to the repository so that you can create a branch in
the main repository (or simply ask the maintainer to create a branch for you).
Once you have a new branch you can push your changes directly to the main
repository and when finished, submit a pull request from that branch to
``develop``.

Unit tests and benchmarks
-------------------------

pymetadata uses `pytest <http://docs.pytest.org/en/latest/>`_ for its
unit-tests and new features should in general always come with new
tests that make sure that the code runs as intended. 

To run all tests do::

    $ tox run-parallel

Branching model
---------------

``develop``
    Is the branch all pull-requests should be based on.
``main``
    Is only touched by maintainers and is the branch with only tested, reviewed
    code that is released or ready for the next release.
``{fix, bugfix, doc, feature}/descriptive-name``
    Is the recommended naming scheme for smaller improvements, bugfixes,
    documentation improvement and new features respectively.

Please use concise descriptive commit messages and consider using
``git pull --rebase`` when you update your own fork to avoid merge commits.

Thank you very much for contributing to pymetadata!
