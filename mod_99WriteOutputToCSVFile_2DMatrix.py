## IMPORT MODULES

import csv

## DECLARE VARIABLES

## DEFINE FUNCTIONS
def fn_WriteOutputToCSVFile(ListOfRows, FileNameForMatrix):

    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open(FileNameForMatrix,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        ## f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(ListOfRows)


   
