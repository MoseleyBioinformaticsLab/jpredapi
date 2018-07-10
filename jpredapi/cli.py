#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
jpredapi command-line interface

The JPred API allows users to submit jobs from the command-line.

Usage:
    jpredapi submit (--mode=<mode> --format=<format>) (--file=<filename> | --seq=<sequence>) [--email=<name@domain.com>] [--name=<name>] [--rest=<address>] [--skipPDB] [--silent]
    jpredapi status (--jobid=<id>) [--results=<path>] [--wait=<interval>] [--attempts=<max>] [--rest=<address>] [--jpred4=<address>] [--extract] [--silent]
    jpredapi get_results (--jobid=<id>) [--results=<path>] [--wait=<interval>] [--attempts=<max>] [--rest=<address>] [--jpred4=<address>] [--extract] [--silent]
    jpredapi quota (--email=<name@domain.com>) [--rest=<address>] [--silent]
    jpredapi check_rest_version [--rest=<address>] [--silent]
    jpredapi -h | --help
    jpredapi -v | --version

Options:
    -h, --help                 Show this help message.
    -v, --version              Show jpredapi package version.
    --silent                   Do not print messages.
    --extract                  Extract results tar.gz archive.
    --skipPDB                  PDB check.
    --mode=<mode>              Submission mode, possible values: single, batch, msa.
    --format=<format>          Submission format, possible values: raw, fasta, msf, blc.
    --file=<filename>          Filename of a file with the job input (sequence(s)).
    --seq=<sequence>           Instead of passing input file, for single-sequence submission.
    --email=<name@domain.com>  E-mail address where job report will be sent (optional for all but batch submissions).
    --name=<name>              Job name.
    --jobid=<id>               Job id.
    --results=<path>           Path to directory where to save archive with results.
    --rest=<address>           REST address of server [default: http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest].
    --jpred4=<address>         Address of Jpred4 server [default: http://www.compbio.dundee.ac.uk/jpred4].
    --wait=<interval>          Wait interval before retrying to check job status in seconds [default: 60].
    --attempts=<max>           Maximum number of attempts to check job status [default: 10].
"""

from . import api


def cli(cmdargs):
    """jpredapi command-line interface processor."""

    api.WAIT_INTERVAL = float(cmdargs["--wait"]) * 1000  # convert from seconds to milliseconds
    api.MAX_ATTEMPTS = int(cmdargs["--attempts"])

    if cmdargs["submit"]:
        api.submit(mode=cmdargs["--mode"],
                   user_format=cmdargs["--format"],
                   file=cmdargs["--file"],
                   seq=cmdargs["--seq"],
                   skipPDB=cmdargs["--skipPDB"],
                   email=cmdargs["--email"],
                   name=cmdargs["--name"],
                   silent=cmdargs["--silent"],
                   host=cmdargs["--rest"])

    elif cmdargs["status"]:
        api.status(job_id=cmdargs["--jobid"],
                   results_dir_path=cmdargs["--results"],
                   extract=cmdargs["--extract"],
                   silent=cmdargs["--silent"],
                   host=cmdargs["--rest"],
                   jpred4=cmdargs["--jpred4"])

    elif cmdargs["get_results"]:
        api.get_results(job_id=cmdargs["--jobid"],
                        results_dir_path=cmdargs["--results"],
                        extract=cmdargs["--extract"],
                        silent=cmdargs["--silent"],
                        host=cmdargs["--rest"],
                        jpred4=cmdargs["--jpred4"])

    elif cmdargs["quota"]:
        api.quota(email=cmdargs["--email"],
                  host=cmdargs["--rest"],
                  suffix="quota",
                  silent=cmdargs["--silent"])

    elif cmdargs["check_rest_version"]:
        api.check_rest_version(host=cmdargs["--rest"],
                               suffix="version",
                               silent=cmdargs["--silent"])
