import argparse
import os
import sys
import subprocess
import shlex
import pandas as pd
import threading, time
from queue import Queue
from resources.func.torah import *
#import modules.resources.xgboost as xgb
from deep_translator import GoogleTranslator
import re
import resources.func.db as db
from resources.func.thread import *


BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange


tracert = 'false'
langin = 'en'
langout = 'es'
ptrans = 'true'
visualice = False
threads = 0
totalvalue = 0
totalresult = 0
res_data = []
res_book = []
torah = Torah()
jobstrans = Jobs()
books.load()

def checkdb(query, result):

		ret = db.getText(query)
		if len(ret) !=0:
				for dbitem in ret:
						if dbitem[2] == result:
								return dbitem

				return False
		else:
				return False




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

def ttranslator():
	global langout, ptrans, totalvalue, tracert, totalresult, jobstrans

	while True:#not jobstrans.empty():
		#print('\nFound', int(jobstrans.queue.qsize()))
		tchunk = jobstrans.get()
		tchunk = tchunk.split('*')
		dchunk = tchunk[0]
		n = 2000
		text_chunk = [dchunk[i:i+n] for i in range(0, len(dchunk), n)]
		lenchunk = len(text_chunk)
		text_trans = ''
		nch = 0
		
		try:
			#print(GREEN, 'chunk size: ', lenchunk, END)
			#print('\nBook:',tchunk[1])
			for chunks in range(0, lenchunk):
				fjoin = checkdb(tchunk[2], text_chunk[chunks])
				#print('vava ', tchunk[2])
				#print(ORANGE + chunks + END+ '\n')
				nch = nch +1
				if fjoin == False:
					#jobstrans.add(dchunk[chunks]+'*'+value)
					#print(BLUE, 'n', str(nch), END, 'chunk', text_chunk[chunks])
					rett = torah.func_translate('iw', langout, text_chunk[chunks])
					retp = torah.func_ParseTranslation(rett,langout, ptrans)
					rett_en = torah.func_translate('iw', 'en', text_chunk[chunks])
					retp_en = torah.func_ParseTranslation(rett_en,'en', ptrans)
					if not retp == 0 and not retp == '': 
						text_trans = str(text_trans) + str(retp)
						db.addText(tchunk[2], text_chunk[chunks], str(retp), str(retp_en))
						totalresult = totalresult+1
						print('\nBook:',tchunk[1], 'Gematria:', tchunk[2]+'\n')
						print(ORANGE+'ES: ==> '+ str(retp) + END+'\n')
						print(GREEN+'EN: ==> '+ str(retp_en) + END+'\n')
						print(BLUE+'HE: ==> '+ str(text_chunk[chunks]) + END+'\n')
				else:
					print('\nBook:',tchunk[1], 'Gematria:', tchunk[2])
					print(ORANGE +'ES: ==> '+ str(fjoin[3]) + END)
					print(GREEN +'EN: ==>'+ str(fjoin[4]) + END)
					print(BLUE +'HE: ==>'+ str(fjoin[2]) + END)
			#print('\nBook:',tchunk[1])
					#print('\nn',nch)
					#print(ORANGE + str(retp) + END)
			
			#print(BLUE + str(text_chunk) + END)

			jobstrans.done()
			#time.sleep(1)
		except Exception as e:
			print('ee t')
			print(e)
			jobstrans.done()
			pass
			#print('nNN', str(nch))

def searchAll(q, number):
	global langout, ptrans, totalvalue, tracert, totalresult, jobstrans
	while not q.empty():
		try:
			value = q.get()
			text_chunk = ''
			ret, tvalue = torah.els(value, number, tracert=tracert)
			totalvalue = totalvalue + tvalue

			text_trans= ''
			len_chunk = len(text_chunk)
			#print(GREEN, 'chunk size: ', len_chunk, END)
			nch = 0
			

			jobstrans.add(str(ret)+'*'+value+'*'+number)
			#print('\nBook:',value)
			#print('\ndata', ret)
			#print('\nFounda', int(jobstrans.count()))

			jobstrans.join()
			q.task_done()
			#rett = torah.func_translate('iw', langout, ret)
			#retp = torah.func_ParseTranslation(rett,langout, ptrans)
			#if not retp == 0:
				#print(ret)
			#	totalresult = totalresult+1
			#	print('\nBook:',value)
			#	print(retp)
				#dfx.clear()
				#res_book.append(value)
				#res_data.append(retp)
			#	q.task_done()
			#else:
			#	q.task_done()
		except Exception as e:
			q.task_done()
			#print(ORANGE + retp + END)
			print(RED,"Exception: {}".format(type(e).__name__),END)
			print(ORANGE,"Exception message: {}".format(e),END)
			#print(e)
			pass

def tonum(options):
	global langin, langout, threads, totalresult
	listform = ''
	print(options[0])
	if len(options) > 1:
		for string in options:
			listform = listform+' '+string
		if langin == 'iw':
			sed = gematria_to_int(listform)
		else:
			sed = torah.gematrix(listform)
	else:
		#print(options[0])
		if langin == 'iw':
			sed = gematria_to_int(u''+options[0].strip())
		else:
			try:
				sed = torah.gematria(options[0].strip())
			except Exception as e:
				pass
				print(e)

	print(sed)


def search(options):
	global langin, langout, threads, totalresult
	listform = ''
	totalresult = 0
	jobs = Queue()
	if visualice:
		dfx.clear()
	if len(options) > 1:
		for string in options:
			listform = listform+' '+string
		if langin == 'iw':
			sed = gematria_to_int(listform)
		else:
			sed = torah.gematrix(listform)
	else:
		#print(options[0])
		if langin == 'iw':
			sed = gematria_to_int(u''+options[0].strip())
		else:
			sed = torah.gematria(options[0].strip())

	for i in books.booklist():
		#print(i)
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, str(sed),))
		worker.start()

	poolsize = 39 - int(jobs.qsize())
	pooltotal = 39
	#print("waiting for ", str(poolsize)+'/'+str(pooltotal), "tasks")

	jobs.join()
	if visualice:
		dfx.clear()
	#for impr in range(0, len(res_book)):
	#	print('\nBook:',res_book[impr])
	#	print(res_data[impr])
	print('\nFound', totalresult, 'Results')
	print("all done")


def searchnumber(options):
	global langin, langout, threads, totalresult, jobstrans
	number = options[0]
	#threads = 1
	totalresult = 0

	jobs = Queue()

	bfor = books.booklist()
	for i in bfor:
	#for i in range(0, 1):
		#print(i)
		#tjobs = bfor[i]
		jobs.put(i)

	for i in range(int(threads)):
		worker = threading.Thread(target=searchAll, args=(jobs, number,))
		worker.start()

	poolsize = 39 - int(jobs.qsize())
	pooltotal = 39
	print("waiting for ", str(poolsize)+'/'+str(pooltotal), "tasks")

	jobs.join()
	if visualice:
		dfx.clear()
	#for impr in range(0, len(res_book)):
	#	print('\nBook:',res_book[impr])
	#	print(res_data[impr])
	print('\nFound', int(jobstrans.queue.qsize()), 'Results')
	print("all done")
	#worker = Threads(func=ttranslator, ntask=50)
	#worker.start()
def xgboost(options):
	print('Coming soon')

def probnet(options):
	print('Coming soon')

def coreOptions():
	options = [["langin", "Translation Lang  In", "en"],["langout", "Translation Lang  Out", "es"],["threads", "Number of threads from search", "20"],["parse", "parse translation", "true"],["tracert", "Tracert Search", "false"]]
	return options

## Extend command usage instructions 
def ExtendCommands():
	commands = [["tonum","get number"],["tt","search number space"],["searchnumber","search number space"],["search","search termsexp"],["xgboost"," XGBOOST"],["probnet","PROBNET"]]
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

worker = Threads(func=ttranslator, ntask=50)
worker.start()
