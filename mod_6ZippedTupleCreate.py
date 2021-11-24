## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #6 - ZIPPED TUPLE CREATE
## FUNCTION () #6 - ZIPPED TUPLE CREATE
## FUNCTION () #6 - ZIPPED TUPLE CREATE
def fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen):

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #6 - ZIPPED TUPLE CREATE")
    
    ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS OF TORAH...
    if len(ListOfDictsOfJSONStringsParsed) == 5:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
        
        ## LOOP THROUGH TUPLE - TEST PRINT OUTPUT
        ## for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 5 TEXTS OF TORAH CHOSEN = ", each[0],len(each[1]))
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 5 TEXTS OF TORAH CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
        
    ## ...ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) TEXTS OF THE PROPHETS (NEVI'IM):
    elif len(ListOfDictsOfJSONStringsParsed) == 21:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
        
        ## LOOP THROUGH TUPLE - TEST PRINT OUTPUT
        ## for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 21 TEXTS OF THE PROPHETS CHOSEN = ", each[0],len(each[1]))
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 21 TEXTS OF THE PROPHETS CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
        
    ## ...ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) TEXTS OF THE WRITINGS (K'TUVIM):
    elif len(ListOfDictsOfJSONStringsParsed) == 13:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
        
        ## LOOP THROUGH TUPLE - TEST PRINT OUTPUT
        ## for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 13 TEXTS OF THE WRITINGS CHOSEN = ", each[0],len(each[1]))
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 13 TEXTS OF THE WRITINGS CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
        
    ## ...ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) TEXTS OF THE HEBREW BIBLE (TANACH):
    elif len(ListOfDictsOfJSONStringsParsed) == 39:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
        
        ## LOOP THROUGH TUPLE - TEST PRINT OUTPUT
        ## for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 39 TEXTS OF THE HEBREW BIBLE CHOSEN = ", each[0],len(each[1]))
            ## print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ALL 39 TEXTS OF THE HEBREW BIBLE CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
        
    ## ...ELSE IF TEXT CHOSEN IS ONLY ONE (1) TEXT:
    elif len(ListOfDictsOfJSONStringsParsed) == 1:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED  
        ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
        
        ## TEST PRINT OUTPUT
        ## print("ZIPPED TUPLE IN FUNCTION 6 = ", ZippedTuple)
    
        ## LOOP THROUGH TUPLE - TEST PRINT OUTPUT
        ## for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("HERE IS EACH ELEMENT IN ZIPPEDTUPLE = ", each)
            ## print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", len(each), type(each))
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", each[0],len(each[1]))
            ## print("Z = ", each[0],len(each[1]))
            
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", each[0],len(each[1]))
            ## print("Z = ", type(each[0]),type(each[1]))
            
            ## TEST PRINT OUTPUT
            ##print("\n")  ## PRINT SPACE
                   
        ## RETURN ZIPPED TUPLE
        return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
        
    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        
        pass      
          

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #6 - ZIPPED TUPLE CREATE")

## END FUNCTION () #6 - ZIPPED TUPLE CREATE
## END FUNCTION () #6 - ZIPPED TUPLE CREATE
## END FUNCTION () #6 - ZIPPED TUPLE CREATE
