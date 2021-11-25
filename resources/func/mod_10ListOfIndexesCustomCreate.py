## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## BEGIN FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE
## BEGIN FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE
## BEGIN FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE

def fn_ListOfIndexesCustomCreate(D5):
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #10 - LIST OF INDEXES (CUSTOM) CREATE")
          
    ## DECLARE VARIABLES
    
    ## EMPTY LIST TO HOLD CUSTOM INDEX NUMBERS TO BE NON-0-INDEXED / 1-INDEXED
    ListOfIndexesCustom = [] 
    
    ## FOR EACH 5-DIGIT TUPLE KEY IN D5...
    for each in D5: ## EACH == KEY OF D5
        
        ## TEST PRINT OUTPUT
        ## print("index = ", each[-1])
        ## print("each D5 key =", each)
        
        ## DECLARE INDEX VALUE
        IndexCustom = each[-1]
        
        ## ADD CUSTOM INDEX TO LIST OF CUSTOM INDEXES
        ListOfIndexesCustom.append(IndexCustom)
    
    ## TEST PRINT OUTPUT        
    ## print(ListOfIndexesCustom)
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #10 - LIST OF INDEXES (CUSTOM) CREATE")
    
    ## RETURN VARIABLES
    return(ListOfIndexesCustom)
    
## END FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE
## END FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE
## END FUNCTION () #10 - LIST OF INDEXES (CUSTOM) CREATE


