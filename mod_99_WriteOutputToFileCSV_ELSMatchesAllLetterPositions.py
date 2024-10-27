## IMPORT MODULES
import csv

## DECLARE VARIABLES
#headers = ["Letter", "LetterPositionIndex", "LetterCoordinatesD5K", "LetterPositionInWord", "WordNumber", "WordNumberInVerse", "WordCoordinatesDWTK"]
headers = ["(n,d,k)", "LetterGematriaNumberValue", "Letter", "LetterPositionIndex", "LetterCoordinatesD5K", "Found in Word in Text", "LetterPositionIndex In Word", "WordNumber", "WordCoordinatesDWTK", "WordNumberInVerse", "Found In Verse"]

## rows = []

## DEFINE FUNCTIONS

def fn_WriteOutputToFile(Dict4FileNames4ELSTerms): ## KEYS: FileNamesForELSTerms, VALUES: MasterList4LetterInfo

    """
    ## MODULE.FUNCTION() #99 - 
    """
    ##  KEY: Dict4FileNames4ELSTerms['USER_FILE_WordsOfELSs_ELS1_המשיח_1Genesis_20x3904.csv']
    ##  VALUE: MasterList4LetterInfo

    ## KEY: Dict4FileNames4ELSTerms['USER_FILE_WordsOfELSs_ELS2_משיחי_1Genesis_20x3904.csv']
    ## VALUE: MasterList4LetterInfo
        
    ELSCounter = 1

    for EachKey, EachValue in Dict4FileNames4ELSTerms.items(): ## EachFileName

        ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
        with open(f"USER_GENERATED_FILES/" + EachKey,'w', encoding="utf-8", newline='') as f:
            
            f_csv = csv.writer(f, delimiter=';')
            f_csv.writerow(headers) ## HEADERS OPTIONAL - REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
            ## f_csv.writerows(MasterList4LetterInfo)

            for EachMasterList in (EachValue):
                f_csv.writerow(EachMasterList)

        ELSCounter += 1

        ## return() - RETURNS NOTHING
