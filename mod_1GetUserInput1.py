## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
def fn_GetUserInput1():

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1 GET USER INPUT; CHOOSE TEXT TO SEARCH")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("Please select text to search:")
    print("1 - Genesis")
    print("2 - Exodus")
    print("3 - Leviticus")
    print("4 - Numbers")
    print("5 - Deuteronomy")
    print("6 - Pentateuch (Entire Torah)")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    TextString = input("Please select text to search:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    TextChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("You have chosen:  ", TextChosen, type(TextChosen))

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(TextChosen)

## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
