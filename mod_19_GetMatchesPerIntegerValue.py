import numpy as np
import math

## BEGIN FUNCTION () #19 -
def fn_GetMatchesPerIntegerValue(NW4ELS, NumpyArrayOfNumberValuesOfEntireText):

    """
    ## MODULE.FUNCTION() #19 - RETURNS: DictOfMatches4ELS
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #19")

    ## DECLARE VARIABLES
    DictOfMatches4ELS = {} ## EMPTY DICTIONARY TO HOLD ALL MATCHES

    ## BEGIN FOR EACH ELS TUPLE
    for EachELSTuple in NW4ELS:

        ELSSearchTermNumber = EachELSTuple[0] ## INTEGER ## ELS SEARCH TERM NUMBER
        AllLettersInELSSearchTerm = EachELSTuple[1] ## LIST OF NUMBERS ## ## GEMATRIA NUMBER VALUES [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
        k = len(AllLettersInELSSearchTerm) ## LENGTH OF ELS SEARCH TERM ## 4
        MaxSkipDistance = math.floor(len(NumpyArrayOfNumberValuesOfEntireText) / k)  ## MAXIMUM SKIP DISTANCE PER ELS SEARCH TERM

        ## BEGIN TEST DEVELOPMENT
        ListOfListsOfIndexMatches = []

        ## LetterCounter = 0 ## FOR 0-BASED LIST 

        ## FOUNDATION FOR CENTRAL SEARCH ALGORITHM: 
        ## 1.) FIND ALL MATCHES OF FIRST LETTER ONLY OF EACH ELS:
        ## 2.) FOR EACH INDEX POSITION n:
        ## 3.) CHECK FOR EACH SKIP DISTANCE d THAT VALUES RETRIEVED FOR EACH ELS INDEX POSITION n ARE EQUAL TO VALUE OF THE ELS: [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
        
        ## BEGIN FOR EACH LETTER ## FOR EACH FIRST LETTER ONLY(!) OF THE ELS SEARCH TERM
        for EachLetter in EachELSTuple[1]: ## FOR EACH LIST OF LETTER GEMATRIA NUMBER VALUES ## GEMATRIA NUMBER VALUES [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
            
            ## MAKE ARRAYS FOR MATCHING INDEX POSITIONS EACH LETTER IN ELS SEARCH TERM

            ## CREATE NUMPY ARRAY OF NUMBER VALUES
            IndexPositionsOfMatchesNPA = np.where(NumpyArrayOfNumberValuesOfEntireText == EachLetter) ## CREATES TUPLE

            ## print(len(IndexPositionsOfMatchesNPA)) ## LENGTH == 1
            ## print(type(IndexPositionsOfMatchesNPA)) ## TUPLE
            ## print(IndexPositionsOfMatchesNPA[0]) ## LIST
            IndexPositionsOfMatchesNPA = (IndexPositionsOfMatchesNPA[0] + 1) ## INCREASES 0-BASED INDEX POSITIONS BY 1 TO BE EQUAL TO DLO[i].LetterPositionIndex
            IndexPositionsOfMatchesNPA = list(IndexPositionsOfMatchesNPA) ## CONVERT EACH NUMPY ARRAY TO PURE PYTHON LIST
            ## print(IndexPositionsOfMatchesNPA)
            
            ListOfListsOfIndexMatches.append(IndexPositionsOfMatchesNPA) ## 0-BASED LISTS OF 1-BASED INDEX POSITIONS OF LETTERS OF ELS MATCHES

            ## Last = EachELSTuple[1][-1]

        ## END FOR EACH LETTER

        ## ArrayOfArrays4Letters = np.array(ListOfArrays)

        ## END TEST DEVELOPMENT
  
        ## BEGIN TEST DEVELOPMENT
        ## CONVERT NUMPY ARRAY OF INDEX MATCHES TO PYTHON LIST
        # IndexPositionsOfMatchesLIST = list(IndexPositionsOfMatchesNPA[0])
        ## END TEST DEVELOPMENT

        ## CREATE TEMP TUPLE
        TupleOfMatches4ELS = (ELSSearchTermNumber, AllLettersInELSSearchTerm, k, MaxSkipDistance, ListOfListsOfIndexMatches)
    
        ## ADD TUPLE AS VALUE TO DICTIONARY KEY POSITION
        DictOfMatches4ELS[ELSSearchTermNumber] = TupleOfMatches4ELS

    ## END FOR EACH ELS TUPLE

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #19")

    ## RETURN VARIABLES
    return(DictOfMatches4ELS)

## END FUNCTION () #19 -