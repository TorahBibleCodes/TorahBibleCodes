## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #8 - DATA OBJECTS CREATE
## FUNCTION () #8 - DATA OBJECTS CREATE
## FUNCTION () #8 - DATA OBJECTS CREATE

def fn_DataObjectsCreate(D, DS):
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #8 - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES      
    DL = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES 
    D5 = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES  
    L = [] ## EMPTY LIST TO HOLD LIST OF LETTERS
    LW = [] ## EMPTY LIST TO HOLD LIST OF WORDS
    ## LengthOfVerse = [] ## EMPTY LIST TO HOLD LENGTH OF EACH STRING IN EACH VERSE
    VerseLetterCounter = 1
    TotalLetterCounter = 1

    ## EMPTY LIST TO HOLD LIST OF VERSES - TEST FOR OA
    #ListOfVerses = []

    ## BEGIN FOR LOOP
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "D"...
    for key, each in D.items():
        
        ## COUNT LENGTH OF STRING, i.e. HOW MANY LETTERS IN EACH STRING
        LengthOfString = len(each)
        
        ## TEST PRINT OUTPUT
        #print("Key = ", key)
        #print("LengthOfVerse = ", LengthOfString)
        #print(each)

        ## FOR EACH LETTER IN STRING/VERSE...
        for letter in each:
            
            ## CREATE LIST OF LETTERS
            L.append(letter)
            #print(letter) ## COMPUTATION INTENSIVE
            
            ## EXPAND TUPLE KEY
            key4 = key + (VerseLetterCounter,)
            #print(t) ## COMPUTATION INTENSIVE
            
            ## CREATE DICTIONARY OF LETTERS - 4-DIGIT TUPLE-KEY
            DL[key4] = letter
            
            ## EXPAND TUPLE KEY
            key5 = key + (VerseLetterCounter, TotalLetterCounter,)
            
            ## CREATE DICTIONARY OF LETTERS - 5-DIGIT TUPLE-KEY
            D5[key5] = letter
            
            ## INCREASE LETTER COUNTER
            TotalLetterCounter += 1
            
            ## INCREASE VERSE COUNTER
            VerseLetterCounter += 1
        
        ## RESET VERSE LETTER COUNTER BACK TO 1       
        VerseLetterCounter = 1
        
        ## APPEND LENGTH OF STRING TO LIST OF STRING-LENGTHS
        ## LengthOfVerse.append(LengthOfString)

    ## END FOR LOOP


    ## CREATE STRING-SEQUENCE OF LETTERS FROM LIST OF LETTERS
    S = ''.join(L)


    ## DECLARE VARIABLES 
    ListOfWords = [] ## CREATE EMPTY LIST TO CONTAIN LIST OF WORDS FROM SELECTED TEXT(S)
        

    ## BEGIN FOR LOOP
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "DS"...
    for key, each in DS.items():
        
        ## COUNT LENGTH OF STRING, i.e. HOW MANY LETTERS IN EACH STRING
        LengthOfString = len(each)
        
        ## TEST PRINT OUTPUT
        #print("Key = ", key)
        #print("LengthOfVerse = ", LengthOfString)
        #print(each)

        ## CREATE LIST OF WORDS FOR ALL WORDS IN THE SELECTED TEXT
        ListOfWords.extend(each.split())

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ##print(len(ListOfWords), type(ListOfWords))
    ##print("ListOfWords[0:99] = ", ListOfWords[0:99])


    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #8 - DATA OBJECTS CREATE")

    ## RETURN VARIABLES TO PROGRAM
    ## RETURN TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS, DICTIONARY OF LETTERS)
    return(S, L, DL, D5, ListOfWords)

## END FUNCTION () #8 - DATA OBJECTS CREATE
## END FUNCTION () #8 - DATA OBJECTS CREATE
## END FUNCTION () #8 - DATA OBJECTS CREATE
