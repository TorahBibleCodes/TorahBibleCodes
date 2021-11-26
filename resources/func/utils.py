import json
import re


def fn_TextFilePreprocess(JSON):
	

	
	ListOfJSONStringsParsed = []
	ListOfJSONStringsParsedWithSpaces = []
	
	
	if isinstance(JSON, str):
		
		
		JSONParsed = fn_TextFileParse(JSON)
		

		ListOfJSONStringsParsed.append(JSONParsed[1]) 
		ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) 
	
	
	elif isinstance(JSON, tuple):
		
		
		for each in JSON:
			
			
			JSONParsed = fn_TextFileParse(each)
			ListOfJSONStringsParsed.append(JSONParsed[1]) 
			ListOfJSONStringsParsedWithSpaces.append(JSONParsed[0]) 
			

	
	return(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces)
	




def fn_TextFileParse(JSONString):

		 
	
	

	

	TextNoHyphensWithSpaces = JSONString.replace("־", " ")







	TextNoBracketsWithSpaces = re.sub("[\[].*?[\]]", "", TextNoHyphensWithSpaces)





	
	

	

	TextNoSpaces = TextNoBracketsWithSpaces.replace(" ", "")



	
	
	TextParsedWithSpaces = TextNoBracketsWithSpaces
	TextParsedNoSpaces = TextNoSpaces







	


	
	TextParsedWithSpaces = TextNoBracketsWithSpaces
	TextParsedNoSpaces = TextNoSpaces
	

	
	return(TextParsedWithSpaces, TextParsedNoSpaces)






def fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed, ListOfJSONStringsParsedWithSpaces):
	ListOfDictsOfJSONStringsParsed = []
	ListOfDictsOfJSONStringsParsedWithSpaces = []
	   
	
	
	for each in ListOfJSONStringsParsed:
		
		
		DictOfConvertedJSON = json.loads(each)
		
		
		ListOfDictsOfJSONStringsParsed.append(DictOfConvertedJSON)


	
	
	for each in ListOfJSONStringsParsedWithSpaces:
		
		
		DictOfConvertedJSON = json.loads(each)
		
		
		ListOfDictsOfJSONStringsParsedWithSpaces.append(DictOfConvertedJSON)
		return(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces)
	

def fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed):

	
	
	TextChosen = []
	
	
	if len(ListOfDictsOfJSONStringsParsed) == 5:
		
		
		LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 1)
		
		
		BookNumbers = list((range(1, LengthForRange, 1)))
		
		
		for each in BookNumbers:
			
			
			TextChosen.append(each)
			
	
	elif len(ListOfDictsOfJSONStringsParsed) == 21:
		
		
		LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 6)
		
		
		BookNumbers = list((range(6, LengthForRange, 1)))
		
		
		for each in BookNumbers:
			
			
			TextChosen.append(each)
			
	
	elif len(ListOfDictsOfJSONStringsParsed) == 13:
		
		
		LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 27)
		
		
		BookNumbers = list((range(27, LengthForRange, 1)))
		
		
		for each in BookNumbers:
			
			
			TextChosen.append(each)
			
	
	elif len(ListOfDictsOfJSONStringsParsed) == 39:
		
		
		LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 1)
		
		
		BookNumbers = list((range(1, LengthForRange, 1)))
		
		
		for each in BookNumbers:
			
			
			TextChosen.append(each)
	
	
	elif len(ListOfDictsOfJSONStringsParsed) == 1:
	
		
		for each in ListOfDictsOfJSONStringsParsed:
			 
			
			TextTitle = each["title"]
		 
			if TextTitle == "Genesis":
				BookNumber = 1
		 
			elif TextTitle == "Exodus":
				BookNumber = 2
		 
			elif TextTitle == "Leviticus":
				BookNumber = 3
		 
			elif TextTitle == "Numbers":
				BookNumber = 4
		 
			elif TextTitle == "Deuteronomy":
				BookNumber = 5
				
			elif TextTitle == "Joshua":
				BookNumber = 6
			
			elif TextTitle == "Judges":
				BookNumber = 7
				
			elif TextTitle == "ISamuel":
				BookNumber = 8
			
			elif TextTitle == "IISamuel":
				BookNumber = 9
				
			elif TextTitle == "IKings":
				BookNumber = 10
				
			elif TextTitle == "IIKings":
				BookNumber = 11
				
			elif TextTitle == "Isaiah":
				BookNumber = 12
				
			elif TextTitle == "Jeremiah":
				BookNumber = 13
				
			elif TextTitle == "Ezekiel":
				BookNumber = 14
				
			elif TextTitle == "Hosea":
				BookNumber = 15
				
			elif TextTitle == "Joel":
				BookNumber = 16
				
			elif TextTitle == "Amos":
				BookNumber = 17
				
			elif TextTitle == "Obadiah":
				BookNumber = 18
				
			elif TextTitle == "Jonah":
				BookNumber = 19
				
			elif TextTitle == "Micah":
				BookNumber = 20
				
			elif TextTitle == "Nahum":
				BookNumber = 21
				
			elif TextTitle == "Habakkuk":
				BookNumber = 22
				
			elif TextTitle == "Zephaniah":
				BookNumber = 23
				
			elif TextTitle == "Haggai":
				BookNumber = 24
				
			elif TextTitle == "Zechariah":
				BookNumber = 25
				
			elif TextTitle == "Malachi":
				BookNumber = 26
				
			elif TextTitle == "Psalms":
				BookNumber = 27
			
			elif TextTitle == "Proverbs":
				BookNumber = 28
				
			elif TextTitle == "Job":
				BookNumber = 29
				
			elif TextTitle == "SongOfSongs":
				BookNumber = 30
			
			elif TextTitle == "Ruth":
				BookNumber = 31
				
			elif TextTitle == "Lamentations":
				BookNumber = 32
				
			elif TextTitle == "Ecclesiastes":
				BookNumber = 33
				
			elif TextTitle == "Esther":
				BookNumber = 34
				
			elif TextTitle == "Daniel":
				BookNumber = 35
				
			elif TextTitle == "Ezra":
				BookNumber = 36
				
			elif TextTitle == "Nehemiah":
				BookNumber = 37
				
			elif TextTitle == "IChronicles":
				BookNumber = 38
				
			elif TextTitle == "IIChronicles":
				BookNumber = 39
				
				
			
			TextChosen.append(BookNumber)
	
	
	else:
		pass
	  
	
	TextChosen = tuple(TextChosen)
	

	
	return(TextChosen)

def fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, ListOfDictsOfJSONStringsParsedWithSpaces, SearchTextChosen):

	
	
	if len(ListOfDictsOfJSONStringsParsed) == 5:
		
		
		ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
		ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))			
	  
		
		return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		
	
	elif len(ListOfDictsOfJSONStringsParsed) == 21:
		
		
		ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
		ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))			
	  
		
		return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		
	
	elif len(ListOfDictsOfJSONStringsParsed) == 13:
		
		
		ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
		ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))			
	  
		
		return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		
	
	elif len(ListOfDictsOfJSONStringsParsed) == 39:
		
		
		ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
		ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))			
	  
		
		return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		
	
	elif len(ListOfDictsOfJSONStringsParsed) == 1:
		
		
		ZippedTupleNoSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsed))
		ZippedTupleWithSpaces = tuple(zip(SearchTextChosen, ListOfDictsOfJSONStringsParsedWithSpaces))
	
		
											
			
			
			
				   
		
		return(ZippedTupleNoSpaces, ZippedTupleWithSpaces)
		
	
	else:
		
		pass      
		  





def fn_DictionaryOfVersesCreate(ZippedTupleNoSpaces, ZippedTupleWithSpaces):

		  
	
	DictOfVersesNoSpaces = {} 
	DictOfVersesWithSpaces = {} 

	for each in ZippedTupleNoSpaces:
		NumberOfBook = each[0]
		NumberOfChapters = len(each[1]['text'])
	
		ChapterCounter = 1
		
		for Chapter in each[1]['text']:			
			
			
			
			VerseCounter = 1
			
			for Verse in Chapter:
				
				
				
				
				
				
				KeyTuple = (NumberOfBook, ChapterCounter, VerseCounter)
				
				
				
				
				
				DictOfVersesNoSpaces[KeyTuple] = Verse
				
				VerseCounter += 1
			
			ChapterCounter += 1


	for each in ZippedTupleWithSpaces:
		NumberOfBook = each[0]
		NumberOfChapters = len(each[1]['text'])
	
		ChapterCounter = 1
		
		for Chapter in each[1]['text']:			
			
			
			
			VerseCounter = 1
			
			for Verse in Chapter:
				
				
				
				
				
				
				KeyTuple = (NumberOfBook, ChapterCounter, VerseCounter)
				
				
				
				
				
				DictOfVersesWithSpaces[KeyTuple] = Verse
				
				VerseCounter += 1
			
			ChapterCounter += 1

			

	
	return(DictOfVersesNoSpaces, DictOfVersesWithSpaces)


def fn_DataObjectsCreate(D, DS):
	DL = {} 
	D5 = {} 
	L = [] 
	LW = [] 
	
	VerseLetterCounter = 1
	TotalLetterCounter = 1

	
	

	
	
	for key, each in D.items():
		
		
		LengthOfString = len(each)
		
		

		
		for letter in each:
			
			
			L.append(letter)
			
			
			
			key4 = key + (VerseLetterCounter,)
			
			
			
			DL[key4] = letter
			
			
			key5 = key + (VerseLetterCounter, TotalLetterCounter,)
			
			
			D5[key5] = letter
			
			
			TotalLetterCounter += 1
			
			
			VerseLetterCounter += 1
		
		
		VerseLetterCounter = 1

	


	
	S = ''.join(L)


	
	ListOfWords = [] 
		

	
	
	for key, each in DS.items():
		
		
		LengthOfString = len(each)
		
		

		
		ListOfWords.extend(each.split())

	




	
	
	return(S, L, DL, D5, ListOfWords)


def fn_GetNumberValues(SequenceOfLetters, ListOfWords):
	ListOfNumberValues4Letters = []
	ListOfNumberValues4Words = []

	ListTemp = []
	ListSum = []
	value = 0
	
	

	

	
	for cada in SequenceOfLetters:

		for each in cada:
			
			if each == 'א':
				value = 1
			elif each == 'ב':
				value = 2    
			elif each == 'ג':
				value = 3 
			elif each == 'ד':
				value = 4 
			elif each == 'ה':
				value = 5 
			elif each == 'ו':
				value = 6 
			elif each == 'ז':
				value = 7 
			elif each == 'ח':
				value = 8 
			elif each == 'ט':
				value = 9 
			elif each == 'י':
				value = 10 
			elif each == 'כ' or each == 'ך':
				value = 20 
			elif each == 'ל':
				value = 30 
			elif each == 'מ' or each == 'ם':
				value = 40 
			elif each == 'נ' or each == 'ן':
				value = 50 
			elif each == 'ס':
				value = 60 
			elif each == 'ע':
				value = 70
			elif each == 'פ' or each == 'ף':
				value = 80  
			elif each == 'צ' or each == 'ץ':
				value = 90 
			elif each == 'ק':
				value = 100  
			elif each == 'ר':
				value = 200 
			elif each == 'ש':
				value = 300 
			elif each == 'ת':
				value = 400

			ListTemp.append(value)

		


		ListSum = sum(ListTemp)
		ListOfNumberValues4Letters.append(ListSum)
		
		ListTemp = [] 
		ListSum = [] 
		

		

		

	


	

	
	for cada in ListOfWords:

		for each in cada:
			
			if each == 'א':
				value = 1
			elif each == 'ב':
				value = 2    
			elif each == 'ג':
				value = 3 
			elif each == 'ד':
				value = 4 
			elif each == 'ה':
				value = 5 
			elif each == 'ו':
				value = 6 
			elif each == 'ז':
				value = 7 
			elif each == 'ח':
				value = 8 
			elif each == 'ט':
				value = 9 
			elif each == 'י':
				value = 10 
			elif each == 'כ' or each == 'ך':
				value = 20 
			elif each == 'ל':
				value = 30 
			elif each == 'מ' or each == 'ם':
				value = 40 
			elif each == 'נ' or each == 'ן':
				value = 50 
			elif each == 'ס':
				value = 60 
			elif each == 'ע':
				value = 70
			elif each == 'פ' or each == 'ף':
				value = 80  
			elif each == 'צ' or each == 'ץ':
				value = 90 
			elif each == 'ק':
				value = 100  
			elif each == 'ר':
				value = 200 
			elif each == 'ש':
				value = 300 
			elif each == 'ת':
				value = 400

			ListTemp.append(value)
			TupleTemp = tuple(ListTemp)
			
		


		SumOfWord = sum(TupleTemp)
		ListOfNumberValues4Words.append(SumOfWord)
		
		ListTemp = [] 
		ListSum = [] 
		

		

	


	
	return(ListOfNumberValues4Letters, ListOfNumberValues4Words)
	
def fn_ListOfIndexesCustomCreate(D5):
	
		  
	ListOfIndexesCustom = [] 
	
	
	for each in D5: 
		IndexCustom = each[-1]
		
		
		ListOfIndexesCustom.append(IndexCustom)
	return(ListOfIndexesCustom)
	




def fn_TupleOfWordsAndGematriaValuesCreate(ListOfWords, NW):
	
		  
	
	

	W = tuple(zip(ListOfWords, NW))
	return(W)
	





