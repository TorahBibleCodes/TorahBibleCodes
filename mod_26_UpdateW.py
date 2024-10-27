## IMPORT MODULES

## DEFINE FUNCTION ##
def fn_UpdateW(W, DWTK):

    """ FUNCTION #26 - UPDATE W OBJECT """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #26 - UPDATE W OBJECT;")

    ## BEGIN UPDATE OF W OBJECT
    ## DECLARE VARIABLES
    i = 1

    MasterList = []

    ## BEGIN FOR LOOP
    for EachTuple in W:

        ## TEST PRINT OUTPUT
        ## print(f"EachTuple: {EachTuple}")
        
        ListTemp = []

        ## CONVERT TUPLE TO LIST
        ListNew = list(EachTuple)

        ## GET GEMATRIA VALUE OF THE WORD TO ALLOW FOR EASY SORTING OF CSV OUTPUT FILE
        WordTotalValueGematria = ListNew[2][2]

        ## ADD GEMATRIA VALUE OF THE WORD TO ALLOW FOR EASY SORTING OF CSV OUTPUT FILE
        ListNew.append(WordTotalValueGematria)

        ## TEST PRINT OUTPUT
        ## print(f"ListNew: {ListNew}")

        ## ADD DWTK ~ DictOfWordsTotalKey
        ListTemp.append(DWTK[i])

        ## TEST PRINT OUTPUT
        ## print(f"ListTemp: {ListTemp}")

        ## ADD OTHER LIST
        ListTemp.extend(ListNew)

        ## TEST PRINT OUTPUT
        ## print(f"ListTemp: {ListTemp}")

        ## MAKE TUPLE
        TempTup = tuple(ListTemp)

        ## TEST PRINT OUTPUT
        ## print(f"TempTup: {TempTup}")

        ## APPEND TUPLE TO MASTER LIST
        MasterList.append(TempTup)

        ## INCREMENT COUNTER
        i += 1

    ## END FOR LOOP

    ## CONVERT NEW LIST TO TUPLE
    W = tuple(MasterList)

    ## END UPDATE OF W OBJECT

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #26 - UPDATE W OBJECT;")

    ## RETURN VARIABLES
    return(W)