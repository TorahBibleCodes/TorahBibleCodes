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
    
    ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS...
    if len(ListOfDictsOfJSONStringsParsed) == 5:
        
        ## CREATE ZIPPED TUPLE OF SEARCH TEXT CHOSEN // DICT OF JSON STRING PARSED 
        ZippedTuple = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
        
        ## LOOP THROUGH TUPLE ()
        for each in ZippedTuple:
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 5 TEXTS CHOSEN = ", each[0],len(each[1]))
            print("EACH IN ZIPPED TUPLE IN FUNCTION 6 ONLY IF All 5 TEXTS CHOSEN = ", type(each[0]),type(each[1]))
      
        ## RETURN ZIPPED TUPLE
        return(ZippedTuple)
        
    ## ...ELSE IF TEXT CHOSEN IS ONLY 1 (ONE) TEXT:
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
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 = ", len(each), type(each))
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 = ", each[0],len(each[1]))
            print("Z = ", each[0],len(each[1]))
            
            ## TEST PRINT OUTPUT
            print("\n")  ## PRINT SPACE
            print("EACH ELEMENT IN ZIPPED TUPLE IN FUNCTION 6 = ", each[0],len(each[1]))
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
