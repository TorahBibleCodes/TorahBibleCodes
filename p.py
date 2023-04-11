## BEGIN IMPORT MODULES

## import re
import numpy as np
import pandas as pd
## import matplotlab.pyplot as plt
## import tkinter as tk

import mod_1_GetUserInput_TextToSearch ## MODULE.FUNCTION() #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER
import mod_2_TextFileOpen ## MODULE.FUNCTION() #2 - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING
import mod_3A_TextFilePreprocess ## MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; ## RETURNS ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces; ## CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
import mod_4_ConvertJSONStringsToDicts ## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS; ## RETURNS ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces
import mod_5_GetNumberOfTextChosen ## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN ## RETURNS TUPLE OF INTEGER NUMBER OF TEXT CHOSEN
import mod_6_ZippedTupleCreate ## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME; ## RETURNS ZippedTupleNoSpaces, ZippedTupleWithSpaces
import mod_7_DictionaryOfVersesCreate ## MODULE.FUNCTION() #7 - CREATE 2 DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED; RETURNS DictOfVersesNoSpaces, DictOfVersesWithSpaces
import mod_8A_DataObjectsCreate ## MODULE.FUNCTION() #8A - DATA OBJECTS CREATE; ## RETURNS TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS WITH 4-DIGIT TUPLE-KEY, DICTIONARY OF LETTERS WITH 5-DIGIT TUPLE-KEY
import mod_8B_DataObjectsCreate ## MODULE.FUNCTION() #8B - DATA OBJECTS CREATE; ## RETURNS LIST OF WORDS
import mod_8C_DataObjectsCreate ## MODULE.FUNCTION() #8C - DATA OBJECTS CREATE; ## RETURNS
import mod_8D_DataObjectsCreate ## MODULE.FUNCTION() #8D - DATA OBJECTS CREATE; ## RETURNS D5K == DICT OF D5 KEYS

## MOD_9A and MOD_9B CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS; ## MOD_9B ALWAYS CALLS MOD_9A;
import mod_9A_GetNumberValues4Letters ## MODULE.FUNCTION() #9A - GET NUMBER VALUE OF EACH LETTER IN STRING-OF-LETTERS; ## RETURNS ListOfNumberValues4Letters
import mod_9AA_AddGematriaNumberValuesToLetterObjects ## MODULE.FUNCTION() #9AA - ADD LETTER GEMATRIA NUMBER VALUE TO EACH INSTANCE OF LETTER OBJECT
import mod_9B_GetNumberValues4Words ## MODULE.FUNCTION() #9B - GET NUMBER VALUE OF EACH LETTER IN WORD STRING ## RETURNS ListOfNumberValues4Words

## MOD_10 CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS
import mod_10_ListOfIndexesCustomCreate ## MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES FOR EACH LETTER IN SELECTED TEXT NON-0-INDEXED / 1-INDEXED ## RETURNS LIST OF CUSTOM INDEXES; ## RETURNS ListOfIndexesCustom

## MOD_11 CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS
import mod_11_TupleOfWordsAndGematriaValuesCreate ## MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
import mod_11B_AssignWordNumberToEachLetterObject ## MODULE.FUNCTION() ## 11B-- ASSIGN WORD NUMBER TO EACH LETTER OBJECT IN SELECT TEXT

import mod_12_GetLengthOfTextToSearch ## MODULE.FUNCTION() #12 - ## RETURNS INTEGER OF THE LENGTH OF THE SELECTED TEXT
import mod_13_GetListOfFactors ## MODULE.FUNCTION() #13 - ## RETURNS LIST OF INTEGERS/FACTORS/DIVISORS OF THE LENGTH OF THE SELECTED TEXT
import mod_14_GetUserInput_SizeOf2DMatrix ## MODULE.FUNCTION() #14 - GET USER INPUT:  SIZE OF 2D MATRIX; RETURNS y, x
import mod_15_CalculateYH_XW ## MODULE.FUNCTION() #15 - CALCULATE XW AND YH FOR THE 2D MATRIX CSV FILE - RETURNS YH, XW, L
import mod_16_GetUserInput_NumberOfSearchTerms ## MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS ## RETURNS NumberOfSearchTerms
import mod_17_GetUserInput_ELSSearchTerms ## MODULE.FUNCTION() #17 - GET USER INPUT: INPUT DESIRED SEARCH TERMS ListOfSearchTerms, DictOfSearchTerms
import mod_18_NumpyArrayOfNumberValuesCreate ## MODULE.FUNCTION() #18 - 
import mod_19_GetMatchesPerIntegerValue ## MODULE.FUNCTION() #19 - RETURNS MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
import mod_20_DictOfELSObjectsCreate ## MODULE.FUNCTION() #20 - CREATE DICTIONARY OF ELS SEARCH OBJECTS: 

## MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV AND EXCEL FILES
import mod_98_FilesNamesCreate ## MODULE.FUNCTION()
import mod_99_Matrix2DOfLettersCreate ## MODULE.FUNCTION()
import mod_99_WriteOutputToFileXLSX_2DMatrix ## MODULE.FUNCTION() -
import mod_99_WriteOutputToFileCSV_2DMatrix ## MODULE.FUNCTION()
import mod_99_WriteOutputToFileCSV_WordsAndGematriaValues ## MODULE.FUNCTION() #99 - 

## TEST DEVELOPMENT
import mod_90_ConvertELSQueryToRegex ## MODULE.FUNCTION() - RETURNS ListOfRegex4ELSSearchTerms
import mod_91_SearchForELSSearchTerms ## MODULE.FUNCTION() - RETURNS 
## import mod_100_GetListOfFirstsAndLasts4ELS ## MODULE.FUNCTION() - RETURNS LIST OF TUPLES FOR EACH WORD OF ELS SEARCH TERMS

## import mod_100XXX_Test
## END IMPORT MODULES

## BEGIN IMPORT CLASSES
from mod_cls_GlobalSearchObject import cls_GlobalSearchObject as GSO
from mod_cls_LetterObject import cls_LetterObject as LO
from mod_cls_ELSObject import cls_ELSObject as ELSO
## END IMPORT CLASSES

## BEGIN DECLARE VARIABLES

IsGameOver = False ## FOR THE INFINITE WHILE LOOP TO KEEP THE PROGRAM RUNNING
IsTextSelected = False ## TO ONLY ALLOW ONE TEXT PER GAME TO BE SELECTED

## n = START INDEX POSITION OF OF EACH INDEX-MATCH POSITION (n) 1ST (FOR FORWARD SEARCH) OR LAST (FOR BACKWORD SEARCH) LETTER IN ELS SEARCH TERM WITHIN STRING/LIST/DICTIONARY

## d = LENGTH OF SKIP DISTANCE BETWEEN LETTERS IN SUCCESSFUL ELSs; THERE CAN BE MANY d VARIABLES FOR EACH INSTANCE index n OF EACH LETTER; [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]

## k = LENGTH OF ELS SEARCH TERM: [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח] == k == 4

## END DECLARE VARIABLES

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## BEGIN WHILE LOOP FOR INFINITE GAME WHILE LOOP
while IsGameOver == False and IsTextSelected == False:

    ## BEGIN CALL MODULES.FUNCTIONS()

    ## GET USER INPUT
    ## CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
    NumberOfTextChosen = mod_1_GetUserInput_TextToSearch.fn_GetUserInput()

    ## BEGIN IF/ELIF/ELSE BLOCK
    ## IF USER CHOOSES NUMBER 0 TO QUIT PROGRAM
    if NumberOfTextChosen == 0:

        ## TEST PRINT OUTPUT
        print("\n")
        print("GAME OVER")

        ## THEN END THE PROGRAM
        IsGameOver = True

    ## ELSE IF USER HAS NOT YET SELECTED NUMBER 0 TO QUIT, AND CHOOSES ANOTHER VALID NUMBER FOR NUMBER OF TEXTS POSSIBLE (1-43)...
    elif NumberOfTextChosen != 0:

        ## THEN THE TEXT FILE(S) SELECTED WILL BE PRE-PROCESSED AND PARSED...

        ## CALL MODULE.FUNCTION() #2 - TEXT FILE OPEN
        JSON = mod_2_TextFileOpen.fn_TextFileOpen(NumberOfTextChosen)

        ## CALL MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
        ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = mod_3A_TextFilePreprocess.fn_TextFilePreprocess(JSON)

        ## CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
        ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = mod_4_ConvertJSONStringsToDicts.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)

        ## CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
        SearchTextChosen = mod_5_GetNumberOfTextChosen.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)

        ## CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE(S) CREATE
        ZippedTupleNoSpaces, ZippedTupleWithSpaces = mod_6_ZippedTupleCreate.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)

        ## THEN SOME INITIAL (AND DERIVATIVE) DATA OBJECTS WILL BE CREATED...

        ## CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE - RETURNS 1.) DICTIONARY OF VERSES WITH NO SPACES; 2.) DICTIONARY OF VERSES WITH SPACES
        D, DS = mod_7_DictionaryOfVersesCreate.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)

        ## CREATE DATA OBJECTS + CREATE DICTIONARY OF CUSTOM LETTER OBJECTS (DLO)
        ## CALL MODULE.FUNCTION() #8A - DATA OBJECTS CREATE - RETURNS 1.) STRING OF LETTERS; 2.) LIST OF LETTERS; 3.) DICT OF LETTERS WITH 4-DIGIT TUPLE KEY; 4.) DICT OF LETTERS WITH 5-DIGIT TUPLE KEY; 5.) DICT OF INSTANCES OF LETTER OBJECTS
        S, L, DL, D5, DLO = mod_8A_DataObjectsCreate.fn_DataObjectsCreate(D)

        ## CALL MODULE.FUNCTION() #8B - DATA OBJECTS CREATE - RETURNS LIST OF [1.) WORD # IN TEXT; 2.) GEMATRIA VALUES FOR EACH LETTER; 3.) GEMATRIA VALUE FOR ENTIRE WORD]
        LW = mod_8B_DataObjectsCreate.fn_DataObjectsCreate(DS) ## RETURNS ListOfWords

        ## CALL MODULE.FUNCTION() #8C - DATA OBJECTS CREATE - RETURNS 
        ListOfIndexes4LettersInEachWord = mod_8C_DataObjectsCreate.fn_DataObjectsCreate(LW)

        ## CALL MODULE.FUNCTION() #8D - DATA OBJECTS CREATE - RETURNS DICT OF D5 KEYS AS VALUES WITH 1-INDEXED KEY FOR # OF LETTERS IN TEXT
        D5K = mod_8D_DataObjectsCreate.fn_DataObjectsCreate(D5)

        ## CALL MODULE.FUNCTION() #9A - GET NUMBER VALUE FOR LETTERS - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        N = mod_9A_GetNumberValues4Letters.fn_GetNumberValues(S) ## RETURNS ListOfNumberValues4Letters

        ## UPDATE LETTER OBJECTS
        ## CALL MODULE.FUNCTION() #9AA - ADD LETTER GEMATRIA NUMBER VALUE TO EACH INSTANCE OF LETTER OBJECT; ## RETURNS DICTIONARY OF LETTER OBJECTS
        DLO = mod_9AA_AddGematriaNumberValuesToLetterObjects.fn_AddGematriaNumberValuesToLetterObjects(DLO, N)
        
        ###########################################
        ## 1ST TIME MODULE.FUNCTION() #9B IS CALLED
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW = mod_9B_GetNumberValues4Words.fn_GetNumberValues(LW) ## CALLS MODULE.FUNCTION() #9A; ## RETURNS LIST OF TUPLES OF GEMATRIA VALUES FOR ('WORD', [L,E,T,T,E,R,S], SUM)

        ## 1ST TIME MODULE.FUNCTION() #10 IS CALLED
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(D5)

        ## TEST DEVELOPMENT
        ## print(f"ListOfIndexesCustom {ListOfIndexesCustom}")

        ## 1ST TIME MODULE.FUNCTION() #11 IS CALLED
        ## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W , DW = mod_11_TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(LW, NW, ListOfIndexesCustom, ListOfIndexes4LettersInEachWord)

        ## CALL MODULE.FUNCTION() ## 11B-- ASSIGN WORD NUMBER TO EACH LETTER OBJECT IN SELECT TEXT
        DLO = mod_11B_AssignWordNumberToEachLetterObject.fn_AssignWordNumberToEachLetterObject(DLO, DW) 

        ## CREATE MATCH PER LETTER GEMATRIA NUMBER VALUE
        ## NPA = np.where(NumpyArrayOfNumberValuesOfEntireText==2) ## RETURN TUPLE OF MATCHES FOR LETTER BET ב
        ## ListNPA = NPA[0].tolist() ## CONVERTS NUMPY ARRAY TO PYTHON LIST

        ## CALL MODULE.FUNCTION() #12 - GET LENGTH OF SELECTED TEXT(S) TO SEARCH
        LengthOfTextToSearch = mod_12_GetLengthOfTextToSearch.fn_GetLengthOfTextToSearch(L) ## MODULE.FUNCTION() #12 - 

        ## CALL MODULE.FUNCTION() #13 - GET LIST OF FACTORS FOR THE INTEGER LENGTH OF SELECTED TEXT TO SEARCH
        ListOfFactors = mod_13_GetListOfFactors.fn_GetListOfFactors(LengthOfTextToSearch)

        ## GET USER INPUT
        ## CALL MODULE.FUNCTION() #14 - GET USER INPUT: CHOOSE # OF ROWS FROM LIST OF FACTORS == CHOOSE SIZE OF 2D MATRIX
        FactorY, FactorX = mod_14_GetUserInput_SizeOf2DMatrix.fn_GetUserInput(ListOfFactors, LengthOfTextToSearch)

        ## TEST DEVELOPMENT
        ## COPY LIST TO KEEP ORIGINAL AS-IS IN CASE SIZE OF 2D MATRIX WILL NOT BE SYMMETRICAL WITH FACTORS FOR X / Y
        LLL = L[:] ## COPYING L TO LLL ALLOWS US TO KEEP ORIGINAL L (IN CASE USER SELECTS FACTOR X THAT IS NOT A PERFECT FACTOR) FOR LATER USE 

        ## CALL MODULE.FUNCTION() #15 - TAKE INTO ACCOUNT FOR USER CHOICE IF NOT EXACT FACTOR
        YH, XW, LLL = mod_15_CalculateYH_XW.fn_CalculateYH_XW(FactorY, FactorX, ListOfFactors, LLL, LengthOfTextToSearch)

        ## TEST DEVELOPMENT
        ## CREATE STRING-SEQUENCE OF LETTERS FROM LIST OF LETTERS OF THE NEW INSTANCE OF LLL AFTER RECALCULATION OF 2D MATRIX SIZE
        SSS = ''.join(LLL)

        ## TEXT IS NOW SELECTED, SO WE SET THIS VARIABLE TO TRUE
        IsTextSelected = True

        ## GET USER INPUT
        ## CALL MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS
        NumberOfSearchTerms = mod_16_GetUserInput_NumberOfSearchTerms.fn_GetUserInput()

        ## GET USER INPUT
        ## CALL MODULE.FUNCTION() #17 - GET USER INPUT: INPUT OF SPECIFIED SEARCH TERMS
        ListOfSearchTerms, DictOfSearchTerms = mod_17_GetUserInput_ELSSearchTerms.fn_GetUserInput(NumberOfSearchTerms)

        ## 2ND TIME MODULE.FUNCTION() #9B IS CALLED
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        nw = mod_9B_GetNumberValues4Words.fn_GetNumberValues(ListOfSearchTerms) ## CALLS MODULE.FUNCTION() #9A; ## RETURNS LIST OF TUPLES OF GEMATRIA VALUES FOR ('WORD', [L,E,T,T,E,R,S], SUM)
        
        ## TEST DEVELOPMENT
        ## TEST IF NOT NECESSARY HERE SINCE FUNCTION() #9B CALLS FUNCTION() #9A FROM WITHIN
        ## CALL MODULE.FUNCTION() #9A - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        # n = mod_9AGetNumberValues4Letters.fn_GetNumberValues(ELSSearchTerm) ## TEST FOR OA - LIST OF WORDS
       
        #########################################################################################################################
        ## TEST DEVELOPMENT
        ## TEST FOR TEXT STRING
        ## CALL MODULE.FUNCTION() #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)
        ListOfRegex4TextString = mod_90_ConvertELSQueryToRegex.fn_ConvertELSQueryToRegex(L) ## RETURNS LIST OF LISTS OF LETTERS

        ## TEST FOR ELS TERMS
        ## CALL MODULE.FUNCTION() #90 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)
        ListOfRegex4ELSSearchTerms = mod_90_ConvertELSQueryToRegex.fn_ConvertELSQueryToRegex(ListOfSearchTerms) ## RETURNS LIST OF LISTS OF LETTERS
        #########################################################################################################################
        
        ## TEST DEVELOPMENT
        ## 2ND TIME MODULE.FUNCTION() #10 IS CALLED
        ## CREATE NEW INDEX TO ACCOUNT FOR THE EXTRA SPACES OF LAST LINE IF USER CHOOSES XW/#COLUMNS THAT IS NOT PERFECT FACTOR/DIVISOR
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(LLL)

        ## TEST DEVELOPMENT
        ## IF LLL IS LONGER THAN L
        ## THEN USER HAS CHOSEN NON-PERFECT FACTOR/DIVISOR OF LENGTH OF TEXT FOR THE SIZE OF X COLUMNS IN 2D MATRIX;
        ## THEREFORE BLANK SPACES NEED TO BE APPENDED TO THE TEXT STRING TO COMPENSATE FOR NON-PERFECT FACTORS/DIVISORS THAT USER INPUTS

        ## BEGIN IF / ELIF BLOCK
        if LLL > L: ## USER HAS CHOSEN A NON-PERFECT FACTOR/DIVISOR

            ## CALL MODULE.FUNCTION() #91 RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_91_SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, LLL, ListOfIndexesCustom)

        elif LLL == L: ## USER HAS CHOSEN A PERFECT FACTOR/DIVISOR
            
            ## CALL MODULE.FUNCTION() #91 RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_91_SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, L, ListOfIndexesCustom)

        ## END BEGIN IF / ELIF BLOCK

        ## BEGIN TEST FOR ELS TERMS

        ## 3RD TIME MODULE.FUNCTION() #9B IS CALLED
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW4ELS = mod_9B_GetNumberValues4Words.fn_GetNumberValues(ListOfSearchTerms)

        ## 3RD TIME MODULE.FUNCTION() #10 IS CALLED
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(ListOfSearchTerms)

        ## 2ND TIME MODULE.FUNCTION() #11 IS CALLED
        ## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W4ELS, DW4ELS = mod_11_TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(ListOfSearchTerms, NW4ELS, ListOfIndexesCustom, ListOfIndexes4LettersInEachWord=[]) ## PASS EMPTY LIST FOR ELSs B/C NO INDEX POSITIONS FOR THESE
        
        
        ## CALL MODULE.FUNCTION() #18 ## TODO: CREATE SEPARATE MODULE TO CONTAIN THIS ONE NUMPY FUNCTION
        ## CREATE NUMPY ARRAY OF NUMBER VALUES
        NumpyArrayOfNumberValuesOfEntireText = mod_18_NumpyArrayOfNumberValuesCreate.fn_NumpyArrayOfNumberValuesCreate(N)

        ## CALL MODULE.FUNCTION() #19- DATA OBJECT CREATE - RETURNS DICT OF MATCHES FOR EACH FIRST LETTER OF EACH ELS SEARCH TERM
        DictOfMatches4ELS = mod_19_GetMatchesPerIntegerValue.fn_GetMatchesPerIntegerValue(NW4ELS, NumpyArrayOfNumberValuesOfEntireText)

        ## CREATE ELS OBJECTS - CREATE DICTIONARY OF ELS [USER-SEARCH-TERM] OBJECTS
        ## CALL MODULE.FUNCTION() #20 - DATA OBJECT CREATE - RETURNS DICT OF ELS OBJECTS (DELSO)
        DELSO = mod_20_DictOfELSObjectsCreate.fn_DictOfELSObjectsCreate(DictOfMatches4ELS)

        ## TEST DEVELOPMENT

        ## END TEST FOR ELS TERMS

        ## TEST DEVELOPMENT
        ## TEST CREATE 2D MATRIX HERE OR MOVE BELOW TO MODULES FOR FINAL STEPS(?)
        ## CALL MODULE.FUNCTION() #99 - 2D MATRIX CREATE FOR OUTPUT
        ListOfRowsOfLetters = mod_99_Matrix2DOfLettersCreate.fn_Matrix2DOfLettersCreate(SSS, YH, XW, D5K) 

        ## MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV FILES

        ## CALL MODULE.FUNCTION() #98
        FileNameForMatrixXLSX, FileNameForMatrixCSV, FileNameForGematriaTexts, FileNameForGematriaELSs = mod_98_FilesNamesCreate.fn_FileNamesCreate(XW, YH, NumberOfTextChosen)
       
        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF SELECTED TEXT(S) WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99_WriteOutputToFileCSV_WordsAndGematriaValues.fn_WriteOutputToFile(W, FileNameForGematriaTexts)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF ELSs WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99_WriteOutputToFileCSV_WordsAndGematriaValues.fn_WriteOutputToFile(W4ELS, FileNameForGematriaELSs)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE 2D MATRIX
        _ = mod_99_WriteOutputToFileCSV_2DMatrix.fn_WriteOutputToFile(ListOfRowsOfLetters, FileNameForMatrixCSV)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO XLSX FILE 2D MATRIX
        ## _ = mod_99_WriteOutputToFileXLSX_2DMatrix.fn_WriteOutputToFile(YH, XW, ListOfRowsOfLetters, FileNameForMatrixXLSX)

        ## END MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV FILES

    ## ELSE: ALL OTHER CONDITIONS (WHAT WOULD THEY BE?) - AND THE CONDITION BELOW IS FOR INFINITE LOOP FOR THE REST OF THE GAME UNTIL USER QUITS
    else: 

        ## TEST DEVELOPMENT
        print(f"ELSE: ELSE CONDITION MET - WHAT IS SUCH A CONDITION?") ## SITUATION NOT YET CALLED UNDER CURRENT DEVELOPMENT CONDITIONS
        IsGameOver = True
      
    ## END IF/ELIF/ELSE BLOCK

    ## TEXT CHOSEN/SELECTED BUT GAME NOT YET OVER

    ## TEST DEVELOPMENT
    ## BEGIN TEST CODE BELOW THIS POINT

    ## 4TH TIME MODULE.FUNCTION() #10 IS CALLED
    ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
    ListOfIndexesCustomL = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(L)

    ## 5TH TIME MODULE.FUNCTION() #10 IS CALLED
    ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
    ListOfIndexesCustomLLL = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(LLL)

    ## END CALL MODULES.FUNCTIONS()


    ## TEST DEVELOPMENT
    ## CREATE PD SERIES WITH 0-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL0 = pd.Series(L) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR THE ORIGINAL TEXT LENGTH
    sL = pd.Series(L, index=ListOfIndexesCustomL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## CREATE PD SERIES WITH 0-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW 
    sLLL0 = pd.Series(LLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR LENGTH OF THE TEXT + EMPTY SPACES IN LAST ROW
    sLLL = pd.Series(LLL, index=ListOfIndexesCustomLLL) ## --> Converts ListOfLetters to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## TEST DEVELOPMENT
    ## CREATE PD SERIES WITH 0-INDEX FOR THE ORIGINAL TEXT LENGTH
    sN0 = pd.Series(N) ## --> Converts ListOfNumbers (N) to Pandas Series (~ Dictionary-like Object)
    
    ## CREATE PD SERIES WITH 1-INDEX FOR THE ORIGINAL TEXT LENGTH
    sN = pd.Series(N, index=ListOfIndexesCustomL) ## --> Converts ListOfNumbers (N) to Pandas Series (~ Dictionary-like Object) with custom indexes for keys of the PD Series starting with 1-index/key

    ## TEST DEVELOPMENT
    ## q = mod_100_Test.fn_Test(sL, NW4ELS, ListOfPDSeries4ELSs, ListOfRegex4ELSSearchTerms)
    ## LM0, LM1, D0, D1 = mod_100XXX_Test.fn_Test(sL, S, ListOfRegex4ELSSearchTerms)
    
    ## TEST DEVELOPMENT CALL FUNCTION
    ## DictOfMatches = fn_Search4ELSs(DELSO, sN, N)
                    
    ## TEST DEVELOPMENT - CREATE OBJECT INSTANCE OF GSO() = GLOBAL SEARCH OBJECT: GSO
    ## CREATE NEW OBJECT INSTANCE OF CLASS: GLOBAL SEARCH OBJECT
    gso = GSO()

    ## ADD ATTRIBUTES TO gso
    gso.SearchTextChosen = SearchTextChosen ## 1-DIGIT TUPLE ## (12,)
    gso.LengthOfTextToSearch = LengthOfTextToSearch ## INTEGER

    gso.D = D ## 3-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#) - NO SPACES BETWEEN WORDS/LETTERS
    gso.DS = DS ## 3-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#) - WITH SPACES BETWEEN WORDS/LETTERS
    gso.S = S ## 0-BASED INDEX POSITIONS
    gso.L = L ## 0-BASED INDEX POSITIONS
    gso.DL = DL ## 4-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE) - NO SPACES BETWEEN WORDS/LETTERS
    gso.D5 = D5 ## 5-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT) - NO SPACES BETWEEN WORDS/LETTERS
    gso.D5K = D5K ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 5-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT)
    gso.N = N ## 0-BASED INDEX POSITIONS
    
    gso.LW = LW ## 0-BASED INDEX POSITIONS
    gso.W = W ## 0-BASED INDEX POSITIONS
    gso.DW = DW ## 1-BASED DICTIONARY KEY-POSITIONS
    gso.NW = NW ## 0-BASED INDEX POSITIONS
    gso.DLO = DLO ## 1-BASED DICTIONARY KEY-POSITIONS

    gso.ListOfSearchTerms = ListOfSearchTerms ## 0-BASED INDEX POSITIONS
    gso.DictOfSearchTerms = DictOfSearchTerms ## 1-BASED DICTIONARY KEY-POSITIONS

    gso.ListOfRegex4TextString = ListOfRegex4TextString ## 0-BASED INDEX POSITIONS
    gso.ListOfRegex4ELSSearchTerms = ListOfRegex4ELSSearchTerms ## 0-BASED INDEX POSITIONS
    gso.ListOfRowsOfLetters = ListOfRowsOfLetters ## 0-BASED INDEX POSITIONS
    gso.ListOfPDSeries4ELSs = ListOfPDSeries4ELSs ## 0-BASED INDEX POSITIONS

    gso.NW4ELS = NW4ELS ## 0-BASED INDEX POSITIONS
    gso.W4ELS = W4ELS ## 0-BASED INDEX POSITIONS
    gso.DW4ELS = DW4ELS ## 1-BASED DICTIONARY KEY-POSITIONS
    gso.DictOfMatches4ELS = DictOfMatches4ELS ## 1-BASED DICTIONARY KEY-POSITIONS
    gso.DELSO = DELSO ## 1-BASED DICTIONARY KEY-POSITIONS

    gso.ListOfFactors = ListOfFactors ## 0-BASED INDEX POSITIONS
    gso.YH = YH ## INTEGER
    gso.XW = XW ## INTEGER
    gso.LLL = LLL ## 0-BASED INDEX POSITIONS

    gso.ListOfIndexesCustomL = ListOfIndexesCustomL ## 0-BASED INDEX POSITIONS
    gso.ListOfIndexesCustomLLL = ListOfIndexesCustomLLL ## 0-BASED INDEX POSITIONS

    gso.sL0 = sL0 ## 0-BASED INDEX POSITIONS
    gso.sL = sL ## 1-BASED INDEX POSITIONS
    gso.sLLL0 = sLLL0 ## 0-BASED INDEX POSITIONS
    gso.sLLL = sLLL ## 1-BASED INDEX POSITIONS
    gso.sN0 = sN0 ## 0-BASED INDEX POSITIONS
    gso.sN = sN ## 1-BASED INDEX POSITIONS

    gso.NumpyArrayOfNumberValuesOfEntireText = NumpyArrayOfNumberValuesOfEntireText ## 0-BASED INDEX POSITIONS
    
    ## END TEST CODE BELOW THIS POINT
    ## TEST DEVELOPMENT

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

## TEST DEVELOPMENT


## TEST CLASS OBJECT
        
print("TEST gso")
# print(f"TEST gso : {gso.SearchTextChosen}")
# print(f"TEST gso : {gso.LengthOfTextToSearch}")
# print(f"TEST gso : {gso.ListOfSearchTerms}")
# print(f"TEST gso : {gso.DictOfSearchTerms}")


## TEST PRINT OUTPUT
print("\n") ## PRINT SPACE
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
