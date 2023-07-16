## IMPORT MODULES
import time
TimeStart = time.time()

## DEFINE FUNCTION
def fn_ELSSearch(sL, sN, DELSO, DLO):

    """ ## MODULE.FUNCTION() #23 - ## RETURNS: DictOfMatches """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #23 - ELS SEARCH - NEGATIVE DIRECTION;")
    
    ## TEST PRINT OUTPUT
    print("\n")
    print(sL)
    print("\n")
    print("Please wait while your ELS Search is conducted...")

    ## DECLARE VARIABLES
    DictOfMatches = {} ## KEY IS (n, d, k) WITH ELS MATCH
        
    ## BEGIN FOR EACH ELS OBJECT IN DICT OF ELS OBJECTS
    for EachELSObject in DELSO.values():  ## DELSO[1] ## DELSO[2] ## DELSO[3]

        ## BEGIN FOR EACH LETTER IN ARRAY OF POSITIONS FOR FIRST LETTER OF ELS SEARCH TERM
        # n, (n + d), (n + 2d), (n + 3d)... (n + (k-1)d)
        # n = EachIndexPosition

        ListTemp = [] ## TEMPORARY LIST
        DictTemp = {} ## TEMPORARY DICTIONARY
        
        ELSSearchTermNumber = EachELSObject.ELSSearchTermNumber
        k = EachELSObject.k ## LENGTH OF ELS TERM
        d = 1 ## SKIP DISTANCE STARTING POINT
        c = list(range(0,k)) ## COUNTER
        
        ## BEGIN WHILE LOOP
        while d < 101: ## while d < EachELSObject.MaxSkipDistance: ## LIMIT TO 100 B/C MAXSKIPDISTANCE MAKES THE PYTHON SEARCH SLOW

            ## TEST PRINT OUTPUT
            ## print("d = ", d)

            ## FOR EACH LAST LETTER IN EACH ELS OBJECT
            for EachIndexPosition in EachELSObject.ListOfListsOfIndexMatches[-1]: ## DELSO[1].ListOfListsOfIndexMatches[-1]  ## ARRAY OF LAST LETTER MATCHES INDEX POSITIONS (n)

                ## GET INDEX POSITION NUMBER N
                n = DLO[EachIndexPosition].LetterPositionIndex

                ## TEST PRINT OUTPUT
                ## print("n = ", n)

                ## CREATE TEMPORARY TUPLE TO HOLD UNIQUE KEY OF (n, d, k)
                TupleTemp = (n, d, k)

                ## BEGIN FOR LOOP FOR k
                for EachNumber in c: ## [0,1,2,3] ## ~k

                    ## CLEVER MATCH TO PYTHONICALLY DEAL WITH THE SEARCH FORMULA (N,D,K)
                    e = (EachNumber * d) ## (0*1), (1*1), (2*1), (3*1)

                    ## sN[n] 
                    ## n, (n + d), (n + 2d), (n + 3d)... (n + (k-1)d)
                    ## sN[n] ## EACH INDEX POSITION OF 1ST LETTER IN ELS
                    ## sN[n+d] ## EACH INDEX POSITION OF 2ND LETTER IN ELS
                    ## sN[n+(2*d)]  ## EACH INDEX POSITION OF 3RD LETTER IN ELS
                    ## sN[n+(3*d)] == sN[n+((k-1)*d)] ## EACH INDEX POSITION OF 4TH LETTER IN ELS

                    ## BEGIN TRY / EXCEPT:
                    ## TRY:
                    try:
                        
                        Letter = sN[n + e]

                        ListTemp.append(Letter)

                    ## EXCEPT:
                    except Exception as e:
                        
                        ## TEST PRINT OUTPUT
                        ## print(f'caught {type(e)}: e') ## KeyError
                        pass
            
                    ## END TRY / EXCEPT

                ## END FOR LOOP FOR k
                            
                ## BEGIN IF / ELSE 
                ## IF ELS MATCH
                if ListTemp == EachELSObject.Letters[::-1]:

                    ## ADD TUPLE TO DICT
                    DictTemp[n, d, k] = ListTemp ## sN[n] ## CREATE KEY WITH INDEX POSITION (n); ADD LIST TO DICT
                    
                    ## TEST PRINT OUTPUT
                    ## print(f"ListTemp = {ListTemp} : EachELSObject.Letters = {EachELSObject.Letters}")
                
                ## ELSE
                else: 

                    pass

                ## END IF / ELSE

                ## RESET LIST
                ListTemp = [] ## RESET TEMPORARY LIST

            ## INCREMENT DISTANCE COUNTER
            d += 1

        ## END WHILE LOOP

        ## ADD TEMP DICT FOR EACH ELS SEARCH TERM TO DICT OF MATCHES
        DictOfMatches[ELSSearchTermNumber] = DictTemp

    ## END FOR EACH ELS OBJECT IN DICT OF ELS OBJECTS

    ## TEST PRINT OUTPUT
    print("--- %s seconds ---" % (time.time() - TimeStart))

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #23 - ELS SEARCH - NEGATIVE DIRECTION;")

    ## RETURN VARIABLES
    return(DictOfMatches)



    