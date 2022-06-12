## BEGIN FUNCTION () #13 - 

def fn_GetListOfFactors(LengthOfTextToSearch):

    """
    ## MODULE.FUNCTION() #13 - ## RETURNS LIST OF INTEGERS/FACTORS/DIVISORS OF THE LENGTH OF THE SELECTED TEXT
    """
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #13 - GET LIST OF FACTORS")
          
    ## DECLARE VARIABLES
    ListOfFactors = [] ## EMPTY LIST

    ## BEGIN FOR LOOP
    for each in range(1, LengthOfTextToSearch + 1):
            
        ## IF THE LENGTH OF THE TEXT TO SEARCH IS EVENLY DIVISIBLE BY A NUMBER,
        if LengthOfTextToSearch % each == 0:

            ## THEN THAT NUMBER IS A FACTOR OF THE LENGTH OF THE TEXT TO SEARCH
            ListOfFactors.append(each) ## APPEND POSITIVE FACTOR
            
        ## OTHERWISE DO NOTHING TO THAT NUMBER
        else:
            pass

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    print(f"ListOfFactors = {ListOfFactors}", len(ListOfFactors))

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #13 - GET LIST OF FACTORS")
    
    ## RETURN LIST OF FACTORS
    return(ListOfFactors)

## END FUNCTION () #13 - 