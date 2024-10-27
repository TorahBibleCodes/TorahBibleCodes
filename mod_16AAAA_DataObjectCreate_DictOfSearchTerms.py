## IMPORT CLASSES

## BEGIN FUNCTION () #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms ##

def fn_DataObjectsCreate(ListOfSearchTerms, ListOfSearchTermsWithSpaces,  NumberOfSearchTerms):

    """
    ## MODULE.FUNCTION() #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms;")

    ## DECLARE VARIABLES
    DictOfSearchTermsWithSpaces = {} ## EMPTY DICT TO HOLD SEARCH TERMS
    DictOfSearchTerms = {} ## EMPTY DICT TO HOLD SEARCH TERMS
    k = 1 ## INITIALIZE K KEY K/COUNTER

    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"Number of Search Terms: {NumberOfSearchTerms}")
    
    ## BEGIN FOR LOOP - NO SPACES
    ## FOR EACH IN NUMBER OF SEARCH TERMS INPUTTED BY USER
    ## for each in range(1, (NumberOfSearchTerms + 1)):
    for each in ListOfSearchTerms:

        ## ADD ELS SEARCH TERM TO DICT OF SEARCH TERMS
        DictOfSearchTerms[k] = each

        ## INCREMENT THE K KEY K/COUNTER
        k += 1

    ## END FOR LOOP
        
    ## RESET K
    k = 1
    
    ## BEGIN FOR LOOP - WITH SPACES
    ## FOR EACH IN NUMBER OF SEARCH TERMS INPUTTED BY USER
    ## for each in range(1, (NumberOfSearchTerms + 1)):
    for each in ListOfSearchTermsWithSpaces:

        ## ADD ELS SEARCH TERM TO DICT OF SEARCH TERMS
        DictOfSearchTermsWithSpaces[k] = each

        ## INCREMENT THE K KEY K/COUNTER
        k += 1
        
    ## END FOR LOOP
    
    ## TEST PRINT OUTPUT - NO SPACES
    print("\n")  ## PRINT SPACE
    ## print("You have inputted the following ELS Search Terms (NO SPACES):  ", ListOfSearchTerms, type(ListOfSearchTerms))
    print("You have inputted the following ELS Search Terms (NO SPACES - IF ANY):  ")
    print(DictOfSearchTerms)

    ## TEST PRINT OUTPUT - WITH SPACES
    print("\n")  ## PRINT SPACE
    ## print("You have inputted the following ELS Search Terms (WITH SPACES):  ", ListOfSearchTermsWithSpaces, type(ListOfSearchTermsWithSpaces))
    print("You have inputted the following ELS Search Terms (WITH SPACES - IF ANY):  ")
    print(DictOfSearchTermsWithSpaces)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms;")

    ## RETURN VARIABLES TO PROGRAM
    return(DictOfSearchTerms, DictOfSearchTermsWithSpaces)

## END FUNCTION () #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms;