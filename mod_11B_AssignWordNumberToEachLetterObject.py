## IMPORT MODULES

## DEFINE FUNCTION
## FUNCTION () #11B - 
def fn_AssignWordNumberToEachLetterObject(DLO, DW, DWTK):

    """
    ## MODULE.FUNCTION() #11B - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #11B")

    ## DECLARE VARIABLES FOR FOR LOOP BELOW WITH 1-INDEX DW OBJECT
   
    ## DW[1] == ('בראשית', [1, 2, 3, 4, 5, 6], (1, [2, 200, 1, 300, 10, 400], 913))

    for key, EachWordTuple in DW.items(): ## 1-BASED KEY, VALUE: EachWordTuple == DW[1] == ('בראשית', [1, 2, 3, 4, 5, 6], (1, [2, 200, 1, 300, 10, 400], 913))

        for EachIndexPosition in EachWordTuple[1]: ## 2ND ITEM IN 0-BASED TUPLE: [1, 2, 3, 4, 5, 6]

            if EachIndexPosition == DLO[EachIndexPosition].LetterPositionIndex:

                DLO[EachIndexPosition].WordNumber = key

                ## TEST
                DLO[EachIndexPosition].WordCoordinatesDWT = DWTK[key]

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #11B")

    ## RETURN VARIABLES
    return(DLO)

## END FUNCTION () #11B - 
