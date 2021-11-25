import argparse
import os
import sys
import subprocess
import shlex
import pandas as pd
import threading, time
from queue import Queue
import resources.func.functions as torah
from deep_translator import GoogleTranslator
import re

langin = 'en'
langout = 'es'
ptrans = True
threads = 0
jobs = Queue()

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


def searchAll(q, number):
	global langout, ptrans
	#if not q.empty():
	#print('init '+ str(number))
	while not q.empty():
		try:
			value = q.get()
			ret = torah.func_GettextFromNumber(value,number)
			rett = torah.func_translate('iw', langout, ret)
			retp = torah.func_ParseTranslation(rett,langout, ptrans)
			if not retp == 0:
				print(retp)
				q.task_done()
			else:
				q.task_done()
		except:
			q.task_done()
			pass

def search(options):
	global jobs, langin, langout, threads
	listform = ''

	for string in options:
		translated = torah.func_translate(langin, 'iw', string)
		listform = listform +translated
	mod_num = torah.mod_9GetNumberValues.fn_GetNumberValues(listform,options)

	sed = mod_num[1][0]

	for i in range(1,43):
	    jobs.put(i)

	for i in range(int(threads)):
	    worker = threading.Thread(target=searchAll, args=(jobs, sed,))
	    worker.start()

	print("waiting for ", str(jobs.qsize())+'/43', "tasks")
	jobs.join()
	#print("all done")


def searchnumber(options):
	global jobs, langin, langout, threads
	number = options[0]

	for i in range(1,43):
	    jobs.put(i)

	for i in range(int(threads)):
	    worker = threading.Thread(target=searchAll, args=(jobs, number,))
	    worker.start()

	print("waiting for ", str(jobs.qsize())+'/43', "tasks")
	jobs.join()
	#print("all done")


def searchnumber2(options):
	global langout
	number = options[0]
	ret = torah.func_GettextFromNumber(1,number)
	print(len(ret))
	rett = torah.func_translate('iw', langout, ret)
	rett = torah.func_ParseTranslation(rett,langout)
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
	options = [["langin", "Translation Lang  In", "en"],["langout", "Translation Lang  Out", "es"],["query", "query db ", "El"], ["modelist", "(simple, full) ", "full"],["threads", "Number of threads from search", "20"],["parse", "parse translation", "true"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["tte","els words space"],["tt","els words space"],["searchnumber","search number space"],["elsa","els words space"],["select","select file"],["search","search termsexp"],["get","get book verse number"],["tonum","tonum (sentence or word)"],["toword","toword \"1,2,3,4,5\""],["get_space","get_spaces sentence"]]
	return commands


def core(moduleOptions):
	global langin, langout, threads, ptrans
	langin = moduleOptions[0][2]
	langout = moduleOptions[1][2]
	query = moduleOptions[2][2]
	modelist = moduleOptions[3][2]
	threads = moduleOptions[4][2]
	ptrans = moduleOptions[5][2]

	print('Command run disabled on current module')

def save(moduleOptions):
	global langin, langout, threads, ptrans
	langin = moduleOptions[0][2]
	langout = moduleOptions[1][2]
	query = moduleOptions[2][2]
	modelist = moduleOptions[3][2]
	threads = moduleOptions[4][2]
	ptrans = moduleOptions[5][2]