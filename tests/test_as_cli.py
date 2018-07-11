#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import subprocess
import pytest


SKIP_REAL_JPREDAPI = bool(int(os.getenv("SKIP_REAL_JPREDAPI", True)))


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
@pytest.mark.parametrize("cmdargs", [
    "--help",
    "--version",
    "check_rest_version",
    "check_rest_version --silent",
    "quota --email=name@domain.com",
    "quota --email=name@domain.com --silent",
    "submit --mode=single --format=raw --seq=MQVWPIEGIKKFETLSYLPP",
    "submit --mode=single --format=raw --file=tests/example_data/single_raw.example",
    "submit --mode=single --format=fasta --file=tests/example_data/single_fasta.example",
    "submit --mode=batch --format=fasta --file=tests/example_data/batch_fasta.example --email=name@domain.com",
    "submit --mode=msa --format=fasta --file=tests/example_data/msa_fasta.example --email=name@domain.com",
    "submit --mode=msa --format=msf --file=tests/example_data/msa_msf.example --email=name@domain.com",
    "submit --mode=msa --format=blc --file=tests/example_data/msa_blc.example --email=name@domain.com",
    "status --jobid=jp_K46D05A",
    "status --jobid=jp_K46D05A --results=jpred_sspred/results",
    "status --jobid=jp_K46D05A --results=jpred_sspred/results --extract",
    "get_results --jobid=jp_K46D05A",
    "get_results --jobid=jp_K46D05A --results=jpred_sspred/results",
    "get_results --jobid=jp_K46D05A --results=jpred_sspred/results --extract"
])
def test_cli(cmdargs):
    cmdargs = ["python", "-m", "jpredapi"] + cmdargs.split()
    subprocess.check_output(cmdargs)
