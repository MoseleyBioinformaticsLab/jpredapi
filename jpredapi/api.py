#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
import re
import os
import tarfile
from collections import OrderedDict

import requests
from retrying import retry


JPRED4 = "http://www.compbio.dundee.ac.uk/jpred4"
HOST = "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"
VERSION = "1.5.0"
WAIT_INTERVAL = 60000  # 60000 milliseconds = 60 seconds


def _check_version(host=HOST, suffix="version"):
    """Check version of Jpred REST interface.

    :param str host: Jpred host address.
    :param str suffix: Host dddress suffix.
    :return: Version of Jpred REST API.
    :rtype: :py:class:`str`
    """
    version_url = "{}/{}".format(host, suffix)
    response = requests.get(version_url)
    version = re.search(r"VERSION=(v\.[0-9]*.[0-9]*)", response.text).group(1)
    return version


def submit(mode, user_format, file=None, seq=None, skipPDB=True, email=None, name=None, silent=False):
    """Submit job to Jpred server.

    :param str mode: Submission mode, possible values: `single`, `batch`, `msa`.
    :param str user_format: Submission format, possible values: `raw`, `fasta`, `msf`, `blc`.
    :param str file: Filename of a file with the job input (sequence or msa).
    :param str seq: Amino acid sequence passed as string of single-letter code without spaces, e.g. --seq=ATWFGTHY
    :param skipPDB: PDB check will not be performed (True), otherwise perform PDB check (False).
    :type skipPDB: :py:obj:`True` or :py:obj:`False`
    :param str email: E-mail address.
    :param str name: Job name.
    :param silent: Print information about job submission.
    :type silent: :py:obj:`True` or :py:obj:`False`
    :return: None
    :rtype: :py:obj:`None`
    """
    if user_format == "raw" and mode == "single":
        rest_format = "seq"
    elif user_format == "fasta" and mode == "single":
        rest_format = "seq"
    elif user_format == "fasta" and mode == "msa":
        rest_format = "fasta"
    elif user_format == "msf" and mode == "msa":
        rest_format = "msf"
    elif user_format == "blc" and mode == "msa":
        rest_format = "blc"
    elif user_format == "fasta" and mode == "batch":
        rest_format = "batch"
    else:
        raise ValueError("""Invalid mode/format combination.
        Valid combinations are: --mode=single --format=raw
                                --mode=single --format=fasta
                                --mode=msa    --format=fasta
                                --mode=msa    --format=msf
                                --mode=msa    --format=blc
                                --mode=batch  --format=fasta""")

    if file is None and seq is None:
        raise ValueError("""Neither input sequence nor input file are defined.
        Please provide either --file or --seq parameters.""")
    elif file and seq:
        raise ValueError("""Both input sequence and input file are defined.
        Please choose --file or --seq parameter.""")

    if file is not None:
        with open(file, "r") as infile:
            sequence_query = infile.read()
    elif seq is not None:
        sequence_query = ">query\n{}".format(seq)
    else:
        sequence_query = ""

    if skipPDB:
        skipPDB = "on"
    else:
        skipPDB = "off"

    if rest_format == "batch" and email is None:
        raise ValueError("""When submitting batch job email is obligatory.
        You will receive detailed report, list of links and a link to archive
        to all results via email.""")

    if not silent:
        print("Your job will be submitted with the following parameters:")
        print("format:", rest_format)
        print("skipPDB:", skipPDB)
        if file is not None:
            print("file:", file)
        elif seq is not None:
            print("seq:", seq)
        if email is not None:
            print("email:", email)
        if name is not None:
            print("name:", name)

    parameters_dict = OrderedDict([("skipPDB", skipPDB),
                                   ("format", rest_format),
                                   ("email", email),
                                   ("name", name)])

    parameters_list = ["{}={}".format(k, v) for k, v in parameters_dict.items() if v]
    parameters_list.append(sequence_query)
    query = u"£€£€".join(parameters_list)

    response = requests.post("{}/{}".format(HOST, "job"),
                             data=query.encode("utf-8"),
                             headers={"Content-type": "text/txt"})

    if response.reason == "Accepted":
        if rest_format != "batch":
            result_url = response.headers['Location']
            job_id = re.search(r"(jp_.*)$", result_url).group(1)

            if not silent:
                print("Created JPred job with jobid:", job_id)
                print("You can check the status of the job using the following URL:", result_url)
            else:
                print("Created JPred job with jobid:", job_id)

        elif rest_format == "batch":
            print(response.content)
    else:
        print(response.reason)


@retry(wait_fixed=WAIT_INTERVAL)
def status(job_id, results_dir_path=None, extract=False, silent=False):
    """Check status of submitted job.

    :param str job_id: Job id.
    :param str results_dir_path: Directory path where to save results if job is finished.
    :param extract: Extract (True) or not (False) results into directory.
    :type extract: :py:obj:`True` or :py:obj:`False`
    :param silent: Print information about job status.
    :type silent: :py:obj:`True` or :py:obj:`False`
    :return: None
    :rtype: :py:obj:`None`
    """
    if not silent:
        print("Your job status will be checked with the following parameters:")
        print("Job id:", job_id)
        print("Get results:", bool(results_dir_path))

    job_url = "{}/{}/{}/{}".format(HOST, "job", "id", job_id)
    response = requests.get(job_url)

    if response.reason == "OK":
        print(response.text)

        if "finished" in response.text:
            if results_dir_path is not None:
                results_dir_path = os.path.join(results_dir_path, job_id)
                if not os.path.exists(results_dir_path):
                    os.makedirs(results_dir_path)

                archive_url = "{}/{}/{}/{}.{}".format(JPRED4, "results", job_id, job_id, "tar.gz")
                archive_path = os.path.join(results_dir_path, "{}.{}".format(job_id, "tar.gz"))

                archive_response = requests.get(archive_url, stream=True)
                with open(archive_path, "wb") as outfile:
                    for chunk in archive_response.iter_content(chunk_size=1024):
                        outfile.write(chunk)

                if extract:
                    tar_archive = tarfile.open(archive_path)
                    tar_archive.extractall(path=results_dir_path)

                if not silent:
                    print("Saving results to: {}".format(os.path.abspath(results_dir_path)))
    else:
        response.raise_for_status()


def get_results(job_id, results_dir_path=None, extract=False, silent=False):
    """Download results from Jpred server.

    :param str job_id: Job id.
    :param str results_dir_path: Path where to save results.
    :param extract: Extract from tar.gz archive.
    :type extract: :py:obj:`True` or :py:obj:`False`
    :param silent: Print information.
    :type silent: :py:obj:`True` or :py:obj:`False`
    :return: None
    :rtype: :py:obj:`None`
    """
    if results_dir_path is None:
        results_dir_path = os.path.join(os.getcwd(), job_id)

    status(job_id=job_id, results_dir_path=results_dir_path, extract=extract, silent=silent)


def quota(email, host=HOST, suffix="quota"):
    """Check how many jobs you have already submitted on a given day
    (out of 1000 maximum allowed jobs per user per day).

    :param str email: E-mail address.
    :param str host: Jpred host address.
    :param str suffix: Host address suffix.
    :return: None
    :rtype: :py:obj:`None`
    """
    quota_url = "{}/{}/{}".format(host, suffix, email)
    response = requests.get(quota_url)
    print(response.text)
