## FUNCTION () #2 - TEXT FILE OPEN
## FUNCTION () #2 - TEXT FILE OPEN
## FUNCTION () #2 - TEXT FILE OPEN
def fn_TextFileOpen(TextChosen):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #2 TEXT FILE OPEN")
          
    ## OPEN TEXT FILE
    ## IF TEXT CHOSEN IS 1 GENESIS...    
    if TextChosen == 1:
        
        with open("text_1genesis.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 2 EXODUS...
    elif TextChosen == 2:
        
        with open("text_2exodus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 3 LEVITICUS
    elif TextChosen == 3:
        
        with open("text_3leviticus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
    
    ## ELSE IF TEXT CHOSEN IS 4 NUMBERS
    elif TextChosen == 4:
        
        with open("text_4numbers.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 5 DEUTERONOMY
    elif TextChosen == 5:
    
        with open("text_5deuteronomy.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    elif TextChosen == 6:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_1genesis.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            TextFile1 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_2exodus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 2 EXODUS
            TextFile2 = File.read()
                
        ## READ STRING FILE TO TEXT FILE VARIABLE    
        with open("text_3leviticus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 3 LEVITICUS
            TextFile3 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_4numbers.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 4 NUMBERS
            TextFile4 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_5deuteronomy.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 5 DEUTERONOMY
            TextFile5 = File.read()
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5)    
          

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #2 - TEXT FILE OPEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextFile)

## END FUNCTION () #2 - TEXT FILE OPEN
## END FUNCTION () #2 - TEXT FILE OPEN
## END FUNCTION () #2 - TEXT FILE OPEN
