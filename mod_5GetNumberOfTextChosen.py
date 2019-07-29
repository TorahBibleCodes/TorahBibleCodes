## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
def fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #5 - GET NUMBER OF TEXT CHOSEN")
    
    ## DECLARE VARIABLES
    TextChosen = []
    
    ## IF TEXT CHOSEN IS ALL FIVE (5) TEXTS...
    if len(ListOfDictsOfJSONStringsParsed) == 5:
        
        ## DECLARE VARIABLES
        LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 1)
        
        ## CREATE LIST OF BOOK NUMBERS SELECTED
        BookNumbers = list((range(1, LengthForRange, 1)))
        
        ## LOOP THROUGH LIST
        for each in BookNumbers:
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(each)
    
    ## ...ELSE IF TEXT CHOSEN IS ONLY 1 (ONE) TEXT:
    elif len(ListOfDictsOfJSONStringsParsed) == 1:
    
        ## LOOP THROUGH LIST
        for each in ListOfDictsOfJSONStringsParsed:
             
            ## GET TEXT TITLE
            TextTitle = each["title"]
         
            if TextTitle == "Genesis":
                BookNumber = 1
         
            elif TextTitle == "Exodus":
                BookNumber = 2
         
            elif TextTitle == "Leviticus":
                BookNumber = 3
         
            elif TextTitle == "Numbers":
                BookNumber = 4
         
            elif TextTitle == "Deuteronomy":
                BookNumber = 5
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(BookNumber)
    
    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        pass
      
    ## CONVERT LIST TO TUPLE
    TextChosen = tuple(TextChosen)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #5 - GET NUMBER OF TEXT CHOSEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextChosen)

## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
