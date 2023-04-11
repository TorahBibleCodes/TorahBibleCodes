## IMPORT MODULES

## FUNCTION () #8C - DATA OBJECTS CREATE

def fn_DataObjectsCreate(ListOfWords):

    """
    ## MODULE.FUNCTION() #8C - DATA OBJECTS CREATE; ## RETURNS
    """
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #8C - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES 
    LetterCounter = 1
    ListOfIndexes4LettersInEachWord = []
    ListTemporary = []

    ## BEGIN FOR LOOP
    ## FOR EACH WORD IN ListOfWords...
    for EachWord in ListOfWords: ## EACH WORD

        ## LW.append(EachWord)

        for EachLetter in EachWord: ## EACH LETTER

            ListTemporary.append(LetterCounter)

            ## INCREMENT LETTER COUNTER
            LetterCounter += 1

        ## ADD EACH CURRENT TOTAL-LETTER-COUNT-VALUE-INDEX-POSITION (I.E. EACH LETTER)
        ListOfIndexes4LettersInEachWord.append(ListTemporary)

        ## RESET TEMPORARY LIST
        ListTemporary = []
       
    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #8C - DATA OBJECTS CREATE")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfIndexes4LettersInEachWord) 

## END FUNCTION () #8C - DATA OBJECTS CREATE

