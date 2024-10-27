## IMPORT MODULES

## FUNCTION () #3A3 - TEXT FILE PREPROCESS - FIX KEYS ##
def fn_FixKeys(ListOfTupleKeysToFix):
    
    """
    ## MODULE.FUNCTION() #3A3 - TEXT FILE PREPROCESS - FIX KEYS; ## RETURNS ListOfTupleKeys - FIXED
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A3 - TEXT FILE PREPROCESS - FIX KEYS")

    ## DECLARE VARIABLES
    #ListOfStringsParsed = []
    #ListOfStringsParsedWithSpaces = []

    ListTempForTupleKey = [] 
    ListOfTupleKeys = []
   
    ## BEGIN FOR LOOP - EXTRACT NUMBERS FOR TUPLE KEY
    for EachTuple in ListOfTupleKeysToFix:

        ## print(f"EachTuple : {EachTuple}")

        ## BEGIN FOR LOOP - FOR EACH ELEMENT IN EACH TUPLE
        for EachElement in EachTuple:

            ## BEGIN IF / ELSE - IF ELEMENT IS NUMERIC
            ## IF ELEMENT IS NUMERIC
            if EachElement.isnumeric():

                ## BEGIN IF / ELSE
                ## IF NUMBER IS TWO DIGITS OR MORE
                if (len(EachElement) != 1):

                    ## REVERSE THE STRING AND CONVERT TO INTEGER
                    IntegerNumber = int(EachElement[::-1])
                
                ## ELSE IF NUMBER IS ONLY ONE DIGIT
                else: 

                    ## CONVERT TO INTEGER
                    IntegerNumber = int(EachElement)

                ## END IF / ELSE

                ## ADD INTEGER NUMBER TO LIST TEMP
                ListTempForTupleKey.append(IntegerNumber) ## CONTAINS 3-INTEGER TUPLE KEY

            ## END IF / ELSE - IF ELEMENT IS NUMERIC

        ## END FOR LOOP - FOR EACH ELEMENT IN EACH TUPLE

        ## CONVERT KEYS TO TUPLES
        TupleKey = tuple(ListTempForTupleKey)

        ## ADD 3-INTEGER TUPLE KEY TO LIST FOR KEYS (DUPLICATES HERE NEED TO BE PARSED)
        ListOfTupleKeys.append(TupleKey)

        ## ListForWordsInLine.append(ListTempWord)
        ## RESET LIST
        ListTempForTupleKey = [] ## RESET LIST

    ## END FOR LOOP - EXTRACT NUMBERS FOR TUPLE KEY

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A3 - TEXT FILE PREPROCESS - FIX KEYS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfTupleKeys)
    
## END FUNCTION () #3A3 - END TEXT FILE PREPROCESS - FIX KEYS

