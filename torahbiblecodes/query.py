import resources.func.db as db
import argparse

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[1;94m', '\033[1;91m', '\33[1;97m', '\33[1;93m', '\033[1;35m', '\033[1;32m', '\033[0m'
ORANGE  = '\033[1;33m' # orange


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


def TextOfESMAKE(query):

		ret = db.getTextOfES(' ')
		if len(ret) !=0:
				for dbitem in ret:
						#print(dbitem[3]+'\n')
						#print(YELLOW +'BOOK: ==> '+str(dbitem[5]) + END)
						if query == 'en':
							print(ORANGE +str(dbitem[4])+'\n' + END)
						else:
							print(ORANGE +str(dbitem[3])+'\n' + END)
						#print(GREEN +'EN: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[4]) + END)
						#print(BLUE +'HE: ==> GE:'+str(dbitem[1])+' ==> '+ str(dbitem[2]) + END)






parser = argparse.ArgumentParser(description="TBC")
#parser.add_argument("--run", action='store_true')

parser.add_argument('--book', action='store', type=str, required=False, help='query book (default: python3 query.py --book text_11IIkings)')
parser.add_argument('--es', action='store', type=str, required=False, help='query spanish lang (default: python3 query.py --es caso)')
parser.add_argument('--en', action='store', type=str, required=False, help='query english lang (default: python3 query.py --en case)')
parser.add_argument('--make', action='store', type=str, required=False, help='make book (default: python3 query.py --make es)')
args = parser.parse_args()

if args.book:
	TextOfBook(args.book)

if args.es:
	TextOfES(args.es)
if args.make:
	TextOfESMAKE(args.make)

if args.en:
	TextOfEN(args.en)
