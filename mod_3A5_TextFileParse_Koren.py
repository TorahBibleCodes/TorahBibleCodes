## IMPORT MODULES

## FUNCTION () #3A5 - TEXT FILE PARSE ##
def fn_TextFileParse(DVK): ## DictOfVersesForKoren

    """
    ## MODULE.FUNCTION() #3A5 - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A5 - TEXT FILE PARSE")
         
    ## DECLARE VARIABLES
    DVKH = {} # DictOfVersesForKoren - HEBREW LETTERS (NO SPACES)
    DVKHS = {} # DictOfVersesForKoren - HEBREW LETTERS (WITH SPACES)

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
    for k, EachListOfWords in DVK.items():
        
        ## CONVERT LIST ELEMENTS TO STRING
        
        ## BEGIN FOR LOOP FOR EACH WORD
        for EachWord in EachListOfWords:
            
            ## BEGIN FOR LOOP FOR EACH LETTER
            for index, EachLetter in enumerate(EachWord):

                ## BEGIN MATCH CASE
                match EachLetter:

                    case ')':

                        TempLetter = 'א'

                    case 'B':

                        TempLetter = 'ב'

                    case 'G':

                        TempLetter = 'ג'

                    case 'D':

                        TempLetter = 'ד'

                    case 'H':

                        TempLetter = 'ה'

                    case 'W':

                        TempLetter = 'ו'

                    case 'Z':

                        TempLetter = 'ז'

                    case 'X':

                        TempLetter = 'ח'

                    case '+':

                        TempLetter = 'ט'

                    case 'Y':

                        TempLetter = 'י'

                    case 'K':

                        ## BEGIN IF / ELSE
                        ## IF NOT LAST LETTER IN WORD
                        if index != (len(EachWord) - 1):

                            TempLetter = 'כ'

                        ## ELSE IF LAST LETTER IN WORD
                        else:

                            TempLetter = 'ך'

                        ## END IF / ELSE

                    case 'L':

                        TempLetter = 'ל'
  
                    case 'M':

                        ## BEGIN IF / ELSE
                        ## IF NOT LAST LETTER IN WORD
                        if index != (len(EachWord) - 1):

                            TempLetter = 'מ'

                        ## ELSE IF LAST LETTER IN WORD
                        else:

                            TempLetter = 'ם'

                        ## END IF / ELSE

                    case 'N':

                        ## BEGIN IF / ELSE
                        ## IF NOT LAST LETTER IN WORD
                        if index != (len(EachWord) - 1):

                            TempLetter = 'נ'

                        ## ELSE IF LAST LETTER IN WORD
                        else:

                            TempLetter = 'ן'
                            
                        ## END IF / ELSE

                    case 'S':

                        TempLetter = 'ס'

                    case '(':

                        TempLetter = 'ע'

                    case 'P':

                        ## BEGIN IF / ELSE
                        ## IF NOT LAST LETTER IN WORD
                        if index != (len(EachWord) - 1):

                            TempLetter = 'פ'

                        ## ELSE IF LAST LETTER IN WORD
                        else:

                            TempLetter = 'ף'
                            
                        ## END IF / ELSE

                    case 'C':

                        ## BEGIN IF / ELSE
                        ## IF NOT LAST LETTER IN WORD
                        if index != (len(EachWord) - 1):

                            TempLetter = 'צ'

                        ## ELSE IF LAST LETTER IN WORD
                        else:

                            TempLetter = 'ץ'
                            
                        ## END IF / ELSE
  
                    case 'Q':

                        TempLetter = 'ק'

                    case 'R':

                        TempLetter = 'ר'

                    case '$':

                        TempLetter = 'ש'
                        
                    case 'T':

                        TempLetter = 'ת'
                
                ## END MATCH CASE

                ## INCREMENT LETTER COUNTERS
                LetterCountInVerse += 1
                LetterCountTotal += 1

                ## ADD LETTER TO WORD
                TempListForWord.append(TempLetter)
    
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

        DVKH[k] = VerseStringNoSpaces

        DVKHS[k] = VerseStringWithSpaces

        ## RESET LIST
        TempListForVerse = []

    ## END FOR LOOP FOR EACH VERSE (LIST OF WORDS)

    ## ADD VERSE TO LIST FOR ALL VERSES
    #ListOfWordsForAllVerses.append(TempListForVerse)
    #print(ListOfWordsForAllVerses)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A5 - TEXT FILE PARSE")

    ## RETURN VARIABLES TO PROGRAM - RETURNS TUPLE OF TWO TEXTS (LISTS):  1.) WITH SPACES; 2.) WITH NO SPACES
    return(ListOfWordsForAllVerses, DVKH, DVKHS, VerseCountTotal, WordCountTotal, LetterCountTotal) ## return(TextParsedWithSpaces, TextParsedNoSpaces)

## END FUNCTION () #3A5 - TEXT FILE PARSE

