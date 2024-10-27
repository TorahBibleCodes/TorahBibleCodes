## IMPORT MODULES
import pandas as pd

## DEFINE FUNCTION ##
def fn_PandasObjectsCreate(L, LLL, N, ListOfIndexesCustomL, ListOfIndexesCustomLLL):

    """ ## MODULE.FUNCTION() #21 - ## RETURNS: sL0, sL, sLLL0, sLLL, sN0, sN """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #21 - PANDAS OBJECTS CREATE")

    ## DECLARE VARIABLES

    ## TEST DEVELOPMENT
    ## TODO CREATE MODULE.FUNCTION() TO CREATE THE PANDAS OBJECTS
    ## CREATE PD SERIES WITH 0-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL0 = pd.Series(L) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL = pd.Series(L, index=ListOfIndexesCustomL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## CREATE PD SERIES WITH 0-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW 
    sLLL0 = pd.Series(LLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW
    sLLL = pd.Series(LLL, index=ListOfIndexesCustomLLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## TEST DEVELOPMENT
    ## CREATE PD SERIES WITH 0-INDEX FOR THE ORIGINAL TEXT LENGTH
    sN0 = pd.Series(N) ## --> Converts ListOfNumbers (N) to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR THE ORIGINAL TEXT LENGTH
    sN = pd.Series(N, index=ListOfIndexesCustomL) ## --> Converts ListOfNumbers (N) to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #21 - PANDAS OBJECTS CREATE")

    ## RETURN VARIABLES
    return(sL0, sL, sLLL0, sLLL, sN0, sN)



    