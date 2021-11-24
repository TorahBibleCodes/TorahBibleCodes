import argparse
import os
import sys
import subprocess
import shlex
import pandas as pd
import mod_1GetUserInput1 ## MODULE.FUNCTION() #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
import mod_2TextFileOpen ## MODULE.FUNCTION() #2 - TEXT FILE OPEN
import mod_3ATextFilePreprocess ## MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
import mod_4ConvertJSONStringsToDicts ## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS
import mod_5GetNumberOfTextChosen ## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
import mod_6ZippedTupleCreate ## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME)
import mod_7DictionaryOfVersesCreate ## MODULE.FUNCTION #7 - CREATE DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED
import mod_8DataObjectsCreate ## MODULE.FUNCTION #8 - DATA OBJECTS CREATE; RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS, 5.) LIST OF WORDS
import mod_9GetNumberValues ## MODULE.FUNCTION #9 - GET NUMBER VALUE OF EACH LETTER IN STRING
import mod_10ListOfIndexesCustomCreate ## MODULE.FUNCTION() #10 - CREATE LIST OF CUSTOM INDEXES NON-0-INDEXED / 1-INDEXED RETURNS LIST OF CUSTOM INDEXES
import mod_11TupleOfWordsAndGematriaValuesCreate ## MODULE.FUNCTION() #11 - DATA OBJECT CREATE - RETURNS TUPLE OF WORDS WITH EACH WORD'S GEMATRIA NUMBER VALUE
import mod_99WriteOutputToCSVFile_WordsAndGematriaValues ## MODULE.FUNCTION() #99 - 



#import p_els
from googletrans import Translator
#from translate import Translator
## search query

import re




def reload():

	global TextChosen, D, DL ,DS, S, N, NW, W,D5, OP
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

## CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
TextChosen = 1
reload()

def file(options):
	global TextChosen
	TextChosen = mod_1GetUserInput1.fn_GetUserInput1()
	reload()
def search(options):
	exp = options[0]
	print(exp)
	#print(D)
	for (z,b,y) in D:
		m = re.search(exp, D[z,b,y])
		#print (D[z,b,y])
		try:
			print(m.group(0))
			print(D[z,b,y])
		except:
			pass



def get_space(options):
	pattern = options[0]
	srun = options[1]
	plist = [char for char in pattern]
	#for a in plist:
	#    get_space([]

	print (plist)

def elsf(options):
	space = options[1]
	i=1
	rese=""
	for (z,b,y) in D:
		#m = re.search(exp, D[z,b,y])
		#print (D[z,b,y])
		try:
		 #   print(m.group(0))
			#print(D[z,b,y])
			res=""
			for char in D[z,b,y]:
				if (i % int(space)) == 0:
					res=(char)+res

				i=i+1
			rese=rese+" "+res
			#print(res)
		except:
			pass




def els(options):
	space = options[1]
	i=1
	rese=""
	for (z,b,y) in D:
		#m = re.search(exp, D[z,b,y])
		#print (D[z,b,y])
		try:
		 #   print(m.group(0))
			#print(D[z,b,y])
			res=""
			for char in D[z,b,y]:
				if (i % int(space)) == 0:
					res=(char)+res

				i=i+1
			rese=rese+" "+res
			#print(res)
		except:
			pass

	print (rese.strip())
	print('======')
	translator = Translator()
	result = translator.translate(rese.strip(),dest='en')
	#translator= Translator(to_lang="en")
	#translation = translator.translate("casa")
	print(result.text)
	print('======')
# get data from letters
def tonum(options):
	ListOfLetters = options[0].split(",")

	print (mod_9GetNumberValues.fn_GetNumberValues(ListOfLetters,ListOfLetters))


## get data from loaded dictionary
def get(options):
	a = options[0]
	b = options[1]
	c = options[2]
	print(D[int(a),int(b),int(c)])


def coreOptions():
	options = [["query", "query db ", "El"], ["modelist", "(simple, full) ", "full"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["els","els words space"],["file","set file"],["search","search termsexp"],["get","get book verse number"],["tonum","tonum (sentence or word)"],["toword","toword \"1,2,3,4,5\""],["get_space","get_spaces sentence"]]
	return commands




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	
