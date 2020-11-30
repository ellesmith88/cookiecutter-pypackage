Python package template
-----------------------

Template with high-level guidelines for making new CEDA Python packages

Also includes a sample Sphinx documentation in ``docs/`` directory.  Run
``make`` in that directory to see a list of targets.  Further instructions are
in ``docs/index.rst``.

Based on Cookiecutter package
-----------------------------

This was originally a fork of the `Cookiecutter PyPackage` that gets used as
the template for a new package:

 https://github.com/audreyr/cookiecutter-pypackage

It gets used by the `Cookiecutter` tool, which provides the command-line tool
to generate a new package:

 https://github.com/audreyr/cookiecutter

Notes on the original `Cookiecutter PyPackage`:

 * GitHub repo: https://github.com/audreyr/cookiecutter-pypackage/
 * Documentation: https://cookiecutter-pypackage.readthedocs.io/
 * Free software: BSD license

Features
--------

 * Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
 * Travis-CI: Ready for Travis Continuous Integration testing
 * Tox testing: Setup to easily test for Python 3.6, 3.7, 3.8
 * Sphinx docs: Documentation ready for generation with, for example, ReadTheDocs_
 * Auto-release to PyPI when you push a new tag to master (optional)
 * Command line interface using Click or ArgParse (optional)


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/cedadev/cookiecutter-pypackage.git

cd to the new directory and initialise a git repository here::

    $ git init

Then:

* Create a repo on github with no extras (License, README etc.).
* Add the repo to your Travis-CI account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* You can enable pre-commit with the command ``pre-commit install`` which will check the formatting of your files before committing.
  Note: This should not be relied upon and ``flake8`` and ``black`` are tested in Travis-CI as part of this cookiecutter.
* Add to the ``requirements.txt`` file that specifies the packages you will need for
  your project and their versions.
* Then follow the instructions on github to add your code to the empty git repository.
* To encrypt your PyPI password in the Travis config:

    - Install travis following these instructions: https://github.com/travis-ci/travis.rb#installation
    - Create an api access token on github which as access to everything listed here: https://docs.travis-ci.com/user/github-oauth-scopes
    - Run ``travis login -—pro -—github-token=<your-token>``
    - Run the Travis CLI command ``travis encrypt --add deploy.password --com <your-password>`` to encrypt your PyPI password in the Travis config and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ``Read the Docs`` account + turn on the Read the Docs service hook. To do this go to admin on Read the Docs. Under Advanced settings enable the ``Build pull requests for this project`` option.

* Release your package by pushing a new tag to master (e.g. tagname = 0.1.0)::

    $ git tag <tagname>
    $ git push origin <tagname>

* Update your release notes on github.
* Activate your project on ``pyup.io``.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-pypackage tutorial`_.

.. _`cookiecutter-pypackage tutorial`: https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html

For more details of the original package (not the CEDA fork), see the
`cookiecutter-pypackage tutorial`:

https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html
