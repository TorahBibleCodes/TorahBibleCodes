## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import csv


## DECLARE VARIABLES
## DECLARE VARIABLES
## DECLARE VARIABLES

headers = ["Word", "Gematria Number Value"]

rows = []


## DEFINE FUNCTIONS
## DEFINE FUNCTIONS
## DEFINE FUNCTIONS

def fn_WriteOutputToCSVFile_WordsAndGematriaValues(W):
    
    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open('WordsOfSelectedTexts_GematriaValues.csv','w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        ## f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(W)

    ## return() - RETURNS NOTHING
