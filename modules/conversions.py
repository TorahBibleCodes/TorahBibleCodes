import argparse
import os
import sys
import subprocess
import shlex
import pandas as pd
import threading, time
from queue import Queue
from resources.func.torah import *
import modules.resources.xgboost as xgb
from deep_translator import GoogleTranslator
import re

tracert = 'false'
langin = 'en'
langout = 'es'
ptrans = 'true'
threads = 0
totalvalue = 0
totalresult = 0

torah = Torah()

books.load()

def tt(options):
	global langin, langout, threads, totalresult
	listform = ''
	#totalresult = 0
	#jobs = Queue()
	#for string in options:
	#	translated = torah.func_translate(langin, 'iw', string)
	#	listform = listform +translated
	#mod_num = torah.func_getnumber(listform,options)

	#sed = mod_num[1][0]
	#print(mod_num)
	#print(sed)
	#ret = gematria_to_int(translated)
	#print(ret)
	#xgb.predict(mod_num[0])

def searchAll(q, number):
	global langout, ptrans, totalvalue, tracert, totalresult
	while not q.empty():
		try:
			value = q.get()
			
			ret, tvalue = torah.els(value, number, tracert=tracert)
			totalvalue = totalvalue + tvalue

			rett = torah.func_translate('iw', langout, ret)
			retp = torah.func_ParseTranslation(rett,langout, ptrans)
			if not retp == 0:
				#print(ret)
				totalresult = totalresult+1
				print('\nBook:',value)
				print(retp)
				
				q.task_done()
			else:
				q.task_done()
		except Exception as e:
			q.task_done()
			#print(e)
			pass

def search(options):
	global langin, langout, threads, totalresult
	listform = ''
	totalresult = 0
	jobs = Queue()

	if len(options) > 1:
		for string in options:
			listform = listform+' '+string
		if langin == 'iw':
			sed = torah.gematria_iw_int(listform)
		else:
			sed = torah.gematrix(listform)
	else:

		if langin == 'iw':
			sed = torah.gematria_iw_int(listform)
		else:
			sed = torah.gematria(options[0])

	for i in books.booklist():
		#print(i)
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, sed,))
		worker.start()

	poolsize = 39 - int(jobs.qsize())
	pooltotal = 39
	print("waiting for ", str(poolsize)+'/'+str(pooltotal), "tasks")

	jobs.join()
	#print('total', totalvalue)
	print('\nFound', totalresult, 'Results')
	print("all done")


def searchnumber(options):
	global langin, langout, threads, totalresult
	number = options[0]
	#threads = 1
	totalresult = 0
	jobs = Queue()
	for i in books.booklist():
		#print(i)
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, number,))
		worker.start()

	poolsize = 39 - int(jobs.qsize())
	pooltotal = 39
	print("waiting for ", str(poolsize)+'/'+str(pooltotal), "tasks")

	jobs.join()
	print('\nFound', totalresult, 'Results')
	print("all done")

def xgboost(options):
	print('Coming soon')

def probnet(options):
	print('Coming soon')

def coreOptions():
	options = [["langin", "Translation Lang  In", "en"],["langout", "Translation Lang  Out", "es"],["threads", "Number of threads from search", "20"],["parse", "parse translation", "true"],["tracert", "Tracert Search", "false"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["tt","search number space"],["searchnumber","search number space"],["search","search termsexp"],["xgboost"," XGBOOST"],["probnet","PROBNET"]]
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