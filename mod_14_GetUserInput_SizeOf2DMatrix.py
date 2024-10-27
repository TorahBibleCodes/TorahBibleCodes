## IMPORT MODULES

## BEGIN FUNCTION() #14 - GET USER INPUT:  SIZE OF 2D MATRIX; ##
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
    print("\n")  ## PRINT SPACE
    print(f"List of {len(ListOfFactors)} Factors from the text(s) that you selected: {ListOfFactors}\n")
    print(f"Choose a size for the 2D matrix from a number from the List of {len(ListOfFactors)} Factors (i.e. # of x columns to output for the 2D Matrix)\n")
    print(f"OR Choose ANY number, and the 2D Matrix will be calculated according to your selection.\n")
    print(f"NOTE: Larger numbers above 800 for X / Width / Columns may (or may not) exceed the maximum allowed by Microsoft Office (Excel), LibreOffice, Apache Open Office, etc.\n")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input(f"Type the number here: ")

    print(f"Size of 2D Matrix : {TextString} columns")

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

## END FUNCTION() #14 - GET USER INPUT: SIZE OF 2D MATRIX;