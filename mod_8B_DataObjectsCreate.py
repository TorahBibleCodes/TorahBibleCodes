## IMPORT MODULES

## FUNCTION () #8B - DATA OBJECTS CREATE

def fn_DataObjectsCreate(DS):

    """
    ## MODULE.FUNCTION() #8B - DATA OBJECTS CREATE; ## RETURNS LIST OF WORDS
    """
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #8B - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES 
    ListOfWords = [] ## CREATE EMPTY LIST TO CONTAIN LIST OF WORDS FROM SELECTED TEXT(S)   
    ListOfWordsEachVerse = [] ## LIST OF WORDS PER VERSE 
    ListOfNumbersOfWordsEachVerse = []
    
    DWV = {} ## DictionaryOfWordsInVerse
    DWT = {} ## DictionaryOfWordsTotal

    
    TotalWordCounter = 1
    
    ## BEGIN FOR LOOP
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "DS"...
    for key, each in DS.items(): ## EACH VERSE
        
        ## COUNT LENGTH OF STRING, i.e. HOW MANY LETTERS IN EACH STRING
        LengthOfString = len(each) ## EACH VERSE
        
        ## TEST PRINT OUTPUT
        #print("Key = ", key)
        #print("LengthOfVerse = ", LengthOfString)
        #print(each)

        ## SPLIT STRING INTO LIST OF WORDS
        ListOfWordsEachVerse = each.split()

        ## COUNT NUMBER OF WORDS IN VERSE
        NumberOfWordsEachVerse = len(ListOfWordsEachVerse)

        ## TEST PRINT OUTPUT
        print(f"ListOfWordsEachVerse : {ListOfWordsEachVerse}")

        VerseWordCounter = 1

        ## FOR LOOP
        for EachWord in ListOfWordsEachVerse:

            ## EXPAND TUPLE KEY
            keyWV = key + (VerseWordCounter,)
            #print(t) ## COMPUTATION INTENSIVE

            ## CREATE DICTIONARY OF WORDS IN VERSE - 4-DIGIT TUPLE-KEY
            DWV[keyWV] = EachWord

            ## EXPAND TUPLE KEY
            keyWT = keyWV + (TotalWordCounter,)
            #print(t) ## COMPUTATION INTENSIVE

            ## CREATE DICTIONARY OF WORDS IN VERSE - 4-DIGIT TUPLE-KEY
            DWT[keyWT] = EachWord

            ## INCREMENT
            VerseWordCounter += 1
            TotalWordCounter += 1

        ## END FOR LOOP

        ## ADD NUMBER OF WORDS IN EACH VERSE TO LIST OF NUMBERS
        ListOfNumbersOfWordsEachVerse.append(NumberOfWordsEachVerse)

        ## CREATE LIST OF WORDS FOR ALL WORDS IN THE SELECTED TEXT
        ListOfWords.extend(ListOfWordsEachVerse) ## SPLIT EACH VERSE INTO WORDS AND ADDS EACH WORD

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ## print(len(ListOfWords), type(ListOfWords))
    ## print("ListOfWords[0:99] = ", ListOfWords[0:99])

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #8B - DATA OBJECTS CREATE")

    ## RETURN VARIABLES TO PROGRAM
    ## RETURN LIST OF WORDS
    return(ListOfWords, ListOfNumbersOfWordsEachVerse, DWV, DWT) 

## END FUNCTION () #8 - DATA OBJECTS CREATE

