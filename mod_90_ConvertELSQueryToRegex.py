## BEGIN FUNCTION () #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO NUMBER VALUES

def fn_ConvertELSQueryToRegex(ListOfSearchTerms):

    """
    ## MODULE.FUNCTION() #90 - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION () #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO NUMBER VALUES")
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TEST: {ListOfSearchTerms}")

    ## DECLARE VARIABLES
    ListOfNumberValues4ELSSearchTerms = [] ## EMPTY LIST TO HOLD [EACH ELS SEARCH TERM AS INDIVIDUAL LETTERS]

    ## BEGIN FOR LOOP - FOR EACH WORD IN LIST OF SEARCH TERMS
    for EachWord in ListOfSearchTerms:

        ## DECLARE VARIABLES
        ListOfRegexStrings = [] ## DECLARE EMPTY LIST FOR REGEX STRINGS

        ## BEGIN FOR LOOP - FOR EACH LETTER IN ELS SEARCH TERM
        for EachLetter in EachWord:

            ## CREATE UNIQUE REGEX TEXT STRING FOR EACH LETTER
            TemporaryVariable = r"[" + EachLetter + r"]"
        
            ## TEST PRINT OUTPUT
            ## print("\n")  ## PRINT SPACE
            ## print(TemporaryVariable, type(TemporaryVariable))
     
            ## APPEND TEMP VARIABLE [I.E. LETTER] TO LIST OF REGEX LETTER-STRINGS 
            ListOfRegexStrings.append(TemporaryVariable)

        ## END FOR LOOP - FOR EACH LETTER IN ELS SEARCH TERM

        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(ListOfRegexStrings)

        ## APPEND LIST OF REGEX LETTER-STRING [I.E. ELS SEARCH TERM AS INDIVIDUAL LETTERS] TO LIST OF LISTS
        ListOfNumberValues4ELSSearchTerms.append(ListOfRegexStrings)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"ListOfNumberValues4ELSSearchTerms = {ListOfNumberValues4ELSSearchTerms}")

    ## END FOR LOOP - FOR EACH WORD IN LIST OF SEARCH TERMS
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION () #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO NUMBER VALUES")
    
    ## RETURN VARIABLES
    ## return(ListOfRegexStrings)
    return(ListOfNumberValues4ELSSearchTerms) ## RETURNS LIST OF LISTS OF LETTERS

## END FUNCTION () #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)

