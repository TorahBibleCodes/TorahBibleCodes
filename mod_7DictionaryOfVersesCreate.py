## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## FUNCTION () #7 - DICTIONARY OF VERSES CREATE

def fn_DictionaryOfVersesCreate(ZippedTuple):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #7 - DICTIONARY OF VERSES CREATE")
          
    ## DECLARE VARIABLES      
    DictOfVerses = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES
    
    ## EACH IS ZIPPED TUPLE:  INTEGER, DICTIONARY
    for each in ZippedTuple:
        
        ## TEST PRINT OUTPUT - each[0] = integer; each[1] = dictionary object
        print(each[0], each[1]['title'])
        print(len(each[1]['text'])) ## len(d['text']) = NUMBER OF CHAPTERS IN SELECTED TEXT
        print(type(each[1]['text'])) # type(d['text']) = LIST OF CHAPTERS (LIST OF LISTS) IN SELECTED TEXT
        
        NumberOfBook = each[0]
        NumberOfChapters = len(each[1]['text'])
    
        ## TEST PRINT OUTPUT
        print(NumberOfBook, NumberOfChapters)
        
        ChapterCounter = 1
        
        for Chapter in each[1]['text']:
            print("\n")  ## PRINT SPACE
            print("NumberOfBook = ", NumberOfBook)
            print("NumberOfChapters = ", NumberOfChapters)
            print("NumberOfChapter = ", ChapterCounter)
            print("Chapter = ", Chapter)
            
            VerseCounter = 1
            
            for Verse in Chapter:
                print("\n")  ## PRINT SPACE
                print("NumberOfChapter = ", ChapterCounter)
                print("NumberOfVerse = ", VerseCounter)
                
                KeyTuple = (NumberOfBook, ChapterCounter, VerseCounter)
                print("KeyTuple = ", KeyTuple)
                print("Verse = ", Verse)
                
                DictOfVerses[KeyTuple] = Verse
                
                VerseCounter += 1
            
            ChapterCounter += 1
                                
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #7 - DICTIONARY OF VERSES CREATE")

    ## RETURN VARIABLES TO PROGRAM
    return(DictOfVerses)

## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE
## END FUNCTION () #7 - DICTIONARY OF VERSES CREATE