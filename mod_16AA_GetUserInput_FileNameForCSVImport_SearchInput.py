## BEGIN FUNCTION () #16AA - GET USER INPUT: CSV FILE NAME FOR SEARCH INPUT ## RETURNS ##
def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #16AA - GET USER INPUT: CSV FILE NAME FOR SEARCH INPUT ## RETURNS 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #16AA - GET USER INPUT: CSV FILE NAME FOR SEARCH INPUT ## RETURNS ;")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please input the CSV File Name (in the root directory where you are running this Torah Bible Codes search program) that contains your ELS Search Terms (e.g. FileName4ELSs.csv):  ")
    
    ## ASSIGN TEXT STRING VALUE TO FILE NAME
    FileNameForCSVImport = TextString
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"The CSV File to be opened is {FileNameForCSVImport}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #16AA - GET USER INPUT: CSV FILE NAME FOR SEARCH INPUT ## RETURNS ;")

    ## RETURN VARIABLES TO PROGRAM
    return(FileNameForCSVImport)

## END FUNCTION () #16AA - GET USER INPUT: FILE NAME SEARCH INPUT ## RETURNS