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



def coreOptions():
	options = [["langin", "Translation Lang  In", "en"],["langout", "Translation Lang  Out", "es"],["threads", "Number of threads from search", "20"],["parse", "parse translation", "true"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["searchnumber","search number space"],["search","search termsexp"]]
	return commands


def core(moduleOptions):
	print('Command run disabled on current module')

def save(moduleOptions):
	global langin, langout, threads, ptrans
	langin = moduleOptions[0][2]
	langout = moduleOptions[1][2]
	threads = moduleOptions[2][2]
	ptrans = moduleOptions[3][2]