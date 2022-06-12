## BEGIN FUNCTION () #14 - GET USER INPUT:  SIZE OF 2D MATRIX;

def fn_GetUserInput(ListOfFactors, LengthOfTextToSearch):

    """
    ## MODULE.FUNCTION() #14 - GET USER INPUT:  SIZE OF 2D MATRIX; RETURNS y, x
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #14 - GET USER INPUT: SIZE OF 2D MATRIX;")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"LengthOfTextToSearch = {LengthOfTextToSearch}")
    print(f"List of Factors from the text(s) that you selected: {ListOfFactors}\n")
    print(f"Choose a number from the List of {len(ListOfFactors)} Factors (i.e. # of x columns to output the 2D Matrix)\n")
    print(f"OR Choose any number, and the 2D Matrix will be calculated according to your selection.\n")
    print(f"NOTE: Larger numbers above 800 for X / Width / Rows may exceed the maximum allowed by EXCEL.\n")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input(f"Type the number here: ")

    print(f"TextString = {TextString}")

    ## CONVERT TEXT STRING TO INTEGER
    x = int(TextString)

    ## CALCULATE CUSTOM Y VALUE; TRUNCATED(??) BY MAKING INTEGER
    y = int((LengthOfTextToSearch / x))

    ## TEST
    # y += 1
   
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #14 - GET USER INPUT: SIZE OF 2D MATRIX;")

    ## RETURN VARIABLES TO PROGRAM
    return(y, x)

## END FUNCTION () #14 - GET USER INPUT: SIZE OF 2D MATRIX;