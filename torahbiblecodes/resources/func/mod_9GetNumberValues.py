## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #9 - GET NUMBER VALUES
## FUNCTION () #9 - GET NUMBER VALUES
## FUNCTION () #9 - GET NUMBER VALUES

def fn_GetNumberValues(SequenceOfLetters, ListOfWords):
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #9 - GET NUMBER VALUES")
    
    ## CREATE EMPTY LIST TO STORE VALUES
    ListOfNumberValues4Letters = []
    ListOfNumberValues4Words = []

    ListTemp = []
    ListSum = []
    value = 0
    ## CREATE EMPTY DICT TO STORE VALUES
    #DictOfNumberValues = {}

    ## BEGIN FOR LOOP 1A

    ## FOR EACH ELEMENT IN SEQUENCE S, L, etc.??
    for cada in SequenceOfLetters:

        ## BEGIN FOR LOOP 1B
        
        ## FOR EACH LETTER IN WORD//STRING S
        for each in cada:
            
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

            ListTemp.append(value)

        
        ## TEST PRINT OUTPUT
        #print("\n")  ## PRINT SPACE
        #print("value = ", value)


        ListSum = sum(ListTemp)
        ListOfNumberValues4Letters.append(ListSum)
        
        ListTemp = [] ## RESET ListTemp
        ListSum = [] ## RESET ListSum
        

        #print(ListOfNumberValues4Letters)

        ## END FOR LOOP 1B

    ## END FOR LOOP 1A


    ## BEGIN FOR LOOP 2A

    ## FOR EACH ELEMENT IN SEQUENCE S, L, etc.??
    for cada in ListOfWords:

        ## BEGIN FOR LOOP 2B
        
        ## FOR EACH LETTER IN WORD//STRING S
        for each in cada:
            
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

            ListTemp.append(value)
            TupleTemp = tuple(ListTemp)
            
        
        ## TEST PRINT OUTPUT
        #print("\n")  ## PRINT SPACE
        #print("value = ", value)


        SumOfWord = sum(TupleTemp)
        ListOfNumberValues4Words.append(SumOfWord)
        
        ListTemp = [] ## RESET ListTemp
        ListSum = [] ## RESET ListSum
        
        ## TEST PRINT OUTPUT
        #print("\n")  ## PRINT SPACE
        #print(ListOfNumberValues4Letters)

        ## END FOR LOOP 2B

    ## END FOR LOOP 2A

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #9 - GET NUMBER VALUES")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfNumberValues4Letters, ListOfNumberValues4Words)
    
## END FUNCTION () #9 - GET NUMBER VALUES
## END FUNCTION () #9 - GET NUMBER VALUES
## END FUNCTION () #9 - GET NUMBER VALUES
