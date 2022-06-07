## IMPORT MODULES

## BEGIN FUNCTION () #11 - TUPLE OF WORDS AND GEMATRIA VALUES CREATE

def fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW, ListOfIndexesCustom): ## NW = TUPLE OF (LIST, INTEGER)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #11 - TUPLE OF WORDS AND GEMATRIA VALUES CREATE ")
          
    ## DECLARE VARIABLES
    ## CALL PYTHON BUILT-IN FUNCTION(S) - CREATE TUPLE OF WORDS AND GEMATRIA VALUES

    W = tuple(zip(ListOfWords, NW))

    DW = dict(zip(ListOfIndexesCustom, W))
    
    ## TEST PRINT OUTPUT        
    ## print(W)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #11 - TUPLE OF WORDS AND GEMATRIA VALUES CREATE")
    
    ## RETURN VARIABLES - TUPLE OF WORDS AND GEMATRIA VALUES
    return(W, DW)
    
## END FUNCTION () #11 - TUPLE OF WORDS AND GEMATRIA VALUES CREATE


