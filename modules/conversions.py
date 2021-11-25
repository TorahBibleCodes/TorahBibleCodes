import argparse
import os
import sys
import subprocess
import shlex
import pandas as pd
import resources.func.functions as torah
from deep_translator import GoogleTranslator
import re


def file(options):
	global TextChosen
	TextChosen = torah.mod_1GetUserInput1.fn_GetUserInput1()
	reload()
def search2(options):
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


def tt(options):
	listform = ''
	for string in options:
		listform = listform +string
	#ListOfLetters = options[0].split(",")
	mod_num = torah.mod_9GetNumberValues.fn_GetNumberValues(listform,options)
	#print (mod_num)

	sed = [0, mod_num[1][0]]
	els(sed)

def searchAll(file, number):

	ret = torah.func_GettextFromNumber(file,number)
	rett = torah.func_translate('iw', 'en', ret)
	retp = torah.func_ParseTranslation(rett,'en')
	if not retp == 0:
		print(retp)

def search(options):
	listform = ''

	for string in options:
		translated = torah.func_translate('en', 'iw', string)
		listform = listform +translated
	mod_num = torah.mod_9GetNumberValues.fn_GetNumberValues(listform,options)

	sed = mod_num[1][0]
	for i in range(1,43):
		searchAll(i, sed)



def searchnumber(options):
	number = options[0]
	ret = torah.func_GettextFromNumber(1,number)
	rett = torah.func_translate('iw', 'en', ret)
	rett = torah.func_ParseTranslation(rett,'en')
	print(rett)


def tonum(options):
	listform = ''
	for string in options:
		listform = listform +string
	#ListOfLetters = options[0].split(",")

	print (torah.mod_9GetNumberValues.fn_GetNumberValues(listform,options))


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
	commands = [["tte","els words space"],["tt","els words space"],["searchnumber","search number space"],["elsa","els words space"],["file","set file"],["search","search termsexp"],["get","get book verse number"],["tonum","tonum (sentence or word)"],["toword","toword \"1,2,3,4,5\""],["get_space","get_spaces sentence"]]
	return commands




def core(moduleOptions):

	query = moduleOptions[0][2]
	modelist = moduleOptions[1][2]
	
