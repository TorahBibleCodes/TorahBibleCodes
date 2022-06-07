## IMPORT MODULES

import re
# import numpy as np
import pandas as pd
## import matplotlab.pyplot as plt

import mod_1GetUserInput_TextToSearch ## MODULE.FUNCTION() #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER
import mod_2TextFileOpen ## MODULE.FUNCTION() #2 - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING
import mod_3ATextFilePreprocess ## MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; ## RETURNS ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
import mod_4ConvertJSONStringsToDicts ## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS; ## RETURNS ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces
import mod_5GetNumberOfTextChosen ## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN ## RETURNS TUPLE OF INTEGER NUMBER OF TEXT CHOSEN
import mod_6ZippedTupleCreate ## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME; ## RETURNS ZippedTupleNoSpaces, ZippedTupleWithSpaces
import mod_7DictionaryOfVersesCreate ## MODULE.FUNCTION #7 - CREATE 2 DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED; RETURNS DictOfVersesNoSpaces, DictOfVersesWithSpaces
import mod_8ADataObjectsCreate ## MODULE.FUNCTION #8A - DATA OBJECTS CREATE; ## RETURNS TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS WITH 4-DIGIT TUPLE-KEY, DICTIONARY OF LETTERS WITH 5-DIGIT TUPLE-KEY
import mod_8BDataObjectsCreate ## MODULE.FUNCTION #8B - DATA OBJECTS CREATE; ## RETURNS LIST OF WORDS
import mod_8CDataObjectsCreate ## MODULE.FUNCTION #8C - DATA OBJECTS CREATE; ## RETURNS D5K == DICT OF D5 KEYS
import mod_9AGetNumberValues4Letters ## MODULE.FUNCTION #9A - GET NUMBER VALUE OF EACH LETTER IN LETTER STRING; ## RETURNS ListOfNumberValues4Letters
import mod_9BGetNumberValues4Words ## MODULE.FUNCTION #9B - GET NUMBER VALUE OF EACH LETTER IN WORD STRING ## RETURNS ListOfNumberValues4Words

## MOD_10 CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS
import mod_10ListOfIndexesCustomCreate ## MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES FOR EACH LETTER IN SELECTED TEXT NON-0-INDEXED / 1-INDEXED ## RETURNS LIST OF CUSTOM INDEXES; ## RETURNS ListOfIndexesCustom
import mod_11TupleOfWordsAndGematriaValuesCreate ## MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
import mod_12GetLengthOfTextToSearch ## MODULE.FUNCTION() #12 - ## RETURNS INTEGER
import mod_13GetListOfFactors ## MODULE.FUNCTION() #13 - ## RETURNS LIST OF INTEGERS/FACTORS
import mod_14GetUserInput_SizeOf2DMatrix ## MODULE.FUNCTION() #14 - 
import mod_15CalculateYH_XW ## MODULE.FUNCTION() #15 - CALCULATE XW AND YH FOR THE 2D MATRIX CSV FILE - RETURNS
import mod_16GetUserInput_NumberOfSearchTerms ## MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS
import mod_17GetUserInput_ELSSearchTerms ## MODULE.FUNCTION() #17 - GET USER INPUT: INPUT DESIRED SEARCH TERMS

## MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV FILES
import mod_98FilesNamesCreate ## MODULE.FUNCTION()
import mod_99Matrix2DOfLettersCreate ## MODULE.FUNCTION()
import mod_99WriteOutputToCSVFile_2DMatrix ## MODULE.FUNCTION()
import mod_99WriteOutputToCSVFile_WordsAndGematriaValues ## MODULE.FUNCTION() #99 - 

## TEST NEW STUFF HERE
import mod_90ConvertELSQueryToRegex ## MODULE.FUNCTION() - RETURNS ListOfRegex4ELSSearchTerms
## import mod_91SearchForELSSearchTerms

## DECLARE VARIABLES

IsGameOver = False ## FOR THE INFINITE WHILE LOOP TO KEEP THE PROGRAM RUNNING
IsTextSelected = False ## TO ONLY ALLOW ONE TEXT PER GAME TO BE SELECTED

## n = START INDEX POSITION OF 1ST (OR LAST) LETTER IN ELS SEARCH TERM WITHIN STRING/LIST/DICTIONARY

## d = LENGTH OF SKIP DISTANCE BETWEEN LETTERS IN SUCCESSFUL ELSs; THERE CAN BE MANY d VARIABLES FOR EACH INSTANCE index n OF EACH LETTER

## k = LENGTH OF ELS SEARCH TERM

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## BEGIN CALL MODULES.FUNCTIONS

## BEGIN WHILE LOOP FOR INFINITE GAME WHILE LOOP
while IsGameOver == False and IsTextSelected == False:

    ## CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
    NumberOfTextChosen = mod_1GetUserInput_TextToSearch.fn_GetUserInput()

    ## BEGIN IF/ELIF/ELSE BLOCK
    ## IF USER CHOOSES NUMBER 0 TO QUIT PROGRAM
    if NumberOfTextChosen == 0:

        ## THEN END THE PROGRAM
        IsGameOver = True

        ## TEST PRINT OUTPUT
        print("\n")
        print("GAME OVER")

    ## ELSE IF USER HAS NOT YET SELECTED NUMBER 0 TO QUIT....
    elif NumberOfTextChosen != 0:

        ## THEN THE TEXT FILE SELECTED WILL BE PROCESSED...

        ## BEGIN CALL MODULES.FUNCTIONS()
    
        ## CALL MODULE.FUNCTION() #2 - TEXT FILE OPEN
        JSON = mod_2TextFileOpen.fn_TextFileOpen(NumberOfTextChosen)

        ## CALL MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
        ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = mod_3ATextFilePreprocess.fn_TextFilePreprocess(JSON)

        ## CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
        ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = mod_4ConvertJSONStringsToDicts.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)

        ## CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
        SearchTextChosen = mod_5GetNumberOfTextChosen.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)

        ## CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE(S) CREATE
        ZippedTupleNoSpaces, ZippedTupleWithSpaces = mod_6ZippedTupleCreate.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)

        ## CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE - RETURNS 1.) DICTIONARY OF VERSES WITH NO SPACES; 2.) DICTIONARY OF VERSES WITH SPACES
        D, DS = mod_7DictionaryOfVersesCreate.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)

        ## CALL MODULE.FUNCTION() #8A - DATA OBJECTS CREATE - RETURNS 1.) STRING OF LETTERS; 2.) LIST OF LETTERS; 3.) DICT OF LETTERS WITH 4-DIGIT TUPLE KEY; 4.) DICT OF LETTERS WITH 5-DIGIT TUPLE KEY
        S, L, DL, D5 = mod_8ADataObjectsCreate.fn_DataObjectsCreate(D)
        
        ## CALL MODULE.FUNCTION() #8C - DATA OBJECTS CREATE - RETURNS DICT OF D5 KEYS AS VALUES WITH 1-INDEXED KEY FOR # OF LETTERS IN TEXT
        D5K = mod_8CDataObjectsCreate.fn_DataObjectsCreate(D5)

        ## CALL MODULE.FUNCTION() #8B - DATA OBJECTS CREATE - RETURNS LIST OF [1.) WORD # IN TEXT; 2.) GEMATRIA VALUES FOR EACH LETTER; 3.) GEMATRIA VALUE FOR ENTIRE WORD]
        ListOfWords = mod_8BDataObjectsCreate.fn_DataObjectsCreate(DS)

        ## CALL MODULE.FUNCTION() #9A - GET NUMBER VALUE FOR LETTERS - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        N = mod_9AGetNumberValues4Letters.fn_GetNumberValues(S) ## TEST FOR OA - LIST OF WORDS

        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW = mod_9BGetNumberValues4Words.fn_GetNumberValues(ListOfWords)

        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(D5)

        ## TEST
        ## print(f"ListOfIndexesCustom {ListOfIndexesCustom}")

        ## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W , DW = mod_11TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW, ListOfIndexesCustom)

        ## CALL MODULE.FUNCTION() #12 - GET LENGTH OF SELECTED TEXT(S) TO SEARCH
        LengthOfTextToSearch = mod_12GetLengthOfTextToSearch.fn_GetLengthOfTextToSearch(L) ## MODULE.FUNCTION() #12 - 

        ## CALL MODULE.FUNCTION() #13 - GET LIST OF FACTORS FOR THE INTEGER LENGTH OF SELECTED TEXT TO SEARCH
        ListOfFactors = mod_13GetListOfFactors.fn_GetListOfFactors(LengthOfTextToSearch)

        ## CALL MODULE.FUNCTION() #14 - GET USER INPUT: CHOOSE # OF ROWS FROM LIST OF FACTORS == CHOOSE SIZE OF 2D MATRIX
        FactorY, FactorX = mod_14GetUserInput_SizeOf2DMatrix.fn_GetUserInput(ListOfFactors, LengthOfTextToSearch)

        ## COPY LIST TO KEEP ORIGINAL AS-IS IN CASE SIZE OF 2D MATRIX WILL NOT BE SYMMETRICAL WITH FACTORS FOR X / Y
        LLL = L[:] ## COPYING L TO LLL ALLOWS US TO KEEP ORIGINAL L (IN CASE USER SELECTS FACTOR X THAT IS NOT A PERFECT FACTOR) FOR LATER USE 

        ## CALL MODULE.FUNCTION() #15 - TAKE INTO ACCOUNT FOR USER CHOICE IF NOT EXACT FACTOR
        YH, XW, LLL = mod_15CalculateYH_XW.fn_CalculateYH_XW(FactorY, FactorX, ListOfFactors, LLL, LengthOfTextToSearch)

        ## TEST
        ## CREATE STRING-SEQUENCE OF LETTERS FROM LIST OF LETTERS OF THE NEW INSTANCE OF LLL AFTER RECALCULATION OF 2D MATRIX SIZE
        SSS = ''.join(LLL)

        ## TEXT IS SELECTED, SO WE SET THIS VARIABLE TO TRUE
        IsTextSelected = True

        ## CALL MODULE.FUNCTION() # - GET USER INPUT: NUMBER OF SEARCH TERMS
        NumberOfSearchTerms = mod_16GetUserInput_NumberOfSearchTerms.fn_GetUserInput()

        ## CALL MODULE.FUNCTION() # - GET USER INPUT: INPUT OF SPECIFIED SEARCH TERMS
        ListOfSearchTerms, DictOfSearchTerms = mod_17GetUserInput_ELSSearchTerms.fn_GetUserInput(NumberOfSearchTerms)

        ## CALL MODULE.FUNCTION() # - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        nw = mod_9BGetNumberValues4Words.fn_GetNumberValues(ListOfSearchTerms) ## RETURNS LIST OF TUPLES OF GEMATRIA VALUES FOR ('WORD', [L,E,T,T,E,R,S], SUM)
        
        ## TEST NOT NECESSARY HERE SINCE THE ABOVE FUNCTION CALLS THIS FUNCTION FROM WITHIN
        ## CALL MODULE.FUNCTION() # - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        # n = mod_9AGetNumberValues4Letters.fn_GetNumberValues(ELSSearchTerm) ## TEST FOR OA - LIST OF WORDS
       

        ## CALL MODULE.FUNCTION() #15 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)
        ListOfRegex4ELSSearchTerms = mod_90ConvertELSQueryToRegex.fn_ConvertELSQueryToRegex(ListOfSearchTerms) ## RETURNS LIST OF LISTS OF LETTERS
        
        ## CALL MODULE.FUNCTION() #15 - 2D MATRIX CREATE FOR OUTPUT
        ListOfRowsOfLetters = mod_99Matrix2DOfLettersCreate.fn_Matrix2DOfLettersCreate(SSS, YH, XW, D5K) 


        ## TEST
        ## CREATE NEW INDEX TO ACCOUNT FOR THE EXTRA SPACES OF LAST LINE IF USER CHOOSES XW/#COLUMNS THAT IS NOT PERFECT FACTOR
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(LLL)

        ## TEST
        ## print(f"ListOfIndexesCustom {ListOfIndexesCustom}")

        ## IF LLL IS LONGER THAN L
        ## THEN USER HAS CHOSEN NON PERFECT FACTOR OF LENGTH OF TEXT FOR THE SIZE OF X COLUMNS IN 2D MATRIX

        if LLL > L: ## USER HAS CHOSEN A NON-PERFECT FACTOR

            ## CALL MODULE.FUNCTION() # RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_91SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, LLL, ListOfIndexesCustom)

        elif LLL == L: ## USER HAS CHOSEN A PERFECT FACTOR
            
            ## CALL MODULE.FUNCTION() # RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_91SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, L, ListOfIndexesCustom)


        ## BEGIN TEST FOR ELS TERMS
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW4ELS = mod_9BGetNumberValues4Words.fn_GetNumberValues(ListOfSearchTerms)

        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(ListOfSearchTerms)

        ## TEST
        ## print(f"ListOfIndexesCustom {ListOfIndexesCustom}")

        ## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W4ELS , DW4ELS = mod_11TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(ListOfSearchTerms, NW4ELS, ListOfIndexesCustom)
        ## END TEST FOR ELS TERMS


        ## CALL MODULE.FUNCTION() #
        FileNameForMatrix, FileNameForGematriaTexts, FileNameForGematriaELSs = mod_98FilesNamesCreate.fn_FileNamesCreate(XW, YH, NumberOfTextChosen)
       
        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF SELECTED TEXT(S) WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99WriteOutputToCSVFile_WordsAndGematriaValues.fn_WriteOutputToCSVFile_WordsAndGematriaValues(W, FileNameForGematriaTexts)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF ELSs WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99WriteOutputToCSVFile_WordsAndGematriaValues.fn_WriteOutputToCSVFile_WordsAndGematriaValues(W4ELS, FileNameForGematriaELSs)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE 2D MATRIX
        _ = mod_99WriteOutputToCSVFile_2DMatrix.fn_WriteOutputToCSVFile(ListOfRowsOfLetters, FileNameForMatrix)

        ## END CALL MODULES.FUNCTIONS

    ## ELSE: ALL OTHER CONDITIONS (WHAT WOULD THEY BE?) - AND THE CONDITION BELOW IS FOR INFINITE LOOP FOR THE REST OF THE GAME UNTIL USER QUITS
    else: 

            ## TEST
            print(f"ELSE: ELSE CONDITION MET - WHAT IS SUCH A CONDITION?") ## SITUATION NOT YET CALLED UNDER CURRENT DEVELOPMENT CONDITIONS
            IsGameOver = True
      

    ## END IF/ELIF/ELSE BLOCK

    ## TEXT CHOSEN BUT GAME NOT YET OVER

    ## TEST DEVELOPMENT
    ## TEST CODE BELOW THIS POINT

    ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
    ListOfIndexesCustomL = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(L)

    ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
    ListOfIndexesCustomLLL = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(LLL)
    
    ## CREATE PD SERIES WITH 0-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL0 = pd.Series(L) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL = pd.Series(L, index=ListOfIndexesCustomL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## CREATE PD SERIES WITH 0-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW 
    sLLL0 = pd.Series(LLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW
    sLLL = pd.Series(LLL, index=ListOfIndexesCustomLLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key


    ### TEST DEVELOPMENT



## END WHILE LOOP FOR INFINITE GAME WHILE LOOP

## TEST PRINT OUTPUT
print("\n")  ## PRINT SPACE
print(f"Length of List of Letters of Selected Text : {len(S)}") ## VALUE OF L GETS CHANGED TO VALUE OF LLL - CHECK WHERE
print(f"Length of List of SPACES of 2D MATRIX CSV FILE : {len(LLL)}")

## TEST PRINT OUTPUT
print("\n")  ## PRINT SPACE
print(f"ListOfSearchTerms : {ListOfSearchTerms}")
print(f"DictOfSearchTerms : {DictOfSearchTerms}")
print(f"Length of Dictionary : {len(DictOfSearchTerms)}")

## TEST PRINT OUTPUT
print("\n")
print("GAME OVER; NO REDOS; END OF GAME FOREVER!")
print("GAME OVER; ...REALLY ...THIS TIME IT'S OVER.")

## GAME OVER
IsGameOver = True

## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER
