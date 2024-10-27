## IMPORT MODULES
import mod_99_WriteOutputToFileCSV_ELSMatchesAllLetterPositions

## BEGIN DEFINE FUNCTION TO WRITE OUTPUT OF EACH INDIVIDUAL ELS DATA ##
def fn_IterateOutput4ELSMatches(MasterList4LetterPositions, Dict4FileNames4ELSTerms):

    """ ## MODULE.FUNCTION() #99 - ITERATE OUTPUT FOR ELS MATCHES - ## RETURNS: """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION: BEGIN FUNCTION #99 - ITERATE OUTPUT FOR ELS MATCHES ALL WORD AND LETTER DATA")

    ## DECLARE VARIABLES
    ELSCounter = 0 ## 

    for EachKey, EachFileName in Dict4FileNames4ELSTerms.items(): ## Dict4FileNames4ELSTerms[1] == 'USER_FILE_WordsOfELSs_ELS1_חישמה_1Genesis_20x3904.csv'

        ## ASSIGN MASTER LIST OF LETTER INFO TO EACH ELS FILE NAME
        Dict4FileNames4ELSTerms[EachKey] = MasterList4LetterPositions[ELSCounter]

        ## INCREMENT ELS COUNTER
        ELSCounter += 1

    _ = mod_99_WriteOutputToFileCSV_ELSMatchesAllLetterPositions.fn_WriteOutputToFile(Dict4FileNames4ELSTerms)

    ## RETURN NOTHING

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION: END FUNCTION #99 - ITERATE OUTPUT FOR ELS MATCHES ALL WORD AND LETTER DATA")

    ## RETURNS NOTHING

## END DEFINE FUNCTION TO WRITE OUTPUT OF EACH INDIVIDUAL ELS DATA
    