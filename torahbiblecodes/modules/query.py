
import argparse
import os
import sys

import torahbiblecodes.resources.func.db as db


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange

global lang


db.createtable()


def TextOfBook(query):

		ret = db.getTextOfBook(query)
		if len(ret) !=0:
				for dbitem in ret:
						#print(dbitem[3]+'\n')
						print(ORANGE +'ES: ==> GE:'+str(dbitem[1])+' ==> '+str(dbitem[3]) + END)
						print(GREEN +'EN: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[4]) + END)
						print(BLUE +'HE: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[2]) + END)


def TextOfES(query):

		ret = db.getTextOfES(query)
		if len(ret) !=0:
				for dbitem in ret:
						#print(dbitem[3]+'\n')
						print(YELLOW +'BOOK: ==> '+str(dbitem[5]) + END)
						print(ORANGE +'ES: ==> GE:'+str(dbitem[1])+' ==> '+str(dbitem[3]) + END)
						print(GREEN +'EN: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[4]) + END)
						print(BLUE +'HE: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[2]) + END)

def TextOfEN(query):

		ret = db.getTextOfEN(query)
		if len(ret) !=0:
				for dbitem in ret:
						#print(dbitem[3]+'\n')
						print(YELLOW +'BOOK: ==> '+str(dbitem[5]) + END)
						print(ORANGE +'ES: ==> GE:'+str(dbitem[1])+' ==> '+str(dbitem[3]) + END)
						print(GREEN +'EN: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[4]) + END)
						print(BLUE +'HE: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[2]) + END)


def TextOfESMAKE():
		global lang
		ret = db.getTextOfES(' ')
		if len(ret) !=0:
				for dbitem in ret:
						#print(dbitem[3]+'\n')
						#print(YELLOW +'BOOK: ==> '+str(dbitem[5]) + END)
						if lang == 'en':
							print(ORANGE +str(dbitem[4])+'\n' + END)
						else:
							print(ORANGE +str(dbitem[3])+'\n' + END)
						#print(GREEN +'EN: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[4]) + END)
						#print(BLUE +'HE: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[2]) + END)


def book(op):
	TextOfBook(op[0])


def make(op):
	TextOfESMAKE()


def search(op):
	global lang
	e = ' '.join(op)
	if lang == 'es':
		TextOfES(e)
	elif lang == 'en':
		TextOfEN(e)


def coreOptions():
	options = [["lang", "lang to search", "es"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["book","search in book torah. example (book text_11IIkings)"],["search","example search 'no es raro que'"],["make","print all results"]]
	return commands


def core(moduleOptions):
	print('Command run disabled on current module')

def save(moduleOptions):
	global lang
	lang = moduleOptions[0][2]
