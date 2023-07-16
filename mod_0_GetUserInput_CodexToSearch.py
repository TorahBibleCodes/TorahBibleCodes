## FUNCTION () #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH

def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #1A - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1A - GET USER INPUT; CHOOSE CODEX TO SEARCH")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("Please select Hebrew Bible codex to search:")
    print("\n")  ## PRINT SPACE
    print("1 - Koren - Claremont Michigan Transliteration")
    print("2 - Leningrad Codex")

    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please select codex to search:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfCodexChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen codex number # {NumberOfCodexChosen}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfCodexChosen)

## END FUNCTION () #1A - GET USER INPUT; CHOOSE CODEX TO SEARCH
