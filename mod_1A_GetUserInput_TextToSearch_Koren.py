## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH

def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #1B - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1B - GET USER INPUT; CHOOSE TEXT TO SEARCH")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("Please select text to search:")
    print("\n")  ## PRINT SPACE
    print("1 - Genesis")
    print("2 - Exodus")
    print("3 - Leviticus")
    print("4 - Numbers")
    print("5 - Deuteronomy")
    print("40 - Pentateuch (Torah)")

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
    print("WITHIN FUNCTION:  END FUNCTION #1B - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfTextChosen)

## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
