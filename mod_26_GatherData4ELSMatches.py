## IMPORT MODULES

## DEFINE FUNCTION
def fn_GatherData4ELSMatches(DictOfSearchTerms, DLO, DW, DELSO, DictOfELSMatchesAbsolute, DS):

    """ ## MODULE.FUNCTION() #26 - ## RETURNS: """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #26")

    LTM4ELS_ABS= [] ## LIST OF TUPLE MATCHES 4 ELS SEARCH TERMS: ABSOLUTE POSITIVE OR NEGATIVE

    c = 1 ## COUNTER

    ## BEGIN FOR LOOP FOR EACH SET OF MATCHES, I.E. FOR ALL DICTS OF TUPLES IN DELSMP
    for EachDict in DictOfELSMatchesAbsolute.values(): ## DELSMP[1] #DELSMP[2] ## DELSMN[1] ## DELSMN[2] ## FOR EACH ELS SEARCH TERM ## 2 FOR MESSIAH & THE MESSIAH

        ## BEGIN FOR LOOP FOR EACH TUPLE IN SET OF MATCHES FOR ELS SEARCH TERM 
        for EachTuple in EachDict.items(): 

            print("Each Tuple", EachTuple)
            print(EachTuple[0]) ## GET EACH (n, d, k) DICT KEY FOR EACH MATCH
            print(EachTuple[1]) ## GET EACH [40, 300, 10, 8] DICT VALUE FOR EACH MATCH
            print(EachTuple[0][0]) ## GET EACH INDEX LETTER POSITION (n)
            print(type(EachTuple))

            ## GET EACH (n, d, k) DICT KEY FOR EACH MATCH
            ndk = EachTuple[0]

            ## GET EACH GEMATRIA VALUES OF LETTERS IN WORD
            GematriaValues = EachTuple[1]

            ## GET EACH (n)
            n = ndk[0]

            ## GET EACH (n)'s WORD NUMBER
            WordNumber = DLO[n].WordNumber

            ## GET EACH (n)'s WORD COORDINATES DWTK
            WordCoordinatesDWT = DLO[n].WordCoordinatesDWT

            ## GET EACH (n)'s WORD TEXT
            WordText = DW[WordNumber][0]

            ## GET EACH (n)'s LETTER POSITION WITHIN WORD
            LetterPositionInWord = (DW[WordNumber][1].index(DLO[n].LetterPositionIndex) + 1) ## DEAL WITH 0-INDEX ## q = List.index(n)

            ## GET EACH n's VERSE NUMBER
            LetterCoordinatesD5K = DLO[n].LetterCoordinatesD5K

            ## GET EACH ELS SEARCH TERM NUMBER
            ELSSearchTermNumber = DELSO[c].ELSSearchTermNumber

            ## GET EACH LETTER'S VERSE NUMBER
            VerseCoordinatesDS = DLO[n].VerseCoordinatesDS

            ## CREATE TUPLE
            TupleTest = (ndk, GematriaValues, DictOfSearchTerms[ELSSearchTermNumber], WordNumber, WordCoordinatesDWT, WordText, LetterPositionInWord, LetterCoordinatesD5K, DS[VerseCoordinatesDS])

            ## APPEND VALUE TO LIST TO BE RETURNED
            LTM4ELS_ABS.append(TupleTest)

        ## END FOR LOOP

        ## INCREMENT COUNTER
        c += 1

    ## END FOR LOOP

    ## DECLARE VARIABLES

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #26")

    ## RETURN VARIABLES
    return(LTM4ELS_ABS)