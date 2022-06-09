## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES
import resources.func.mod_3BTextFileParse as mod_3BTextFileParse ## MODULE.FUNCTION() #3B - TEXT FILE PARSE

## FUNCTION () #3A - TEXT FILE PREPROCESS
## FUNCTION () #3A - TEXT FILE PREPROCESS
## FUNCTION () #3A - TEXT FILE PREPROCESS
def fn_TextFilePreprocess(JSON):
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #3A TEXT FILE PREPROCESS")

    ## DECLARE VARIABLES
    ListOfJSONStringsParsed = []
    ListOfJSONStringsParsedWithSpaces = []
    
    ## IF JSON IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT
    if isinstance(JSON, str):
        
        ## ...THEN CALL MODULE.FUNCTION() #3B - TEXT FILE PARSE
        JSONParsed = mod_3BTextFileParse.fn_TextFileParse(JSON)
        
        ## TEST PRINT OUTPUT
        ##print("\n")
        ##print("JSONParsed = ", len(JSONParsed), type(JSONParsed))

        ListOfJSONStringsParsed.append(JSONParsed[1]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
        ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
    
    ## ELSE IF JSON IS A TUPLE... ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS
    elif isinstance(JSON, tuple):
        
        ## ...THEN FOR EACH TUPLE IN JSON...
        for each in JSON:
            
            ## ...THEN CALL MODULE.FUNCTION() #3B - TEXT FILE PARSE -  - RETURNS TUPLE??
            JSONParsed = mod_3BTextFileParse.fn_TextFileParse(each)

            ## TEST PRINT OUTPUT
            ##print("\n")
            ##print("JSONParsed = ", len(JSONParsed), type(JSONParsed))
            
            ListOfJSONStringsParsed.append(JSONParsed[1]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpace
            ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
            
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #3A - TEXT FILE PREPROCESS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)
    
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
## END FUNCTION () #3A - END TEXT FILE PREPROCESS
