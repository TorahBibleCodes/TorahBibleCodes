## IMPORT MODULES
import csv

## DECLARE VARIABLES
headers = ["WordCoordinatesDWTK", "Word in Text", "Letter Positions (n)", "(Word#, [Gematria LetterValues], Gematria WordTotal)", "GematriaWordTotal"]
## rows = []

## DEFINE FUNCTIONS

def fn_WriteOutputToFile(W, FileNameForGematria):

    """
    ## MODULE.FUNCTION() #99 - 
    """
    
    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open("USER_GENERATED_FILES/" + FileNameForGematria,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(W)

    ## return() - RETURNS NOTHING
