Perl and Python environments are necessary to run, and modules requests, BeautifulSoup4, lxml, time, csv, os, re, and urlopen are also required.

1. Do not delete the folder 'TEM';

2. Download a latest list of all the genome records of prokaryotes from NCBI website (https://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/prokaryotes.txt), and put it in this folder;

3. Change the working directory of cmd or terminal into this fold, and run 'python GetTypeStrainNumFromLPSN.py --url https://lpsn.dsmz.de/order/rhodobacterales --output TEM'; the url of the taxon of interest (e.g. https://lpsn.dsmz.de/order/rhodobacterales);

4. Change the working directory of cmd or terminal into this fold, and run 'perl GetItemsOfInterest.pl prokaryotes.txt';

5. The results will be writen in the file 'TypeStrainGenomeInfo.txt'. Open it using Excel or a text reader.

6. After modification of the result (step 5), use the assembly accessions to download genome datasets by using Batch Entrez (https://www.ncbi.nlm.nih.gov/sites/batchentrez).
