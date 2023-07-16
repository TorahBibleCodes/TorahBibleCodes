## IMPORT MODULES

## FUNCTION () #3A2 - TEXT FILE PREPROCESS - EXTRACT KEYS AND WORDS

def fn_ExtractKeysAndWords(TextKoren):
    
    """
    ## MODULE.FUNCTION() #3A2 - TEXT FILE PREPROCESS - EXTRACT KEYS AND WORDS; ## RETURNS ListOfTupleKeysToFix
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A2 TEXT FILE PREPROCESS - EXTRACT KEYS AND WORDS")

    ## DECLARE VARIABLES
    ListOfLines = []
    ListOfTupleKeysToFix = []
    ListOfWordsInLine = []

    ## BEGIN IF / ELIF
    ## BEGIN IF TEXT FILE IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT OR ALL FIVE (5) TEXTS
    if isinstance(TextKoren, str):
        
        ## TEST PRINT OUTPUT
        print("\n")
        print("TextKoren = ", len(TextKoren), type(TextKoren))

        ## SPLIT THE STRING AT THE NEW LINE \N CHARACTER
        ListOfStrings = TextKoren.split("\n")

        ## SPLIT STRINGS AT \n
        ## BEGIN FOR LOOP - FOR EACH LINE IN LIST OF STRINGS
        for EachLine in ListOfStrings:

            ## SPLIT THE STRING AT THE SPACES
            ListOfElementsInString = EachLine.split(" ")
        
            ## ADD EACH LIST OF ELEMENTS TO LIST OF LINES
            ListOfLines.append(ListOfElementsInString)

        ## END FOR LOOP - FOR EACH LINE IN LIST OF STRINGS

        ## DECLARE VARIABLES
        BookChapterVerse = []

        ## BEGIN FOR LOOP - EXTRACT TEXT STRINGS FOR EACH NUMBER
        for EachLine in ListOfLines:

            ## print(f"EachLine : {EachLine}, , {type(EachLine)}, {len(EachLine)}")

            ## GET LIST ELEMENTS OF THE WORDS IN LINE
            JustText = EachLine[3:]
            ## print(f'JustText : {JustText}')

            ## ADD LIST OF WORDS FOR EACH LINE
            ListOfWordsInLine.append(JustText)

            ## GET BIBLE BOOK, CHAPTER, VERSE INTEGER STRINGS
            ## IF FIRST ELEMENT IN EACH LINE IS NOT AN EMPTY STRING, I.E. IF INTEGER STRING
            if EachLine[0] != '':

                ## ADD INTEGER STRING TO LIST OF INTEGER STRINGS
                BookChapterVerse.append(EachLine[0])
                BookChapterVerse.append(EachLine[1])
                BookChapterVerse.append(EachLine[2])

            ## CONVERT LIST TO TUPLE
            TupleKeyToFix = tuple(BookChapterVerse)

            ## ADD 3-INTEGER TUPLE KEY TO LIST FOR KEYS (DUPLICATES HERE NEED TO BE PARSED)
            ListOfTupleKeysToFix.append(TupleKeyToFix)

            ## RESET LIST
            BookChapterVerse = [] ## RESET LIST

        ## END FOR LOOP - EXTRACT TEXT STRINGS FOR EACH NUMBER

    ## END IF / ELIF
    ## END IF TEXT FILE IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT OR ALL FIVE (5) TEXTS


    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A2 - TEXT FILE PREPROCESS - EXTRACT KEYS AND WORDS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfTupleKeysToFix, ListOfWordsInLine)
        
    ## END FUNCTION () #3A2 - END TEXT FILE PREPROCESS - EXTRACT KEYS AND WORDS