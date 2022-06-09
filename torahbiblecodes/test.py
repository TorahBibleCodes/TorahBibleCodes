import threading, time
from queue import Queue
#import resources.func.functions as torah
from resources.func.torah import *
import time
import argparse
import resources.func.db as db
import json
from resources.func.thread import *

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange

torah = Torah()
books.load()



parser = argparse.ArgumentParser(description="TBC")
#parser.add_argument("--run", action='store_true')
parser.add_argument("--crack", action='store_true')
parser.add_argument("--db", action='store_true')
parser.add_argument("--db1", action='store_true')
parser.add_argument("--dbinit", action='store_true')
parser.add_argument("--searchnumber", action='store_true')
parser.add_argument("--search", action='store_true')
parser.add_argument('--capa', action='store', type=int, required=False)
parser.add_argument('--query', action='store', type=str, required=False)
parser.add_argument('--query2', action='store', type=str, required=False)
parser.add_argument('--book', action='store', type=str, required=False)
parser.add_argument('--lang', action='store', type=str, required=False)
parser.add_argument('--col', action='store', type=int, required=False)
args = parser.parse_args()


def checkdb(query, result):

		ret = db.getText(query)
		if len(ret) !=0:
				for dbitem in ret:
						if dbitem[2] == result:
								return dbitem

				return False
		else:
				return False





def loadBook(IntBook):
		global books
		book_rawdata = books.rawdata(torah.numtobook(IntBook))
		book_rawdata = json.loads(book_rawdata)
		outData = ''
		for verse in range(0, len(book_rawdata['text'])):
				for rowbook in book_rawdata['text'][verse]:
						outData =  outData + rowbook.replace(' ', '')
		return outData


def datatorah2():

		letras = loadBook(1)
		letras = letras+ loadBook(2)
		letras = letras+ loadBook(3)
		letras = letras+ loadBook(4)
		letras = letras+ loadBook(5)
		letras = letras+ loadBook(6)
		letras = letras+ loadBook(7)
		letras = letras+ loadBook(8)

		return letras

def datatorah():

		letras = loadBook(1)
		for ld in range(2, 40):
			letras = letras+ loadBook(ld)
		return letras

def capa(salto, letras):
		#letras = ''
		while not jobs.empty():
				ncapa = jobs.get()
				letras = letras[ncapa:]
				ivalue = 1
				output = ''
				for x in range(1, len(letras)):
						ivalue = int(salto) * x - 1
						try:
								if not letras[ivalue] == '':
										toutput = letras[ivalue]
										toutput = toutput.replace(' ', '')
										output = output + toutput + ' '
						except:

								break


				#print(output)
				#print(len(output))
				#print(GREEN + str('E: ') +str(output) + END+ '\n')
				print(GREEN +str(output) + END+ '\n')
				n = 3000
				#text_trans = ''
				text_chunk = [output[i:i+n] for i in range(0, len(output), n)]

				traducir = True
				if traducir:
						for chunks in text_chunk:
								#print(ORANGE + chunks + END+ '\n')
								try:
										fjoin = checkdb(salto, chunks)
										if fjoin == False:
												rett = torah.func_translate('iw', 'es', chunks)
												retp = torah.func_ParseTranslation(rett,'es', 'true')
												if not retp == 0 and not retp == '': 
														#text_trans = str(text_trans) + str(retp)
														db.addText(salto, chunks, str(retp), '')
														print(ORANGE + str(retp) + END)
														#print(BLUE + str(chunks) + END)
										else:

												print(GREEN + str(fjoin[3]) + END)
												#print(BLUE + str(chunks) + END)
								except Exception as e:
												print('Error')
												print(e)
												pass
				#print('Size', len(letras))

				#print('Capa', int(ncapa) +1, end='\r')
				jobs.done()

jobs = Jobs()
if args.capa:

		dtorah = datatorah()
		for x in range(0, int(args.capa)):
				jobs.add(x)
				#capa(args.query, x, dtorah)
		worker = Threads(func=capa, args=(args.query, dtorah,), ntask=1)
		worker.start()


if args.dbinit:
		db.createtable()

if args.db:
		db.addText('busss', 'hebreoooo', 'esspa', 'inglesss')
if args.db1:

		print(checkdb(args.query, args.query2))

def pepa():

	letras = 'abcdeiestsersgisgxy'
	salto = 3
	output = ''
	for x in range(1, len(letras)):
		ivalue = int(salto) * x - 1
		try:
			if not letras[ivalue] == '':
				toutput = letras[ivalue]
				toutput = toutput.replace(' ', '')
				output = output + toutput + ' '
		except:
				break
	print(output)


if args.crack:
	   # letras = loadBook(1)
		#print(letras)
		#crack()
		pepa()
if args.searchnumber:
		searchnumber()
if args.search:
		data = loadBook(1)
		data = data+ loadBook(2)
		ldata = len(data)
		print(ldata)
