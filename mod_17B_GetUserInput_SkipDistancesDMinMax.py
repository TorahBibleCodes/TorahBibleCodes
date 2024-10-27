## BEGIN FUNCTION () #17B - GET USER INPUT - SKIP DISTANCES D MINIMUM / MAXIMUM; ##
def fn_GetUserInput(NumberOfSearchTerms):

    """
    ## MODULE.FUNCTION() #17B - GET USER INPUT - SKIP DISTANCES D MINIMUM / MAXIMUM; ## RETURNS 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #17B - GET USER INPUT - SKIP DISTANCES D MINIMUM / MAXIMUM;")
    
    ## GET USER INPUT ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString1 = input("What is the lowest/smallest (NEGATIVE or POSITIVE) skip distance (d) you would like to use for this ELS search? (e.g. -100, -50, -10, -1, 1, 10, 50, 100):\n")
    print("\n")  ## PRINT SPACE
    TextString2 = input("What is the highest/largest (NEGATIVE or POSITIVE) skip distance (d) you would like to use for this ELS search? (e.g. -100, -50, -10, -1, 1, 10, 50, 100):\n")

    ## CONVERT TEXT STRING TO INTEGER
    SkipDistanceDMinimum = int(TextString1)
    SkipDistanceDMaximum = int(TextString2)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen to search for {NumberOfSearchTerms} ELS Search Term(s) with a skip distance(s) (d) from {SkipDistanceDMinimum} to {SkipDistanceDMaximum}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #17B - GET USER INPUT - SKIP DISTANCES D MINIMUM / MAXIMUM;")

    ## RETURN VARIABLES TO PROGRAM
    return(SkipDistanceDMinimum, SkipDistanceDMaximum)

## END FUNCTION () #17B - GET USER INPUT - SKIP DISTANCES D MINIMUM / MAXIMUM;