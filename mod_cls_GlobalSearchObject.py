## DEFINE CLASS
class cls_GlobalSearchObject():

    """
    ## CLASS FOR GLOBAL SEARCH OBJECT
    """
    
    def __init__(self, SearchTextChosen=None, LengthOfTextToSearch=None, D=None, DS=None, \
            S=None, L=None, DL=None, D5=None, D5K=None, N=None, \
            LW=None, W=None, DW=None, NW=None, DLO=None, \
            ListOfSearchTerms=None, DictOfSearchTerms=None, \
            ListOfRegex4TextString=None, ListOfRegex4ELSSearchTerms=None, ListOfRowsOfLetters=None, ListOfPDSeries4ELSs=None, \
            NW4ELS=None, W4ELS=None, DW4ELS=None, DictOfMatches4ELS=None, DELSO=None, \
            ListOfFactors=None, YH=None, XW=None, LLL=None, \
            ListOfIndexesCustomL=None, ListOfIndexesCustomLLL=None, \
            sL0=None, sL=None, sLLL0=None, sLLL=None, sN0=None, sN=None, \
            NumpyArrayOfNumberValuesOfEntireText=None, ListOfFirstsAndLasts4ELS=None, ListOfBooleanMatches4ELS=None):

        self.SearchTextChosen = SearchTextChosen ## 1-DIGIT TUPLE ## (12,)
        self.LengthOfTextToSearch = LengthOfTextToSearch ## INTEGER

        self.D = D ## 3-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#) - NO SPACES BETWEEN WORDS/LETTERS
        self.DS = DS ## 3-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#) - WITH SPACES BETWEEN WORDS/LETTERS

        self.S = S ## 0-BASED INDEX POSITIONS
        self.L = L ## 0-BASED INDEX POSITIONS
        self.DL = DL ## 4-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE) - NO SPACES BETWEEN WORDS/LETTERS
        self.D5 = D5 ## 5-DIGIT-TUPLE-BASED DICTIONARY KEY POSITION OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT) - NO SPACES BETWEEN WORDS/LETTERS
        self.D5K = D5K ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 5-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT)
        self.N = N ## 0-BASED INDEX POSITIONS
        
        self.LW = LW ## 0-BASED INDEX POSITIONS
        self.W = W ## 0-BASED INDEX POSITIONS
        self.DW = DW ## 1-BASED DICTIONARY KEY-POSITIONS
        self.NW = NW ## 0-BASED INDEX POSITIONS

        self.DLO = DLO ## 1-BASED DICTIONARY KEY-POSITIONS

        self.ListOfSearchTerms = ListOfSearchTerms ## 0-BASED INDEX POSITIONS
        self.DictOfSearchTerms = DictOfSearchTerms ## 1-BASED DICTIONARY KEY-POSITIONS

        self.ListOfRegex4TextString = ListOfRegex4TextString ## 0-BASED INDEX POSITIONS
        self.ListOfRegex4ELSSearchTerms = ListOfRegex4ELSSearchTerms ## 0-BASED INDEX POSITIONS
        self.ListOfRowsOfLetters = ListOfRowsOfLetters ## 0-BASED INDEX POSITIONS
        self.ListOfPDSeries4ELSs = ListOfPDSeries4ELSs ## 0-BASED INDEX POSITIONS

        self.NW4ELS = NW4ELS ## 0-BASED INDEX POSITIONS
        self.W4ELS = W4ELS ## 0-BASED INDEX POSITIONS
        self.DW4ELS = DW4ELS ## 1-BASED DICTIONARY KEY-POSITIONS
        self.DictOfMatches4ELS = DictOfMatches4ELS ## 1-BASED DICTIONARY KEY-POSITIONS
        self.DELSO = DELSO ## 1-BASED DICTIONARY KEY-POSITIONS

        self.ListOfFactors = ListOfFactors ## 0-BASED INDEX POSITIONS
        self.YH = YH ## INTEGER
        self.XW = XW ## INTEGER
        self.LLL = LLL ## 0-BASED INDEX POSITIONS

        self.ListOfIndexesCustomL = ListOfIndexesCustomL ## 0-BASED INDEX POSITIONS
        self.ListOfIndexesCustomLLL = ListOfIndexesCustomLLL ## 0-BASED INDEX POSITIONS

        self.sL0 = sL0 ## 0-BASED INDEX POSITIONS
        self.sL = sL ## 1-BASED INDEX POSITIONS
        self.sLLL0 = sLLL0 ## 0-BASED INDEX POSITIONS
        self.sLLL = sLLL ## 1-BASED INDEX POSITIONS
        self.sN0 = sN0 ## 0-BASED INDEX POSITIONS
        self.sN = sN ## 1-BASED INDEX POSITIONS

        self.NumpyArrayOfNumberValuesOfEntireText = NumpyArrayOfNumberValuesOfEntireText ## 0-BASED INDEX POSITIONS

        ## TEST DEVELOPMENT
        ## self.ListOfFirstsAndLasts4ELS = ListOfFirstsAndLasts4ELS
        ## self.ListOfBooleanMatches4ELS = ListOfBooleanMatches4ELS
        ## self.IndexPositionsOfBooleanMatches = IndexPositionsOfBooleanMatches

        


