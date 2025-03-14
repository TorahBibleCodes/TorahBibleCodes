## BEGIN IMPORT MODULES

## import re
import numpy as np
import pandas as pd
## import matplotlab.pyplot as plt
## import tkinter as tk
np.set_printoptions(legacy="1.25") ## DEAL WITH NUMPY UPDATE THAT SCREWS UP OUTPUT FORMATTING IN THE CSV FILE - THIS IS NUMPY'S SUGGESTED SOLUTION

import mod_0_GetUserInput_CodexToSearch ## MODULE.FUNCTION() #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER
import mod_1A_GetUserInput_TextToSearch_Koren ## MODULE.FUNCTION() #1A - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER
import mod_1B_GetUserInput_TextToSearch_Leningrad ## MODULE.FUNCTION() #1B - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER
import mod_1C_GetUserInput_TextToSearch_MAM ## MODULE.FUNCTION() #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER
import mod_2A_TextFileOpen_Koren ## MODULE.FUNCTION() #2A - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING
import mod_2B_TextFileOpen_Leningrad ## MODULE.FUNCTION() #2B - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING
import mod_2C_TextFileOpen_MAM ## MODULE.FUNCTION() #2C - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING

import mod_3A1_TextFilePreprocess_Koren_ExtractStrings ## MODULE.FUNCTION() #3A1 - TEXT FILE PREPROCESS; ## RETURNS ListOfStringsParsed, ListOfStringsParsedWithSpaces; ## CALLS MODULE.FUNCTION() #3A2 - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
## import mod_3A2_TextFilePreprocess_Koren_ExtractKeysAndWords ## MODULE.FUNCTION #3A2 - 
import mod_3A3_TextFilePreprocess_Koren_FixKeys ## MODULE.FUNCTION #3A3 - 
import mod_3A4_TextFilePreprocess_Koren_FixLines ## MODULE.FUNCTION #3A4 - 
import mod_3A5_TextFileParse_Koren ## MODULE.FUNCTION() #3A5 - TEXT FILE PARSE
import mod_3B_TextFilePreprocess_Leningrad ## MODULE.FUNCTION() #3B - TEXT FILE PREPROCESS; ## RETURNS ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces; ## CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
import mod_3C_TextFilePreprocess_MAM_ExtractStrings ## FUNCTION() #3C CALLS #3CC INTERNALLY
import mod_3CCC_TextFileParse_MAM ## MODULE.FUNCTION() #3CCC - RETURNS: LW4AV, DVMAMH, DVMAMHS, VerseCountTotal, WordCountTotal, LetterCountTotal
import mod_4_ConvertJSONStringsToDicts ## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS; ## RETURNS ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces
import mod_5_GetNumberOfTextChosen ## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN ## RETURNS TUPLE OF INTEGER NUMBER OF TEXT CHOSEN
import mod_6_ZippedTupleCreate ## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME; ## RETURNS ZippedTupleNoSpaces, ZippedTupleWithSpaces
import mod_7_DictionaryOfVersesCreate ## MODULE.FUNCTION() #7 - CREATE 2 DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED; RETURNS DictOfVersesNoSpaces, DictOfVersesWithSpaces
import mod_8A_DataObjectsCreate ## MODULE.FUNCTION() #8A - DATA OBJECTS CREATE; ## RETURNS TUPLE OF (STRING-SEQUENCE OF LETTERS, LIST OF LETTERS, DICTIONARY OF LETTERS WITH 4-DIGIT TUPLE-KEY, DICTIONARY OF LETTERS WITH 5-DIGIT TUPLE-KEY
import mod_8B_DataObjectsCreate ## MODULE.FUNCTION() #8B - DATA OBJECTS CREATE; ## RETURNS LIST OF WORDS
import mod_8C_DataObjectsCreate ## MODULE.FUNCTION() #8C - DATA OBJECTS CREATE; ## RETURNS ListOfIndexes4LettersInEachWord
import mod_8D_DataObjectsCreate ## MODULE.FUNCTION() #8D - DATA OBJECTS CREATE; ## RETURNS D5K == DICT OF D5 KEYS
import mod_8E_DataObjectsCreate ## MODULE.FUNCTION() #8E - DATA OBJECTS CREATE; ## RETURNS DWTK == DICT OF DWT KEYS

## MOD_9A and MOD_9B CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS; ## MOD_9B ALWAYS CALLS MOD_9A;
import mod_9A_GetNumberValues4Letters ## MODULE.FUNCTION() #9A - GET NUMBER VALUE OF EACH LETTER IN STRING-OF-LETTERS; ## RETURNS ListOfNumberValues4Letters
import mod_9AA_CalculateLetterPercentages ## MODULE.FUNCTION() #9AA - CALCULATE LETTER PERCENTAGES; ## RETURNS 
import mod_9AAA_AddGematriaNumberValuesToLetterObjects ## MODULE.FUNCTION() #9AAA - ADD LETTER GEMATRIA NUMBER VALUE TO EACH INSTANCE OF LETTER OBJECT
import mod_9B_GetNumberValues4Words ## MODULE.FUNCTION() #9B - GET NUMBER VALUE OF EACH LETTER IN WORD STRING ## RETURNS ListOfNumberValues4Words

## MOD_10 CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS
import mod_10_ListOfIndexesCustomCreate ## MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES FOR EACH LETTER IN SELECTED TEXT NON-0-INDEXED / 1-INDEXED ## RETURNS LIST OF CUSTOM INDEXES; ## RETURNS ListOfIndexesCustom

## MOD_11 CALLED MULTIPLE TIMES BY VARIOUS DATA OBJECTS
import mod_11A_TupleOfWordsAndGematriaValuesCreate ## MODULE.FUNCTION() ## 11A - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
import mod_11B_AssignWordNumberToEachLetterObject ## MODULE.FUNCTION() ## 11B-- ASSIGN WORD NUMBER TO EACH LETTER OBJECT IN SELECT TEXT

import mod_12_GetLengthOfTextToSearch ## MODULE.FUNCTION() #12 - ## RETURNS INTEGER OF THE LENGTH OF THE SELECTED TEXT
import mod_13_GetListOfFactors ## MODULE.FUNCTION() #13 - ## RETURNS LIST OF INTEGERS/FACTORS/DIVISORS OF THE LENGTH OF THE SELECTED TEXT
import mod_14_GetUserInput_SizeOf2DMatrix ## MODULE.FUNCTION() #14 - GET USER INPUT:  SIZE OF 2D MATRIX; RETURNS y, x
import mod_15_CalculateYH_XW ## MODULE.FUNCTION() #15 - CALCULATE XW AND YH FOR THE 2D MATRIX CSV FILE - RETURNS YH, XW, L
import mod_16A_GetUserInput_TypeOfSearchInput ## MODULE.FUNCTION() #16A - GET USER INPUT: TYPE OF SEARCH INPUT ## RETURNS TypeOfSearchInput
import mod_16AA_GetUserInput_FileNameForCSVImport_SearchInput ## MODULE.FUNCTION() #16AA - GET USER INPUT: ## RETURNS FileNameForCSVImport
import mod_16AAA_ReadInputFromFileCSV_ELSSearchTerms ## MODULE.FUNCTION() #16AAA - OPEN / READ CSV FILE WITH ELS SEARCH TERMS: DATA OBJECT CREATE: ListOfSearchTerms
import mod_16AAAA_DataObjectCreate_DictOfSearchTerms ## MODULE.FUNCTION() #16AAAA - DATA OBJECT CREATE: DictOfSearchTerms
import mod_16_GetUserInput_NumberOfSearchTerms ## MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS ## RETURNS NumberOfSearchTerms
import mod_17A_GetUserInput_ELSSearchTerms ## MODULE.FUNCTION() #17A - GET USER INPUT: INPUT DESIRED SEARCH TERMS ListOfSearchTerms, DictOfSearchTerms
import mod_17B_GetUserInput_SkipDistancesDMinMax ## MODULE.FUNCTION() #17B - GET USER INPUT: INPUT MIN / MAX SKIP DISTANCES ## RETURNS SkipDistanceDMinimum=None, SkipDistanceDMaximum=None

import mod_18_NumpyArrayOfNumberValuesCreate ## MODULE.FUNCTION() #18 - ## RETURNS NumpyArrayOfNumberValuesOfEntireText
import mod_19_GetMatchesPerIntegerValue ## MODULE.FUNCTION() #19 - ## RETURNS MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
import mod_20_DictOfELSObjectsCreate ## MODULE.FUNCTION() #20 - CREATE DICTIONARY OF ELS SEARCH OBJECTS; ## RETURNS DELSO
import mod_21_PandasObjectsCreate ## MODULE.FUNCTION() #21 - ## RETURNS sL0, sL, sLLL0, sLLL, sN0, sN)
import mod_22A_ELSSearchByLetterFirst ## MODULE.FUNCTION() #22A - ## RETURNS ELS MATCHES SEARCH BY FIRST LETTER
import mod_22B_NegativesAndPositivesExtract ## MODULE.FUNCTION() #22B - ## RETURNS DELSMP, DELSMN
import mod_23_ELSSearchByLetterLast ## MODULE.FUNCTION() #23 - ## RETURNS ELS MATCHES SEARCH BY LAST LETTER
import mod_24_AddSearchResultsToDELSO ## MODULE.FUNCTION() #24 - ## RETURNS DELSO
import mod_25_UpdateW4ELS ## MODULE.FUNCTION() #25 - ## RETURNS W4ELS
import mod_26_UpdateW ## MODULE.FUNCTION() #26 - ## RETURNS W
import mod_27_GatherData4ELSMatches ## MODULE.FUNCTION() #27 - ## RETURNS: LTM4ELS_LF_ABS, DLO, DELSO
import mod_28_ExtractAllELSLetterPositions ## ## MODULE.FUNCTION() #28 - RETURNS: MasterList4LetterPositions, DLO 

## TEST DEVELOPMENT
import mod_40_ConvertELSQueryToRegex ## MODULE.FUNCTION() #40 - RETURNS ListOfRegex4ELSSearchTerms
import mod_41_SearchForELSSearchTerms ## MODULE.FUNCTION() #41 - RETURNS

## MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV AND EXCEL FILES
import mod_98_FileNamesCreate ## MODULE.FUNCTION() #98
import mod_98_FileNamesCreate4ELSTerms_POS ## MODULE.FUNCTION() #98 INDIVIDUAL FILES FOR EACH ELS: ALL LETTER MATCHES: POSITIVE
import mod_98_FileNamesCreate4ELSTerms_NEG ## MODULE.FUNCTION() #98 INDIVIDUAL FILES FOR EACH ELS: ALL LETTER MATCHES: NEGATIVE
import mod_99_Matrix2DOfLettersCreate ## MODULE.FUNCTION() #99
import mod_99_WriteOutputToFileCSV_WordsAndGematriaValues ## MODULE.FUNCTION() #99 - 
import mod_99_WriteOutputToFileCSV_ELSMatches_DATASUMMARY ## MODULE.FUNCTION() #99 - 
import mod_99_WriteOutputToFileCSV_ELSMatches ## MODULE.FUNCTION() #99 -
import mod_99_WriteOutputToFileCSV_LetterStatistics ## MODULE.FUNCTION() #99 - 
import mod_99_WriteOutputToFileCSV_2DMatrix ## MODULE.FUNCTION()
import mod_99_IterateOutput4ELSMatches #MODULE.FUNCTION() #99 ## RETURNS NOTHING - IMPORTS mod_99_WriteOutputToFileCSV_ELSMatchesAllLetterPositions
## import mod_99_WriteOutputToFileXLSX_2DMatrix ## MODULE.FUNCTION() #99 -

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

## d = LENGTH OF SKIP DISTANCE BETWEEN LETTERS IN SUCCESSFUL ELSs; THERE CAN BE MANY (d) VARIABLES FOR EACH INSTANCE INDEX POSITION (n) OF EACH LETTER; [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]

## k = LENGTH OF ELS SEARCH TERM: [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח] == k == 4

## END DECLARE VARIABLES

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## BEGIN WHILE LOOP FOR INFINITE GAME WHILE LOOP
while IsGameOver == False and IsTextSelected == False:

    ## BEGIN CALL MODULES.FUNCTIONS()

    ## GET USER INPUT
    ## CALL MODULE.FUNCTION() #1A - GET USER INPUT 1A - CHOOSE CODEX TO SEARCH
    NumberOfCodexChosen = mod_0_GetUserInput_CodexToSearch.fn_GetUserInput()

    ## TEST PRINT OUTPUT
    ## print(f"{NumberOfCodexChosen}{type(NumberOfCodexChosen)}")

    ## BEGIN MATCH CASE - DEAL WITH CHOICE OF TEXT(S)
    match NumberOfCodexChosen:

        ## KOREN CODEX
        case 1:
        
            ## GET USER INPUT
            ## CALL MODULE.FUNCTION() #1A - GET USER INPUT 1A - CHOOSE TEXT TO SEARCH - KOREN CODEX
            NumberOfTextChosen = mod_1A_GetUserInput_TextToSearch_Koren.fn_GetUserInput(NumberOfCodexChosen)
        
        ## LENINGRAD CODEX
        case 2:

            ## GET USER INPUT
            ## CALL MODULE.FUNCTION() #1B - GET USER INPUT 1B - CHOOSE TEXT TO SEARCH - LENINGRAD CODEX
            NumberOfTextChosen = mod_1B_GetUserInput_TextToSearch_Leningrad.fn_GetUserInput(NumberOfCodexChosen)

        ## MAM CODEX
        case 3:

            ## GET USER INPUT
            ## CALL MODULE.FUNCTION() #1C - GET USER INPUT 1C- CHOOSE TEXT TO SEARCH - MAM CODEX
            NumberOfTextChosen = mod_1C_GetUserInput_TextToSearch_MAM.fn_GetUserInput(NumberOfCodexChosen)
            
    ## END MATCH CASE - DEAL WITH CHOICE OF TEXT(S)

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

        ## BEGIN MATCH CASE - DEAL WITH CHOICE OF CODEX
        match NumberOfCodexChosen:

            ## KOREN CODEX - CODEX A
            case 1:

                ## CALL MODULE.FUNCTION() #2A - TEXT FILE OPEN
                TextKoren = mod_2A_TextFileOpen_Koren.fn_TextFileOpen(NumberOfTextChosen)

                ## CALL MODULE.FUNCTION() #3A1 - TEXT FILE PREPROCESS - EXTRACT STRINGS (STRING OR TUPLE); ## CALLS MODULE.FUNCTION() #3A2
                ListOfTupleKeysToFix, ListOfWordsInLine = mod_3A1_TextFilePreprocess_Koren_ExtractStrings.fn_ExtractStrings(TextKoren)

                ## CALL MODULE.FUNCTION() #3A3 - TEXT FILE PREPROCESS - FIX KEYS (DOUBLE INSTANCES WITH VERSE SPLIT BETWEEN THE TWO LINES)
                ListOfTupleKeysForKoren = mod_3A3_TextFilePreprocess_Koren_FixKeys.fn_FixKeys(ListOfTupleKeysToFix)

                ## CALL MODULE.FUNCTION() #3A4 - TEXT FILE PREPROCESS - FIX LINES / VERSES (DOUBLE INSTANCES WITH VERSE SPLIT BETWEEN THE TWO LINES)
                DVK = mod_3A4_TextFilePreprocess_Koren_FixLines.fn_FixLines(ListOfTupleKeysForKoren, ListOfWordsInLine)

                ## CALL MODULE.FUNCTION() #3A5 - TEXT FILE PARSE - PARSE ## (Koren DVKH ~ DS Leningrad); (Koren DVKHS ~ DS Leningrad)
                LW4AV, DVKH, DVKHS, VerseCountTotal, WordCountTotal, LetterCountTotal = mod_3A5_TextFileParse_Koren.fn_TextFileParse(DVK)
                
                ## TODO TESTHANDLE LW4AV ABOVE

                ## TODO CREATE MODULE.FUNCTION(): CREATE TUPLE OF ONE INTEGER ONLY FOR SEARCH TEXT CHOSEN
                x = []
                x.append(NumberOfCodexChosen)
                SearchTextChosen = tuple(x)

                ## AFTER CHOICE OF CODEX + PARSING TEXT
                ## THEN SOME INITIAL (AND DERIVATIVE) DATA OBJECTS WILL BE CREATED...

                ## INTEGRATE KOREN DICTIONARIES INTO OJBECTS: D AND DS
                D, DS = DVKH, DVKHS

            ## LENINGRAD CODEX - CODEX B
            case 2:

                ## CALL MODULE.FUNCTION() #2B - TEXT FILE OPEN
                JSON = mod_2B_TextFileOpen_Leningrad.fn_TextFileOpen(NumberOfTextChosen)

                ## CALL MODULE.FUNCTION() #3B - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
                ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = mod_3B_TextFilePreprocess_Leningrad.fn_TextFilePreprocess(JSON)

                ## CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
                ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = mod_4_ConvertJSONStringsToDicts.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)

                ## CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN -  
                SearchTextChosen = mod_5_GetNumberOfTextChosen.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed, NumberOfTextChosen)

                ## CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE(S) CREATE
                ZippedTupleNoSpaces, ZippedTupleWithSpaces = mod_6_ZippedTupleCreate.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)

                ## GET NUMBER OF TEXT CHOSEN
                ## RENAME VARIABLE BECAUSE FUNCTION #5 IS NECESSARY FOR FUNCTION #6 TO RUN
                SearchTextChosen = NumberOfTextChosen ## e.g. 1, 5, 35, 39, 40, 41, 42, 43, 44, 45, 46, 47

                ## AFTER CHOICE OF CODEX + PARSING TEXT
                ## THEN SOME INITIAL (AND DERIVATIVE) DATA OBJECTS WILL BE CREATED...

                ## CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE - RETURNS 1.) DICTIONARY OF VERSES WITH NO SPACES; 2.) DICTIONARY OF VERSES WITH SPACES
                D, DS = mod_7_DictionaryOfVersesCreate.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)

            ## MAM COLLECTION OF MANUSCRIPTS - CODEX C
            case 3:

                ## CALL MODULE.FUNCTION() #2C - TEXT FILE OPEN
                ListOfTuples = mod_2C_TextFileOpen_MAM.fn_TextFileOpen(NumberOfTextChosen)

                ## CALL MODULE.FUNCTION() #3C - TEXT FILE PREPROCESS - EXTRACT KEYS AND VERSES & WORDS; DICT OF VERSES CREATE
                DictOfKeysVersesWithSpaces, DictOfKeysVersesNoSpaces, DictOfListsOfWordsInVerse = mod_3C_TextFilePreprocess_MAM_ExtractStrings.fn_ExtractStrings(ListOfTuples)

                ## INTEGRATE MAM DICTIONARY OF VERSES (NO SPACES) INTO OJBECT: D ## CHANGE VARIABLE NAME
                DVMAM = DictOfListsOfWordsInVerse ## DICT OF VERSES [LIST OF WORDS IN VERSE] FOR MAM ## EQUIVALENT TO DVK OBJECT IN KOREN CODEX

                ## CALL MODULE.FUNCTION() #3CCC - TEXT FILE PARSE - PARSE ## (MAM DVMAM ~ Koren DVKH ~ DS Leningrad)
                LW4AV, DVMAMH, DVMAMHS, VerseCountTotal, WordCountTotal, LetterCountTotal = mod_3CCC_TextFileParse_MAM.fn_TextFileParse(DVMAM)

                ## INTEGRATE MAM DICTIONARY OF VERSES (WITH SPACES) INTO OJBECT: DS ## CHANGE VARIABLE NAME
                DVMAMHS = DictOfKeysVersesWithSpaces

                ## GET NUMBER OF TEXT CHOSEN
                ## RENAME VARIABLE BECAUSE FUNCTION #5 IS NECESSARY FOR FUNCTION #6 TO RUN
                SearchTextChosen = NumberOfTextChosen ## e.g. 1, 5, 35, 39, 40, 41, 42, 43, 44, 45, 46, 47

                ## AFTER CHOICE OF CODEX + PARSING TEXT
                ## THEN SOME INITIAL (AND DERIVATIVE) DATA OBJECTS WILL BE CREATED...

                ## INTEGRATE MAM DICTIONARIES OF VERSES INTO OBJECTS: D AND DS ## CREATE DICTIONARY OF VERSES FOR MAM CODEX
                D, DS = DVMAMH, DVMAMHS

        ## END MATCH CASE - DEAL WITH CHOICE OF CODEX

        ## CREATE DATA OBJECTS + CREATE DICTIONARY OF CUSTOM LETTER OBJECTS (DLO)
        ## CALL MODULE.FUNCTION() #8A - DATA OBJECTS CREATE - RETURNS 1.) STRING OF LETTERS; 2.) LIST OF LETTERS; 3.) DICT OF LETTERS WITH 4-DIGIT TUPLE KEY; 4.) DICT OF LETTERS WITH 5-DIGIT TUPLE KEY; 5.) DICT OF INSTANCES OF LETTER OBJECTS
        S, L, DL, D5, DLO = mod_8A_DataObjectsCreate.fn_DataObjectsCreate(D)

        ## CALL MODULE.FUNCTION() #9AA - CALCULATE LETTER PERCENTAGES
        ListOfTuplesOfLetterStatistics = mod_9AA_CalculateLetterPercentages.fn_CalculatePercentages(S)

        ## CALL MODULE.FUNCTION() #8B - DATA OBJECTS CREATE - RETURNS LIST OF [1.) WORD # IN TEXT; 2.) GEMATRIA VALUES FOR EACH LETTER; 3.) GEMATRIA VALUE FOR ENTIRE WORD]
        LW, LNWEV, DWV, DWT = mod_8B_DataObjectsCreate.fn_DataObjectsCreate(DS) ## RETURNS ListOfWords, ListOfNumbersOfWordsEachVerse, DictionaryOfWordsEachVerse

        ## CALL MODULE.FUNCTION() #8C - DATA OBJECTS CREATE - RETURNS ListOfIndexes4LettersInEachWord
        ListOfIndexes4LettersInEachWord = mod_8C_DataObjectsCreate.fn_DataObjectsCreate(LW)

        ## CALL MODULE.FUNCTION() #8D - DATA OBJECTS CREATE - RETURNS DICT OF D5 KEYS AS VALUES WITH 1-INDEXED KEY FOR # OF LETTERS IN TEXT
        D5K = mod_8D_DataObjectsCreate.fn_DataObjectsCreate(D5)

        ## CALL MODULE.FUNCTION() #8E - DATA OBJECTS CREATE - RETURNS DICT OF DWT KEYS AS VALUES WITH 1-INDEXED KEY FOR # OF WORDS IN TEXT
        DWTK = mod_8E_DataObjectsCreate.fn_DataObjectsCreate(DWT)

        ## CALL MODULE.FUNCTION() #9A - GET NUMBER VALUE FOR LETTERS - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
        N = mod_9A_GetNumberValues4Letters.fn_GetNumberValues(S) ## RETURNS ListOfNumberValues4Letters

        ## UPDATE LETTER OBJECTS
        ## CALL MODULE.FUNCTION() #9AAA - ADD LETTER GEMATRIA NUMBER VALUE TO EACH INSTANCE OF LETTER OBJECT; ## RETURNS DICTIONARY OF LETTER OBJECTS
        DLO = mod_9AAA_AddGematriaNumberValuesToLetterObjects.fn_AddGematriaNumberValuesToLetterObjects(DLO, N)
        
        ###########################################
        ## 1ST TIME MODULE.FUNCTION() #9B IS CALLED
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW = mod_9B_GetNumberValues4Words.fn_GetNumberValues(LW) ## CALLS MODULE.FUNCTION() #9A; ## RETURNS LIST OF TUPLES OF GEMATRIA VALUES FOR ('WORD', [L,E,T,T,E,R,S], SUM)

        ## 1ST TIME MODULE.FUNCTION() #10 IS CALLED
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(D5)

        ## TEST PRINT OUTPUT
        ## print(f"ListOfIndexesCustom {ListOfIndexesCustom}")

        ## 1ST TIME MODULE.FUNCTION() #11A IS CALLED
        ## CALL MODULE.FUNCTION() #11A - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W, DW = mod_11A_TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(LW, NW, ListOfIndexesCustom, ListOfIndexes4LettersInEachWord)

        ## CALL MODULE.FUNCTION() ## 11B - ASSIGN WORD NUMBER TO EACH LETTER OBJECT IN SELECT TEXT
        DLO = mod_11B_AssignWordNumberToEachLetterObject.fn_AssignWordNumberToEachLetterObject(DLO, DW, DWTK) 

        ## BEGIN TEST DEVELOPMENT
        ## CREATE MATCH PER LETTER GEMATRIA NUMBER VALUE
        ## NPA = np.where(NumpyArrayOfNumberValuesOfEntireText==2) ## RETURN TUPLE OF MATCHES FOR LETTER BET ב
        ## ListNPA = NPA[0].tolist() ## CONVERTS NUMPY ARRAY TO PYTHON LIST
        ## END TEST DEVELOPMENT

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
        ## CALL MODULE.FUNCTION() #16A - GET USER INPUT: TYPE OF INPUT FOR SEARCH TERMS
        NumberOfInputType = mod_16A_GetUserInput_TypeOfSearchInput.fn_GetUserInput()

        ## BEGIN MATCH CASE - DEAL WITH CHOICE OF TYPE OF ELS SEARCH TERM INPUT
        match NumberOfInputType:

            ## MANUAL INPUT
            case 1:

                ## DISPLAY IMPORT TYPE
                print("Input Type: Manual by Keyboard")

                ## GET USER INPUT
                ## CALL MODULE.FUNCTION() #16 - GET USER INPUT: NUMBER OF SEARCH TERMS
                NumberOfSearchTerms = mod_16_GetUserInput_NumberOfSearchTerms.fn_GetUserInput()

                ## GET USER INPUT
                ## CALL MODULE.FUNCTION() #17A - GET USER INPUT: INPUT OF SPECIFIED SEARCH TERMS
                ListOfSearchTerms, ListOfSearchTermsWithSpaces, DictOfSearchTerms, DictOfSearchTermsWithSpaces = mod_17A_GetUserInput_ELSSearchTerms.fn_GetUserInput(NumberOfSearchTerms)

            ## IMPORT FROM CSV FILE
            case 2:

                ## DISPLAY IMPORT TYPE
                print("Input Type: CSV Import")

                ## CALL MODULE.FUNCTION() #16AA - GET USER INPUT: FILE NAME FOR CSV IMPORT FOR ELS SEARCH TERMS
                FileNameForCSVImport = mod_16AA_GetUserInput_FileNameForCSVImport_SearchInput.fn_GetUserInput()

                ## CALL MODULE.FUNCTION() #16AAA - EXTRACT ELS SEARCH TERMS FROM CSV FILE: CREATE DATA OBJECT: ListOfSearchTerms
                ListOfSearchTerms, ListOfSearchTermsWithSpaces, NumberOfSearchTerms = mod_16AAA_ReadInputFromFileCSV_ELSSearchTerms.fn_ReadInputFromFile(FileNameForCSVImport)

                ## CALL MODULE.FUNCTION() #16AAAA - CREATE DATA OBJECT: DictOfSearchTerms
                DictOfSearchTerms, DictOfSearchTermsWithSpaces = mod_16AAAA_DataObjectCreate_DictOfSearchTerms.fn_DataObjectsCreate(ListOfSearchTerms, ListOfSearchTermsWithSpaces, NumberOfSearchTerms)

        ## END MATCH CASE - DEAL WITH CHOICE OF TYPE OF ELS SEARCH TERM INPUT

        ## GET USER INPUT
        ## CALL MODULE.FUNCTION() #17B - GET USER INPUT: SKIP DISTANCES MINIMUM / MAXIMUM
        SkipDistanceDMinimum, SkipDistanceDMaximum = mod_17B_GetUserInput_SkipDistancesDMinMax.fn_GetUserInput(NumberOfSearchTerms)

        ## 2ND TIME MODULE.FUNCTION() #9B IS CALLED
        ## CALL MODULE.FUNCTION() #9B - GET NUMBER VALUE FOR WORDS - RETURNS LIST OF TUPLES OF NUMBER VALUES FOR EACH LETTER OF STRING
        NW4ELS = mod_9B_GetNumberValues4Words.fn_GetNumberValues(ListOfSearchTerms) ## CALLS MODULE.FUNCTION() #9A; ## RETURNS LIST OF TUPLES OF GEMATRIA VALUES FOR ('WORD', [L,E,T,T,E,R,S], SUM)

        ## 2ND TIME MODULE.FUNCTION() #10 IS CALLED
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustom = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(ListOfSearchTerms)

        ## 2ND TIME MODULE.FUNCTION() #11 IS CALLED
        ## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
        W4ELS, DW4ELS = mod_11A_TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(ListOfSearchTermsWithSpaces, NW4ELS, ListOfIndexesCustom, ListOfIndexes4LettersInEachWord=[]) ## PASS EMPTY LIST FOR ELSs B/C NO INDEX POSITIONS FOR THESE
        
        ## CALL MODULE.FUNCTION() #18 - ## CREATE NUMPY ARRAY OF NUMBER VALUES
        NPANV = mod_18_NumpyArrayOfNumberValuesCreate.fn_NumpyArrayOfNumberValuesCreate(N) ## RETURNS: NumpyArrayOfNumberValuesOfEntireText

        ## CALL MODULE.FUNCTION() #19 - DATA OBJECT CREATE - RETURNS DICT OF MATCHES FOR EACH FIRST LETTER OF EACH ELS SEARCH TERM
        DictOfMatches4ELS = mod_19_GetMatchesPerIntegerValue.fn_GetMatchesPerIntegerValue(NW4ELS, NPANV)

        ## CREATE ELS OBJECTS - CREATE DICTIONARY OF ELS [USER-SEARCH-TERM] OBJECTS
        ## CALL MODULE.FUNCTION() #20 - DATA OBJECT CREATE - RETURNS DICT OF ELS OBJECTS (DELSO)
        DELSO = mod_20_DictOfELSObjectsCreate.fn_DictOfELSObjectsCreate(DictOfMatches4ELS)

        ## 3RD TIME MODULE.FUNCTION() #10 IS CALLED
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustomL = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(L)

        ## 4TH TIME MODULE.FUNCTION() #10 IS CALLED
        ## CREATE NEW INDEX TO ACCOUNT FOR THE EXTRA SPACES OF LAST LINE IF USER CHOOSES XW/#COLUMNS THAT IS NOT PERFECT FACTOR/DIVISOR
        ## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
        ListOfIndexesCustomLLL = mod_10_ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(LLL)

        #########################################################################################################################
        ## TEST DEVELOPMENT
        ## IF LLL IS LONGER THAN L
        ## THEN USER HAS CHOSEN NON-PERFECT FACTOR/DIVISOR OF LENGTH OF TEXT FOR THE SIZE OF X COLUMNS IN 2D MATRIX;
        ## THEREFORE BLANK SPACES NEED TO BE APPENDED TO THE TEXT STRING TO COMPENSATE FOR NON-PERFECT FACTORS/DIVISORS THAT USER INPUTS

        ## BEGIN IF / ELIF BLOCK
        if LLL > L: ## USER HAS CHOSEN A NON-PERFECT FACTOR/DIVISOR

            ## CALL MODULE.FUNCTION() #41 RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_41_SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, LLL, ListOfIndexesCustomLLL)

        elif LLL == L: ## USER HAS CHOSEN A PERFECT FACTOR/DIVISOR
            
            ## CALL MODULE.FUNCTION() #41 RETURNS LIST OF SERIES OF BOOLEAN MATCHES FOR EACH LETTER IN EACH WORD OF ELS SEARCH TERM WITHIN TEXT
            ListOfPDSeries4ELSs = mod_41_SearchForELSSearchTerms.fn_SearchForELSSearchTerms(ListOfSearchTerms, L, ListOfIndexesCustomL)

        ## END BEGIN IF / ELIF BLOCK
        ########################################################################################################################

        ## CALL MODULE.FUNCTION() #21
        sL0, sL, sLLL0, sLLL, sN0, sN = mod_21_PandasObjectsCreate.fn_PandasObjectsCreate(L, LLL, N, ListOfIndexesCustomL, ListOfIndexesCustomLLL)

        ## CALL MODULE.FUNCTION() #22A
        DELSMLF = mod_22A_ELSSearchByLetterFirst.fn_ELSSearch(sL, sN, DELSO, DLO, SkipDistanceDMinimum, SkipDistanceDMaximum) ## RETURNS DictOfMatches (FIRST LETTER)

        ## FIRST TIME MODULE #22B IS CALLED
        ## EXTRACT NEGATIVES AND POSITIVES ## ALLOWS US TO KEEP ORIGINAL DELSMLF WITH COORDINATES FOR EACH LETTER FIRST (OF ELS) FOR LATER USE
        DELSMLF_POS, DELSMLF_NEG = mod_22B_NegativesAndPositivesExtract.fn_NegativesAndPositivesExtract(DELSMLF)  ## mod_22B_NegativesAndPositivesExtract.fn_NegativesAndPositivesExtract(DELSMLF) 

        ## CALL MODULE.FUNCTION() #23
        DELSMLL = mod_23_ELSSearchByLetterLast.fn_ELSSearch(sL, sN, DELSO, DLO, SkipDistanceDMinimum, SkipDistanceDMaximum) ## RETURNS DictOfMatches (LAST LETTER)

        ## SECOND TIME MODULE #22B IS CALLED
        ## EXTRACT NEGATIVES AND POSITIVES ## ALLOWS US TO KEEP ORIGINAL DELSMLF WITH COORDINATES FOR EACH LETTER LAST (OF ELS) FOR LATER USE
        DELSMLL_POS, DELSMLL_NEG = mod_22B_NegativesAndPositivesExtract.fn_NegativesAndPositivesExtract(DELSMLL) ## mod_22B_NegativesAndPositivesExtract.fn_NegativesAndPositivesExtract(DELSMLL) 

        ## UPDATE ELSO OBJECTS
        ## CALL MODULE.FUNCTION() #24
        DELSO = mod_24_AddSearchResultsToDELSO.fn_AddSearchResultsToDELSO(DELSO, DELSMLF_POS, DELSMLF_NEG, DELSMLL_POS, DELSMLL_NEG)

        ## UPDATE W4ELS OBJECT
        ## CALL MODULE.FUNCTION() #25
        W4ELS = mod_25_UpdateW4ELS.fn_UpdateW4ELS(W4ELS, DELSO)

        ## UPDATE W OBJECT
        ## CALL MODULE.FUNCTION() #26
        W = mod_26_UpdateW.fn_UpdateW(W, DWTK)

        ## 1ST TIME MODULE.FUNCTION() #27 IS CALLED
        ## CALL MODULE.FUNCTION() #27
        LTM4ELS_LF_POS, DLO, DELSO = mod_27_GatherData4ELSMatches.fn_GatherData4ELSMatches(DictOfSearchTerms, DictOfSearchTermsWithSpaces, DLO, DW, DW4ELS, DELSO, DELSMLF_POS, DS) ## EXTRACT MATCHES POSITIVE
        
        ## 2ND TIME MODULE.FUNCTION() #27 IS CALLED
        ## CALL MODULE.FUNCTION() #27
        LTM4ELS_LF_NEG, DLO, DELSO = mod_27_GatherData4ELSMatches.fn_GatherData4ELSMatches(DictOfSearchTerms, DictOfSearchTermsWithSpaces, DLO, DW, DW4ELS, DELSO, DELSMLF_NEG, DS) ## EXTRACT MATCHES NEGATIVE

        ## 3RD TIME MODULE.FUNCTION() #27 IS CALLED
        ## CALL MODULE.FUNCTION() #27
        LTM4ELS_LL_POS, DLO, DELSO = mod_27_GatherData4ELSMatches.fn_GatherData4ELSMatches(DictOfSearchTerms, DictOfSearchTermsWithSpaces, DLO, DW, DW4ELS, DELSO, DELSMLL_POS, DS) ## EXTRACT MATCHES POSITIVE
        
        ## 4TH TIME MODULE.FUNCTION() #27 IS CALLED
        ## CALL MODULE.FUNCTION() #27
        LTM4ELS_LL_NEG, DLO, DELSO = mod_27_GatherData4ELSMatches.fn_GatherData4ELSMatches(DictOfSearchTerms, DictOfSearchTermsWithSpaces, DLO, DW, DW4ELS, DELSO, DELSMLL_NEG, DS) ## EXTRACT MATCHES NEGATIVE

        ## BEGIN POSITIVE ELS MATCHES
        ## 1ST TIME MODULE.FUNCTION() #28 IS CALLED
        ## CALL MODULE.FUNCTION() #28
        MasterList4LetterPositions_POS, DLO = mod_28_ExtractAllELSLetterPositions.fn_ExtractAllELSLetterPositions(LTM4ELS_LF_POS, DLO, DW, DS) ## RETURNS:

        ## END POSITIVE ELS MATCHES

        ## BEGIN NEGATIVE ELS MATCHES
        ## 2ND TIME MODULE.FUNCTION() #28 IS CALLED
        ## CALL MODULE.FUNCTION() #28
        MasterList4LetterPositions_NEG, DLO = mod_28_ExtractAllELSLetterPositions.fn_ExtractAllELSLetterPositions(LTM4ELS_LF_NEG, DLO, DW, DS) ## RETURNS:
    
        ## END NEGATIVE ELS MATCHES

        ## BEGIN TEST DEVELOPMENT

        #########################################################################################################################
        ## TEST DEVELOPMENT
        ## TEST FOR TEXT STRING
        ## CALL MODULE.FUNCTION() #40 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)
        ListOfRegex4TextString = mod_40_ConvertELSQueryToRegex.fn_ConvertELSQueryToRegex(L) ## RETURNS LIST OF LISTS OF LETTERS

        ## TEST FOR ELS TERMS
        ## CALL MODULE.FUNCTION() #40 - CONVERT EACH LETTER IN ELS SEARCH QUERY TO REGULAR EXPRESSIONS (REGEX)
        ListOfRegex4ELSSearchTerms = mod_40_ConvertELSQueryToRegex.fn_ConvertELSQueryToRegex(ListOfSearchTerms) ## RETURNS LIST OF LISTS OF LETTERS
        #########################################################################################################################

        ## END TEST DEVELOPMENT

        ## TEST CREATE 2D MATRIX HERE OR MOVE BELOW TO MODULES FOR FINAL STEPS(?)
        ## CALL MODULE.FUNCTION() #99 - 2D MATRIX CREATE FOR OUTPUT
        ListOfRowsOfLetters = mod_99_Matrix2DOfLettersCreate.fn_Matrix2DOfLettersCreate(SSS, YH, XW, D5K) 

        ## MODULES FOR FINAL STEPS OF PROGRAM TO OUTPUT DATA AS CSV FILES

        ## CALL MODULE.FUNCTION() #98 - FILE NAMES CREATE
        FileNameForMatrixXLSX, FileNameForMatrixCSV, FileNameForLetterStatistics, FileNameForGematriaTexts, FileNameForELSMatchesDataSummary, FileNameForELSMatchesByLetterFirstPositive, FileNameForELSMatchesByLetterFirstNegative, FileNameForELSMatchesByLetterLastPositive, FileNameForELSMatchesByLetterLastNegative = mod_98_FileNamesCreate.fn_FileNamesCreate(XW, YH, NumberOfTextChosen, NumberOfCodexChosen)
       
        ## CALL MODULE.FUNCTION() #98 - FILE NAMES CREATE POSITIVE
        FileNamesForELSTerms_POS, Dict4FileNames4ELSTerms_POS = mod_98_FileNamesCreate4ELSTerms_POS.fn_FileNamesCreate(XW, YH, NumberOfCodexChosen, NumberOfTextChosen, W4ELS, DELSO)
    
        ## CALL MODULE.FUNCTION() #98 - FILE NAMES CREATE NEGATIVE
        FileNamesForELSTerms_NEG, Dict4FileNames4ELSTerms_NEG = mod_98_FileNamesCreate4ELSTerms_NEG.fn_FileNamesCreate(XW, YH, NumberOfCodexChosen, NumberOfTextChosen, W4ELS, DELSO)
   
        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV 
        _ = mod_99_WriteOutputToFileCSV_LetterStatistics.fn_WriteOutputToFile(ListOfTuplesOfLetterStatistics, FileNameForLetterStatistics)
        
        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE 2D MATRIX
        _ = mod_99_WriteOutputToFileCSV_2DMatrix.fn_WriteOutputToFile(ListOfRowsOfLetters, FileNameForMatrixCSV)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF SELECTED TEXT(S) WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99_WriteOutputToFileCSV_WordsAndGematriaValues.fn_WriteOutputToFile(W, FileNameForGematriaTexts)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF ELSs WITH EACH WORD'S GEMATRIA VALUE
        _ = mod_99_WriteOutputToFileCSV_ELSMatches_DATASUMMARY.fn_WriteOutputToFile(W4ELS, FileNameForELSMatchesDataSummary)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL MATCHES OF ELS WITH POSITIVE SKIPDISTANCES (d) BY FIRST LETTER
        _ = mod_99_WriteOutputToFileCSV_ELSMatches.fn_WriteOutputToFile(LTM4ELS_LF_POS, FileNameForELSMatchesByLetterFirstPositive)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL MATCHES OF ELS WITH NEGATIVE SKIPDISTANCES (d) BY FIRST LETTER
        _ = mod_99_WriteOutputToFileCSV_ELSMatches.fn_WriteOutputToFile(LTM4ELS_LF_NEG, FileNameForELSMatchesByLetterFirstNegative)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL MATCHES OF ELS WITH POSITIVE SKIPDISTANCES (d) BY LAST LETTER
        _ = mod_99_WriteOutputToFileCSV_ELSMatches.fn_WriteOutputToFile(LTM4ELS_LL_POS, FileNameForELSMatchesByLetterLastPositive)

        ## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL MATCHES OF ELS WITH NEGATIVE SKIPDISTANCES (d) BY LAST LETTER
        _ = mod_99_WriteOutputToFileCSV_ELSMatches.fn_WriteOutputToFile(LTM4ELS_LL_NEG, FileNameForELSMatchesByLetterLastNegative)

        ## 1ST TIME MODULE.FUNCTION() #99 IS CALLED
        ## CALL MODULE.FUNCTION() #99 : WRITE OUTPUT OF EACH INDIVIDUAL ELS DATA: POSITIVE ELS MATCHES
        _ = mod_99_IterateOutput4ELSMatches.fn_IterateOutput4ELSMatches(MasterList4LetterPositions_POS, Dict4FileNames4ELSTerms_POS)

        ## 2ND TIME MODULE.FUNCTION() #99 IS CALLED
        ## CALL MODULE.FUNCTION() #99 : WRITE OUTPUT OF EACH INDIVIDUAL ELS DATA: NEGATIVE ELS MATCHES
        _ = mod_99_IterateOutput4ELSMatches.fn_IterateOutput4ELSMatches(MasterList4LetterPositions_NEG, Dict4FileNames4ELSTerms_NEG)

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

    ## BEGIN TEST DEVELOPMENT
    ## BEGIN TEST CODE BELOW THIS POINT

    ## END CALL MODULES.FUNCTIONS()
                    
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

    gso.NPANV = NPANV ## 0-BASED INDEX POSITIONS

    ## END GSO

    ## END TEST CODE BELOW THIS POINT
    ## END TEST DEVELOPMENT

## END WHILE LOOP FOR INFINITE GAME WHILE LOOP

## TEST PRINT OUTPUT
print("\n")  ## PRINT SPACE
print(f"Length of List of Letters of Selected Text : {len(S)}") ## VALUE OF L GETS CHANGED TO VALUE OF LLL - CHECK WHERE
print(f"Length of List of SPACES of 2D MATRIX CSV FILE : {len(LLL)}")

## TEST PRINT OUTPUT
print("\n")  ## PRINT SPACE
## print(f"ListOfSearchTerms : {ListOfSearchTerms}")
## print(f"DictOfSearchTerms : {DictOfSearchTerms}")
print(f"Length of Dictionary : {len(DictOfSearchTerms)}")

## TEST DEVELOPMENT

## TEST CLASS OBJECT
        
## print("TEST gso")
## print(f"TEST gso : {gso.SearchTextChosen}")
## print(f"TEST gso : {gso.LengthOfTextToSearch}")
## print(f"TEST gso : {gso.ListOfSearchTerms}")
## print(f"TEST gso : {gso.DictOfSearchTerms}")

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
