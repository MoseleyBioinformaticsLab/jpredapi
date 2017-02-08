User Guide
==========

Description
~~~~~~~~~~~

The :mod:`jpredapi` package provides a simple Python interface for submitting
and retrieving jobs from JPRED: A Protein Secondary Structure Prediction Server 
(JPRED_).


Installation
~~~~~~~~~~~~

The :mod:`jpredapi` package runs under Python 2.7 and Python 3.4+. Starting with Python 3.4 
pip_ is included by default. To install system-wide with pip_ run the following:

Install on Linux, Mac OS X
--------------------------

.. code:: bash

   python3 -m pip install jpredapi

Install on Windows
------------------

.. code:: bash

   py -3 -m pip install jpredapi


Install inside virtualenv
-------------------------

For an isolated install, you can run the same inside a virtualenv_.

.. code:: bash

   $ virtualenv -p /usr/bin/python3 venv  # create virtual environment, use python3 interpreter

   $ source venv/bin/activate             # activate virtual environment

   $ python3 -m pip install jpredapi      # install jpredapi as usually

   $ deactivate                           # if you are done working in the virtual environment


Dependencies
~~~~~~~~~~~~

:mod:`jpredapi` depends on several Python libraries, it will install its
dependencies automatically, but if you wish to install them manually, 
then run commands below:

   * docopt_ for creating :mod:`jpredapi` command-line interface.
      * To install docopt_ run the following:

        .. code:: bash

           python3 -m pip install docopt  # On Linux, Mac OS X
           py -3 -m pip install docopt    # On Windows

   * requests_ for sending HTTP/1.1 requesrs to JPRED server.
      * To install requests_ Python library run the following:

        .. code:: bash

           python3 -m pip install requests  # On Linux, Mac OS X
           py -3 -m pip install requests    # On Windows

   * retrying_ for controlling status requests.
      * To install retrying_ Python library run the following:

        .. code:: bash

           python3 -m pip install retrying  # On Linux, Mac OS X
           py -3 -m pip install retrying    # On Windows


Basic usage
~~~~~~~~~~~

:mod:`jpredapi` can be used in several ways:

   * As a library within interactive Python shell or Python script and as a command-line tool to:

      * Submit JPRED job.
      * Check status of JPRED job.
      * Retrieve results of JPRED job.

.. note:: Read :doc:`tutorial` to learn more and see code examples on using :mod:`jpred`.

.. _pip: https://pip.pypa.io/
.. _virtualenv: https://virtualenv.pypa.io/
.. _docopt: http://docopt.readthedocs.io/
.. _requests: http://docs.python-requests.org/en/master/
.. _retrying: https://pypi.python.org/pypi/retrying
.. _JPRED: http://www.compbio.dundee.ac.uk/jpred/