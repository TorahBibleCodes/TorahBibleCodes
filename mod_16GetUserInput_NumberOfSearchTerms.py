## BEGIN FUNCTION () #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;

def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS ## RETURNS NumberOfSearchTerms
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;")
    
    ## GET USER INPUT ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("How many total number of ELS Search-Terms would you like to search for within the selected text?:\n")

    ## CONVERT TEXT STRING TO INTEGER
    NumberOfSearchTerms = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen to search for {NumberOfSearchTerms} ELS Search Terms")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfSearchTerms)

## END FUNCTION () #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;