## FUNCTION () #2 - TEXT FILE OPEN
## FUNCTION () #2 - TEXT FILE OPEN
## FUNCTION () #2 - TEXT FILE OPEN
def fn_TextFileOpen(TextChosen):

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #2 TEXT FILE OPEN")
          
    ## OPEN TEXT FILE
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    
    ## IF TEXT CHOSEN IS 1:  GENESIS...    
    if TextChosen == 1:
        
        with open("text_1genesis.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 2:  EXODUS...
    elif TextChosen == 2:
        
        with open("text_2exodus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 3:  LEVITICUS
    elif TextChosen == 3:
        
        with open("text_3leviticus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
    
    ## ELSE IF TEXT CHOSEN IS 4:  NUMBERS
    elif TextChosen == 4:
        
        with open("text_4numbers.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 5:  DEUTERONOMY
    elif TextChosen == 5:
    
        with open("text_5deuteronomy.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 6:  JOSHUA
    elif TextChosen == 6:
    
        with open("text_6joshua.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 7:  JUDGES
    elif TextChosen == 7:
    
        with open("text_7judges.json", encoding="utf-8-sig") as File:
            TextFile = File.read()       
            
    ## ELSE IF TEXT CHOSEN IS 8:  I SAMUEL        
    elif TextChosen == 8:
    
        with open("text_8Isamuel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 9:  II SAMUEL        
    elif TextChosen == 9:
    
        with open("text_9IIsamuel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 10:  I KINGS
    elif TextChosen == 10:
    
        with open("text_10Ikings.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 11:  II KINGS
    elif TextChosen == 11:
    
        with open("text_11IIkings.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 12:  ISAIAH
    elif TextChosen == 12:
    
        with open("text_12isaiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 13:  JEREMIAH
    elif TextChosen == 13:
    
        with open("text_13jeremiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 14:  EZEKIEL
    elif TextChosen == 14:
    
        with open("text_14ezekiel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 15:  HOSEA
    elif TextChosen == 15:
    
        with open("text_15hosea.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 16:  JOEL
    elif TextChosen == 16:
    
        with open("text_16joel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 17:  AMOS
    elif TextChosen == 17:
    
        with open("text_17amos.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 18:  OBADIAH
    elif TextChosen == 18:
    
        with open("text_18obadiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 19:  JONAH
    elif TextChosen == 19:
    
        with open("text_19jonah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 20:  MICAH
    elif TextChosen == 20:
    
        with open("text_20micah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 21:  NAHUM
    elif TextChosen == 21:
    
        with open("text_21nahum.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 22:  HABAKKUK
    elif TextChosen == 22:
    
        with open("text_22habakkuk.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 23:  ZEPHANIAH
    elif TextChosen == 23:
    
        with open("text_23zephaniah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 24:  HAGGAI
    elif TextChosen == 24:
    
        with open("text_24haggai.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 25:  ZECHARIAH
    elif TextChosen == 25:
    
        with open("text_25zechariah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 26:  MALACHI
    elif TextChosen == 26:
    
        with open("text_26malachi.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 27:  PSALMS
    elif TextChosen == 27:
    
        with open("text_27psalms.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 28:  PROVERBS
    elif TextChosen == 28:
    
        with open("text_28proverbs.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 29:  JOB
    elif TextChosen == 29:
    
        with open("text_29job.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 30:  SONG OF SONGS
    elif TextChosen == 30:
    
        with open("text_30songofsongs.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 31:  RUTH
    elif TextChosen == 31:
    
        with open("text_31ruth.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 32:  LAMENTATIONS
    elif TextChosen == 32:
    
        with open("text_32lamentations.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 33:  ECCLESIASTES
    elif TextChosen == 33:
    
        with open("text_33ecclesiastes.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 34:  ESTHER
    elif TextChosen == 34:
    
        with open("text_34esther.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 35:  DANIEL
    elif TextChosen == 35:
    
        with open("text_35daniel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 36:  EZRA
    elif TextChosen == 36:
    
        with open("text_36ezra.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 37:  NEHEMIAH
    elif TextChosen == 37:
    
        with open("text_37nehemiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 38:  I CHRONICLES
    elif TextChosen == 38:
    
        with open("text_38Ichronicles.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 39:  II CHRONICLES
    elif TextChosen == 39:
    
        with open("text_39IIchronicles.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...        
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    elif TextChosen == 40:
        
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
        
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    elif TextChosen == 41:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_6joshua.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            TextFile1 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_7judges.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile2 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_8Isamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile3 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_9IIsamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile4 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_10Ikings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile5 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_11IIkings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile6 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_12isaiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile7 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_13jeremiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile8 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_14ezekiel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile9 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_15hosea.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile10 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_16joel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile11 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_17amos.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile12 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_18obadiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile13 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_19jonah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile14 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_20micah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile15 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_21nahum.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile16 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_22habakkuk.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile17 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_23zephaniah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile18 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_24haggai.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile19 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_25zechariah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile20 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_26malachi.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 
            TextFile21 = File.read()
            
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, TextFile11, TextFile12, TextFile13, TextFile14, TextFile15, TextFile16, TextFile17, TextFile18, TextFile19, TextFile20, TextFile21)
          
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    elif TextChosen == 42:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_27psalms.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_28proverbs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile2 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_29job.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile3 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_30songofsongs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile4 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_31ruth.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile5 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_32lamentations.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile6 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_33ecclesiastes.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile7 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_34esther.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile8 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_35daniel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile9 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_36ezra.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile10 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_37nehemiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile11 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_12Ichronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile12 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("text_13IIchronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN:
            TextFile13 = File.read()
            
            
         ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, TextFile11, TextFile12, TextFile13)
            
            
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #2 - TEXT FILE OPEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextFile)

## END FUNCTION () #2 - TEXT FILE OPEN
## END FUNCTION () #2 - TEXT FILE OPEN
## END FUNCTION () #2 - TEXT FILE OPEN
