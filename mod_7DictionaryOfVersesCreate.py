## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## FUNCTION () #7 - DICTIONARY OF VERSES CREATE

def fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces):

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #7 - DICTIONARY OF VERSES CREATE")
          
    ## DECLARE VARIABLES      
    DictOfVersesNoSpaces = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES
    DictOfVersesWithSpaces = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES

    ## BELOW FOR ZIPPED TUPLE WITH NO SPACES
    
    ## EACH IS ZIPPED TUPLE:  INTEGER, DICTIONARY
    for each in ZippedTupleNoSpaces:
        
        ## TEST PRINT OUTPUT - each[0] = integer; each[1] = dictionary object
        ## print(each[0], each[1]['title'])
        ## print(len(each[1]['text'])) ## len(d['text']) = NUMBER OF CHAPTERS IN SELECTED TEXT
        ## print(type(each[1]['text'])) # type(d['text']) = LIST OF CHAPTERS (LIST OF LISTS) IN SELECTED TEXT
        
        NumberOfBook = each[0]
        NumberOfChapters = len(each[1]['text'])
    
        ## TEST PRINT OUTPUT
        ## print(NumberOfBook, NumberOfChapters)
        
        ChapterCounter = 1
        
        for Chapter in each[1]['text']:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("NumberOfBook = ", NumberOfBook)
            ## print("NumberOfChapters = ", NumberOfChapters)
            ## print("NumberOfChapter = ", ChapterCounter)
            ## print("Chapter = ", Chapter)
            
            VerseCounter = 1
            
            for Verse in Chapter:
                
                ## TEST PRINT OUTPUT
                ## print("\n")  ## PRINT SPACE
                ## print("NumberOfChapter = ", ChapterCounter)
                ## print("NumberOfVerse = ", VerseCounter)
                
                KeyTuple = (NumberOfBook, ChapterCounter, VerseCounter)
                
                ## TEST PRINT OUTPUT
                ## print("KeyTuple = ", KeyTuple)
                ## print("Verse = ", Verse)
                
                DictOfVersesNoSpaces[KeyTuple] = Verse
                
                VerseCounter += 1
            
            ChapterCounter += 1


    ## BELOW FOR ZIPPED TUPLE WITH SPACES
    
    ## EACH IS ZIPPED TUPLE:  INTEGER, DICTIONARY
    for each in ZippedTupleWithSpaces:
        
        ## TEST PRINT OUTPUT - each[0] = integer; each[1] = dictionary object
        ## print(each[0], each[1]['title'])
        ## print(len(each[1]['text'])) ## len(d['text']) = NUMBER OF CHAPTERS IN SELECTED TEXT
        ## print(type(each[1]['text'])) # type(d['text']) = LIST OF CHAPTERS (LIST OF LISTS) IN SELECTED TEXT
        
        NumberOfBook = each[0]
        NumberOfChapters = len(each[1]['text'])
    
        ## TEST PRINT OUTPUT
        ## print(NumberOfBook, NumberOfChapters)
        
        ChapterCounter = 1
        
        for Chapter in each[1]['text']:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("NumberOfBook = ", NumberOfBook)
            ## print("NumberOfChapters = ", NumberOfChapters)
            ## print("NumberOfChapter = ", ChapterCounter)
            ## print("Chapter = ", Chapter)
            
            VerseCounter = 1
            
            for Verse in Chapter:
                
                ## TEST PRINT OUTPUT
                ## print("\n")  ## PRINT SPACE
                ## print("NumberOfChapter = ", ChapterCounter)
                ## print("NumberOfVerse = ", VerseCounter)
                
                KeyTuple = (NumberOfBook, ChapterCounter, VerseCounter)
                
                ## TEST PRINT OUTPUT
                ## print("KeyTuple = ", KeyTuple)
                ## print("Verse = ", Verse)
                
                DictOfVersesWithSpaces[KeyTuple] = Verse
                
                VerseCounter += 1
            
            ChapterCounter += 1

            
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #7 - DICTIONARY OF VERSES CREATE")

    ## RETURN VARIABLES TO PROGRAM
    return(DictOfVersesNoSpaces, DictOfVersesWithSpaces)

## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE
