Perl and Python environments are necessary to run, and modules requests, BeautifulSoup4, lxml, time, csv, os, re, and urlopen are also required.

1. Do not delete the folder 'TEM';

2. Download a latest list of all the genome records of prokaryotes from NCBI website (https://ftp.ncbi.nlm.nih.gov/genomes/genbank/archaea/assembly_summary.txt
; https://ftp.ncbi.nlm.nih.gov/genomes/genbank/bacteria/assembly_summary.txt; https://ftp.ncbi.nlm.nih.gov/genomes/refseq/archaea/assembly_summary.txt; OR https://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt), and put it in this folder;

3. Change the working directory of cmd or terminal into this fold, and run 'python GetTypeStrainNumFromLPSN.py --url https://lpsn.dsmz.de/order/rhodobacterales --output TEM'; the url of the taxon of interest (e.g. https://lpsn.dsmz.de/order/rhodobacterales);

4. Change the working directory of cmd or terminal into this fold, and run 'perl GetItemsOfInterest.pl prokaryotes.txt';

5. The results will be writen in the file 'TypeStrainGenomeInfo.txt'. Open it using Excel or a text reader.

6. After modification of the result (step 5), use the assembly accessions to download genome datasets by using NCBI datasets (https://www.ncbi.nlm.nih.gov/datasets/docs/v2/download-and-install/).

If it is helpful, please cite: Zhang, D.-F., He, W., Shao, Z., Ahmed, I., Zhang, Y., Li, W.-J., Zhao, Z., 2023. Phylotaxonomic assessment based on four core gene sets and proposal of a genus definition among the families Paracoccaceae and Roseobacteraceae. Int. J. Syst. Evol. Microbiol. 73 (11), 006156. https://doi.org/10.1099/ijsem.0.006156
