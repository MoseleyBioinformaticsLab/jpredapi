#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
jpredapi Python library
~~~~~~~~~~~~~~~~~~~~~~~
The RESTful API allows JPred users to submit jobs from the command-line.

Usage example for command-line:

   .. code:: bash

      python3 -m jpredapi --help
      python3 -m jpredapi --version
      python3 -m jpredapi submit --mode=single --format=raw --seq=MQVWPIEGIKKFETLSYLPP
      python3 -m jpredapi status --job_id=jp_K46D05A
      python3 -m jpredapi get_results --job_id=jp_K46D05A --results_dir=jpred_sspred/results
      python3 -m jpredapi quota --email=name@domain.com

Usage example for interactive Python shell:

   >>> import jpredapi
   >>>
   >>> jpredapi.submit(mode="single", user_format="raw", seq="MQVWPIEGIKKFETLSYLPP")
   >>>
   >>> jpredapi.status(job_id="jp_K46D05A")
   >>>
   >>> jpredapi.get_results(job_id="jp_K46D05A", results_dir_path="jpred_sspred/results")
   >>>
   >>> jpredapi.quota(email="name@domain.com")
   >>>
"""

from .api import submit
from .api import status
from .api import get_results
from .api import quota


__version__ = "1.5.1"
