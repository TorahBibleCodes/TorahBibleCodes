## DEFINE CLASS
class cls_ELSObject():

    """
    ## CLASS FOR EACH ELS OBJECT - ELSO() - elso
    """
    
    def __init__(self, ELSSearchTermNumber=None, Letters=None, k=None, MaxSkipDistance=None, ListOfListsOfIndexMatches=None):

        self.ELSSearchTermNumber = ELSSearchTermNumber ## INTEGER
        self.Letters = Letters ## ACTUALLY: GEMATRIA NUMBER VALUES [40, 300, 10, 8] ====== [ח, י, ש, מ] ====== [מ, ש, י, ח]
        self.k = k ## INTEGER : LENGTH OF ELS SEARCH TERM ## 4
        self.MaxSkipDistance = MaxSkipDistance ## (LengthOfTextToSearch / k)
        self.ListOfListsOfIndexMatches = ListOfListsOfIndexMatches ## 0-BASED INDEX POSITIONS ## ONE (1) LIST PER LETTER MATCH FOR EACH LETTER IN EACH (MULTIPLE) ELS SEARCH TERM; MATCHES OF INDEX POSITIONS
  
        ## ListOfListsOfIndexMatches[0][0] == 40 == מ
        ## ListOfListsOfIndexMatches[0][1] == 300 == ש
        ## ListOfListsOfIndexMatches[0][2] == 10 == י
        ## ListOfListsOfIndexMatches[0][3] == 8 == ח

        ## ListOfListsOfIndexMatches[1][0] == 5 == ה
        ## ListOfListsOfIndexMatches[1][1] == 40 == מ
        ## ListOfListsOfIndexMatches[1][2] == 300 == ש
        ## ListOfListsOfIndexMatches[1][3] == 10 == י
        ## ListOfListsOfIndexMatches[1][4] == 8 == ח

        ## TEST DEVELOPMENT
        # self.sN0 =
        # self.sN 



