## IMPORT CLASSES
from mod_cls_ELSObject import cls_ELSObject as ELSO

## CREATE ELS OBJECTS
## FUNCTION() #20 - DATA OBJECT CREATE - RETURNS DICT OF ELS OBJECTS ##
def fn_DictOfELSObjectsCreate(DictOfMatches4ELS):

    """
    ## MODULE.FUNCTION() #20 - RETURNS: DELSO
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #20 - DICT OF ELS OBJECTS (DELSO) - CREATE")

    ## DECLARE VARIABLES
    DELSO = {} ## Dictionary of ELS Objects

    ## BEGIN FOR LOOP
    for EachTuple in DictOfMatches4ELS.values():
        
        ## CREATE INSTANCE OF ELS OBJECT
        elso = ELSO()

        ## UPDATE THE OBJECT PROPERTIES.
        elso.ELSSearchTermNumber = EachTuple[0]
        elso.Letters = EachTuple[1] ## GEMATRIA NUMBER VALUES  ## GEMATRIA NUMBER VALUES [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
        elso.WordGematriaNumberValue = None
        elso.k = EachTuple[2]
        elso.MaxSkipDistance = EachTuple[3]
        ## x = DELSO[1].ArrayOfArraysOfIndexPositions[0]+1 ## INCREASES 0-BASED INDEX POSITIONS BY 1 TO GET EXACT LetterPositionIndex
        elso.ListOfListsOfIndexMatches = EachTuple[4] ##  (EachTuple[1] + 1) ## INCREASES 0-BASED INDEX POSITIONS BY 1 TO BE EQUAL TO DLO[i].LetterPositionIndex
        
        ## CREATE KEY NUMBER
        key = EachTuple[0] ## ELS SEARCH NUMBER ## INTEGER
        
        ## ADD OBJECT TO DICT OF ELS OBJECTS
        DELSO[key] = elso
    
    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #20 - DICT OF ELS OBJECTS (DELSO) - CREATE")

    ## RETURN
    return(DELSO)

## END FUNCTION() #20 - DATA OBJECT CREATE - RETURNS DICT OF ELS OBJECTS