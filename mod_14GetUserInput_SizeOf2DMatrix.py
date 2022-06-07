## BEGIN FUNCTION () #14 - GET USER INPUT - SIZE OF 2D MATRIX;

def fn_GetUserInput(ListOfFactors, LengthOfTextToSearch):

    print(f"LengthOfTextToSearch = {LengthOfTextToSearch}")
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #14 - GET USER INPUT - SIZE OF 2D MATRIX;")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"List of Factors from the text(s) that you selected: {ListOfFactors}\n")
    print(f"Choose a number from the List of {len(ListOfFactors)} Factors (i.e. # of x columns to output the 2D Matrix)\n")
    print(f"OR Choose any number and we'll soon see if it works.\n")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input(f"Type the number here: ")

    print(f"TextString = {TextString}")

    ## CONVERT TEXT STRING TO INTEGER
    x = int(TextString)

    y = int((LengthOfTextToSearch / x))

    ## TEST
    # y += 1
   
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #14 - GET USER INPUT - SIZE OF 2D MATRIX;")

    ## RETURN VARIABLES TO PROGRAM
    return(y, x)

## END FUNCTION () #14 - GET USER INPUT - SIZE OF 2D MATRIX;