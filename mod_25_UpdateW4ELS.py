## IMPORT MODULES

## DEFINE FUNCTION ##
def fn_UpdateW4ELS(W4ELS, DELSO):

    """ """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #25 - UPDATE W4ELS OBJECT;")

    ## BEGIN SUMMARIZE ELS SEARCH MATCH DATA
    ## DECLARE VARIABLES
    i = 1

    MasterList = []

    ## BEGIN FOR LOOP
    for EachTuple in W4ELS:
        
        ## CONVERT TUPLE TO LIST
        ListNew = list(EachTuple)

        ## GET GEMATRIA VALUE OF THE WORD TO ALLOW FOR EASY SORTING OF CSV OUTPUT FILE
        WordTotalValueGematria = ListNew[1][2]

        ## ADD GEMATRIA VALUE OF THE WORD TO ALLOW FOR EASY SORTING OF CSV OUTPUT FILE
        ListNew.append(WordTotalValueGematria)

        ## ADD NUMBER OF MATCHES (POSITIVE)
        ListNew.append(DELSO[i].NMP)

        ## ADD NUMBER OF MATCHES (NEGATIVE)
        ListNew.append(DELSO[i].NMN)

        TempTup = tuple(ListNew)
        MasterList.append(TempTup)

        ## INCREMENT COUNTER
        i += 1

    ## END FOR LOOP

    W4ELS = tuple(MasterList)
    ## END SUMMARIZE ELS SEARCH MATCH DATA

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #25 - UPDATE W4ELS OBJECT;")

    ## RETURN VARIABLES
    return(W4ELS)