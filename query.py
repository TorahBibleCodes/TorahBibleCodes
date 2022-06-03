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

#ret = db.getTextOfBook('text_11IIkings')


parser = argparse.ArgumentParser(description="TBC")
#parser.add_argument("--run", action='store_true')

parser.add_argument('--book', action='store', type=str, required=False)

args = parser.parse_args()

if args.book:
	TextOfBook(args.book)
