## IMPORT MODULES

## DEFINE FUNCTION ##
def fn_ExtractAllELSLetterPositions(LTM4ELS_LF_ABS, DLO, DW, DS):

    """ FUNCTION #28 - EXTRACT ALL ELS LETTER POSITIONS """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #28 - EXTRACT ALL ELS LETTER POSITIONS;")

    List4IndexMatches = [] ## SKIP DISTANCE (d) TO CALCULATE ALL LETTER POSITIONS
    ListTemp = []
    ListOfTuples4LetterInfo = []
    MasterList4LetterPositions = [] ## TO HOLD LIST OF TUPLES

    ## FOR EACH ELS SEARCH TERM
    for each in LTM4ELS_LF_ABS:
    
        ## GRAB (n,d,k)
        ndk = each[0]

        ##TEST PRINT OUTPUT
        ## print("\n")
        ## print(f"ndk: {ndk} ; type: {type(ndk)}")

        ## GET POSITION (n) OF FIRST LETTER IN ELS MATCH ## 726
        n = ndk[0] ## (n,d,k)

        ##TEST PRINT OUTPUT
        ## print(f"n: {n} ; type: {type(n)}")

        ## GET SKIP DISTANCE (d) ## 5, 2
        d = ndk[1] ## (n,d,k)

        ##TEST PRINT OUTPUT
        ## print(f"d: {d} ; type: {type(d)}")

        ## GET LENGTH OF ELS TERM (k)
        k = ndk[2] ## (n,d,k)

        ##TEST PRINT OUTPUT
        ## print(f"k: {k} ; type: {type(k)}")

        ## GET RANGE OF ELS TERM
        if d > 0: ## IF POSITIVE SKIP DISTANCE (d)

            RangeOfELSTerm = (d * (k - 1))
            ##TEST PRINT OUTPUT
            ## print(f"RangeOfELSTerm: {RangeOfELSTerm} ; type: {type(RangeOfELSTerm)}")
            
            ## INDEX POSITION OF LAST LETTER IN ELS TERM
            PositionOfFinalLetter = (n + RangeOfELSTerm)
            ##TEST PRINT OUTPUT
            ## print(f"PositionOfFinalLetter: {PositionOfFinalLetter} ; type: {type(PositionOfFinalLetter)}")

        elif d < 0: ## IF NEGATIVE SKIP DISTANCE (d)

            RangeOfELSTerm = ((-1 * d) * (k - 1))
            ##TEST PRINT OUTPUT
            ## print(f"RangeOfELSTerm: {RangeOfELSTerm} ; type: {type(RangeOfELSTerm)}")

            ## INDEX POSITION OF FIRST LETTER IN ELS TERM
            PositionOfFinalLetter = (n - RangeOfELSTerm)
            ##TEST PRINT OUTPUT
            ## print(f"PositionOfFinalLetter: {PositionOfFinalLetter} ; type: {type(PositionOfFinalLetter)}")


        ## IF POSITIVE: CALCULATE RANGE FORWARD ACC. TO SKIP DISTANCE (d) ## 89
        if d > 0:

            ## FOR EACH LETTER POSITION INDEX
            for integer in range(n, (PositionOfFinalLetter + 1), d): ## POSITIVE DIRECTION ## SKIP DISTANCE (d) FORWARDS TO FINAL LETTER

                ## APPEND LETTER POSITION INDEX
                List4IndexMatches.append(integer) ## SKIP DISTANCE (d) BACKWARDS TO ZERO
            
            ##TEST PRINT OUTPUT
            ## print(f"PositionOfFinalLetter: {List4IndexMatches} ; type: {type(List4IndexMatches)}")


        ## IF NEGATIVE: CALCULATE RANGE BACKWARD ACC. TO SKIP DISTANCE (d) ## -89
        elif d < 0:

            ## FOR EACH LETTER POSITION INDEX
            for integer in range(n, (PositionOfFinalLetter - 1), d): ## POSITIVE DIRECTION ## SKIP DISTANCE (d) FORWARDS TO FINAL LETTER

                ## APPEND LETTER POSITION INDEX
                List4IndexMatches.append(integer) ## SKIP DISTANCE (d) BACKWARDS TO ZERO

            ##TEST PRINT OUTPUT
            ## print(f"List4IndexMatches: {List4IndexMatches} ; type: {type(List4IndexMatches)}")

        ## TEST PRINT OUTPUT
        ## print(f"IndexPositionOfFirstMatch: {IndexPositionOfFirstMatch}")

        ## TEST PRINT OUTPUT
        ## print(f"List4IndexMatches: {List4IndexMatches}")

        ## RESET
        ## List4IndexMatches = []

        ## CALCULATE RANGE FORWARDS ACC. TO SKIP DISTANCE (d) ## 89
        ## FOR EACH LETTER INDEX POSITION
        for numero in List4IndexMatches: ## ALL LETTER POSITIONS (n) IN ELS TERM

            ## GET EACH (n)'s WORD NUMBER FOR FINDING LETTER POSITION INDEX BELOW FOR EACH LETTER IN ELS
            WordNumber = DLO[numero].WordNumber

            ## UPDATE DLO WITH EACH (n)'s LETTER POSITION IN WORD FOR EACH LETTER IN ELS
            DLO[numero].LetterPositionInWord = (DW[WordNumber][1].index(DLO[numero].LetterPositionIndex) + 1) ## DEAL WITH 0-INDEX
            
            ## GET EACH (n)'s WORD TEXT FOR UPDATING DLO FOR EACH LETTER IN ELS
            WordText = DW[WordNumber][0]

            ## UPDATE DLO WITH WORD TEXT 
            DLO[numero].Word = WordText

            ## EXTRACT WORD NUMBER IN VERSE
            WordNumberInVerse = DLO[numero].WordCoordinatesDWTK[3] ## FOURTH ELEMENT IN TUPLE: (1,1,1,1,1)

            ## UPDATE DLO WITH WORD NUMBER IN VERSE
            DLO[numero].WordNumberInVerse = WordNumberInVerse

            ## GET EACH LETTER'S VERSE NUMBER COORDINATES TO EXTRACT VERSE TEXT
            VerseCoordinatesDS = DLO[numero].VerseCoordinatesDS

            ## GET EACH (n)'s VERSE TEXT FOR UPDATING DLO FOR EACH LETTER IN ELS
            VerseText = DS[VerseCoordinatesDS]

            ## UPDATE DLO WITH EACH (n)'s VERSE TEXT FOR UPDATING DLO FOR EACH LETTER IN ELS
            DLO[numero].Verse = VerseText

            ## APPEND ID INFORMATOIN FOR THE ABOVE LETTER
            ListTemp.append(ndk)
            ListTemp.append(DLO[numero].LetterGematriaNumberValue)
            ListTemp.append(DLO[numero].Letter)
            ListTemp.append(DLO[numero].LetterPositionIndex)
            ListTemp.append(DLO[numero].LetterCoordinatesD5K)
            ListTemp.append(DLO[numero].Word)
            ListTemp.append(DLO[numero].LetterPositionInWord)
            ListTemp.append(DLO[numero].WordNumber)
            ListTemp.append(DLO[numero].WordCoordinatesDWTK)
            ListTemp.append(DLO[numero].WordNumberInVerse)
            ListTemp.append(DLO[numero].Verse)

            """
            HEADERS FOR CSV OUTPUT
            ["(n,d,k)", "LetterGematriaNumberValue", "Letter", "LetterPositionIndex", "LetterCoordinatesD5K", "Found in Word in Text", "LetterPositionIndex In Word", "WordNumber", "WordCoordinatesDWTK", "WordNumberInVerse", "Found In Verse"]
            """

            ## CONVERT INFO FOR EACH LETTER TO TUPLE
            TupleOfLetterInfo = tuple(ListTemp)
            ##print(f"TupleOfLetterInfo : {TupleOfLetterInfo}")

            ## APPEND TUPLE TO THE LIST OF LETTER INFO
            ListOfTuples4LetterInfo.append(TupleOfLetterInfo)

            ## RESET
            ListTemp = []

        ## RESET
        List4IndexMatches = []

        ## APPEND
        MasterList4LetterPositions.append(ListOfTuples4LetterInfo)

        ## RESET
        ListOfTuples4LetterInfo = []

    ## print(ListOfTuples4LetterInfo)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #28 - EXTRACT ALL ELS LETTER POSITIONS;")

    ## RETURN VARIABLES
    return(MasterList4LetterPositions, DLO) ## == TOTAL NUMBER OF ELS TERM MATCHES FOUND FOR ALL ELS TERMS