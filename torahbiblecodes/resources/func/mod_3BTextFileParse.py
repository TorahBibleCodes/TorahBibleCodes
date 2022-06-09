## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES
import re

## FUNCTION () #3B - TEXT FILE PARSE
## FUNCTION () #3B - TEXT FILE PARSE
## FUNCTION () #3B - TEXT FILE PARSE
def fn_TextFileParse(JSONString):

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #3B TEXT FILE PARSE")
         
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ##print(JSONString)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of JSONString =", len(JSONString), type(JSONString))
    
    ## BEGIN TEXT FILE PARSE
    ## BEGIN TEXT FILE PARSE
    ## BEGIN TEXT FILE PARSE

    ## REMOVE HYPHENS FROM STRING
    ## REMOVE HYPHENS FROM STRING
    ## REMOVE HYPHENS FROM STRING
    

    TextNoHyphensWithSpaces = JSONString.replace("־", " ")





    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextNoHyphensWithSpaces =", len(TextNoHyphensWithSpaces), type(TextNoHyphensWithSpaces))

    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING
    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING
    ## REMOVE BRACKETS AND CONTENTS WIHIN BRACKETS FROM STRING

    TextNoBracketsWithSpaces = re.sub("[\[].*?[\]]", "", TextNoHyphensWithSpaces)





    
    
    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextNoBracketsWithSpaces =", len(TextNoBracketsWithSpaces), type(TextNoBracketsWithSpaces))

    ## REMOVE WHITE SPACES FROM STRING
    ## REMOVE WHITE SPACES FROM STRING
    ## REMOVE WHITE SPACES FROM STRING
    

    TextNoSpaces = TextNoBracketsWithSpaces.replace(" ", "")



    
    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextNoSpaces =", len(TextNoSpaces), type(TextNoSpaces))
    
    ## CHANGE VARIABLE NAME
    ## CHANGE VARIABLE NAME
    ## CHANGE VARIABLE NAME
    TextParsedWithSpaces = TextNoBracketsWithSpaces
    TextParsedNoSpaces = TextNoSpaces







    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextParsedWithSpaces =", len(TextParsedWithSpaces), type(TextParsedWithSpaces))
    
    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextParsedNoSpaces =", len(TextParsedNoSpaces), type(TextParsedNoSpaces))


    
    
    ## END TEXT FILE PARSE
    ## END TEXT FILE PARSE
    ## END TEXT FILE PARSE
    
    ## CHANGE VARIABLE NAMES
    ## CHANGE VARIABLE NAMES
    ## CHANGE VARIABLE NAMES
    
    TextParsedWithSpaces = TextNoBracketsWithSpaces
    TextParsedNoSpaces = TextNoSpaces
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #3B - TEXT FILE PARSE")

    ## RETURN VARIABLES TO PROGRAM - RETURNS TUPLE OF TWO TEXTS (LISTS):  1.) WITH SPACES; 2.) WITH NO SPACES
    return(TextParsedWithSpaces, TextParsedNoSpaces)

## END FUNCTION () #3B - TEXT FILE PARSE
## END FUNCTION () #3B - TEXT FILE PARSE
## END FUNCTION () #3B - TEXT FILE PARSE
