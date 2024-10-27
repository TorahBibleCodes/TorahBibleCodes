## IMPORT MODULES
import mod_3A2_TextFilePreprocess_Koren_ExtractKeysAndWords

## FUNCTION () #3A1 - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS ##
def fn_ExtractStrings(TextKoren):
    
    """
    ## MODULE.FUNCTION() #3A1 - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS; ## RETURNS ListOfTupleKeysToFix ##
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A1 - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS")

    ## DECLARE VARIABLES
    ListOfLines = []
    ListOfTupleKeysToFix = []
    ListOfWordsInLine = []

    ## BEGIN IF / ELIF
    ## BEGIN IF TEXT FILE IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT
    if isinstance(TextKoren, str):
        
        ## ...THEN CALL MODULE.FUNCTION() #3A2 
        ListOfTupleKeysToFix, ListOfWordsInLine = mod_3A2_TextFilePreprocess_Koren_ExtractKeysAndWords.fn_ExtractKeysAndWords(TextKoren)

        ## TEST PRINT OUTPUT
        ## print(f"ListOfTupleKeysToFix : {ListOfTupleKeysToFix}")
        
        ## TEST PRINT OUTPUT
        ## print("\n")
        ## print("TextKoren = ", len(TextKoren), type(TextKoren))

    ## END IF / ELIF
    ## END IF TEXT FILE IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT

    ## ELSE IF TXT IS A TUPLE... ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS
    ## BEGIN IF / ELIFs
    elif isinstance(TextKoren, tuple):
        
        TextString = ""

        ## ...THEN FOR EACH STRING IN TUPLE...CONCATENATE THE STRINGS
        ## BEGIN FOR LOOP
        for EachTuple in TextKoren:

            ## TEST PRINT OUTPUT
            ## print(f"EachTuple : {EachTuple}")

            ## 
            TextString = TextString + EachTuple

            ## TEST PRINT OUTPUT
            ## print("\n")
            ## print("TextKoren = ", len(TextKoren), type(TextKoren))
           
        ## END FOR LOOP

        ## ...THEN CALL MODULE.FUNCTION() #3A2 
        ListOfTupleKeysToFix, ListOfWordsInLine = mod_3A2_TextFilePreprocess_Koren_ExtractKeysAndWords.fn_ExtractKeysAndWords(TextString)

    ## END IF / ELIF 

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A1 - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfTupleKeysToFix, ListOfWordsInLine)
        
    ## END FUNCTION () #3A1 - END TEXT FILE PREPROCESS - EXTRACT KEY STRINGS