## IMPORT CLASSES


## BEGIN FUNCTION () #17 - GET USER INPUT - ELS SEARCH TERMS;

def fn_GetUserInput(NumberOfSearchTerms):

    """
    ## MODULE.FUNCTION() #17 - GET USER INPUT: INPUT DESIRED SEARCH TERMS ListOfSearchTerms, DictOfSearchTerms
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #17 - GET USER INPUT - ELS SEARCH TERMS;")

    ## DECLARE VARIABLES
    ListOfSearchTerms = [] ## EMPTY LIST
    DictOfSearchTerms = {} ## EMPTY DICT TO HOLD SEARCH TERMS
    k = 1 ## INITIALIZE K KEY K/COUNTER

    ## TEST DEVELOPMENT
    #k = 0
    #while k < 10:
    #    # dynamically create key
    #    key = ...
    #    # calculate value
    #    value = ...
    #    DictOfSearchTerms[key] = value 
    #    k += 1

    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"Number of Search Terms: {NumberOfSearchTerms}")
    print(f"Please enter each term for the {NumberOfSearchTerms} terms that you specified\n")
    
    ## BEGIN FOR LOOP
    ## FOR EACH IN NUMBER OF SEARCH TERMS INPUTTED BY USER
    for each in range(1, (NumberOfSearchTerms + 1)):

        ## TEXT CHOSEN = USER INPUT (TEXT STRING)
        print("\n")  ## PRINT SPACE
        TextString = input(f"ELS Search Term {each}: ")

        ## TEST PRINT OUTPUT
        print("\n")  ## PRINT SPACE
        print(f"ELS Search Term TextString = {TextString}")

        ## APPEND ELS SEARCH TERM TEXT TO LIST OF SEARCH TERMS
        ListOfSearchTerms.append(TextString)

        ## ADD ELS SEARCH TERM TO DICT OF SEARCH TERMS
        DictOfSearchTerms[k] = TextString

        ## INCREMENT THE K KEY K/COUNTER
        k += 1
          
        ## TEST DEVELOPMENT
        #k = 1
        #while k < NumberOfSearchTerms:
        #        #    # dynamically create key
        #    key = k
        #        #    # calculate value
        #    value = TextString

        #    DictOfSearchTerms[key] = value 
        #    k += 1

    ## END FOR LOOP
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("You have entered the following terms:  ", ListOfSearchTerms, type(ListOfSearchTerms))
    print(DictOfSearchTerms)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #17 - GET USER INPUT - ELS SEARCH TERMS;")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfSearchTerms, DictOfSearchTerms)

## END FUNCTION () #17 - GET USER INPUT - ELS SEARCH TERMS;