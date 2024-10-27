## DEFINE CLASS ##
class cls_ELSObject():

    """
    ## CLASS FOR EACH ELS OBJECT - ELSO() - elso
    """
    
    def __init__(self, ELSSearchTermNumber=None, Letters=None, WordGematriaNumberValue=None, k=None, MaxSkipDistance=None, DELSMLF_POS=None, DELSMLF_NEG=None, DELSMLL_POS=None, DELSMLL_NEG=None, NMP=None, NMN=None, ListOfListsOfIndexMatches=None):

        self.ELSSearchTermNumber = ELSSearchTermNumber ## INTEGER
        self.Letters = Letters ## ACTUALLY: GEMATRIA NUMBER VALUES [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
        self.WordGematriaNumberValue = WordGematriaNumberValue ## 
        self.k = k ## INTEGER : LENGTH OF ELS SEARCH TERM ## 4
        self.MaxSkipDistance = MaxSkipDistance ## (LengthOfTextToSearch / k)
        self.DELSMLF_POS = DELSMLF_POS ## DictOfELSMatchesPositive BY LETTER FIRST
        self.DELSMLF_NEG = DELSMLF_NEG ## DictOfELSMatchesNegative BY LETTER FIRST
        self.DELSMLL_POS = DELSMLL_POS ## DictOfELSMatchesPositive BY LETTER LAST
        self.DELSMLL_NEG = DELSMLL_NEG ## DictOfELSMatchesNegative BY LETTER LAST
        self.NMP = NMP ##NumberOfMatchesPositive
        self.NMN = NMN ##NumberOfMatchesNegative

        self.ListOfListsOfIndexMatches = ListOfListsOfIndexMatches ## 0-BASED INDEX POSITIONS ## ONE (1) LIST PER LETTER MATCH FOR EACH LETTER IN EACH (MULTIPLE) ELS SEARCH TERM; MATCHES OF INDEX POSITIONS
  
        ## DELSO[1] ~= משיח

        ## 40 == מ / ם
        ## len(DELSO[1].ListOfListsOfIndexMatches[0]) --> 25090 ## NUMBER OF MATCHES FOR 1ST LETTER IN 1ST ELS SEARCH TERM

        ## 300 == ש
        ## len(DELSO[1].ListOfListsOfIndexMatches[1]) --> 15595 ## NUMBER OF MATCHES FOR 2ND LETTER IN 1ST ELS SEARCH TERM
        
        ## 10 == י
        ## len(DELSO[1].ListOfListsOfIndexMatches[2]) --> 31556 ## NUMBER OF MATCHES FOR 3RD LETTER IN 1ST ELS SEARCH TERM
        
        ## 8 == ח
        ## len(DELSO[1].ListOfListsOfIndexMatches[3]) --> 7189 ## NUMBER OF MATCHES FOR 4TH LETTER IN 1ST ELS SEARCH TERM

        ## ListOfListsOfIndexMatches[0][0] == 40 == מ
        ## ListOfListsOfIndexMatches[1][0] == 300 == ש
        ## ListOfListsOfIndexMatches[2][0] == 10 == י
        ## ListOfListsOfIndexMatches[3][0] == 8 == ח

        ## DELSO[2] ~= המשיח

        ## 5 == ה
        ## len(DELSO[2].ListOfListsOfIndexMatches[0]) --> 28055 ## NUMBER OF MATCHES FOR 2ND LETTER IN 2ND ELS SEARCH TERM

        ## 40 == מ / ם
        ## len(DELSO[2].ListOfListsOfIndexMatches[1]) --> 25090 ## NUMBER OF MATCHES FOR 2ND LETTER IN 2ND ELS SEARCH TERM

        ## 300 == ש
        ## len(DELSO[2].ListOfListsOfIndexMatches[2]) --> 15595 ## NUMBER OF MATCHES FOR 3RD LETTER IN 2ND ELS SEARCH TERM
        
        ## 10 == י
        ## len(DELSO[2].ListOfListsOfIndexMatches[3]) --> 31556 ## NUMBER OF MATCHES FOR 4TH LETTER IN 2ND ELS SEARCH TERM
        
        ## 8 == ח
        ## len(DELSO[2].ListOfListsOfIndexMatches[4]) --> 7189 ## NUMBER OF MATCHES FOR 5TH LETTER IN 2ND ELS SEARCH TERM

        ## ListOfListsOfIndexMatches[0][0] == 5 == ה
        ## ListOfListsOfIndexMatches[1][0] == 40 == מ
        ## ListOfListsOfIndexMatches[2][0] == 300 == ש
        ## ListOfListsOfIndexMatches[3][0] == 10 == י
        ## ListOfListsOfIndexMatches[4][0] == 8 == ח


