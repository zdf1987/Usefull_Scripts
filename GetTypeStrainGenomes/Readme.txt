Perl and Python environments are necessary to run.

1. Do not delete the folder 'TEM';

2. Download a list of all the genome records of prokaryotes from NCBI website (https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt), and put it in this folder;

3. Modify the url in line 85 of 'GetTypeStrainNumFromLPSN.py' to the url of the taxon of interest, and run this script in IDLE of Python;

4. Change the working directory of cmd or terminal into this fold, and run 'perl GetItemsOfInterest.pl prokaryotes.txt';

5. The results will be writen in the file 'TypeStrainGenomeInfo.txt'. Open it using Excel or a text reader.