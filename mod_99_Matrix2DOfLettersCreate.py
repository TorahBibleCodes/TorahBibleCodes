## BEGIN FUNCTION () #99 - MATRIX 2D OF LETTERS CREATE

def fn_Matrix2DOfLettersCreate(S, YH, XW, D5K):

    """
    ## MODULE.FUNCTION() #99 - 
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #99 - MATRIX 2D OF LETTERS CREATE FOR OUTPUT;")
    
    ## TEST 

    #print(f"x = {FactorX}; y = {FactorY}")
    print(f"x = {XW}; y = {YH}")

    # Creates a list containing 5 lists (COLUMNS = W = X), each of 8 items (ROWS = H = Y) , all set to 0
    h, w = YH, XW ## 455, 670 ## 469, 650 ## 335, 910 # 8, 5

    #print(f"x = {FactorX}; y = {FactorY}")
    print(f"w = {XW}; h = {YH}")

    ## CREATE MATRIX FROM THE NUMBERS OF PERMISSIBLE NUMBERS: NOT ONLY PERFECT FACTORS
    ## CREATE LIST OF LISTS == LIST OF ROWS; EACH ROW == LIST OF LETTERS
    # Matrix = [[0 for x in range(w)] for y in range(h)]
    M = [[0 for x in range(w)] for y in range(h)]

    #yy = h-h ## 670 - 670 ## 871 - 871 ## 910 - 910 = 0
    #xx = w-w ## 455- 455 ## 455 - 455 ## 335 - 335 = 0

    #for EachRow in M: ## FOR EACH LIST IN MATRIX M; == HEIGHT OF MATRIX, i.e. ROWS, i.e. Y

    CountUp = 0
    CountDown = len(S)
    D5KCountUp = 1
    D5KCountUpLeft = XW

    ## TEST
    a = M
    print(len(M), type(M))

    ListOfRows = []
    ListOfLettersInRow = []

    ## BEGIN FOR LOOP
    for i in range(len(a)): ## ROWS, Y, H ## 0 - 909 ## FOR EACH ROW
        
        ## TEST PRINT OUTPUT
        # print(f"i = {i}")

        ListOfLettersInRow.append(D5K[D5KCountUp])

        ## BEGIN FOR LOOP
        for j in range(len(a[i])): ## COLUMNS, X, W ## 0 - 334 ##  ## FOR EACH COLUMN

            ## TEST PRINT OUTPUT
            # print(f"j = {j}")

            ## USE THE COUNTUP TO SPECIFIC INDEX NUMBER; APPEND THAT LETTER TO LIST OF LETTERS IN EACH ROW
            ListOfLettersInRow.append(S[CountUp])
            
            ## TEST PRINT OUTPUT
            #a[i][j] = S[CounterVariable]

            ## TEST PRINT OUTPUT
            # print(f"{a[i][j]}, {c}, {countdown}")
        
            ## INCREMENT 2 COUNTERS; 1 COUNT UP; 1 COUNT DOWN
            CountUp += 1
            CountDown -= 1
            

        ## END FOR LOOP

        ## TEST PRINT OUTPUT
        ## print(D5K[D5KCountUp])
        ## print(D5K[D5KCountUpLeft]) ## DOES NOT EXIST FOR ISAIAH DICT KEY 66900 FOR TEXT 66888
       
        LengthOfText = len(D5K)
        LengthOfMatrix = len(S)

        ## IF LENGTH OF MATRIX IS SAME LENGTH AS DICT OF LETTERS
        if LengthOfMatrix == LengthOfText:

            ListOfLettersInRow.append(D5K[D5KCountUpLeft])

        
        ## IF USER CHOICE OF 2D MATRIX SIZE IS NOT A PERFECT FACTOR
        ## THEN CALCULATE TO MAKE EXPORT OF NON-PERFECT FACTORS FOR X & Y POSSIBLE.
        elif LengthOfMatrix > LengthOfText:       

            ## IF INDEX TO GET D5K KEY FOR THE LETTER IS GREATER THAN THE POSSIBLE KEY VALUES
            if D5KCountUpLeft == LengthOfMatrix: # D5K[D5KCountUpLeft] in D5K.values(): 
            
                ## APPEND LEFT SIDE D5K COUNTER

                KeyOfFirstLetterInRow = D5K[D5KCountUp]
                ## KeyOfLastLetterInRow = D5K[D5KCountUpLeft]

                print(f"Key of D5 / D5K in D5K.keys() is {KeyOfFirstLetterInRow} ")
                ## print(f"Last Letter Index in D5K.keys() is {KeyOfLastLetterInRow} ")
                print(f"len(S) Length of Matrix = {len(S)}")
                print(f"len(D5K) Length Of Text = {len(D5K)}")

                ## GET LAST VALUE OF D5K VALUE (SAME AS KEY OF D5)
                LastIndexForD5KLastRow = list(D5K)[-1]

                # APPEND LEFT SIDE D5K COUNTER WITH THE LAST POSSIBLE D5K KEY VALUE  
                ListOfLettersInRow.append(D5K[LastIndexForD5KLastRow])

            else: ## ELSE IF THE KEY IS A POSSIBLE LEFT SIDE KEY

                ListOfLettersInRow.append(D5K[D5KCountUpLeft])


        ## INCREMENT THE D5K BY THE NUMBER OF XW COLUMNS
        D5KCountUp += XW
        D5KCountUpLeft += XW

        ## TEST PRINT OUTPUT
        #print(f"D5KCountUp {D5KCountUp}")
        #print(f"D5KCountUpLeft {D5KCountUpLeft}")
        
        ## REVERSE DIRECTION FROM LEFT-TO-RIGHT TO RIGHT-TO-LEFT FOR HEBREW
        ListOfLettersInRow.reverse()

        ## APPEND EACH REVERSED LIST AS A ROW OF LETTERS TO THE LIST OF ROWS
        ListOfRows.append(ListOfLettersInRow)

        ## RESET THE LIST TO BE EMPTY FOR THE NEXT ROW IN LOOP
        ListOfLettersInRow = []

    ## END FOR LOOP  
            
    # print(a[0])
   
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #99 - MATRIX 2D OF LETTERS CREATE FOR OUTPUT;")

    ## RETURN VARIABLES TO PROGRAM
    return(ListOfRows)

## END FUNCTION () #99 - MATRIX 2D OF LETTERS CREATE FOR OUTPUT