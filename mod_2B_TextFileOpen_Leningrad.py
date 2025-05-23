## FUNCTION () #2B - TEXT FILE OPEN ##

def fn_TextFileOpen(TextChosen):

    """
    ## MODULE.FUNCTION() #2B - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING ##
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION - #2B TEXT FILE OPEN")
          
    ## OPEN TEXT FILE
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    
    ## IF TEXT CHOSEN IS 1:  GENESIS...    
    if TextChosen == 1:
        
        with open("texts/text_leningrad_1genesis.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 2:  EXODUS...
    elif TextChosen == 2:
        
        with open("texts/text_leningrad_2exodus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 3:  LEVITICUS
    elif TextChosen == 3:
        
        with open("texts/text_leningrad_3leviticus.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
    
    ## ELSE IF TEXT CHOSEN IS 4:  NUMBERS
    elif TextChosen == 4:
        
        with open("texts/text_leningrad_4numbers.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
        
    ## ELSE IF TEXT CHOSEN IS 5:  DEUTERONOMY
    elif TextChosen == 5:
    
        with open("texts/text_leningrad_5deuteronomy.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 6:  JOSHUA
    elif TextChosen == 6:
    
        with open("texts/text_leningrad_6joshua.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 7:  JUDGES
    elif TextChosen == 7:
    
        with open("texts/text_leningrad_7judges.json", encoding="utf-8-sig") as File:
            TextFile = File.read()       
            
    ## ELSE IF TEXT CHOSEN IS 8:  I SAMUEL        
    elif TextChosen == 8:
    
        with open("texts/text_leningrad_8Isamuel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 9:  II SAMUEL        
    elif TextChosen == 9:
    
        with open("texts/text_leningrad_9IIsamuel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 10:  I KINGS
    elif TextChosen == 10:
    
        with open("texts/text_leningrad_10Ikings.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 11:  II KINGS
    elif TextChosen == 11:
    
        with open("texts/text_leningrad_11IIkings.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 12:  ISAIAH
    elif TextChosen == 12:
    
        with open("texts/text_leningrad_12isaiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 13:  JEREMIAH
    elif TextChosen == 13:
    
        with open("texts/text_leningrad_13jeremiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 14:  EZEKIEL
    elif TextChosen == 14:
    
        with open("texts/text_leningrad_14ezekiel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 15:  HOSEA
    elif TextChosen == 15:
    
        with open("texts/text_leningrad_15hosea.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 16:  JOEL
    elif TextChosen == 16:
    
        with open("texts/text_leningrad_16joel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 17:  AMOS
    elif TextChosen == 17:
    
        with open("texts/text_leningrad_17amos.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 18:  OBADIAH
    elif TextChosen == 18:
    
        with open("texts/text_leningrad_18obadiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 19:  JONAH
    elif TextChosen == 19:
    
        with open("texts/text_leningrad_19jonah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 20:  MICAH
    elif TextChosen == 20:
    
        with open("texts/text_leningrad_20micah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 21:  NAHUM
    elif TextChosen == 21:
    
        with open("texts/text_leningrad_21nahum.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 22:  HABAKKUK
    elif TextChosen == 22:
    
        with open("texts/text_leningrad_22habakkuk.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 23:  ZEPHANIAH
    elif TextChosen == 23:
    
        with open("texts/text_leningrad_23zephaniah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 24:  HAGGAI
    elif TextChosen == 24:
    
        with open("texts/text_leningrad_24haggai.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 25:  ZECHARIAH
    elif TextChosen == 25:
    
        with open("texts/text_leningrad_25zechariah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 26:  MALACHI
    elif TextChosen == 26:
    
        with open("texts/text_leningrad_26malachi.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 27:  PSALMS
    elif TextChosen == 27:
    
        with open("texts/text_leningrad_27psalms.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 28:  PROVERBS
    elif TextChosen == 28:
    
        with open("texts/text_leningrad_28proverbs.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 29:  JOB
    elif TextChosen == 29:
    
        with open("texts/text_leningrad_29job.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 30:  SONG OF SONGS
    elif TextChosen == 30:
    
        with open("texts/text_leningrad_30songofsongs.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 31:  RUTH
    elif TextChosen == 31:
    
        with open("texts/text_leningrad_31ruth.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 32:  LAMENTATIONS
    elif TextChosen == 32:
    
        with open("texts/text_leningrad_32lamentations.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 33:  ECCLESIASTES
    elif TextChosen == 33:
    
        with open("texts/text_leningrad_33ecclesiastes.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 34:  ESTHER
    elif TextChosen == 34:
    
        with open("texts/text_leningrad_34esther.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 35:  DANIEL
    elif TextChosen == 35:
    
        with open("texts/text_leningrad_35daniel.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 36:  EZRA
    elif TextChosen == 36:
    
        with open("texts/text_leningrad_36ezra.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 37:  NEHEMIAH
    elif TextChosen == 37:
    
        with open("texts/text_leningrad_37nehemiah.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 38:  I CHRONICLES
    elif TextChosen == 38:
    
        with open("texts/text_leningrad_38Ichronicles.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS 39:  II CHRONICLES
    elif TextChosen == 39:
    
        with open("texts/text_leningrad_39IIchronicles.json", encoding="utf-8-sig") as File:
            TextFile = File.read()
            
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...        
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    elif TextChosen == 40:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_1genesis.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            TextFile1 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_2exodus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 2 EXODUS
            TextFile2 = File.read()
                
        ## READ STRING FILE TO TEXT FILE VARIABLE    
        with open("texts/text_leningrad_3leviticus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 3 LEVITICUS
            TextFile3 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_4numbers.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 4 NUMBERS
            TextFile4 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_5deuteronomy.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 5 DEUTERONOMY
            TextFile5 = File.read()
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5)
        
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    elif TextChosen == 41:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_6joshua.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 6 JOSHUA
            TextFile1 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_7judges.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 7 JUDGES
            TextFile2 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_8Isamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            TextFile3 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_9IIsamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            TextFile4 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_10Ikings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            TextFile5 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_11IIkings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            TextFile6 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_12isaiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 12 ISAIAH
            TextFile7 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_13jeremiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 13 JEREMIAH
            TextFile8 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_14ezekiel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 14 EZEKIEL
            TextFile9 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_15hosea.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 15 HOSEA
            TextFile10 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_16joel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 16 JOEL
            TextFile11 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_17amos.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 17 AMOS
            TextFile12 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_18obadiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 18 OBADIAH
            TextFile13 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_19jonah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 19 JONAH
            TextFile14 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_20micah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 20 MICAH
            TextFile15 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_21nahum.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 21 NAHUM
            TextFile16 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_22habakkuk.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 22 HABAKKUK
            TextFile17 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_23zephaniah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 23 ZEPHANIAH
            TextFile18 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_24haggai.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 24 HAGGAI
            TextFile19 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_25zechariah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 25 ZECHARIAH
            TextFile20 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_26malachi.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 26 MALACHI
            TextFile21 = File.read()
            
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, \
                    TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, \
                    TextFile11, TextFile12, TextFile13, TextFile14, TextFile15, \
                    TextFile16, TextFile17, TextFile18, TextFile19, TextFile20, \
                    TextFile21)
          
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTEEN (13) BOOKS OF THE WRITINGS (K'TUVIM) TOGETHER...
    elif TextChosen == 42:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_27psalms.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 27 PSALMS
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_28proverbs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 28 PROVERBS
            TextFile2 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_29job.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 29 JOB
            TextFile3 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_30songofsongs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 30 SONG OF SONGS
            TextFile4 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_31ruth.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 31 RUTH
            TextFile5 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_32lamentations.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 32 LAMENTATIONS
            TextFile6 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_33ecclesiastes.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 33 ECCLESIASTES
            TextFile7 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_34esther.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 34 ESTHER
            TextFile8 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_35daniel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 35 DANIEL
            TextFile9 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_36ezra.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            TextFile10 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_37nehemiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            TextFile11 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_38Ichronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            TextFile12 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_39IIchronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            TextFile13 = File.read()
            
            
         ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, \
                    TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, \
                    TextFile11, TextFile12, TextFile13)
    
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    elif TextChosen == 43:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_1genesis.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            TextFile1 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_2exodus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 2 EXODUS
            TextFile2 = File.read()
                
        ## READ STRING FILE TO TEXT FILE VARIABLE    
        with open("texts/text_leningrad_3leviticus.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 3 LEVITICUS
            TextFile3 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_4numbers.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 4 NUMBERS
            TextFile4 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_5deuteronomy.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 5 DEUTERONOMY
            TextFile5 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_6joshua.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 6 JOSHUA
            TextFile6 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_7judges.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 7 JUDGES
            TextFile7 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_8Isamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            TextFile8 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_9IIsamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            TextFile9 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_10Ikings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            TextFile10 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_11IIkings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            TextFile11 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_12isaiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 12 ISAIAH
            TextFile12 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_13jeremiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 13 JEREMIAH
            TextFile13 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_14ezekiel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 14 EZEKIEL
            TextFile14 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_15hosea.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 15 HOSEA
            TextFile15 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_16joel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 16 JOEL
            TextFile16 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_17amos.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 17 AMOS
            TextFile17 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_18obadiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 18 OBADIAH
            TextFile18 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_19jonah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 19 JONAH
            TextFile19 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_20micah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 20 MICAH
            TextFile20 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_21nahum.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 21 NAHUM
            TextFile21 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_22habakkuk.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 22 HABAKKUK
            TextFile22 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_23zephaniah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 23 ZEPHANIAH
            TextFile23 = File.read()
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_24haggai.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 24 HAGGAI
            TextFile24 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_25zechariah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 25 ZECHARIAH
            TextFile25 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_26malachi.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 26 MALACHI
            TextFile26 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_27psalms.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 27 PSALMS
            TextFile27 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_28proverbs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 28 PROVERBS
            TextFile28 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_29job.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 29 JOB
            TextFile29 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_30songofsongs.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 30 SONG OF SONGS
            TextFile30 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_31ruth.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 31 RUTH
            TextFile31 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_32lamentations.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 32 LAMENTATIONS
            TextFile32 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_33ecclesiastes.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 33 ECCLESIASTES
            TextFile33 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_34esther.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 34 ESTHER
            TextFile34 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_35daniel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 35 DANIEL
            TextFile35 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_36ezra.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            TextFile36 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_37nehemiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            TextFile37 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_38Ichronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            TextFile38 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_39IIchronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            TextFile39 = File.read()    
            
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, \
                    TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, \
                    TextFile11, TextFile12, TextFile13, TextFile14, TextFile15, \
                    TextFile16, TextFile17, TextFile18, TextFile19, TextFile20, \
                    TextFile21, TextFile22, TextFile23, TextFile24, TextFile25, \
                    TextFile26, TextFile27, TextFile28, TextFile29, TextFile30, \
                    TextFile31, TextFile32, TextFile33, TextFile34, TextFile35, \
                    TextFile36, TextFile37, TextFile38, TextFile39)
        
    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF SAMUEL TOGETHER...
    elif TextChosen == 44:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_8Isamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_9IIsamuel.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            TextFile2 = File.read()

        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2) 
        
    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF KINGS TOGETHER...
    elif TextChosen == 45:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_10Ikings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_11IIkings.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            TextFile2 = File.read()

        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2) 
        
    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF EZRA AND NEHEMIAH TOGETHER...
    elif TextChosen == 46:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_36ezra.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_37nehemiah.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            TextFile2 = File.read()

        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2) 

    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF CHRONICLES TOGETHER...
    elif TextChosen == 47:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_38Ichronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            TextFile1 = File.read()
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_leningrad_39IIchronicles.json", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            TextFile2 = File.read()

        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2) 

    ## END IF ELSE BLOCK
             
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #2B - TEXT FILE OPEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextFile)

## END FUNCTION () #2B - TEXT FILE OPEN

