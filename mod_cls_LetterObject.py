## DEFINE CLASS ##
class cls_LetterObject():

    """
    ## CLASS FOR EACH LETTER OBJECT - LO() - lo
    """
    
    def __init__(self, Letter=None, LetterGematriaNumberValue=None, LetterPositionIndex=None, LetterCoordinatesD5K=None, LetterCoordinatesDL=None, \
        LetterPositionInWord=None, WordNumber=None, Word=None, WordNumberInVerse=None, WordCoordinatesDWTK=None, VerseCoordinatesDS=None, \
        Verse = None, IsMatchInELS=None, NumberOfMatches=None, ListOfMatches=None, DictOfMatches=None):

        self.Letter = Letter
        self.LetterGematriaNumberValue = LetterGematriaNumberValue ## == SET INITIAL VALUE == None; LETTER GEMATRIA VALUE

        self.LetterPositionIndex = LetterPositionIndex ## 1-BASED DICTIONARY KEY-POSITIONS
        self.LetterCoordinatesD5K = LetterCoordinatesD5K ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 5-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT)
        self.LetterCoordinatesDL = LetterCoordinatesDL ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 4-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE)
        
        self.LetterPositionInWord = LetterPositionInWord ## RETURNS INTEGER FOR LETTER POSITION IN WORD - OTHERWISE NONE
        self.WordNumber = WordNumber ## 1-BASED DICTIONARY KEY-POSITIONS
        self.Word = Word ## RETURNS WORD TEXT ONLY FOR ELS MATCHES - OTHERWISE NONE
        self.WordNumberInVerse = WordNumberInVerse ## RETURNS WORD NUMBER IN VERSE ONLY FOR ELS MATCHES - OTHERWISE NONE 
        self.WordCoordinatesDWTK = WordCoordinatesDWTK ## RETURNS 5-DIGIT TUPLE-BASED
        self.VerseCoordinatesDS = VerseCoordinatesDS ## RETURNS 3-DIGIT TUPLE-BASED
        self.Verse = Verse ## RETURNS VERSE TEXT ONLY FOR ELS MATCHES - OTHERWISE NONE

        ## TEST DEVELOPMENT
        self.IsMatchInELS = IsMatchInELS ## SET INITIAL VALUE == None; ## EACH LETTER POSITION (n) CAN HAVE ONE-TO-MANY MULTIPLE MATCHES (== OVERLAP) WITH MULTIPLE POSSIBLE CONNECTIONS TO ELS WORDS
        self.NumberOfMatches = NumberOfMatches ## SET INITIAL VALUE == None;
        self.ListOfMatches = ListOfMatches ## SET INITIAL VALUE == None;
        self.DictOfMatches = DictOfMatches ## SET INITIAL VALUE == None;
