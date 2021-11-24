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
from console_progressbar import ProgressBar
from deep_translator import GoogleTranslator

#import p_els
#from googletrans import Translator
#from translate import Translator
## search query

import re




def reload():

	global TextChosen, D, DL ,DS, S, N, NW, W,D5, OP, SearchTextChosen, ListOfWords, L, ZippedTupleWithSpaces
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

def elsa(options):
	global TextChosen
	space = options[1]
	#pb = ProgressBar(total=100,prefix='Loading', suffix='', decimals=3, length=50, fill='|', zfill='-')

	#for space in range(140,500):

	abd = 'abcdefghijklmnñopqrstuvwxyz'
	array_final = []
	try:
		for ff in range(1, 43):
			#pb.print_progress_bar(pbc)
			#pbc = pbc + 2.32
			TextChosen = ff
			reload()
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

			#print (rese.strip())
			#print('======')
			#translator = Translator()
			#result = translator.translate(rese.strip(),dest='en')
			translated = GoogleTranslator(source='iw', target='es').translate(rese.strip()) 
			#translator= Translator(to_lang="en")
			#translation = translator.translate("casa")
			str_split = translated.split(' ')
			str_final = ''
			for word in str_split:
				try:
					if word[0].lower() in abd:
						#print(word+' ')
						str_final = str_final+ word+' '
				except:
					pass
			
			if not str_final == '':
				#array_final.append(str_final)
				print(str_final)
				print()
			#print('======')
		#print(array_final)
		#pb.print_progress_bar(100)
		#for pf in array_final:
		#	print(pf)
	except:
		pass
def tt(options):
	listform = ''
	for string in options:
		listform = listform +string
	#ListOfLetters = options[0].split(",")
	mod_num = mod_9GetNumberValues.fn_GetNumberValues(listform,options)
	#print (mod_num)

	sed = [0, mod_num[1][0]]
	els(sed)
def tte(options):
	listform = ''

	for string in options:
		translated = GoogleTranslator(source='en', target='iw').translate(string) 
		listform = listform +translated
	#ListOfLetters = options[0].split(",")
	mod_num = mod_9GetNumberValues.fn_GetNumberValues(listform,options)
	#print (mod_num)

	sed = [0, mod_num[1][0]]
	elsa(sed)
def els(options):
	space = options[1]
	#print(space)
	abd = 'abcdefghijklmnñopqrstuvwxyz'
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
	#translator = Translator()
	#result = translator.translate(rese.strip(),dest='en')
	#translator= Translator(to_lang="en")
	#translation = translator.translate("casa")
	translated = GoogleTranslator(source='iw', target='es').translate(rese.strip()) 

	str_split = translated.split(' ')
	str_final = ''
	for word in str_split:
		try:
			if word[0].lower() in abd:
				#print(word+' ')
				str_final = str_final+ word+' '
		except:
			pass
	
	if not str_final == '':
		#array_final.append(str_final)
		print(str_final)
		print()
	#print(translated)
	#print('======')
# get data from letters
def tonum(options):
	listform = ''
	for string in options:
		listform = listform +string
	#ListOfLetters = options[0].split(",")

	print (mod_9GetNumberValues.fn_GetNumberValues(listform,options))


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
	commands = [["tte","els words space"],["tt","els words space"],["els","els words space"],["elsa","els words space"],["file","set file"],["search","search termsexp"],["get","get book verse number"],["tonum","tonum (sentence or word)"],["toword","toword \"1,2,3,4,5\""],["get_space","get_spaces sentence"]]
	return commands




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	
