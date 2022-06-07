## BEGIN FUNCTION () #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;

def fn_GetUserInput():

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("How many total number of ELS Search-Terms to search?")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("How many total number of ELS Search-Terms within the selected text?:\n")

    ## CONVERT TEXT STRING TO INTEGER
    NumberOfTextChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen to search for {NumberOfTextChosen} ELS Search Terms")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfTextChosen)

## END FUNCTION () #16 - GET USER INPUT - NUMBER OF SEARCH TERMS;