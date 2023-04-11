## IMPORT MODULES

## FUNCTION () #9AA - 
def fn_AddGematriaNumberValuesToLetterObjects(DLO, N):

    """
    ## MODULE.FUNCTION() #9AA - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #9AA")

    ## TEST - ADD GEMATRIA NUMBER VALUES TO EACH LETTER OBJECT (LO) IN DICTIONARY OF LETTER OBJECTS (DLO)

    ## DECLARE VARIABLES - FOR FOR LOOP BELOW WITH 0-INDEX N OBJECT
    CurrentLetterIndexPosition = 0
    TotalLetterCount = 1

    ## ADDING LETTER NUMBER VALUE PROPERTY VALUE TO EACH INSTANCE OF LETTER OBJECT
    for EachLetterObject in DLO.values():

        ## GET VALUE OF NUMBER BY INDEX START:STOP
        LetterGematriaNumberValue = N[CurrentLetterIndexPosition: TotalLetterCount]
        
        ## ADD VALUE OF NUMBER TO INSTANCE OF LETTER OBJECT
        EachLetterObject.LetterGematriaNumberValue = LetterGematriaNumberValue

        ## INCREMENT
        CurrentLetterIndexPosition += 1
        TotalLetterCount += 1
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #9AA")

    ## RETURN VARIABLES
    return(DLO)

## END FUNCTION () #9AA - 