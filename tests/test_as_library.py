from unittest.mock import patch
import pytest
import jpredapi


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

    assert response.status_code == 202 and "Created JPred job" in response.text
