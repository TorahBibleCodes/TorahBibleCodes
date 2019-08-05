## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #6 - ZIPPED TUPLE CREATE
## FUNCTION () #6 - ZIPPED TUPLE CREATE
## FUNCTION () #6 - ZIPPED TUPLE CREATE
def fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, SearchTextChosen):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #6 - ZIPPED TUPLE CREATE")
    
    ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS OF TORAH...
    if len(ListOfDictsOfJSONStringsParsed) == 5:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTuple = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        
        ## LOOP THROUGH TUPLE ()
        for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 5 TEXTS OF TORAH CHOSEN = ", each[0],len(each[1]))
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 5 TEXTS OF TORAH CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTuple)
        
    ## ...ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) TEXTS OF THE PROPHETS (NEVI'IM):
    elif len(ListOfDictsOfJSONStringsParsed) == 21:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTuple = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        
        ## LOOP THROUGH TUPLE ()
        for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 21 TEXTS OF THE PROPHETS CHOSEN = ", each[0],len(each[1]))
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 21 TEXTS OF THE PROPHETS CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTuple)
        
    ## ...ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) TEXTS OF THE WRITINGS (K'TUVIM):
    elif len(ListOfDictsOfJSONStringsParsed) == 13:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTuple = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        
        ## LOOP THROUGH TUPLE ()
        for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 13 TEXTS OF THE WRITINGS CHOSEN = ", each[0],len(each[1]))
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 13 TEXTS OF THE WRITINGS CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTuple)
        
    ## ...ELSE IF TEXT CHOSEN IS ONLY ONE (1) TEXT:
    elif len(ListOfDictsOfJSONStringsParsed) == 1:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED  
        ZippedTuple = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        
        ## TEST PRINT OUTPUT
        print("ZIPPED TUPLE IN FUNCTION 6 = ", ZippedTuple)
    
        ## LOOP THROUGH TUPLE
        for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("HERE IS EACH ELEMENT IN ZIPPEDTUPLE = ", each)
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", len(each), type(each))
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", each[0],len(each[1]))
            print("Z = ", each[0],len(each[1]))
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF ONE BOOK CHOSEN = ", each[0],len(each[1]))
            print("Z = ", type(each[0]),type(each[1]))
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
                   
        ## RETURN ZIPPED TUPLE
        return(ZippedTuple)
        
    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        
        pass      
          

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #6 - ZIPPED TUPLE CREATE")

## END FUNCTION () #6 - ZIPPED TUPLE CREATE
## END FUNCTION () #6 - ZIPPED TUPLE CREATE
## END FUNCTION () #6 - ZIPPED TUPLE CREATE