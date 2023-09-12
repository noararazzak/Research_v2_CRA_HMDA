Instructions...

This project converts .DAT files obtained from the Community Reinvestment Act website and the US National Archives that contain LAR files containing the Home Mortgage Disclosure Act data. 

A. For the CRA Flat Files


1. Get CRA Aggregate Flat Files from:

https://www.ffiec.gov/cra/craflatfiles.htm

2. Unzip the files and store the files in specific year folders named 2011, 2012 etc. depending on the year.

3. Files between 2003 and 2015:

a. Rename all aggregate files as "exp_aggr.dat"

4. Files between 2016 and present:

b. Rename all aggregate files as "exp_aggr_A1-1.dat" or "exp_aggr_A1-2.dat" etc. depending on table. 

5. Change the variables year and table_id in the conversion_cra_dat_to_csv.py file. 

6. Keep the conversion_cra_dat_to_csv.py file and CRA_Flat_Agg_Specs.csv in the same folder and run. 


B. For the HMDA LAR Files