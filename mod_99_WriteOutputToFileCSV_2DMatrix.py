## IMPORT MODULES
import csv

## DECLARE VARIABLES

## DEFINE FUNCTIONS
def fn_WriteOutputToFile(ListOfRows, FileNameForMatrix):

    """
    ## MODULE.FUNCTION() #99 - 
    """

    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open("USER_GENERATED_FILES/" + FileNameForMatrix,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        ## f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(ListOfRows)


   
