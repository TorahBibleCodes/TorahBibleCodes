## IMPORT MODULES

import csv

## DECLARE VARIABLES

headers = ["ELS Search Term", "(ELS Search Term #, [Gematria LetterValues], Gematria WordTotal)", "# Positive ELS Matches", "# Negative ELS Matches"]

## rows = []

## DEFINE FUNCTIONS

def fn_WriteOutputToFile(W, FileNameForELSMatchesDataSummary):

    """
    ## MODULE.FUNCTION() #99 - 
    """
    
    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open(FileNameForELSMatchesDataSummary,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(W)

    ## return() - RETURNS NOTHING
