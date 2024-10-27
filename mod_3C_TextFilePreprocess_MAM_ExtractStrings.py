## IMPORT MODULES
import re
import unicodedata
import mod_3CC_TextFileParse_MAM

## BEGIN FUNCTION () #3C #1 - CONVERT BOOK NAME TO NUMBER 
def fn_ConvertBookNameToNumber(BookName):

    ## BEGIN MATCH CASE
    match BookName:

        case "Genesis":
            BookNumber = 1
        case "Exodus":
            BookNumber = 2
        case "Leviticus":
            BookNumber = 3
        case "Numbers":
            BookNumber = 4
        case "Deuteronomy":
            BookNumber = 5
        case "Joshua":
            BookNumber = 6
        case "Judges":
            BookNumber = 7
        case "I Samuel":
            BookNumber = 8
        case "II Samuel":
            BookNumber = 9
        case "I Kings":
            BookNumber = 10
        case "II Kings":
            BookNumber = 11
        case "Isaiah":
            BookNumber = 12
        case "Jeremiah":
            BookNumber = 13
        case "Ezekiel":
            BookNumber = 14
        case "Hosea":
            BookNumber = 15
        case "Joel":
            BookNumber = 16
        case "Amos":
            BookNumber = 17
        case "Obadiah":
            BookNumber = 18
        case "Jonah":
            BookNumber = 19
        case "Micah":
            BookNumber = 20
        case "Nahum":
            BookNumber = 21
        case "Habakkuk":
            BookNumber = 22
        case "Zephaniah":
            BookNumber = 23
        case "Haggai":
            BookNumber = 24
        case "Zechariah":
            BookNumber = 25
        case "Malachi":
            BookNumber = 26
        case "Psalms":
            BookNumber = 27
        case "Proverbs":
            BookNumber = 28
        case "Job":
            BookNumber = 29
        case "Song of Songs":
            BookNumber = 30
        case "Ruth":
            BookNumber = 31
        case "Lamentations":
            BookNumber = 32
        case "Ecclesiastes":
            BookNumber = 33
        case "Esther":
            BookNumber = 34
        case "Daniel":
            BookNumber = 35
        case "Ezra":
            BookNumber = 36
        case "Nehemiah":
            BookNumber = 37
        case "I Chronicles":
            BookNumber = 38
        case "II Chronicles":
            BookNumber = 39
        ## case "Pentateuch (Torah)":
        ##     BookNumber = 41
        ## case "Prophets (Nevi'im)":
        ##     BookNumber = 42
        ## case "Hebrew Bible (Tanach)":
        ##     BookNumber = 43

    ## END MATCH CASE
    
    ## RETURN VARIABLES
    return(BookNumber)

## END FUNCTION

## BEGIN FUNCTION() - #2 - REMOVE PASEQ HERE BECAUSE IT DOES NOT GET REMOVED WHEN PLACED AFTER THE NORMALIZATION
def fn_RemovePaseq(text):

    ## PATTERN TO MATCH PASEQ
    pattern = r'\u05C0'  # Paseq

    ## REPLACE THE MATCHED PATTERNS WITH AN EMPTY STRING
    clean_text = re.sub(pattern, ' ', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION () #3C #3 - 
def fn_HebrewTextNormalize(TextHebrew):

    """
        # Normalize the text to decompose combined characters into their base characters and diacritics
        normalized_text = unicodedata.normalize('NFD', text)
        
        # Define a regex pattern to match Hebrew diacritic marks EXCLUDING MAQAF (UNICODE: \u05BE) IN ORDER TO KEEP IT WITH THE HEBREW LETTERS
        ## PatternOfDiacritics = re.compile(r'[\u0591-\u05B9\u05BB-\u05C7]') 
        ## diacritics_pattern = re.compile(r'[\u0591-\u05C7]') ## ALL DIACRITIC MARKS
        ## 
        
        # Remove the diacritics from the normalized text
        cleaned_text = diacritics_pattern.sub('', normalized_text)
        
        # Normalize the text back to the composed form
        return unicodedata.normalize('NFC', cleaned_text)
    """

    ## REMOVE PASEQ - REMOVE PASEQ HERE BECAUSE IT DOES NOT GET REMOVED WHEN PLACED AFTER THE NORMALIZATION
    TextWithNoPaseq = fn_RemovePaseq(TextHebrew)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoPaseq : {TextWithNoPaseq}")
    ## print(f"TextWithNoPaseq : {TextWithNoPaseq[::-1]}")

    # NORMALIZE TEXT TO DECOMPOSE CHARACTERS INTO BASE CHARACTERS AND DIACRITICS
    TextNormalized = unicodedata.normalize('NFD', TextWithNoPaseq)

    ## REMOVE MAQAFS FROM STRING
    TextNormalizedNoMaqafs = TextNormalized.replace("־", " ")
    
    # DEFINE REGEX PATTERN TO MATCH HEBREW DIACRITIC MARKS - ALL DIACRITIC MARKS
    PatternOfDiacritics = re.compile(r'[\u0591-\u05C7]')
    
    # REMOVE DIACRITICS FROM NORMALIZED TEXT
    TextCleaned = PatternOfDiacritics.sub('', TextNormalizedNoMaqafs)
    
    ## TextCleaned = PatternOfDiacritics(TextHebrew)
    ## print(f"Normalized text: {TextNormalized}")
    ## print(f"Cleaned text: {TextCleaned}")

    # NORMALIZE AND RETURN TEXT BACK TO COMPOSED FORM 
    return(unicodedata.normalize('NFC', TextCleaned))

## END FUNCTION

## BEGIN MAIN FUNCTION
## FUNCTION () #3C #0 - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS (BELOW)
def fn_ExtractStrings(ListOfTuples):
    
    """
    ## MODULE.FUNCTION() #3C - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS; ## RETURNS ListOfTupleKeysToFix
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3C TEXT FILE PREPROCESS - EXTRACT KEY STRINGS")
    ## print(ListOfTuples)

    ## DECLARE VARIABLES
    ListOfLines = []
    ListOfTupleKeys = []
    DictOfListsOfWordsInVerse = {}
    DictOfKeysVersesWithSpaces = {}
    DictOfKeysVersesNoSpaces = {}

    ## IF TXT IS A TUPLE... ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS
    ## BEGIN IF / ELIFs
    if isinstance(ListOfTuples, tuple):
        
        TextString = ""

        ## ...THEN FOR EACH STRING IN TUPLE...CONCATENATE THE STRINGS
        ## BEGIN FOR LOOP
        for EachTuple in ListOfTuples: ## EachTuple[0] = EACH BOOK; ## EachTuple[1] = EACH BOOK, ## EachTuple[2] = EACH BOOK

            """ ListOfTuples, e.g.
            ( [('Daniel 12:10',
                'יִ֠תְבָּֽרְר֠וּ וְיִֽתְלַבְּנ֤וּ וְיִצָּֽרְפוּ֙ רַבִּ֔ים וְהִרְשִׁ֣יעוּ רְשָׁעִ֔ים וְלֹ֥א יָבִ֖ינוּ כׇּל־רְשָׁעִ֑ים וְהַמַּשְׂכִּלִ֖ים יָבִֽינוּ׃'),
              ('Daniel 12:11',
                'וּמֵעֵת֙ הוּסַ֣ר הַתָּמִ֔יד וְלָתֵ֖ת שִׁקּ֣וּץ שֹׁמֵ֑ם יָמִ֕ים אֶ֖לֶף מָאתַ֥יִם וְתִשְׁעִֽים׃'),
              ('Daniel 12:12',
                'אַשְׁרֵ֥י הַֽמְחַכֶּ֖ה וְיַגִּ֑יעַ לְיָמִ֕ים אֶ֕לֶף שְׁלֹ֥שׁ מֵא֖וֹת שְׁלֹשִׁ֥ים וַחֲמִשָּֽׁה׃'),
              ('Daniel 12:13',
                'וְאַתָּ֖ה לֵ֣ךְ לַקֵּ֑ץ וְתָנ֛וּחַ וְתַעֲמֹ֥ד לְגֹרָלְךָ֖ לְקֵ֥ץ הַיָּמִֽין׃')], )
            """

            ## TEST PRINT OUTPUT
            ## print(f"EachTuple : {EachTuple}", len(EachTuple), type(EachTuple))

            for EachTupleOfVerse in EachTuple: ## 

                ## TEST PRINT OUTPUT
                ## print(f"EachTupleOfVerse : {EachTupleOfVerse}", len(EachTupleOfVerse), type(EachTupleOfVerse))
                ## print(f"EachTupleOfVerse : {EachTupleOfVerse[::-1]}", len(EachTupleOfVerse), type(EachTupleOfVerse))

                ## EXTRACT TEXT STRING KEY TO FIX
                KeyToFix = EachTupleOfVerse[0] ## --RETURNS--> 'Daniel 12:10'
                
                ## EXTRACT TEXT STRING VERSE TO FIX
                VerseToParse = EachTupleOfVerse[1] ## --RETURNS--> 'VERSE IN HEBREW'
                
                ## print(f"KeyToFix : {KeyToFix}")

                ## SPLIT TEXT STRING TO BOOK NAME AND CHAPTER:VERSE
                BookChapterVerse = KeyToFix.split(" ") ## 'Daniel 12:10' --RETURNS--> ['Daniel', '12:10'] ## 'II Samuel 1:1' --RETURNS--> ['II', 'Samuel', '1:1']

                ## BEGIN IF / ELSE
                ## IF
                if len(BookChapterVerse) == 4: ## SONG OF SONGS --> ['Song', 'of', 'Songs', '1:1']

                    BookNumber = 30
                    BookName = " ".join(BookChapterVerse[0:3]) ## 'Song of Songs'

                ## ELIF
                elif len(BookChapterVerse) == 3: ## I SAMUEL --> ['II', 'Samuel', '1:1'], OR II SAMUEL, I KINGS, II KINGS, I CHRONICLES, II CHRONICLES: 

                    ##
                    BookName = " ".join(BookChapterVerse[0:2]) ## 'I SAMUEL ## II SAMUEL, ETC.

                    ## BEGIN MATCH CASE: ## IF THERE IS A SPACE IN THE BOOKNAME TEXT STRING
                    match BookName: # 'I Samuel' ## 'II Samuel' ## 'I Kings' ## 'II Kings' ## 'I Chronicles' ## 'II Chronicles' ## 'Song of Songs'
                        
                        ## 
                        case 'I Samuel':

                            BookNumber = 8

                        ## 
                        case 'II Samuel':

                            BookNumber = 9

                        ## 
                        case 'I Kings':

                            BookNumber = 10

                        ## 
                        case 'II Kings':

                            BookNumber = 11

                        ## 
                        case 'I Chronicles':

                            BookNumber = 38

                        ## 
                        case 'II Chronicles':

                            BookNumber = 39

                    ## END MATCH CASE

                ## ELSE
                else: ## ALL OTHER CASES: BOOKS WITH ONE WORD ONLY: E.G. GENESIS, EXODUS, LEVITICUS...

                    ## EXTRACT TEXT STRING BOOK NAME
                    BookName = BookChapterVerse[0] ## --RETURNS--> 'Daniel'

                ## END IF / ELSE

                ## TEST PRINT OUTPUT
                ## print(f"BookName : {BookName}")

                ## SPLIT TEXT STRING TO CHAPTER AND VERSE
                ChapterVerse = BookChapterVerse[-1].split(":") ## '12:10' --RETURNS --> ['12', '10']

                ## ASSIGN INTEGER TO CHAPTER NUMBER VARIABLE
                Chapter = int(ChapterVerse[0]) ## 12
                
                ## ASSIGN INTEGER TO CHAPTER NUMBER VARIABLE
                Verse = int(ChapterVerse[1]) ## 10

                ## CALL FUNCTION FOR EACH BOOK NAME TO CONVERT TO INTEGER
                BookNumber = fn_ConvertBookNameToNumber(BookName) ## --RETURNS--> PYTHON INTEGER NUMBER

                ## CONVERT INTEGER INTO TUPLE NOW IN ORDER TO INTEGRATE INTO PREVIOUS CODE IN P.PY
                ## SearchTextChosen = (BookNumber,)

                ## CREATE TUPLE KEY FOR (BOOK, CHAPTER, VERSE)
                KeyFixed = (BookNumber, Chapter, Verse)

                ## APPEND TUPLE KEY TO LIST OF TUPLE KEYS
                ListOfTupleKeys.append(KeyFixed)
                
                ## TEST - REMOVE PASEQ


                ## CALL FUNCTION TO NORMALIZE/PARSE VERSE
                VerseNormalized = fn_HebrewTextNormalize(VerseToParse)

                ## TEST PRINT OUTPUT
                ## print(f"{KeyFixed}")
                ## print(f"{VerseToParse}")
                ## print(f"{VerseNormalized}")
                ## print(f"{VerseNormalized[::-1]}")
            
                ## PARSE EACH VERSE INDIVIDUALLY
                TextParsedWithSpaces, TextParsedNoSpaces, ListOfWordsInVerse = mod_3CC_TextFileParse_MAM.fn_TextFileParse(VerseNormalized)

                ## print(f"TextParsedWithSpaces : {TextParsedWithSpaces}")
                ## print(f"TextParsedNoSpaces : {TextParsedNoSpaces}")

                ## ADD KEY : VERSE TO DICTIONARY
                DictOfKeysVersesWithSpaces[KeyFixed] = TextParsedWithSpaces
                DictOfKeysVersesNoSpaces[KeyFixed] = TextParsedNoSpaces

                ## 
                DictOfListsOfWordsInVerse[KeyFixed] = ListOfWordsInVerse

            ## TEST PRINT OUTPUT
            ## print("\n")
            ## print("ListOfTuples = ", len(ListOfTuples), type(ListOfTuples))
           
        ## END FOR LOOP

        ## TEST PRINT OUTPUT
        print("\n")  ## PRINT SPACE
        print("WITHIN FUNCTION:  END FUNCTION #3C - TEXT FILE PREPROCESS - EXTRACT KEY STRINGS")

        ## RETURN VARIABLES
        return(DictOfKeysVersesWithSpaces, DictOfKeysVersesNoSpaces, DictOfListsOfWordsInVerse)
    
        ## ...THEN CALL MODULE.FUNCTION() #3A2 
        ## ListOfTupleKeysToFix, ListOfWordsInLine = mod_3A2_TextFilePreprocess_Koren_ExtractKeysAndWords.fn_ExtractKeysAndWords(TextString)
    
    ## END IF / ELIF 

    ## RETURN VARIABLES TO PROGRAM
    ## return(ListOfTupleKeys, ListOfWordsInLine)
        
    ## END FUNCTION () #3C - END TEXT FILE PREPROCESS - EXTRACT KEY STRINGS ##