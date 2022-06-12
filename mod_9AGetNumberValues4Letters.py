## IMPORT MODULES

## FUNCTION () #9A - GET NUMBER VALUES FOR LETTERS
def fn_GetNumberValues(SequenceOfLetters): 

    """
    ## MODULE.FUNCTION() #9A - GET NUMBER VALUE OF EACH LETTER IN LETTER STRING; ## RETURNS ListOfNumberValues4Letters
    """
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("WITHIN FUNCTION:  BEGIN FUNCTION #9A - GET NUMBER VALUES FOR LETTERS") ## COMPUTATION INTENSIVE
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(SequenceOfLetters) 

    ## DECLARE VARIABLES
    ## CREATE EMPTY LISTS TO STORE VALUES
    ListOfNumberValues4Letters = []
    ListTemp = [] ## TEMPORARY LIST
    ListSum = [] ## TEMPORARY LIST

    ## BEGIN FOR LOOP

    ## FOR EACH ELEMENT IN SEQUENCE S, L, etc.
    for each in SequenceOfLetters:

        ## FOR EACH LETTER IN WORD SEQUENCE // STRING S
    
        if each == 'א':
            value = 1
        elif each == 'ב':
            value = 2    
        elif each == 'ג':
            value = 3 
        elif each == 'ד':
            value = 4 
        elif each == 'ה':
            value = 5 
        elif each == 'ו':
            value = 6 
        elif each == 'ז':
            value = 7 
        elif each == 'ח':
            value = 8 
        elif each == 'ט':
            value = 9 
        elif each == 'י':
            value = 10 
        elif each == 'כ' or each == 'ך':
            value = 20 
        elif each == 'ל':
            value = 30 
        elif each == 'מ' or each == 'ם':
            value = 40 
        elif each == 'נ' or each == 'ן':
            value = 50 
        elif each == 'ס':
            value = 60 
        elif each == 'ע':
            value = 70
        elif each == 'פ' or each == 'ף':
            value = 80  
        elif each == 'צ' or each == 'ץ':
            value = 90 
        elif each == 'ק':
            value = 100  
        elif each == 'ר':
            value = 200 
        elif each == 'ש':
            value = 300 
        elif each == 'ת':
            value = 400

        ## DEAL WITH POTENTIAL SPACES IN THE ELS SEARCH TERMS
        elif each == ' ':
            value = 0

        ## APPEND VALUE TO THE TEMPORARY LIST
        ListTemp.append(value)

        ## TEST PRINT OUTPUT
        #print("\n")  ## PRINT SPACE
        #print("value = ", value)

        ## SUM THE VALUES IN TEMPORARY LIST
        ListSum = sum(ListTemp)

        ## APPEND THIS VALUE OF THE SUM TO THE MAIN LIST TO RETURN LATER
        ListOfNumberValues4Letters.append(ListSum)
        
        ## RESET ListTemp
        ListTemp = []

        ## RESET ListSum
        ListSum = []
        
        ## TEST PRINT OUTPUT
        ## print("\n")  ## PRINT SPACE
        ## print(ListOfNumberValues4Letters)

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("WITHIN FUNCTION:  END FUNCTION #9A - GET NUMBER VALUES FOR LETTERS") ## COMPUTATION INTENSIVE

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfNumberValues4Letters)
    
## END FUNCTION () #9A - GET NUMBER VALUES FOR LETTERS

