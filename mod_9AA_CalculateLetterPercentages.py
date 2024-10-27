## IMPORT MODULES

## BEGIN FUNCTION () #9AA - CALCULATE LETTER PERCENTAGES ##
def fn_CalculatePercentages(S):

    """
    ## MODULE.FUNCTION() #9AA - CALCULATE LETTER PERCENTAGES
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #9AA - CALCULATE LETTER PERCENTAGES ")

    Letter1 = ("א", S.count("א"))
    Letter2 = ("ב", S.count("ב"))
    Letter3 = ("ג", S.count("ג"))
    Letter4 = ("ד", S.count("ד"))
    Letter5 = ("ה", S.count("ה"))
    Letter6 = ("ו", S.count("ו"))
    Letter7 = ("ז", S.count("ז"))
    Letter8 = ("ח", S.count("ח"))
    Letter9 = ("ט", S.count("ט"))
    Letter10 = ("י", S.count("י"))
    Letter11A = ("כ", S.count("כ"))
    Letter11B = ("ך", S.count("ך"))
    Letter11 = ("כ/ך", Letter11A[1] + Letter11B[1])

    Letter12 = ("ל", S.count("ל"))
    Letter13A = ("מ", S.count("מ"))
    Letter13B = ("ם", S.count("ם"))
    Letter13 = ("מ/ם", Letter13A[1] + Letter13B[1])

    Letter14A = ("נ", S.count("נ"))
    Letter14B = ("ן", S.count("ן"))
    Letter14 = ("נ/ן", Letter14A[1] + Letter14B[1])

    Letter15 = ("ס", S.count("ס"))
    Letter16 = ("ע", S.count("ע"))
    Letter17A = ("פ", S.count("פ"))
    Letter17B = ("ף", S.count("ף"))
    Letter17 = ("פ/ף", Letter17A[1] + Letter17B[1])

    Letter18A = ("צ", S.count("צ"))
    Letter18B = ("ץ", S.count("ץ"))
    Letter18 = ("צ/ץ", Letter18A[1] + Letter18B[1])

    Letter19 = ("ק", S.count("ק"))
    Letter20 = ("ר", S.count("ר"))
    Letter21 = ("ש", S.count("ש"))
    Letter22 = ("ת", S.count("ת"))

    ListOfTuplesOfLetterInstances = (Letter1, Letter2, Letter3, Letter4, Letter5, Letter6, Letter7, Letter8, Letter9, Letter10, Letter11A, Letter11B, Letter11, Letter12, Letter13A, Letter13B, Letter13, Letter14A, Letter14B, Letter14, Letter15, Letter16, Letter17A, Letter17B, Letter17, Letter18A, Letter18B, Letter18, Letter19, Letter20, Letter21, Letter22)

    ListOfTuplesOfLetterStatistics = []
    
    LengthOfText = len(S)

    ## BEGIN FOR LOOP
    for EachLetterTuple in ListOfTuplesOfLetterInstances:

        ## TEST PRINT OUTPUT
        ## print(f"EachLetterTuple: {EachLetterTuple}")

        TempList = []

        NumberOfLetterInstances = EachLetterTuple[1]
        PercentageOfLetterInTextAsDecimal = NumberOfLetterInstances / LengthOfText
        PercentageOfLetterInTextAsPercentage = (PercentageOfLetterInTextAsDecimal * 100)

        TempList.append(EachLetterTuple[0])
        TempList.append(NumberOfLetterInstances)
        TempList.append(LengthOfText)
        TempList.append(PercentageOfLetterInTextAsDecimal)
        TempList.append(PercentageOfLetterInTextAsPercentage)

        TempTuple = tuple(TempList)

        ListOfTuplesOfLetterStatistics.append(TempTuple)
    
    ## END FOR LOOP
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #9AA - CALCULATE LETTER PERCENTAGES")

    ## RETURN VARIABLE(S)
    return(ListOfTuplesOfLetterStatistics)

## END FUNCTION () #9AA - CALCULATE LETTER PERCENTAGES
