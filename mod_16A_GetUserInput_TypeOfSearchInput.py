## BEGIN FUNCTION () #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS NumberOfInputType ##
def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS TypeOfSearchInput
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS TypeOfSearchInput;")
    
    ## GET USER INPUT - TYPE OF INPUT
    print("\n")  ## PRINT SPACE
    print("Please select the type of input for ELS Search Terms:")
    print("\n")  ## PRINT SPACE
    print("1 - Manual Input of ELS Search Term(s) via keyboard (i.e. type OR copy/paste Hebrew one-by-one)")
    print("2 - Import Multiple ELS Search Term(s) from CSV file (i.e. list of one OR more Hebrew search terms in CSV file)")
  
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please select type of input:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfInputType = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen input type number # {NumberOfInputType}.")
    ## GET USER INPUT ## TYPE OF SEARCH INPUT = USER INPUT (TEXT STRING)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS TypeOfSearchInput;")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfInputType)

## END FUNCTION () #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS NumberOfInputType