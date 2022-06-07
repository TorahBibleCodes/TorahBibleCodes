## BEGIN FUNCTION () #15 - 

def fn_CalculateYH_XW(FactorY, FactorX, ListOfFactors, L, LengthOfTextToSearch): ## PARAMETER L HERE IS ACTUALLY LLL

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #15 - CALCULATE XW / YH")
    
    print(f"FactorY = {FactorY}") ## 491 ## 159 ## THIS VALUE MUST BE CORRECTED IF NOT PERFECT FACTORIAL
    print(f"FactorX = {FactorX}") ## 159 ## 491 ## TEST USER CASE X50; Y1561

    ## TEST - FACTORS - EXAMPLE: TEXT OF BOOK OF GENESIS
    ## XXX = 159 ## NECESSARY FOR CALCULATING ABSOLUTE X BELOW
    ## YYY = 491
    LLL = L ## PECULAR PROPERTY OF PYTHON THAT THIS WILL ALTER THE ORIGINAL LIST L WHEN WE ALTER LLL

    ## IF FACTORY AND FACTORX ARE IN LIST OF PERFECT FACTORS FOR LENGTH OF THE TEXT...
    if FactorY in ListOfFactors and FactorX in ListOfFactors:
        print("True - The X / W / #COLUMNS you have chosen is in the list of factors of this text length of {LengthOfTextToSearch} letters")
        YH = FactorY
        XW = FactorX

    ## ELSE IF NOT IN LIST OF PERFECT FACTORS FOR LENGTH OF THE TEST...
    else:
        print("False - The X / W / #COLUMNS you have chosen is NOT in the list of factors of this text length of {LengthOfTextToSearch} letters")
        ## YH = FactorY
        ## XW = FactorX

        ## THEN RECALCULATE FOR 2D MATRIX OUTPUT BUG IF NOT CORRECTED...
        
        ## TEST
        ## GET ABSOLUTE VALUE OF DIFFERENCE BETWEEN USER CHOICE AND FACTOR X
        ## AbsX = abs(FactorX - XXX) ## 50 - 159 == 109
        # print(f"AbsX {AbsX}")

        ## TEST - EXAMPLE: TEXT OF BOOK OF GENESIS
        ## AreaToSliceOff = (AbsX * FactorY) ## 109 * 491 == 53519 == AREA THAT WE MUST SLICE OFF TO RECALCULATE
        ## 78069 - 53519 == 24550 ## == AREA LEFT AFTER WE SLICE OFF OTHER AREA
        ## 78069 / 50 == 1561.38
        ## 78069 % 50 == 19 ## REMAINDER AFTER MODULO OPERATION
        ## 50 * 1561 == 78050 ## MISSING REMAINDER OF 19

        ## GET AREA OF SYMMETRICAL 2D MATRIX FOR SELECTED TEXT  
        AreaOf2DMatrix = LengthOfTextToSearch
        print(f"AreaOf2DMatrix BEFORE USER CHOICE OF X {AreaOf2DMatrix}")

        ## GET REMAINDER FROM USER CHOICE OF FACTOR X / W / HORIZONTAL ROWS FOR 2D MATRIX CSV FILE
        RemainderAfterUserChoice = (LengthOfTextToSearch % FactorX)
        print(f"RemainderAfterUserChoice {RemainderAfterUserChoice}")

        ## CALCULATE # OF #EMPTY SPACES NECESSARY IN LAST ROW OF 2D MATRIX IF USER CHOICE OF FACTOR X IX NOT PERFECT FACTOR
        SpaceToFillInLastRow = (FactorX - RemainderAfterUserChoice)
        print(f"SpaceToFillInLastRow {SpaceToFillInLastRow}")

        ## ADD SPACES TO END OF TEXT STRING IN ORDER TO KEEP XW VS. YH CONSISTENTLY SYMMETRICAL
        NewLengthOfTextToOutput = (LengthOfTextToSearch + SpaceToFillInLastRow) ## 78100 == (78069 + 31)
        print(f"NewLengthOfTextToOutput {NewLengthOfTextToOutput}")

        ## CALCULATE NEW YH / COLUMNS
        YH = int(NewLengthOfTextToOutput / FactorX)
        print(f"YH {YH}")

        ## CALCULATE NEW XY / ROWS
        XW = int(FactorX)
        print(f"XW {XW}")

        ## DECLARE VARIABLES
        CCC = 0 ## CREATE COUNTER VARIABLE

        ## ADD SPACES TO END OF TEXT STRING IN ORDER TO KEEP XW VS. YH CONSISTENTLY SYMMETRICAL
        while CCC < SpaceToFillInLastRow:

            LLL.append(" ")

            CCC += 1
        
        ## TEST PRINT OUTPUT
        print("\n")  ## PRINT SPACE
        print(f"Length of LLL {len(LLL)}")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #15 - CALCULATE XW / YH")

    ## RETURN VARIABLES TO PROGRAM
    return(YH, XW, L)

## END FUNCTION () #15