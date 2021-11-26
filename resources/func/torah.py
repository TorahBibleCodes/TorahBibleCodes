import pandas as pd
from deep_translator import GoogleTranslator
import resources.func.utils as util
from hebrew_numbers import gematria_to_int
from textblob import TextBlob
from os import listdir
from os.path import isfile, join
import re




class BibleBooks():
    def __init__(self):
        self.folder = 'resources/data/'
        self.book = {}
    def load(self):
        
        for f in listdir(self.folder):
            if isfile(join(self.folder, f)) and f.endswith(".json"):
                fn = f.split('.')
                #print('Load', fn[0])
                with open(self.folder+f, encoding="utf-8-sig") as File:
                    self.book[fn[0]] = File.read()

    def rawdata(self, bookname):
        return self.book[bookname]

    def booklist(self):
        return list(self.book.keys())

books = BibleBooks()

class Torah():
	def __init__(self):
		self.book = ''

	def loadbooks(self):
		books.load()

	def func_getnumber(self, listL, listW):
		return util.fn_GetNumberValues(listL, listW)

	def func_checklang(self, word, lang):
		b = TextBlob(word)
		
		try:
			b.detect_language()
			if (b.detect_language() == lang):
				return True
		except:
			return True
		return False


	def func_translate(self, lang_in, lang_out, data):
		translated = GoogleTranslator(source=lang_in, target=lang_out).translate(data.strip()) 
		return translated

	def gematria(self, word: str) -> int:
	    gcode = {   'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':600,
	                'k':10, 'l':20, 'm':30, 'n':40, 'o':50, 'p':60, 'q':70, 'r':80, 's':90,
	                't':100,'u':200,'v':700,'w':900,'x':300,'y':400, 'z':500  }
	    try:
	        return sum([gcode[char] for char in word])
	    except:
	        print(word)
	        raise ValueError


	def gematrix(self, phrase: str) -> int:
	    phrase = self.strip_accents(phrase.lower())
	    phrase = ''.join([i for i in phrase if i.isalpha()])
	    try: 
	        return sum([self.gematria(word.lower()) for word in phrase.split(' ')])
	    except:
	        print(phrase)
	        raise ValueError


	def strip_accents(self, s):
	    """
	    Sanitarize the given unicode string and remove all special/localized
	    characters from it.
	 
	    Category "Mn" stands for Nonspacing_Mark

	    (thx http://www.ultrabug.fr/convert-special-characters-to-ascii-in-python/)
	    """
	    try:
	        return ''.join(
	            c for c in unicodedata.normalize('NFD', s)
	            if unicodedata.category(c) != 'Mn'
	        )
	    except:
	        return s


	def gematria_iw_int(text):
		return gematria_to_int(text)
	def func_ParseTranslation(self, translated, lang, active):
		abd = 'abcdefghijklmnñopqrstuvwxyz'
		str_split = translated.split(' ')
		str_final = ''
		for word in str_split:
			try:
				if word[0].lower() in abd:
					if active == 'true':
						if self.func_checklang(word, lang) == True:
							str_final = str_final+ word+' '
					else:
						str_final = str_final+ word+' '
			except:
				pass
		
		if not str_final == '':
			return str_final
		else:
			return 0
	def els(self, namebook, number, tracert='false'):
		space = number
		abd = 'abcdefghijklmnñopqrstuvwxyz'
		i=1
		rese=""
		totalvalue = 0
		D = self.GetDataBook(namebook)
		for (z,b,y) in D:
			try:
				charnum = 0
				res=""
				#print('----')
				#print(D[int(z),int(b),int(y)])
				#print('----')
				for char in D[z,b,y]:
					charnum = charnum+1
					if (i % int(space)) == 0:
						
						if tracert == 'true':
							totalvalue = totalvalue + int(charnum)
							print('Source:',int(z),'chapter:', int(b),'Verse:', int(y),'CharNum:',int(charnum),'Char:', char)
						#print(char)
						#res=(char)+res
						res=res+char

					i=i+1
				rese=rese+" "+res
			except:
				pass
		#print('Total', totalvalue)
		ret = re.sub('\s+', ' ', rese.strip())
		return ret, totalvalue

	def GetDataBook(self, bibleNumberBook):


		JSON = books.rawdata(bibleNumberBook) 
		ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces = util.fn_TextFilePreprocess(JSON)
		ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces = util.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)
		SearchTextChosen = util.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)
		ZippedTupleNoSpaces, ZippedTupleWithSpaces = util.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen)
		D, DS = util.fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		S, L, DL, D5, ListOfWords = util.fn_DataObjectsCreate(D, DS)
		N, NW = util.fn_GetNumberValues(S, ListOfWords) 
		ListOfIndexesCustom = util.fn_ListOfIndexesCustomCreate(D5)
		W = util.fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW)

		return D


