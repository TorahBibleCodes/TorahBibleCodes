## IMPORT MODULES

## FUNCTION () #3A4 - TEXT FILE PREPROCESS - FIX LINES ##
def fn_FixLines(ListOfTupleKeysForKoren, ListOfWordsForEachLine):
    
    """
    ## MODULE.FUNCTION() #3A4 - TEXT FILE PREPROCESS - FIX LINES; ## RETURNS DictOfVersesForKoren
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A4 - TEXT FILE PREPROCESS - FIX LINES")

    ## DECLARE VARIABLES
    DictOfVersesForKoren = {}

    ZippedTuple = tuple(zip(ListOfTupleKeysForKoren, ListOfWordsForEachLine))

    ## BEGIN FOR LOOP - FOR EACH ZIPPED TUPLE
    for EachTuple in ZippedTuple:

        ## BEGIN IF / ELSE
        ## IF TUPLE KEY ALREADY EXISTS IN DICT (BOOK#, CHAPTER#, VERSE#)
        if EachTuple[0] in DictOfVersesForKoren.keys(): ## (1,1,1) ## (1, 50, 26)

            ## GET CURRENT VALUE IN DICT ITEM
            ListOfWords = DictOfVersesForKoren[EachTuple[0]] ## ['WYMT', 'YWSP', 'BN', 'M)H', 'W($R', '$NYM', 'WYXN+W', ')TW', 'WYY$M', 'B)RWN', 'BMCRYM', '']

            ## EXTEND THAT LIST WITH THE NEXT LINE
            ListOfWords.extend(EachTuple[1])

        ## ELSE IF NOT YET IN DICT
        else:

            ## CREATE NEW TUPLE KEY IN DICT (BOOK#, CHAPTER#, VERSE#) TOGETHER WITH ITS VALUE
            DictOfVersesForKoren[EachTuple[0]] = EachTuple[1]

        ## END IF / ELSE

    ## END FOR LOOP - FOR EACH ZIPPED TUPLE

    ## BEGIN FOR LOOP - DELETE LAST ELEMENT (LIST) IF BLANK
    for k, v in list(DictOfVersesForKoren.items()):

        ## IF KEY IS NOT A 3-INTEGER TUPLE-KEY, THEN DELETE - e.g. ()
        if len(k) != 3:

            ## TEST PRINT OUTPUT
            ## print(k) ## SHOULD NOT PRINT IF ALL OK

            ## DELETE KEY
            del(DictOfVersesForKoren[k])
            
            ## print(f"len(DictOfVersesForKoren) : {len(DictOfVersesForKoren)}")

    ## BEGIN FOR LOOP - DELETE LAST ELEMENT (LETTER) IF BLANK  
    for k, v in DictOfVersesForKoren.items():

        ## BEGIN IF / ELSE - IF LIST NOT EMPTY
        ## IF NOT THE EMPTY LIST AT THE END
        if v != []:
        
            ## print(f"EachListOfWords : {v}")

            ## BEGIN IF / ELSE
            ## IF THE LAST ELEMENT IN LIST IS BLANK STRING / EMPTY
            if v[-1] == '':

                ## DELETE LAST ELEMENT IN LIST OF WORDS IF BLANK STRING / EMPTY
                del(v[-1])

            ## END IF / ELSE

        ## END IF / ELSE - IF LIST NOT EMPTY

        ## ELSE - DELETE LAST ELEMENT (LIST) IN LIST OF LISTS OF WORDS IF EMPTY
        elif v == []:
            
            ## SHOULD DELETE ONLY THE LAST BLANK LIST
            del(v)

    ## END FOR LOOP - DELETE LAST ELEMENT IF BLANK

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A4 - TEXT FILE PREPROCESS - FIX LINES")

    ## RETURN VARIABLES TO PROGRAM
    return(DictOfVersesForKoren)
