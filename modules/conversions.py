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

tracert = 'false'
langin = 'en'
langout = 'es'
ptrans = 'true'
threads = 0
totalvalue = 0
jobs = Queue()


def searchAll(q, number):
	global langout, ptrans, totalvalue, tracert
	#if not q.empty():
	#print('init '+ str(number))
	while not q.empty():
		try:
			value = q.get()
			ret, tvalue = torah.func_GettextFromNumber(value,number, tracert=tracert)
			#ret = ret.replace('\n', '')
			ret2 = re.sub('\s+', ' ', ret)
			totalvalue = totalvalue + tvalue

			rett = torah.func_translate('iw', langout, ret2)
			retp = torah.func_ParseTranslation(rett,langout, ptrans)
			if not retp == 0:
				#print(ret)
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

	#for i in range(40,41):
	for i in range(1,44):
		#print(i)
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, sed,))
		worker.start()

	poolsize = 43 - int(jobs.qsize())
	print("waiting for ", str(poolsize)+'/43', "tasks")

	jobs.join()
	#print('total', totalvalue)
	print("all done")


def searchnumber(options):
	global jobs, langin, langout, threads
	number = options[0]

	for i in range(1,44):
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, number,))
		worker.start()

	poolsize = int(jobs.qsize())
	print("waiting for ", str(poolsize)+'/43', "tasks")

	jobs.join()
	#print("all done")

def xgboost(options):
	print('Coming soon')

def probnet(options):
	print('Coming soon')

def coreOptions():
	options = [["langin", "Translation Lang  In", "en"],["langout", "Translation Lang  Out", "es"],["threads", "Number of threads from search", "40"],["parse", "parse translation", "true"],["tracert", "Tracert Search", "false"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["searchnumber","search number space"],["search","search termsexp"],["xgboost"," XGBOOST"],["probnet","PROBNET"]]
	return commands


def core(moduleOptions):
	print('Command run disabled on current module')

def save(moduleOptions):
	global langin, langout, threads, ptrans, tracert
	langin = moduleOptions[0][2]
	langout = moduleOptions[1][2]
	threads = moduleOptions[2][2]
	ptrans = moduleOptions[3][2]
	tracert = moduleOptions[4][2]