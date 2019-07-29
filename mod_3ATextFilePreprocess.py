## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES
import mod_3BTextFileParse ## MODULE.FUNCTION() #3B - TEXT FILE PARSE

## FUNCTION () #3A - TEXT FILE PREPROCESS
## FUNCTION () #3A - TEXT FILE PREPROCESS
## FUNCTION () #3A - TEXT FILE PREPROCESS
def fn_TextFilePreprocess(JSON):
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3A TEXT FILE PREPROCESS")

    ## DECLARE VARIABLES
    ListOfJSONStringsParsed = []
    
    ## IF JSON IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT
    if isinstance(JSON, str):
        
        ## ...THEN CALL MODULE.FUNCTION() #3B - TEXT FILE PARSE
        JSONParsed = mod_3BTextFileParse.fn_TextFileParse(JSON)
        ListOfJSONStringsParsed.append(JSONParsed)
    
    ## ELSE IF JSON IS A TUPLE... ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS
    elif isinstance(JSON, tuple):
        
        ## ...THEN FOR EACH TUPLE IN JSON...
        for each in JSON:
            
            ## ...THEN CALL MODULE.FUNCTION() #3B - TEXT FILE PARSE
            JSONParsed = mod_3BTextFileParse.fn_TextFileParse(each)
            ListOfJSONStringsParsed.append(JSONParsed)
            
            
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3A - TEXT FILE PREPROCESS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfJSONStringsParsed)
    
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
