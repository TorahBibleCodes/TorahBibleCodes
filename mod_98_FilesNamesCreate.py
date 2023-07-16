## IMPORT MODULES

## FUNCTION () #98 - FILE NAMES CREATE
def fn_FileNamesCreate(XW, YH, NumberOfTextChosen, NumberOfCodexChosen):

    """
    ## MODULE.FUNCTION() #98 - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #98 - FILE NAMES CREATE")

    ## DECLARE VARIABLES
    XWString = str(XW)

    YHString = str(YH)

    ## BEGIN MATCH CASE
    match NumberOfCodexChosen:

        case 1:
            CodexTitle = "Koren"
        case 2:
            CodexTitle = "Leningrad"
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
         

    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        pass

    ## CREATE DYNAMIC FILE NAME FOR CSV . XLSX FILES
    FileNameForMatrixXLSX = f"USER_FILE_Matrix2D_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.xlsx"
    FileNameForMatrixCSV = f"USER_FILE_Matrix2D_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.csv"
    FileNameForGematriaTexts = f"USER_FILE_WordsOfSelectedTexts_LetterPositions_GematriaValues_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.csv"
    FileNameForELSMatchesDataSummary = f"USER_FILE_WordsOfELSs_ELSMatches_DATASUMMARY_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.csv"
    FileNameForELSMatchesPositive = f"USER_FILE_WordsOfELSs_ELSMatches_POSITIVE_ALL_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.csv"
    FileNameForELSMatchesNegative = f"USER_FILE_WordsOfELSs_ELSMatches_NEGATIVE_ALL_{CodexTitle}_{NumberOfTextChosen}{TextTitle}_{XWString}x{YHString}.csv"
   
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #98 - FILE NAMES CREATE")

    ## RETURN VARIABLES TO PROGRAM
    return(FileNameForMatrixXLSX, FileNameForMatrixCSV, FileNameForGematriaTexts, FileNameForELSMatchesDataSummary,  FileNameForELSMatchesPositive,  FileNameForELSMatchesNegative)

## END FUNCTION () #98- FILE NAMES CREATE
