## IMPORT MODULES
import mod_3BB_TextFileParse_Leningrad ## MODULE.FUNCTION() #3BB - TEXT FILE PARSE

## FUNCTION () #3B - TEXT FILE PREPROCESS
def fn_TextFilePreprocess(JSON):
    
    """
    ## MODULE.FUNCTION() #3B - TEXT FILE PREPROCESS; ## RETURNS ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces;
    ## CALLS MODULE.FUNCTION() #3BB - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3B - TEXT FILE PREPROCESS")

    ## DECLARE VARIABLES
    ListOfJSONStringsParsed = []
    ListOfJSONStringsParsedWithSpaces = []
    
    ## IF JSON IS A STRING... ## IF TEXT CHOSEN IS ONE (1) TEXT
    if isinstance(JSON, str):
        
        ## ...THEN CALL MODULE.FUNCTION() #3BB - TEXT FILE PARSE
        JSONParsed = mod_3BB_TextFileParse_Leningrad.fn_TextFileParse(JSON)
        
        ## TEST PRINT OUTPUT
        ##print("\n")
        ##print("JSONParsed = ", len(JSONParsed), type(JSONParsed))

        ListOfJSONStringsParsed.append(JSONParsed[1]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
        ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
    
    ## ELSE IF JSON IS A TUPLE... ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS
    elif isinstance(JSON, tuple):
        
        ## ...THEN FOR EACH TUPLE IN JSON...
        for each in JSON:
            
            ## ...THEN CALL MODULE.FUNCTION() #3BB - TEXT FILE PARSE -  - RETURNS TUPLE??
            JSONParsed = mod_3BB_TextFileParse_Leningrad.fn_TextFileParse(each)

            ## TEST PRINT OUTPUT
            ## print("\n")
            ## print("JSONParsed = ", len(JSONParsed), type(JSONParsed))
            
            ListOfJSONStringsParsed.append(JSONParsed[1]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpace
            ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) ## JSONParsed[0] = TextWithSpaces ## JSONParsed[1] = TextNoSpaces
            

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3B - TEXT FILE PREPROCESS")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)
    
## END FUNCTION () #3B - END TEXT FILE PREPROCESS ##

