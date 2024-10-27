## IMPORT MODULES
import csv

## DECLARE VARIABLES
headers = ["(n, d, k)", "[Gematria of ELS]", "Gematria WordTotal of ELS", "ELS Search Term", "Found in WordNumber In Text", "WordCoordinatesDWTK", "Found in Word In Text", \
           "LetterPositionIndex In Word", "LetterCoordinatesD5K of First Letter in ELS", "Found In Verse" ]
## rows = []

## DEFINE FUNCTIONS ##
def fn_WriteOutputToFile(TupleOfTuples, FileNameForELSMatches):

    """
    ## MODULE.FUNCTION() #99 - 
    """
    
    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open("USER_GENERATED_FILES/" + FileNameForELSMatches,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(TupleOfTuples)

    ## return() - RETURNS NOTHING
