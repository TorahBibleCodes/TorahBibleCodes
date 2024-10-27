## FUNCTION () #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH ###

def fn_GetUserInput(NumberOfCodexChosen):

    """
    ## MODULE.FUNCTION() #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER ##
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    match NumberOfCodexChosen:

        case 1: 
            NameOfCodex = "Koren Codex"
        case 2:
            NameOfCodex = "Leningrad Codex"
        case 3:
            NameOfCodex = "Miqra According to the Masorah (MAM) Collection of Manuscripts"
            
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"Please select text to search in the {NameOfCodex}:")
    print("\n")  ## PRINT SPACE
    print("1 - Genesis - 78064 letters")
    print("2 - Exodus - 63529 letters")
    print("3 - Leviticus - 44790 letters")
    print("4 - Numbers - 63530 letters")
    print("5 - Deuteronomy - 54892 letters")
    print("40 - Pentateuch (Torah) - 304805 letters")

    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please select text to search:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfTextChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen text number # {NumberOfTextChosen}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfTextChosen)

## END FUNCTION () #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH
