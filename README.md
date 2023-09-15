Instructions...

This project converts .dat files obtained from the Community Reinvestment Act website and the US National Archives website (that contains the Home Mortgage Disclosure Act data). 

A. For the CRA Flat Files


1. Get CRA Aggregate Flat Files from:

https://www.ffiec.gov/cra/craflatfiles.htm

2. Unzip the folders and store the files in specific year folders named 2011, 2012 etc. depending on the year. The year folders should be stored in a folder named "raw_data_CRA". 

3. Files between 2003 and 2015:

a. Rename all aggregate files as "exp_aggr.dat"

4. Files between 2016 and present:

b. Rename all aggregate files as "exp_aggr_A1-1.dat" or "exp_aggr_A1-2.dat" etc. depending on table. 

5. Change the variables year and table_id in the conversion_cra_dat_to_csv.py file. 

6. Store the folder "raw_data_CRA" in another folder named "data". Keep the conversion_cra_dat_to_csv.py file and CRA_Flat_Agg_Specs.csv in the working folder and run. 


B. For the HMDA LAR Files

1. Get HMDA LAR Files from:

https://catalog.archives.gov/id/2456161

2. Unzip the folders and store the files in "raw_data_HMDA"

3. Rename the file "yearHMDALAR.dat". Here year will be 2011, 2012 etc. 

4. Store the folder "raw_data_HMDA" in another folder named "data". Keep the conversion_hmda_dat_to_csv.py file and HMDA_Lar_Specs.csv in the working folder and run. 

5. This script has only been tested for LAR files from 2011, 2012 and 2013. However, in theory, it should work on any HMDA LAR files from 2004 onwards. HMDA LAR files from 2014 onwards are already in .csv format and is available at https://www.ffiec.gov/hmda/hmdaproducts.htm
