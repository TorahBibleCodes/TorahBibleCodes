## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import pandas as pd
from deep_translator import GoogleTranslator
#import mod_1GetUserInput1 ## MODULE.FUNCTION() #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
import resources.func.mod_2TextFileOpen as mod_2TextFileOpen ## MODULE.FUNCTION() #2 - TEXT FILE OPEN
import resources.func.mod_3ATextFilePreprocess as mod_3ATextFilePreprocess## MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
import resources.func.mod_4ConvertJSONStringsToDicts as mod_4ConvertJSONStringsToDicts## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS
import resources.func.mod_5GetNumberOfTextChosen as mod_5GetNumberOfTextChosen## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
import resources.func.mod_6ZippedTupleCreate as mod_6ZippedTupleCreate## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME)
import resources.func.mod_7DictionaryOfVersesCreate as mod_7DictionaryOfVersesCreate## MODULE.FUNCTION #7 - CREATE DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED
import resources.func.mod_8DataObjectsCreate as mod_8DataObjectsCreate## MODULE.FUNCTION #8 - DATA OBJECTS CREATE; RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS, 5.) LIST OF WORDS
import resources.func.mod_9GetNumberValues as mod_9GetNumberValues## MODULE.FUNCTION #9 - GET NUMBER VALUE OF EACH LETTER IN STRING
import resources.func.mod_10ListOfIndexesCustomCreate as mod_10ListOfIndexesCustomCreate## MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
import resources.func.mod_11TupleOfWordsAndGematriaValuesCreate as mod_11TupleOfWordsAndGematriaValuesCreate## MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
import resources.func.mod_99WriteOutputToCSVFile_WordsAndGematriaValues as mod_99WriteOutputToCSVFile_WordsAndGematriaValues## MODULE.FUNCTION() #99 - 
#import mod_GetUserInput2 ## MODULE.FUNCTION() # - GET USER INPUT; INPUT ELS SEARCH TERM
from textblob import TextBlob

## DECLARE VARIABLES
## DECLARE VARIABLES
## DECLARE VARIABLES

## n = START POSITION OF ELS IN STRING/LIST/DICTIONARY

## d = LENGTH OF SKIP BETWEEN LETTERS IN ELS

## k = LENGTH OF ELS: i.e. SEARCH TERM // USER INPUT 2

def func_checklang(word, lang):
	return True

	b = TextBlob(word)
	
	try:
		b.detect_language()
		if (b.detect_language() == lang):
			return True
	except:
		return True
	return False


def func_checklang2(word, lang):
	return True
	for language in Detector(word).languages:
		print('sss: ' +word)
		if language.code == lang:
			print('found: ' +word)
			return True
	print('not found: ' +word)
	return False

def func_translate(lang_in, lang_out, data):
	translated = GoogleTranslator(source=lang_in, target=lang_out).translate(data.strip()) 
	return translated


def func_ParseTranslation(translated, lang):
	abd = 'abcdefghijklmnñopqrstuvwxyz'
	str_split = translated.split(' ')
	str_final = ''
	for word in str_split:
		try:
			if word[0].lower() in abd:
				if func_checklang(word, lang) == True:
					str_final = str_final+ word+' '
		except:
			pass
	
	if not str_final == '':
		return str_final
	else:
		return 0

def func_GettextFromNumber(torahNumber, number):

	## CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
	TextChosen = torahNumber #mod_1GetUserInput1.fn_GetUserInput1()

	## CALL MODULE.FUNCTION() #2 - TEXT FILE OPEN
	JSON = mod_2TextFileOpen.fn_TextFileOpen(TextChosen)

	## CALL MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
	ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = mod_3ATextFilePreprocess.fn_TextFilePreprocess(JSON)

	## CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
	ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = mod_4ConvertJSONStringsToDicts.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)

	## CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
	SearchTextChosen = mod_5GetNumberOfTextChosen.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)

	## CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE(S) CREATE
	ZippedTupleNoSpaces, ZippedTupleWithSpaces = mod_6ZippedTupleCreate.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)

	## CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE
	D, DS = mod_7DictionaryOfVersesCreate.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)

	## CALL MODULE.FUNCTION() #8 - DATA OBJECTS CREATE - RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS
	S, L, DL, D5, ListOfWords = mod_8DataObjectsCreate.fn_DataObjectsCreate(D, DS)

	## CALL MODULE.FUNCTION() #9 - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
	N, NW = mod_9GetNumberValues.fn_GetNumberValues(S, ListOfWords) ## TEST FOR OA - LIST OF WORDS

	## CALL MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
	ListOfIndexesCustom = mod_10ListOfIndexesCustomCreate.fn_ListOfIndexesCustomCreate(D5)

	## CALL MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
	W = mod_11TupleOfWordsAndGematriaValuesCreate.fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW)

	## CALL MODULE.FUNCTION() # - GET USER INPUT 2 - INPUT TEXT EQUIDISTANT LETTER SEQUENCES (ELS = K) TO SEARCH
	# UserInput2 = mod_GetUserInput2.fn_GetUserInput2()

	## CALL MODULE.FUNCTION() #99 = OUTPUT/WRITE TO CSV FILE ALL WORDS OF SELECTED TEXT(S) WITH EACH WORD'S GEMATRIA VALUE
	OP = mod_99WriteOutputToCSVFile_WordsAndGematriaValues.fn_WriteOutputToCSVFile_WordsAndGematriaValues(W)

	space = number
	abd = 'abcdefghijklmnñopqrstuvwxyz'
	i=1
	rese=""
	for (z,b,y) in D:
		try:
			res=""
			for char in D[z,b,y]:
				if (i % int(space)) == 0:
					res=(char)+res

				i=i+1
			rese=rese+" "+res
		except:
			pass
	return rese.strip()