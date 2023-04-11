## DEFINE CLASS
class cls_LetterObject():

    """
    ## CLASS FOR EACH LETTER OBJECT - LO() - lo
    """
    
    def __init__(self, Letter=None, LetterGematriaNumberValue=None, LetterPositionIndex=None, LetterCoordinatesD5K=None, LetterCoordinatesDL=None, \
        WordNumber=None, IsMatchInELS=None, ListOfMatches=None):

        self.Letter = Letter
        self.LetterGematriaNumberValue = LetterGematriaNumberValue ## == SET INITIAL VALUE == None; LETTER GEMATRIA VALUE

        self.LetterPositionIndex = LetterPositionIndex ## 1-BASED DICTIONARY KEY-POSITIONS
        self.LetterCoordinatesD5K = LetterCoordinatesD5K ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 5-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE, LETTER#INTEXT)
        self.LetterCoordinatesDL = LetterCoordinatesDL ## 1-BASED DICTIONARY KEY-POSITIONS: RETURNS ## 4-DIGIT-TUPLE-BASED DICTIONARY VALUE OF (BOOK#, CHAPTER#, VERSE#, LETTER#INVERSE)

        self.WordNumber = WordNumber ## 1-BASED DICTIONARY KEY-POSITIONS

        ## TEST DEVELOPMENT
        self.IsMatchInELS = IsMatchInELS ## SET INITIAL VALUE == None; ## EACH LETTER POSITION (n) CAN HAVE ONE-TO-MANY MULTIPLE MATCHES (== OVERLAP) WITH MULTIPLE POSSIBLE CONNECTIONS TO ELS WORDS
        self.ListOfMatches = ListOfMatches ## SET INITIAL VALUE == None;

