## IMPORT MODULES

## IMPORT CLASSES
from mod_cls_LetterObject import cls_LetterObject as LO

## FUNCTION () #8A - DATA OBJECTS CREATE ##
def fn_DataObjectsCreate(D):
    
    """
    ## MODULE.FUNCTION() #8A - DATA OBJECTS CREATE; ## RETURNS TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS WITH 4-DIGIT TUPLE-KEY, DICTIONARY OF LETTERS WITH 5-DIGIT TUPLE-KEY
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #8A - DATA OBJECTS CREATE")
    
    ## DECLARE VARIABLES      
    DL = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES 
    D5 = {} ## EMPTY DICTIONARY TO HOLD KEYS + VERSES  
    L = [] ## EMPTY LIST TO HOLD LIST OF LETTERS
    DictOfLetterObjects = {} ## EMPTY DICTIONARY TO HOLD KEY OF LETTER OBJECT: DICTIONARY OF LETTER OBJECTS

    VerseLetterCounter = 1
    TotalLetterCounter = 1
    
    ## EMPTY LIST TO HOLD LIST OF VERSES - TEST FOR OA
    #ListOfVerses = []

    ## BEGIN FOR LOOP
    ## FOR EACH KEY:VALUE PAIR IN STRING/VERSE IN DICTIONARY "D"...
    for key, each in D.items():
        
        ## COUNT LENGTH OF STRING, i.e. HOW MANY LETTERS IN EACH STRING
        LengthOfString = len(each) ## EACH VERSE
        
        ## TEST PRINT OUTPUT
        #print("Key = ", key)
        #print("LengthOfVerse = ", LengthOfString)
        #print(each)

        ## BEGIN FOR LOOP
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

            ## ADD KEY FOR DS FOR EACH LETTER TO LETTER OBJECT
            ## INITIALIZE / CREATE INSTANCE OF CLASS: LETTER OBJECT ## ALL OTHER VALUES SET TO DEFAULT NONE
            lo = LO(Letter=letter, LetterPositionIndex=TotalLetterCounter, LetterCoordinatesD5K=key5, LetterCoordinatesDL=key4, VerseCoordinatesDS=key)

            ## CREATE KEY IN DICT + ADD INSTANCE OF EACH LETTER OBJECT CLASS OF ENTIRE TEXT
            DictOfLetterObjects[TotalLetterCounter] = lo

            ## INCREASE LETTER COUNTER
            TotalLetterCounter += 1
            
            ## INCREASE VERSE COUNTER
            VerseLetterCounter += 1

        ## END FOR LOOP
        
        ## RESET VERSE LETTER COUNTER BACK TO 1       
        VerseLetterCounter = 1
        
        ## APPEND LENGTH OF STRING TO LIST OF STRING-LENGTHS
        ## LengthOfVerse.append(LengthOfString)

    ## END FOR LOOP

    ## CREATE STRING-SEQUENCE OF LETTERS FROM LIST OF LETTERS
    S = ''.join(L)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #8A - DATA OBJECTS CREATE ")

    ## RETURN VARIABLES TO PROGRAM
    ## RETURN TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS WITH 4-DIGIT TUPLE-KEY, DICTIONARY OF LETTERS WITH 5-DIGIT TUPLE-KEY, LIST OF LETTER OBJECTS INSTANCES)
    return(S, L, DL, D5, DictOfLetterObjects) 

## END FUNCTION () #8A - DATA OBJECTS CREATE

