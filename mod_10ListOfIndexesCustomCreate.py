## IMPORT MODULES

## BEGIN FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE
## NOTE: REFACTORED CODE TO TAKE INTO ACCOUNT PARAMETER TYPES: DICT OR LIST
def fn_ListOfIndexesCustomCreate(DictOrList):
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #10 - LIST OF INDEXES (CUSTOM) CREATE")
          
    ## DECLARE VARIABLES
    ## EMPTY LIST TO HOLD CUSTOM INDEX NUMBERS TO BE NON-0-INDEXED / 1-INDEXED
    ListOfIndexesCustom = [] 
    
    ## IF PARAMETER IS DICTIONARY, THEN DO THIS...
    if isinstance(DictOrList, dict):

        ## FOR EACH 5-DIGIT TUPLE KEY IN D5...
        for each in DictOrList: ## EACH == KEY OF D5
        
            ## TEST PRINT OUTPUT
            ## print("index = ", each[-1])
            ## print("each D5 key =", each)
        
            ## DECLARE INDEX VALUE
            IndexCustom = each[-1]
        
            ## ADD CUSTOM INDEX TO LIST OF CUSTOM INDEXES
            ListOfIndexesCustom.append(IndexCustom)
    
    

    ## IF PARAMETER IS LIST, THEN DO THIS
    if isinstance(DictOrList, list):

        ## CREATE COUNTER FOR THE LIST INDEXES
        IndexCustom = 1

        ## FOR EACH ELEMENT IN LIST...
        for each in DictOrList:

            ## ADD CUSTOM INDEX TO LIST OF CUSTOM INDEXES
            ListOfIndexesCustom.append(IndexCustom)

            ## INCREMENT INDEX COUNTER
            IndexCustom += 1



    ## TEST PRINT OUTPUT        
    ## print(ListOfIndexesCustom)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #10 - LIST OF INDEXES (CUSTOM) CREATE")
    
    ## RETURN VARIABLES
    return(ListOfIndexesCustom)
    
## END FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE



