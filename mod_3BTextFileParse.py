## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES
import re

## FUNCTION () #3B - TEXT FILE PARSE
## FUNCTION () #3B - TEXT FILE PARSE
## FUNCTION () #3B - TEXT FILE PARSE
def fn_TextFileParse(JSONString):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #3B TEXT FILE PARSE")
         
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(JSONString)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of JSONString =", len(JSONString), type(JSONString))
    
    ## BEGIN TEXT FILE PARSE
    ## BEGIN TEXT FILE PARSE
    ## BEGIN TEXT FILE PARSE
    
    ## REMOVE WHITE SPACES FROM STRING
    ## REMOVE WHITE SPACES FROM STRING
    ## REMOVE WHITE SPACES FROM STRING
    TextNoSpaces = JSONString.replace(" ", "")
    
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(TextNoSpaces)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of TextNoSpaces =", len(TextNoSpaces), type(TextNoSpaces))
    
    
    ## REMOVE HYPHENS FROM STRING
    ## REMOVE HYPHENS FROM STRING
    ## REMOVE HYPHENS FROM STRING
    TextNoHyphens = TextNoSpaces.replace("־", "")

    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(TextNoHyphens)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of TextNoHyphens =", len(TextNoHyphens), type(TextNoHyphens))
    

    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING
    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING
    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING
    #TextNoBrackets = re.sub("[\(\[].*?[\)\]]", "", TextNoHyphens)
    TextNoBrackets = re.sub("[\[].*?[\]]", "", TextNoHyphens)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(TextNoBrackets)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of TextNoBrackets =", len(TextNoBrackets), type(TextNoBrackets))
    
    ## END TEXT FILE PARSE
    ## END TEXT FILE PARSE
    ## END TEXT FILE PARSE
    
    ## CHANGE VARIABLE NAME
    ## CHANGE VARIABLE NAME
    ## CHANGE VARIABLE NAME
    TextParsed = TextNoBrackets
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of TextParsed =", len(TextParsed), type(TextParsed))
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #3B - TEXT FILE PARSE")

    ## RETURN VARIABLES TO PROGRAM
    return(TextParsed)

## END FUNCTION () #3B - TEXT FILE PARSE
## END FUNCTION () #3B - TEXT FILE PARSE
## END FUNCTION () #3B - TEXT FILE PARSE