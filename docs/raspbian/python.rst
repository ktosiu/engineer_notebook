Python
======

.. figure:: ../pics/python.png
   :width: 200px

Python Modules
--------------

Simple structure:

::

    module_name
    -- CONTRIB
    -- LICENSE
    -- MANIFEST.in
    -- setup.py
    -- README.rst
    -- module
       -- __init__.py
       -- script1.py
       -- script2.py

Install from source:

::

    [kevin@Tardis media_server]$ sudo python setup.py develop
    running develop
    /usr/local/lib/python2.7/site-packages/pkg_resources/__init__.py:2510: PEP440Warning: 'pygame (1.9.1release)' is being parsed as a legacy, non PEP 440, version. You may find odd behavior and sort order. In particular it will be sorted as less than 0.0. It is recommend to migrate to PEP 440 compatible versions.
    PEP440Warning,
    running egg_info
    writing requirements to media.egg-info/requires.txt
    writing media.egg-info/PKG-INFO
    writing top-level names to media.egg-info/top_level.txt
    writing dependency_links to media.egg-info/dependency_links.txt
    writing entry points to media.egg-info/entry_points.txt
    reading manifest file 'media.egg-info/SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    warning: no previously-included files matching '*.html' found under directory '*'
    warning: no previously-included files matching '.AppleDouble' found under directory '*'
    warning: no previously-included files matching '*.yaml' found under directory '*'
    warning: no previously-included files matching '.gitignore' found under directory '*'
    warning: no previously-included files matching '*.pyc' found under directory '*'
    writing manifest file 'media.egg-info/SOURCES.txt'
    running build_ext
    Creating /usr/local/lib/python2.7/site-packages/media.egg-link (link to .)
    Adding media 0.1.0 to easy-install.pth file
    Installing media script to /usr/local/bin

    Installed /Users/kevin/github/media_server
    Processing dependencies for media==0.1.0
    Searching for PyYAML==3.11
    Best match: PyYAML 3.11
    PyYAML 3.11 is already the active version in easy-install.pth

    Using /Library/Python/2.7/site-packages
    Searching for tmdb3==0.7.2
    Best match: tmdb3 0.7.2
    Adding tmdb3 0.7.2 to easy-install.pth file

    Using /usr/local/lib/python2.7/site-packages
    Searching for rottentomatoes==2.1
    Best match: rottentomatoes 2.1
    Adding rottentomatoes 2.1 to easy-install.pth file

    Using /usr/local/lib/python2.7/site-packages
    Finished processing dependencies for media==0.1.0

Uninstall

::

    sudo pip uninstall module

Run command line program

::

    python -m module.script

where ``module`` is your package name and ``script`` is the python
script that does something.

PyPi
----

Some good resources are `Python Packaging
Guide <https://packaging.python.org/en/latest/distributing.html#uploading-your-project-to-pypi>`__
and `Tom Christie <https://tom-christie.github.io/articles/pypi/>`__ for
more info.

1. Create an account at pypi.org
2. Create a package repository at pypi.org using the `web
   form <https://pypi.python.org/pypi?%3Aaction=submit_form>`__ and
   uploading the PKG-INFO file
3. Run a test to ensure no problems ``python setup.py test``
4. Create the package for upload ``python setup.py sdist``
5. Upload package to pypi.org ``twine upload dist/*``

Twine can be installed using ``pip install twine`` which will secure
your upload and protect your password. Also the username and password
are stored in a ``.pypirc`` in your home directory.
