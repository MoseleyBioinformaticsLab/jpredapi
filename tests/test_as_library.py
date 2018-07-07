import re
from unittest.mock import patch
import pytest
import jpredapi


SKIP_REAL_JPREDAPI = True


def test_check_rest_version():
    version = 'v.1.5'
    with patch('jpredapi.check_rest_version') as mock_version:
        mock_version = 'v.1.5'
    assert mock_version == version


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
def test_check_rest_version_real():
    version = jpredapi.check_rest_version()
    assert version == 'v.1.5'


def test_quota():
    with patch('jpredapi.quota') as response:
        response.status_code = 200
    assert response.status_code == 200


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
def test_quota_real():
    response = jpredapi.quota(email="name@domain.com")
    assert response.status_code == 200


@pytest.mark.parametrize("mode,user_format,file,seq,skipPDB,email,name,silent,host", [
    ("single", "raw", None, "MQVWPIEGIKKFETLSYLPP", True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("single", "raw", "tests/example_data/single_raw.example", None, True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("single", "fasta", "tests/example_data/single_fasta.example", None, True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("batch", "fasta", "tests/example_data/batch_fasta.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "fasta", "tests/example_data/msa_fasta.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "msf", "tests/example_data/msa_msf.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "blc", "tests/example_data/msa_blc.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest")
])
def test_submit(mode, user_format, file, seq, skipPDB, email, name, silent, host):
    with patch('jpredapi.submit') as mock_submit:
        mock_submit.return_value.status_code = 202
        mock_submit.return_value.text = "Created JPred job"

        response = jpredapi.submit(mode=mode, user_format=user_format, file=file, seq=seq, skipPDB=skipPDB,
                                   email=email, name=name, silent=silent, host=host)
        assert response.status_code == 202 and "Created JPred job" or "You have successfully submitted" in response.text


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
@pytest.mark.parametrize("mode,user_format,file,seq,skipPDB,email,name,silent,host", [
    ("single", "raw", None, "MQVWPIEGIKKFETLSYLPP", True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("single", "raw", "tests/example_data/single_raw.example", None, True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("single", "fasta", "tests/example_data/single_fasta.example", None, True, None, None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("batch", "fasta", "tests/example_data/batch_fasta.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "fasta", "tests/example_data/msa_fasta.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "msf", "tests/example_data/msa_msf.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest"),
    ("msa", "blc", "tests/example_data/msa_blc.example", None, True, "name@domain.com", None, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest")
])
def test_submit_real(mode, user_format, file, seq, skipPDB, email, name, silent, host):
    response = jpredapi.submit(mode=mode, user_format=user_format, file=file, seq=seq, skipPDB=skipPDB,
                               email=email, name=name, silent=silent, host=host)
    assert response.status_code == 202 and "Created JPred job" or "You have successfully submitted" in response.text


@pytest.mark.parametrize("job_id,results_dir_path,extract,silent,host,jpred4", [
    ("jp_TEST", None, False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jp_TEST", "jpred_results", False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jp_TEST", "jpred_results", True, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4")
])
def test_status(job_id, results_dir_path, extract, silent, host, jpred4):
    with patch("jpredapi.status") as mock_status:
        mock_status.return_value.status_code = 200
        response = jpredapi.status(job_id=job_id, results_dir_path=results_dir_path, extract=extract,
                                   silent=silent, host=host, jpred4=jpred4)
    assert response.status_code == 200


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
@pytest.mark.parametrize("results_dir_path,extract,silent,host,jpred4", [
    (None, False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jpred_results", False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jpred_results", True, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4")
])
def test_status_real(results_dir_path, extract, silent, host, jpred4):
    job_response = jpredapi.submit(mode="single", user_format="raw", seq="MQVWPIEGIKKFETLSYLPP")
    result_url = job_response.headers['Location']
    job_id = re.search(r"(jp_.*)$", result_url).group(1)

    response = jpredapi.status(job_id=job_id, results_dir_path=results_dir_path, extract=extract,
                               silent=silent, host=host, jpred4=jpred4)
    assert response.status_code == 200


@pytest.mark.parametrize("job_id,results_dir_path,extract,silent,host,jpred4", [
    ("jp_TEST", None, False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jp_TEST", "jpred_results", False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jp_TEST", "jpred_results", True, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4")
])
def test_get_results(job_id, results_dir_path, extract, silent, host, jpred4):
    with patch("jpredapi.get_results") as mock_results:
        mock_results.return_value.status_code = 200
        response = jpredapi.status(job_id=job_id, results_dir_path=results_dir_path, extract=extract,
                                   silent=silent, host=host, jpred4=jpred4)
    assert response.status_code == 200


@pytest.mark.skipif(SKIP_REAL_JPREDAPI, reason="Skipping tests that hit the real JPred API server.")
@pytest.mark.parametrize("results_dir_path,extract,silent,host,jpred4", [
    (None, False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jpred_results", False, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4"),
    ("jpred_results", True, False, "http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest", "http://www.compbio.dundee.ac.uk/jpred4")
])
def test_get_results_real(results_dir_path, extract, silent, host, jpred4):
    job_response = jpredapi.submit(mode="single", user_format="raw", seq="MQVWPIEGIKKFETLSYLPP")
    result_url = job_response.headers['Location']
    job_id = re.search(r"(jp_.*)$", result_url).group(1)

    response = jpredapi.get_results(job_id=job_id, results_dir_path=results_dir_path, extract=extract,
                                    silent=silent, host=host, jpred4=jpred4)
    assert response.status_code == 200
