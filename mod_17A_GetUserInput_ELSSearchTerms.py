## IMPORT CLASSES

## BEGIN FUNCTION () #17A - GET USER INPUT - ELS SEARCH TERMS; ##
def fn_GetUserInput(NumberOfSearchTerms):

    """
    ## MODULE.FUNCTION() #17A - GET USER INPUT: INPUT DESIRED SEARCH TERMS ListOfSearchTerms, DictOfSearchTerms
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #17A - GET USER INPUT - ELS SEARCH TERMS;")

    ## DECLARE VARIABLES
    ListOfSearchTermsWithSpaces = [] ## EMPTY LIST
    DictOfSearchTermsWithSpaces = {} ## EMPTY DICT TO HOLD SEARCH TERMS
    ListOfSearchTerms = [] ## EMPTY LIST
    DictOfSearchTerms = {} ## EMPTY DICT TO HOLD SEARCH TERMS
    k = 1 ## INITIALIZE K KEY K/COUNTER

    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"Number of ELS Search Terms: {NumberOfSearchTerms}")
    print(f"Please input each ELS Search Term (in Hebrew) for the {NumberOfSearchTerms} terms that you specified\n")
    
    ## BEGIN FOR LOOP
    ## FOR EACH IN NUMBER OF SEARCH TERMS INPUTTED BY USER
    for each in range(1, (NumberOfSearchTerms + 1)):

        ## TEXT CHOSEN = USER INPUT (TEXT STRING)
        print("\n")  ## PRINT SPACE
        TextString = input(f"ELS Search Term {each} (type OR copy/paste Hebrew): ")

        ## TEST PRINT OUTPUT
        print("\n")  ## PRINT SPACE
        print(f"ELS Search Term (type OR copy/paste Hebrew): {TextString}")
        print(f"ELS Search Term (R-T-L): {TextString[::-1]}")

        ## ASSIGN VALUE OF TEXT STRING TO VARIABLE
        ELSSearchTermTextWithSpaces = TextString

        ## APPEND ELS SEARCH TERM TEXT TO LIST OF SEARCH TERMS WITH SPACES
        ListOfSearchTermsWithSpaces.append(ELSSearchTermTextWithSpaces)

        ## ADD ELS SEARCH TERM TO DICT OF SEARCH TERMS WITH SPACES
        DictOfSearchTermsWithSpaces[k] = ELSSearchTermTextWithSpaces

        ## DEAL WITH SPACES IN ELS SEARCH TERM - ## REMOVE SPACES FROM STRING
        ELSSearchTermText = ELSSearchTermTextWithSpaces.replace(" ", "")

        ## APPEND ELS SEARCH TERM TEXT TO LIST OF SEARCH TERMS
        ListOfSearchTerms.append(ELSSearchTermText)

        ## ADD ELS SEARCH TERM TO DICT OF SEARCH TERMS
        DictOfSearchTerms[k] = ELSSearchTermText

        ## INCREMENT THE K KEY K/COUNTER
        k += 1

    ## END FOR LOOP
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("You have entered the following ELS search terms (NO SPACES - IF ANY):  ", ListOfSearchTerms, type(ListOfSearchTerms))
    print(DictOfSearchTerms)

    print("\n")  ## PRINT SPACE
    print("You have entered the following ELS search terms (WITH SPACES - IF ANY):  ", ListOfSearchTermsWithSpaces, type(ListOfSearchTermsWithSpaces))
    print(DictOfSearchTermsWithSpaces)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #17A - GET USER INPUT - ELS SEARCH TERMS;")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfSearchTerms, ListOfSearchTermsWithSpaces, DictOfSearchTerms, DictOfSearchTermsWithSpaces)

## END FUNCTION () #17A - GET USER INPUT - ELS SEARCH TERMS;