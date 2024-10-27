## IMPORT MODULES
import pandas as pd
import tqdm

## BEGIN FUNCTION () # SEARCH FOR ELS SEARCH TERMS - VIA PANDAS SERIES;
## BEGIN FUNCTION () # - fn_SearchForELSSearchTerms(ListOfSearchTerms):; ##
def fn_SearchForELSSearchTerms(ListOfSearchTerms, L, ListOfIndexesCustom):

    """
    ## MODULE.FUNCTION() #41 - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #41 - SEARCH FOR ELS LETTER MATCHES VIA PANDAS SERIES;")
    
    ## TEST DEVELOPMENT
    ## ELSSearchTerm = ListOfSearchTerms[0]

    ## DECLARE VARIABLES
    ListOfListOfSeries4EachLetterInText = []

    ## BEGIN FOR LOOP
    for ELSSearchTerm in tqdm.tqdm(ListOfSearchTerms, total=(len(ListOfSearchTerms)), desc="SEARCH PROGRESS: ", unit="Search-Term"):

        ## DECLARE VARIABLES
        Sub_ListOfLetterPositions = []
        Main_ListOfLetterPositions = []

        ## CREATE PD SERIES FOR THE SELECTED TEXT STRING / LIST OF LETTERS WITH CUSTOM 1-INDEX
        s = pd.Series(L, index=ListOfIndexesCustom)
        
        ## BEGIN FOR LOOP
        for EachLetter in ELSSearchTerm:
            Sub_ListOfLetterPositions = s.str.startswith(EachLetter)
            Main_ListOfLetterPositions.append(Sub_ListOfLetterPositions)

        ## END FOR LOOP

        ## TEST DEVELOPMENT
        ## print(Main_ListOfLetterPositions)
        ## print(f"Main_ListOfLetterPositions = {Main_ListOfLetterPositions}, {type(Main_ListOfLetterPositions)}") ## LIST OF PD SERIES
        ## print(f"Main_ListOfLetterPositions[0] =  {Main_ListOfLetterPositions[0]}, type(Main_ListOfLetterPositions[0])") ## PD SERIES

        ## ListOfListOfSeries4EachLetterInText[0] == LIST OF PD SERIES FOR ONE ELS SEARCH TERM
        ## ListOfListOfSeries4EachLetterInText[0][0] == PD SERIES FOR EACH LETTER IN ONE ELS SEARCH TERM

        ## APPEND
        ListOfListOfSeries4EachLetterInText.append(Main_ListOfLetterPositions)

    ## END FOR LOOP    
   
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #41 - SEARCH FOR ELS LETTER MATCHES VIA PANDAS SERIES;")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfListOfSeries4EachLetterInText)

## END FUNCTION () # SEARCH FOR ELS SEARCH TERMS - VIA PANDAS SERIES;