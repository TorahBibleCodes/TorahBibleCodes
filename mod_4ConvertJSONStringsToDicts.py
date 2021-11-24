## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import json

## FUNCTION () #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES
## FUNCTION () #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES
## FUNCTION () #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES
def fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces):
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #4 CONVERT PARSED JSON STRINGS TO DICTIONARIES")
    
    ## DECLARE VARIABLES      
    ListOfDictsOfJSONStringsParsed = []
    ListOfDictsOfJSONStringsParsedWithSpaces = []
       
    ## FOR NO SPACES
    ## FOR EACH PARSED JSON STRING, CONVERT JSON STRING TO DICTIONARY
    for each in ListOfJSONStringsParsed:
        
        ## CONVERT JSON TO PYTHON DICTIONARY
        DictOfConvertedJSON = json.loads(each)
        
        ## APPEND EACH DICTIONARY TO LIST
        ListOfDictsOfJSONStringsParsed.append(DictOfConvertedJSON)


    ## FOR WITH SPACES
    ## FOR EACH PARSED JSON STRING, CONVERT JSON STRING TO DICTIONARY
    for each in ListOfJSONStringsParsedWithSpaces:
        
        ## CONVERT JSON TO PYTHON DICTIONARY
        DictOfConvertedJSON = json.loads(each)
        
        ## APPEND EACH DICTIONARY TO LIST
        ListOfDictsOfJSONStringsParsedWithSpaces.append(DictOfConvertedJSON)
        
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES")    
    
    ## RETURN VARIABLES TO PROGRAM
    return(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces)
    
## END FUNCTION () #4 - END CONVERT PARSED JSON STRINGS TO DICTIONARIES
## END FUNCTION () #4 - END CONVERT PARSED JSON STRINGS TO DICTIONARIES
## END FUNCTION () #4 - END CONVERT PARSED JSON STRINGS TO DICTIONARIES
