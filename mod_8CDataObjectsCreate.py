## IMPORT MODULES

## FUNCTION () #8C - DATA OBJECTS CREATE

def fn_DataObjectsCreate(D5):
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #8C - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES 
    LetterCounter = 1
    D5K = {}

    ## BEGIN FOR LOOP
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "DS"...
    for EachKey in D5.keys(): ## EACH VERSE
        
        D5K[LetterCounter] = EachKey

        LetterCounter += 1
       

    ## END FOR LOOP



    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #8C - DATA OBJECTS CREATE")

    ## RETURN VARIABLES TO PROGRAM
   
    return(D5K) 

## END FUNCTION () #8C - DATA OBJECTS CREATE

