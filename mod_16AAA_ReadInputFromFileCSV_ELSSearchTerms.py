## IMPORT MODULES
import csv

## DECLARE VARIABLES

## DEFINE FUNCTIONS ##
def fn_ReadInputFromFile(FileNameForCSVImport):

    """
    ## MODULE.FUNCTION() #16AAA - 
    """

    ## DEFINE VARIABLES
    ListOfSearchTermsWithSpaces = [] ## LIST OF ROWS
    ListOfSearchTerms = [] ## LIST OF ROWS

    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open(FileNameForCSVImport,'r', encoding="utf-8", newline='') as f:

        ## CREATE CSV READER OBJECT
        f_csv_reader = csv.reader(f, delimiter=';')

        ## BEGIN FOR LOOP - ITERATE THROUGH CSV READER OBJECT
        for row in f_csv_reader:

            ## EXTRACT
            ELSSearchTermTextWithSpaces = row[0]

            ## APPEND
            ListOfSearchTermsWithSpaces.append(ELSSearchTermTextWithSpaces)

            ## DEAL WITH SPACES IN ELS SEARCH TERMS - ## REMOVE SPACES FROM STRING
            ELSSearchTermText = ELSSearchTermTextWithSpaces.replace(" ", "")

            ## APPEND
            ListOfSearchTerms.append(ELSSearchTermText)
        
        ## END FOR LOOP - ITERATE THROUGH CSV READER OBJECT
            
        ## COUNT NUMBER OF SEARCH TERMS
        NumberOfSearchTerms = len(ListOfSearchTerms)

        ## RETURN VARIABLES
        return(ListOfSearchTerms, ListOfSearchTermsWithSpaces, NumberOfSearchTerms)


   
