## IMPORT MODULES

## DEFINE FUNCTION
def fn_UpdateW(W, DWTK):

    """ """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #26 - UPDATE W OBJECT;")

    ## BEGIN UPDATE OF W OBJECT
    ## DECLARE VARIABLES
    i = 1

    MasterList = []

    ## BEGIN FOR LOOP
    for EachTuple in W:
        
        ListTemp = []

        ## CONVERT TUPLE TO LIST
        ListNew = list(EachTuple)

        ## ADD DWTK ~ DictOfWordsTotalKey
        ListTemp.append(DWTK[i])

        ## ADD OTHER LIST
        ListTemp.extend(ListNew)

        ## MAKE TUPLE
        TempTup = tuple(ListTemp)

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