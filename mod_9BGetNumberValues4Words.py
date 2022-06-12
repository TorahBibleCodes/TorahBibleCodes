## IMPORT MODULES
import mod_9AGetNumberValues4Letters ## MODULE.FUNCTION() #9A - GET NUMBER VALUE OF EACH LETTER IN STRING

## FUNCTION () #9B - GET NUMBER VALUES FOR EACH WORDSTRING IN LIST OF WORDS

def fn_GetNumberValues(ListOfWords):

    """
    ## MODULE.FUNCTION() #9B - GET NUMBER VALUE OF EACH LETTER IN WORD STRING ## RETURNS ListOfNumberValues4Words
    """
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #9B - GET NUMBER VALUES FOR WORDS")
    
    ## DECLARE VARIABLES
    ListOfNumberValues4Words = [] ## CREATE EMPTY LIST TO STORE VALUES
    WordCounter = 1 ## INITIALIZE WORD COUNTER

    ## BEGIN FOR LOOP
    ## FOR EACH ELEMENT IN SEQUENCE S, L, etc.??
    for EachWord in ListOfWords:

        ## CALL FUNCTION - 
        NumberValuesForEachWord = mod_9AGetNumberValues4Letters.fn_GetNumberValues(EachWord)

        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(NumberValuesForEachWord)

        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(type(NumberValuesForEachWord))

        ## SUM TOTAL NUMBER VALUE FOR EACH WORD
        TotalNumberValueForEachWord = sum(NumberValuesForEachWord)

        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(TotalNumberValueForEachWord)

        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(type(TotalNumberValueForEachWord))
        
        ## DECLARE TEMP TUPLE VARIABLE
        t = (WordCounter, NumberValuesForEachWord, TotalNumberValueForEachWord)

        ## APPEND TUPLE TO LIST OF NUMBER VALUES 4 WORDS
        ListOfNumberValues4Words.append(t)

        ## INCREMENT WORD COUNTER
        WordCounter += 1
        
    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(ListOfNumberValues4Words)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("WITHIN FUNCTION:  END FUNCTION #9B - GET NUMBER VALUES FOR WORDS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfNumberValues4Words) ## LIST OF TUPLES
    
## END FUNCTION () #9B - GET NUMBER VALUES FOR EACH WORDSTRING IN LIST OF WORDS

