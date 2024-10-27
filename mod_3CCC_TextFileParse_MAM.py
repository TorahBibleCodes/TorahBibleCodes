## IMPORT MODULES

## FUNCTION () #3CCC - TEXT FILE PARSE
def fn_TextFileParse(DVMAM): ## DictOfVerses for MAM

    """
    ## MODULE.FUNCTION() #3CCC - TEXT FILE PARSE ## RETURNS 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3CCC - TEXT FILE PARSE")
         
    ## DECLARE VARIABLES
    DVMAMH = {} # DictOfVerses for MAM - HEBREW LETTERS (NO SPACES)
    DVMAMHS = {} # DictOfVerses for MAM - HEBREW LETTERS (WITH SPACES)

    LetterCountInVerse = 0
    LetterCountTotal = 0
    WordCountInVerse = 0
    WordCountTotal = 0
    VerseCountTotal = 0

    TempListForWord = []
    TempListForVerse = []
    ListOfWordsForAllVerses = []

    ## BEGIN TEXT FILE PARSE

    ## BEGIN FOR LOOP FOR EACH VERSE (LIST OF WORDS)
    for k, EachListOfWords in DVMAM.items():
        
        ## CONVERT LIST ELEMENTS TO STRING
        
        ## BEGIN FOR LOOP FOR EACH WORD
        for EachWord in EachListOfWords:
            
            ## BEGIN FOR LOOP FOR EACH LETTER
            for index, EachLetter in enumerate(EachWord):

                ## INCREMENT LETTER COUNTERS
                LetterCountInVerse += 1
                LetterCountTotal += 1

                ## ADD LETTER TO WORD
                TempListForWord.append(EachLetter)
    
            ## END FOR LOOP FOR EACH LETTER

            ## CONVERT LIST OF LETTERS TO WORD STRING
            WordString = ''.join(TempListForWord)

            ## RESET LIST
            TempListForWord = []

            ## INCREMENT COUNTER FOR WORDS
            WordCountInVerse += 1
            WordCountTotal += 1

            ## ADD WORD TO TEMP LIST FOR WORDS IN VERSE
            TempListForVerse.append(WordString)

        ## END FOR LOOP FOR EACH WORD

        ## TEST PRINT OUTPUT
        ## print(f"TempListForVerse : {TempListForVerse}")

        ## RESET LETTER / WORD COUNTERS FOR VERSE
        LetterCountInVerse = 0
        WordCountInVerse = 0  

        ## INCREMENT VERSE COUNTER
        VerseCountTotal += 1
        
        ## TEST PRINT OUTPUT
        ## print(f"Verse #: {VerseCountTotal}")

        ## TEST PRINT OUTPUT
        ## print(f"TempListForVerse : {TempListForVerse}")

        ## CONVERT LIST OF WORDS TO VERSE STRING (NO SPACES)
        VerseStringNoSpaces = ''.join(TempListForVerse)

        ## CONVERT LIST OF WORDS TO VERSE STRING (WITH SPACES)
        VerseStringWithSpaces = ' '.join(TempListForVerse)

        DVMAMH[k] = VerseStringNoSpaces

        DVMAMHS[k] = VerseStringWithSpaces

        ## RESET LIST
        TempListForVerse = []

    ## END FOR LOOP FOR EACH VERSE (LIST OF WORDS)

    ## ADD VERSE TO LIST FOR ALL VERSES
    #ListOfWordsForAllVerses.append(TempListForVerse)
    #print(ListOfWordsForAllVerses)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3CCC - TEXT FILE PARSE")

    ## RETURN VARIABLES TO PROGRAM - RETURNS TUPLE OF TWO TEXTS (LISTS):  1.) WITH SPACES; 2.) WITH NO SPACES
    return(ListOfWordsForAllVerses, DVMAMH, DVMAMHS, VerseCountTotal, WordCountTotal, LetterCountTotal) ## return(TextParsedWithSpaces, TextParsedNoSpaces)

## END FUNCTION () #3CCC - TEXT FILE PARSE ##

