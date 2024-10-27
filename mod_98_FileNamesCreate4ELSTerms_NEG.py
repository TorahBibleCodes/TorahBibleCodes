## IMPORT MODULES

## FUNCTION () #98 - FILE NAMES CREATE ##
def fn_FileNamesCreate(XW, YH, NumberOfCodexChosen, NumberOfTextChosen, W4ELS, DELSO):

    """
    ## MODULE.FUNCTION() #98 - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #98 - FILE NAMES CREATE FOR ELS TERMS - NEGATIVE")

    ## DECLARE VARIABLES
    Dict4FileNames4ELSTerms = {}
    FileNamesForELSTerms = []
    XWString = str(XW)
    YHString = str(YH)

    ## BEGIN MATCH CASE
    match NumberOfCodexChosen:

        case 1:
            CodexTitle = "Koren"
        case 2:
            CodexTitle = "Leningrad"
        case 3:
            CodexTitle = "MiqraAccordingToMasorah_MAM"
    ## END MATCH CASE

    ## BEGIN IF ELSE BLOCK

    if NumberOfTextChosen == 1:
        TextTitle = "Genesis"

    elif NumberOfTextChosen == 2:
        TextTitle = "Exodus"

    elif NumberOfTextChosen == 3:
        TextTitle = "Leviticus"

    elif NumberOfTextChosen == 4:
        TextTitle = "Numbers"

    elif NumberOfTextChosen == 5:
        TextTitle = "Deuteronomy"

    elif NumberOfTextChosen == 6:
        TextTitle = "Joshua"

    elif NumberOfTextChosen == 7:
        TextTitle = "Judges"

    elif NumberOfTextChosen == 8:
        TextTitle = "ISamuel"

    elif NumberOfTextChosen == 9:
        TextTitle = "IISamuel"

    elif NumberOfTextChosen == 10:
        TextTitle = "IKings"

    elif NumberOfTextChosen == 11:
        TextTitle = "IIKings"

    elif NumberOfTextChosen == 12:
        TextTitle = "Isaiah"

    elif NumberOfTextChosen == 13:
        TextTitle = "Jeremiah"

    elif NumberOfTextChosen == 14:
        TextTitle = "Ezekiel"

    elif NumberOfTextChosen == 15:
        TextTitle = "Hosea"

    elif NumberOfTextChosen == 16:
        TextTitle = "Joel"

    elif NumberOfTextChosen == 17:
        TextTitle = "Amos"

    elif NumberOfTextChosen == 18:
        TextTitle = "Obadiah"

    elif NumberOfTextChosen == 19:
        TextTitle = "Jonah"

    elif NumberOfTextChosen == 20:
        TextTitle = "Micah"

    elif NumberOfTextChosen == 21:
        TextTitle = "Nahum"

    elif NumberOfTextChosen == 22:
        TextTitle = "Habakkuk"

    elif NumberOfTextChosen == 23:
        TextTitle = "Zephaniah"

    elif NumberOfTextChosen == 24:
         TextTitle = "Haggai"

    elif NumberOfTextChosen == 25:
        TextTitle = "Zechariah"

    elif NumberOfTextChosen == 26:
        TextTitle = "Malachi"

    elif NumberOfTextChosen == 27:
        TextTitle = "Psalms"

    elif NumberOfTextChosen == 28:
        TextTitle = "Proverbs"

    elif NumberOfTextChosen == 29:
        TextTitle = "Job"

    elif NumberOfTextChosen == 30:
        TextTitle = "SongOfSongs"

    elif NumberOfTextChosen == 31:
        TextTitle = "Ruth"

    elif NumberOfTextChosen == 32:
        TextTitle = "Lamentations"

    elif NumberOfTextChosen == 33:
        TextTitle = "Ecclesiastes"

    elif NumberOfTextChosen == 34:
        TextTitle = "Esther"

    elif NumberOfTextChosen == 35:
        TextTitle = "Daniel"

    elif NumberOfTextChosen == 36:
        TextTitle = "Ezra"

    elif NumberOfTextChosen == 37:
        TextTitle = "Nehemiah"

    elif NumberOfTextChosen == 38:
        TextTitle = "IChronicles"

    elif NumberOfTextChosen == 39:
        TextTitle = "IIChronicles"

    elif NumberOfTextChosen == 40:
        TextTitle = "TORAH_Instruction"

    elif NumberOfTextChosen == 41:
        TextTitle = "NEVIIM_Prophets"

    elif NumberOfTextChosen == 42:
        TextTitle = "KETUVIM_Writings"

    elif NumberOfTextChosen == 43:
        TextTitle = "TANACH_HebrewBible"

    elif NumberOfTextChosen == 44:
        TextTitle = "SAMUEL_Both_Books_Together"

    elif NumberOfTextChosen == 45:
        TextTitle = "KINGS_Both_Books_Together"

    elif NumberOfTextChosen == 46:
        TextTitle = "EZRA-NEHEMIAH_Both_Books_Together"

    elif NumberOfTextChosen == 47:
        TextTitle = "CHRONICLES_Both_Books_Together"
         
    
    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        pass

    ## DECLARE VARIABLES
    ELSMatchCounter = 1
    DictOfMatches = {}

    ## BEGIN FOR LOOP
    for EachELSTuple in W4ELS:

        ELSTerm = EachELSTuple[0] ## GET HEBREW WORD ## [::-1] ## REVERSE

        ## GET ELS NUMBER:
        ELSNumber = EachELSTuple[1][0] ## TUPLE IS BACKWARDS (('משיח', (1, [40, 300, 10, 8], 358), 83, 79),)

        ## GET DELSO OBJECT
        DictOfMatches = DELSO[ELSNumber].DELSMLF_NEG

        ## FOR EACH (n,d,k) MATCH:
        for key, value in DictOfMatches.items():

            n = key[0] ## ndkTuple[0] (n,d,k)
            ## print(f"n: {n}")

            d = key[1] ## ndkTuple[1] (n,d,k)
            ## print(f"d: {d}")

            k = key[2] ## ndkTuple[2] (n,d,k)
            ## print(f"n: {k}")

            ## CHECK IF SKIP DISTANCE (d) IS NEGATIVE OR POSITIVE
            ## IF SKIP DISTANCE (d) IS POSITIVE
            if d > 0:

                ## CREATE FILE NAME FOR POSITIVE SKIP DISTANCE (d)
                FileNameForELSTerm = f"USER_FILE_WordsOfELSs_POSITIVE_ELS{ELSNumber}_d{d}_n{n}_k{k}_ELSMatch{ELSMatchCounter}_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}_{ELSTerm}.csv"
                
                ## TEST PRINT OUTPUT
                ## print(f"FileNameForELSTerm: {FileNameForELSTerm}")

            ## ELSE IF SKIP DISTANCE (-d) IS NEGATIVE
            elif d < 0:

                ## CONVERT SKIP DISTANCE (d) TO POSITIVE TO COMPENSATE FOR ALPHABETICAL FILE NAMES
                d = (-1 * d)

                ## CREATE FILE NAME FOR NEGATIVE SKIP DISTANCE (-d)
                FileNameForELSTerm = f"USER_FILE_WordsOfELSs_NEGATIVE_ELS{ELSNumber}_ELSMatch{ELSMatchCounter}_-d{d}_n{n}_k{k}_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}_{ELSTerm}.csv"
                                
                ## TEST PRINT OUTPUT
                ## print(f"FileNameForELSTerm: {FileNameForELSTerm}")

            ## INCREMENT COUNTER
            ELSMatchCounter += 1

            ## APPEND FILE NAME TO LIST OF FILE NAMES
            FileNamesForELSTerms.append(FileNameForELSTerm)

            ## CREATE DICTIONARY WITH ELS FILE NAMES AS THE KEYS
            Dict4FileNames4ELSTerms[FileNameForELSTerm] = None

        ## END FOR LOOP

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #98 - FILE NAMES CREATE FOR ELS TERMS - NEGATIVE")

    ## RETURN VARIABLES TO PROGRAM
    return(FileNamesForELSTerms, Dict4FileNames4ELSTerms)

## END FUNCTION () #98- FILE NAMES CREATE
