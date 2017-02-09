The jpredapi Tutorial
=======================

The :mod:`jpredapi` package provides functions to submit, check status, and 
retrieve results from JPRED: A Secondary Structure Prediction Server.

Command Line Interface
~~~~~~~~~~~~~~~~~~~~~~

.. code::

   jpredapi command-line interface

   The RESTful API allows JPred users to submit jobs from the command-line.

   Usage:
       jpredapi -h | --help
       jpredapi --version
       jpredapi submit (--mode=<mode> --format=<format>) (--file=<filename> | --seq=<sequence>) 
                       [--email=<name@domain.com>] [--name=<job_name>] [--skipPDB=<value>] 
                       [--rest=<address>] [--jpred4=<address>] [--silent]
       jpredapi status (--job_id=<id>) [--results_dir=<path>] 
                       [--wait_interval=<interval>] [--extract] [--silent]
       jpredapi get_results (--job_id=<id>) [--results_dir=<path>] 
                            [--wait_interval=<interval>] [--extract] [--silent]
       jpredapi quota (--email=<name@domain.com>)

   Options:
       -h, --help                   Show this help message.
       --version                    Show jpredapi version.
       --silent                     Do not print messages.
       --extract                    Extract results tar.gz archive into folder.
       --mode=<mode>                Submission mode, possible values: single, batch, msa.
       --format=<format>            Submission format, possible values: raw, fasta, msf, blc.
       --file=<filename>            Filename of a file with the job input (sequence(s)).
       --seq=<sequence>             Instead of passing input file, for single-sequence submission.
       --email=<name@domain.com>    E-mail address where job report will be sent 
                                    (optional for all but batch submissions).
       --name=<job_name>            Job name.
       --job_id=<job_id>            Job id.
       --skipPDB=<value>            PDB check, possible values: True, False [default: True].
       --results_dir=<path>         Path where to save archive with results.
       --rest=<address>             REST address of server 
                                    [default: http://www.compbio.dundee.ac.uk/jpred4/cgi-bin/rest].
       --jpred4=<address>           Address of Jpred4 server 
                                    [default: http://www.compbio.dundee.ac.uk/jpred4].
       --wait_interval=<interval>   Wait interval before retrying to check job status in seconds 
                                    [default: 60].

Print jpredapi help message
---------------------------

   .. code:: bash

      $ python3 -m jpredapi --help


Print jpredapi version
----------------------

   .. code:: bash

      $ python3 -m jpredapi --version

Submit jobs to JPRED server 
---------------------------

Submit single sequence in ``raw`` format using ``--seq`` parameter:
*******************************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=single --format=raw --seq=MQVWPIEGIKKFETLSYLPP

Submit single sequence in ``raw`` format using ``--file`` parameter:
********************************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=single --format=raw --file=tests/example_data/single_raw.example

Content of ``single_raw.example`` file:
   .. code:: bash

      MQVWPIEGIKKFETLSYLPPLTVEDLLKQIEYLLRSKWVPCLEFSKVGFVYRENHRSPGYYDGRYWTMWKLPMFGCTDATQVLKELEEAKKAYPDAFVRIIGFDNVRQVQLISFIAYKPPGC


Submit single sequence in ``fasta`` format using ``--file`` parameter:
**********************************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=single --format=fasta --file=tests/example_data/single_raw.example

Content of ``single_fasta.example`` file:
   .. code:: bash

      >my test sequence
      MQVWPIEGIKKFETLSYLPPLTVEDLLKQIEYLLRSKWVPCLEFSKVGFVYRENHRSPGYYDGRYWTMWKLPMFGCTDATQVLKELEEAKKAYPDAFVRIIGFDNVRQVQLISFIAYKPPGC

Submit multiple sequences in ``fasta`` format using ``--file`` parameter:
*************************************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=batch --format=fasta --file=tests/example_data/batch_fasta.example --email=name@domain.com

Content of ``batch_fasta.example`` file:
   .. code:: bash

      >my_seq1
      MKFLVLLFNILCLFPILGADELVMSPIPTTDVQPKVTFDINSEVSSGPLYLNPVEMAGVK
      YLQLQRQPGVQVHKVVEGDIVIWENEEMPLYTCAIVTQNEVPYMAYVELLEDPDLIFFLK
      EGDQWAPIPEDQYLARLQQLRQQIHTESFFSLNLSFQHENYKYEMVSSFQHSIKMVVFTP
      KNGHICKMVYDKNIRIFKALYNEYVTSVIGFFRGLKLLLLNIFVIDDRGMIGNKYFQLLD
      DKYAPISVQGYVATIPKLKDFAEPYHPIILDISDIDYVNFYLGDATYHDPGFKIVPKTPQ
      CITKVVDGNEVIYESSNPSVECVYKVTYYDKKNESMLRLDLNHSPPSYTSYYAKREGVWV
      TSTYIDLEEKIEELQDHRSTELDVMFMSDKDLNVVPLTNGNLEYFMVTPKPHRDIIIVFD
      GSEVLWYYEGLENHLVCTWIYVTEGAPRLVHLRVKDRIPQNTDIYMVKFGEYWVRISKTQ
      >my_seq2
      MASVKSSSSSSSSSFISLLLLILLVIVLQSQVIECQPQQSCTASLTGLNVCAPFLVPGSP
      TASTECCNAVQSINHDCMCNTMRIAAQIPAQCNLPPLSCSAN
      >my_seq3
      MEKKSIAGLCFLFLVLFVAQEVVVQSEAKTCENLVDTYRGPCFTTGSCDDHCKNKEHLLS
      GRCRDDVRCWCTRNC

Submit multiple sequence alignment files in ``fasta`` format:
*************************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=msa --format=fasta --file=tests/example_data/msa_fasta.example --email=name@domain.com

Content of ``msa_fasta.example`` file:
   .. code:: bash

      >QUERY_1
      MQVWPIEGIKKFETLSYLPPLTVEDLLKQIEYLLRSKWVPCLEFSKVGFVYRENHRSPGYYDGRYWTMWKLP
      MFGCTDATQVLKELEEAKKAYPDAFVRIIGFDNVRQVQLISFIAYKPPGC
      >UniRef90_Q40250_2
      MKVWPPIGLKKYETLSYLPPLSDEALSKEIDYLIRNKWIPCLEFEEHGFVYREHHHSPGYYDGRYWTMWKLP
      MFGCTDSAQVMKEVGECKKEYPNAFIRVIGFDNIRQVQCISFIVAKPPGV
      >UniRef90_A7YVW5_3
      MQVWPPLGKRKFETLSYLPPLPVDALLKQIDYLIRSGWIPCIEFTVEGFVYREHHHSPGYYDGRYWTMWKLP
      MYGCTDSTQVLAEVEANKKEYPNSYIRIIGFDNKRQVQCVSFIVHTPPS-
      >UniRef90_P04714_4
      MQVWPPYGKKKYETLSYLPDLTDEQLLKEIEYLLNKGWVPCLEFTEHGFVYREYHASPRYYDGRYWTMWKLP
      MFGCTDATQVLGELQEAKKAYPNAWIRIIGFDNVRQVQCISFIAYKPPG-
      >UniRef90_W9RUU9_5
      MQVWPPRGKLKFETLSYLPDLTDEQLLKEIDYLLRSNWIPCLEFEVKAHIYRENNRSPGYYDGRYWTMWKLP
      MFGCTDATQVLAEVQETKKAYPDAHVRIIGFDNNRQVQCISFIAYKPPA-

Submit multiple sequence alignment files in ``msf`` format:
***********************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=msa --format=msf --file=tests/example_data/msa_msf.example --email=name@domain.com

Content of ``msa_msf.example`` file:
   .. code:: bash

      /tmp/filelPdICy  MSF: 108  Type: N  January 01, 1776  12:00  Check: 2741 ..

      Name: 0_1a             Len:   108  Check:  4063  Weight:  1.00
      Name: 1_MA             Len:   108  Check:  4875  Weight:  1.00
      Name: 2_KE             Len:   108  Check:   449  Weight:  1.00
      Name: 3_NC             Len:   108  Check:  3354  Weight:  1.00

      //

                 0_1a  APAFSVSPAS GASDGQSVSV SVAAAGETYY IAQCAPVGGQ DACNPATATS
                 1_MA  APGVTVTPAT GLSNGQTVTV SATTPGTVYH VGQCAVVEGV IGCDATTSTD
                 2_KE  SAAVSVSPAT GLADGATVTV SASATSTSAT ALQCAILAGR GACNVAEFHD
                 3_NC  APTATVTPSS GLSDGTVVKV AGAQAGTAYD VGQCAWVDGV LACNPADFSS

                 0_1a  FTTDASGAAS FSFTVRKSYA GQTPSGTPVG SVDCATDACN LGAGNSGLNL
                 1_MA  VTADAAGKIT AQLKVHSSFQ AVVANGTPWG TVNCKVVSCS AGLGSDSGEG
                 2_KE  FSLSG.GEGT TSVVVRRSFT GYVPDGPEVG AVDCDTAPCE IVVGGNTGEY
                 3_NC  VTADANGSAS TSLTVRRSFE GFLFDGTRWG TVDCTTAACQ VGLSDAAGNG

                 0_1a  GHVALTFG
                 1_MA  AAQAITFA
                 2_KE  GNAAISFG
                 3_NC  PGVAISFN


Submit multiple sequence alignment files in ``blc`` format:
***********************************************************

   .. code:: bash

      python3 -m jpredapi submit --mode=msa --format=blc --file=tests/example_data/msa_blc.example --email=name@domain.com

Content of ``msa_blc.example`` file:
   .. code:: bash

      >0_1a  Name
      >1_MA  Name
      >2_KE  Name
      >3_NC  Name
      * iteration 1
      AASA
      PPAP
      AGAT
      FVVA
      STST
      VVVV
      STST
      PPPP
      AAAS
      *

Check job status on JPRED server 
--------------------------------

Check single job status using ``job_id``:
*****************************************

   .. code:: bash

      python3 -m jpredapi status --job_id=jp_K46D05A

Check single job status using ``job_id`` and retrieve results:
**************************************************************

   .. code:: bash

      python3 -m jpredapi status --job_id=jp_K46D05A --results_dir=jpred_sspred/results

Check single job status using ``job_id``, retrieve results, and decompress archive:
***********************************************************************************

   .. code:: bash

      python3 -m jpredapi status --job_id=jp_K46D05A --results_dir=jpred_sspred/results --extract


Retrieve results from JPRED server 
----------------------------------

Retrieve results using ``job_id``:
**********************************

   .. code:: bash

      python3 -m jpredapi get_results --job_id=jp_K46D05A --results_dir=jpred_sspred/results

Retrieve results using ``job_id`` and decompress archive:
*********************************************************

   .. code:: bash

      python3 -m jpredapi get_results --job_id=jp_K46D05A --results_dir=jpred_sspred/results --extract


Check how many jobs you have already submitted on a given day:
**************************************************************

   .. code:: bash

      python3 -m jpredapi quota --email=name@domain.com


Using jpredapi as a library
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Importing jpredapi module
-------------------------

If :mod:`jpredapi` package is installed on the system the :mod:`nmrstarlib.nmrstarlib`
module can be imported:

>>> import jpredapi

Submit jobs to JPRED server 
---------------------------

Submit single sequence in ``raw`` format using ``seq`` parameter:
*****************************************************************

>>> import jpredapi
>>> 
>>> jpredapi.submit(mode="single", user_format="raw", seq="MQVWPIEGIKKFETLSYLPP")
>>>

Submit single sequence in ``raw`` format using ``file`` parameter:
******************************************************************

>>> jpredapi.submit(mode="single", user_format="raw", file="tests/example_data/single_raw.example")
>>>

Submit single sequence in ``fasta`` format using ``file`` parameter:
********************************************************************

>>> jpredapi.submit(mode="single", user_format="fasta", file="tests/example_data/single_fasta.example")
>>>

Submit multiple sequences in ``fasta`` format using ``file`` parameter:
***********************************************************************

>>> jpredapi.submit(mode="batch", user_format="fasta", file="tests/example_data/batch_fasta.example", email="name@domain.com")
>>> 

Submit multiple sequence alignment files in ``fasta`` format:
*************************************************************

>>> jpredapi.submit(mode="msa", user_format="fasta", file="tests/example_data/msa_fasta.example", email="name@domain.com")
>>> 

Submit multiple sequence alignment files in ``msf`` format:
***********************************************************

>>> jpredapi.submit(mode="msa", user_format="msf", file="tests/example_data/msa_msf.example", email="name@domain.com")
>>> 

Submit multiple sequence alignment files in ``blc`` format:
***********************************************************

>>> jpredapi.submit(mode="msa", user_format="blc", file="tests/example_data/msa_blc.example", email="name@domain.com")
>>> 

Check job status on JPRED server 
--------------------------------

Check single job status using ``job_id``:
*****************************************

>>> import jpredapi
>>>
>>> jpredapi.status(job_id="jp_K46D05A")
>>> 


Check single job status using ``job_id`` and retrieve results:
**************************************************************

>>> jpredapi.status(job_id="jp_K46D05A", results_dir_path="jpred_sspred/results")
>>>

Check single job status using ``job_id``, retrieve results, and decompress archive:
***********************************************************************************

>>> jpredapi.status(job_id="jp_K46D05A", results_dir_path="jpred_sspred/results", extract=True)
>>> 

Retrieve results from JPRED server 
----------------------------------

Retrieve results using ``job_id``:
**********************************

>>> import jpredapi
>>>
>>> jpredapi.get_results(job_id="jp_K46D05A", results_dir_path="jpred_sspred/results")
>>> 

Retrieve results using ``job_id`` and decompress archive:
*********************************************************

>>> jpredapi.get_results(job_id="jp_K46D05A", results_dir_path="jpred_sspred/results", extract=True)
>>> 

Check how many jobs you have already submitted on a given day:
--------------------------------------------------------------

>>> import jpredapi
>>> 
>>> jpredapi.quota(email="name@domain.com")
>>>