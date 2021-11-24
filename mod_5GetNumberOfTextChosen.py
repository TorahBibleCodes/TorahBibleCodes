## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
def fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed):

    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  BEGIN FUNCTION #5 - GET NUMBER OF TEXT CHOSEN")
    
    ## DECLARE VARIABLES
    TextChosen = []
    
    ## IF TEXT CHOSEN IS ALL FIVE (5) TORAH TEXTS...
    if len(ListOfDictsOfJSONStringsParsed) == 5:
        
        ## DECLARE VARIABLES
        LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 1)
        
        ## CREATE LIST OF BOOK NUMBERS SELECTED
        BookNumbers = list((range(1, LengthForRange, 1)))
        
        ## LOOP THROUGH LIST
        for each in BookNumbers:
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(each)
            
    ## ...ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) THE PROPHETS (NEVI'IM) TEXTS...
    elif len(ListOfDictsOfJSONStringsParsed) == 21:
        
        ## DECLARE VARIABLES
        LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 6)
        
        ## CREATE LIST OF BOOK NUMBERS SELECTED
        BookNumbers = list((range(6, LengthForRange, 1)))
        
        ## LOOP THROUGH LIST
        for each in BookNumbers:
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(each)
            
    ## ...ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) THE WRITINGS (K'TUVIM) TEXTS...
    elif len(ListOfDictsOfJSONStringsParsed) == 13:
        
        ## DECLARE VARIABLES
        LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 27)
        
        ## CREATE LIST OF BOOK NUMBERS SELECTED
        BookNumbers = list((range(27, LengthForRange, 1)))
        
        ## LOOP THROUGH LIST
        for each in BookNumbers:
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(each)
            
    ## ...ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) HEBREW BIBLE (TANACH) TEXTS...
    elif len(ListOfDictsOfJSONStringsParsed) == 39:
        
        ## DECLARE VARIABLES
        LengthForRange = (len(ListOfDictsOfJSONStringsParsed) + 1)
        
        ## CREATE LIST OF BOOK NUMBERS SELECTED
        BookNumbers = list((range(1, LengthForRange, 1)))
        
        ## LOOP THROUGH LIST
        for each in BookNumbers:
            
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(each)
    
    ## ...ELSE IF TEXT CHOSEN IS ONLY 1 (ONE) TEXT:
    elif len(ListOfDictsOfJSONStringsParsed) == 1:
    
        ## LOOP THROUGH LIST
        for each in ListOfDictsOfJSONStringsParsed:
             
            ## GET TEXT TITLE
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
                
                
            ## APPEND BOOK NUMBER TO LIST
            TextChosen.append(BookNumber)
    
    ## ELSE ALL OTHER CASES (NEVER CALLED)
    else:
        pass
      
    ## CONVERT LIST TO TUPLE
    TextChosen = tuple(TextChosen)
    
    ## TEST PRINT OUTPUT
    #print("\n")  ## PRINT SPACE
    #print("WITHIN FUNCTION:  END FUNCTION #5 - GET NUMBER OF TEXT CHOSEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextChosen)

## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN
## END FUNCTION () #5 - GET NUMBER OF TEXT CHOSEN