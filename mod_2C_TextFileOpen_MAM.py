## IMPORT MODULES
import csv

## TWO FUNCTIONS IN THIS MODULE
## FUNCTION () #2D FUNCTION #2 (SECOND FUNCTION IN THIS MODULE) - READ CSV FILE
def fn_TextFileCSVRead(File):

    """
    ## MODULE.FUNCTION() #2D - TEXT FILE CSV READ; ## RETURNS ##
    """

    ## DECLARE VARIABLES
    TextFile = [] 

    ## CALL FUNCTION
    CSVFile = csv.reader(File, delimiter=',')

    for ListOfRowCells in CSVFile: ## FOR LIST IN FILE
        
        ## APPEND ROW OF CELLS TO LIST
        TextFile.append((ListOfRowCells[0], ListOfRowCells[1]))

        ## TEST PRINT OUTPUT
        ## print(ListOfRowCells, type(ListOfRowCells))

    return(TextFile)


## FUNCTION () #2C FUNCTION #1 - TEXT FILE OPEN
def fn_TextFileOpen(TextChosen):

    """
    ## MODULE.FUNCTION() #2C - TEXT FILE OPEN; ## RETURNS TEXT FILE STRING
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #2C TEXT FILE OPEN")
          
    ## OPEN TEXT FILE
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...
    ## IF TEXT CHOSEN IS ONLY ONE (1) TEXT...

    ## IF TEXT CHOSEN IS 1:  GENESIS...    
    if TextChosen == 1:
        
        with open("texts/text_MAM_1genesis.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)

    ## ELSE IF TEXT CHOSEN IS 2:  EXODUS...
    elif TextChosen == 2:
        
        with open("texts/text_MAM_2exodus.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)

    ## ELSE IF TEXT CHOSEN IS 3:  LEVITICUS
    elif TextChosen == 3:
        
        with open("texts/text_MAM_3leviticus.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
    
    ## ELSE IF TEXT CHOSEN IS 4:  NUMBERS
    elif TextChosen == 4:
        
        with open("texts/text_MAM_4numbers.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
  
    ## ELSE IF TEXT CHOSEN IS 5:  DEUTERONOMY
    elif TextChosen == 5:
    
        with open("texts/text_MAM_5deuteronomy.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)

    ## ELSE IF TEXT CHOSEN IS 6:  JOSHUA
    elif TextChosen == 6:
    
        with open("texts/text_MAM_6joshua.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 7:  JUDGES
    elif TextChosen == 7:
    
        with open("texts/text_MAM_7judges.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)       
            
    ## ELSE IF TEXT CHOSEN IS 8:  I SAMUEL        
    elif TextChosen == 8:
    
        with open("texts/text_MAM_8Isamuel.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 9:  II SAMUEL        
    elif TextChosen == 9:
    
        with open("texts/text_MAM_9IIsamuel.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 10:  I KINGS
    elif TextChosen == 10:
    
        with open("texts/text_MAM_10Ikings.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 11:  II KINGS
    elif TextChosen == 11:
    
        with open("texts/text_MAM_11IIkings.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 12:  ISAIAH
    elif TextChosen == 12:
    
        with open("texts/text_MAM_12isaiah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 13:  JEREMIAH
    elif TextChosen == 13:
    
        with open("texts/text_MAM_13jeremiah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 14:  EZEKIEL
    elif TextChosen == 14:
    
        with open("texts/text_MAM_14ezekiel.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 15:  HOSEA
    elif TextChosen == 15:
    
        with open("texts/text_MAM_15hosea.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 16:  JOEL
    elif TextChosen == 16:
    
        with open("texts/text_MAM_16joel.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 17:  AMOS
    elif TextChosen == 17:
    
        with open("texts/text_MAM_17amos.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 18:  OBADIAH
    elif TextChosen == 18:
    
        with open("texts/text_MAM_18obadiah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 19:  JONAH
    elif TextChosen == 19:
    
        with open("texts/text_MAM_19jonah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 20:  MICAH
    elif TextChosen == 20:
    
        with open("texts/text_MAM_20micah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 21:  NAHUM
    elif TextChosen == 21:
    
        with open("texts/text_MAM_21nahum.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 22:  HABAKKUK
    elif TextChosen == 22:
    
        with open("texts/text_MAM_22habakkuk.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 23:  ZEPHANIAH
    elif TextChosen == 23:
    
        with open("texts/text_MAM_23zephaniah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 24:  HAGGAI
    elif TextChosen == 24:
    
        with open("texts/text_MAM_24haggai.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 25:  ZECHARIAH
    elif TextChosen == 25:
    
        with open("texts/text_MAM_25zechariah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 26:  MALACHI
    elif TextChosen == 26:
    
        with open("texts/text_MAM_26malachi.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 27:  PSALMS
    elif TextChosen == 27:
    
        with open("texts/text_MAM_27psalms.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 28:  PROVERBS
    elif TextChosen == 28:
    
        with open("texts/text_MAM_28proverbs.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 29:  JOB
    elif TextChosen == 29:
    
        with open("texts/text_MAM_29job.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 30:  SONG OF SONGS
    elif TextChosen == 30:
    
        with open("texts/text_MAM_30songofsongs.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 31:  RUTH
    elif TextChosen == 31:
    
        with open("texts/text_MAM_31ruth.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 32:  LAMENTATIONS
    elif TextChosen == 32:
    
        with open("texts/text_MAM_32lamentations.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 33:  ECCLESIASTES
    elif TextChosen == 33:
    
        with open("texts/text_MAM_33ecclesiastes.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 34:  ESTHER
    elif TextChosen == 34:
    
        with open("texts/text_MAM_34esther.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 35:  DANIEL
    elif TextChosen == 35:
    
        with open("texts/text_MAM_35daniel.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 36:  EZRA
    elif TextChosen == 36:
    
        with open("texts/text_MAM_36ezra.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 37:  NEHEMIAH
    elif TextChosen == 37:
    
        with open("texts/text_MAM_37nehemiah.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 38:  I CHRONICLES
    elif TextChosen == 38:
    
        with open("texts/text_MAM_38Ichronicles.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
            
    ## ELSE IF TEXT CHOSEN IS 39:  II CHRONICLES
    elif TextChosen == 39:
    
        with open("texts/text_MAM_39IIchronicles.csv", encoding="utf-8-sig") as File:
            ## TextFile = File.read()
            ## CALL FUNCTION
            TextFile = fn_TextFileCSVRead(File)
            TextFile = (TextFile,)
    
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...        
    ## ELSE IF TEXT CHOSEN IS ALL FIVE (5) BOOKS OF TORAH TOGETHER...
    elif TextChosen == 40:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_1genesis.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_2exodus.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 2 EXODUS
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
                
        ## READ STRING FILE TO TEXT FILE VARIABLE    
        with open("texts/text_MAM_3leviticus.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 3 LEVITICUS
            ## CALL FUNCTION
            TextFile3 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_4numbers.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 4 NUMBERS
            ## CALL FUNCTION
            TextFile4 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_5deuteronomy.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 5 DEUTERONOMY
            ## CALL FUNCTION
            TextFile5 = fn_TextFileCSVRead(File)
        
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5)
        
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL TWENTY-ONE (21) BOOKS OF THE PROPHETS (NEVI'IM) TOGETHER...
    elif TextChosen == 41:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_6joshua.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 6 JOSHUA
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_7judges.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 7 JUDGES
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_8Isamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            ## CALL FUNCTION
            TextFile3 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_9IIsamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            ## CALL FUNCTION
            TextFile4 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_10Ikings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            ## CALL FUNCTION
            TextFile5 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_11IIkings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            ## CALL FUNCTION
            TextFile6 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_12isaiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 12 ISAIAH
            ## CALL FUNCTION
            TextFile7 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_13jeremiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 13 JEREMIAH
            ## CALL FUNCTION
            TextFile8 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_14ezekiel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 14 EZEKIEL
            ## CALL FUNCTION
            TextFile9 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_15hosea.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 15 HOSEA
            ## CALL FUNCTION
            TextFile10 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_16joel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 16 JOEL
            ## CALL FUNCTION
            TextFile11 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_17amos.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 17 AMOS
            ## CALL FUNCTION
            TextFile12 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_18obadiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 18 OBADIAH
            ## CALL FUNCTION
            TextFile13 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_19jonah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 19 JONAH
            ## CALL FUNCTION
            TextFile14 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_20micah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 20 MICAH
            ## CALL FUNCTION
            TextFile15 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_21nahum.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 21 NAHUM
            ## CALL FUNCTION
            TextFile16 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_22habakkuk.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 22 HABAKKUK
            ## CALL FUNCTION
            TextFile17 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_23zephaniah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 23 ZEPHANIAH
            ## CALL FUNCTION
            TextFile18 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_24haggai.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 24 HAGGAI
            ## CALL FUNCTION
            TextFile19 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_25zechariah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 25 ZECHARIAH
            ## CALL FUNCTION
            TextFile20 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_26malachi.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 26 MALACHI
            ## CALL FUNCTION
            TextFile21 = fn_TextFileCSVRead(File)
            
        
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
        with open("texts/text_MAM_27psalms.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 27 PSALMS
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_28proverbs.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 28 PROVERBS
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_29job.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 29 JOB
            ## CALL FUNCTION
            TextFile3 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_30songofsongs.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 30 SONG OF SONGS
            ## CALL FUNCTION
            TextFile4 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_31ruth.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 31 RUTH
            ## CALL FUNCTION
            TextFile5 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_32lamentations.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 32 LAMENTATIONS
            ## CALL FUNCTION
            TextFile6 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_33ecclesiastes.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 33 ECCLESIASTES
            ## CALL FUNCTION
            TextFile7 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_34esther.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 34 ESTHER
            ## CALL FUNCTION
            TextFile8 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_35daniel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 35 DANIEL
            ## CALL FUNCTION
            TextFile9 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_36ezra.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            ## CALL FUNCTION
            TextFile10 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_37nehemiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            ## CALL FUNCTION
            TextFile11 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_38Ichronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            ## CALL FUNCTION
            TextFile12 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_39IIchronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            ## CALL FUNCTION
            TextFile13 = fn_TextFileCSVRead(File)
            
            
         ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2, TextFile3, TextFile4, TextFile5, \
                    TextFile6, TextFile7, TextFile8, TextFile9, TextFile10, \
                    TextFile11, TextFile12, TextFile13)
    
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    ## ELSE IF TEXT CHOSEN IS ALL THIRTY-NINE (39) BOOKS OF THE HEBREW BIBLE (TANACH) TOGETHER...
    elif TextChosen == 43:
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_1genesis.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 1 GENESIS
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_2exodus.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 2 EXODUS
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
                
        ## READ STRING FILE TO TEXT FILE VARIABLE    
        with open("texts/text_MAM_3leviticus.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 3 LEVITICUS
            ## CALL FUNCTION
            TextFile3 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_4numbers.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 4 NUMBERS
            ## CALL FUNCTION
            TextFile4 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_5deuteronomy.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 5 DEUTERONOMY
            ## CALL FUNCTION
            TextFile5 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_6joshua.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 6 JOSHUA
            ## CALL FUNCTION
            TextFile6 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_7judges.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 7 JUDGES
            ## CALL FUNCTION
            TextFile7 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_8Isamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            ## CALL FUNCTION
            TextFile8 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_9IIsamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            ## CALL FUNCTION
            TextFile9 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_10Ikings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            ## CALL FUNCTION
            TextFile10 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_11IIkings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            ## CALL FUNCTION
            TextFile11 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_12isaiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 12 ISAIAH
            ## CALL FUNCTION
            TextFile12 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_13jeremiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 13 JEREMIAH
            ## CALL FUNCTION
            TextFile13 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_14ezekiel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 14 EZEKIEL
            ## CALL FUNCTION
            TextFile14 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_15hosea.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 15 HOSEA
            ## CALL FUNCTION
            TextFile15 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_16joel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 16 JOEL
            ## CALL FUNCTION
            TextFile16 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_17amos.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 17 AMOS
            ## CALL FUNCTION
            TextFile17 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_18obadiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 18 OBADIAH
            ## CALL FUNCTION
            TextFile18 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_19jonah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 19 JONAH
            ## CALL FUNCTION
            TextFile19 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_20micah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 20 MICAH
            ## CALL FUNCTION
            TextFile20 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_21nahum.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 21 NAHUM
            ## CALL FUNCTION
            TextFile21 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_22habakkuk.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 22 HABAKKUK
            ## CALL FUNCTION
            TextFile22 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_23zephaniah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 23 ZEPHANIAH
            ## CALL FUNCTION
            TextFile23 = fn_TextFileCSVRead(File)
        
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_24haggai.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 24 HAGGAI
            ## CALL FUNCTION
            TextFile24 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_25zechariah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 25 ZECHARIAH
            ## CALL FUNCTION
            TextFile25 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_26malachi.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 26 MALACHI
            ## CALL FUNCTION
            TextFile26 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_27psalms.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 27 PSALMS
            ## CALL FUNCTION
            TextFile27 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_28proverbs.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 28 PROVERBS
            ## CALL FUNCTION
            TextFile28 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_29job.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 29 JOB
            ## CALL FUNCTION
            TextFile29 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_30songofsongs.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 30 SONG OF SONGS
            ## CALL FUNCTION
            TextFile30 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_31ruth.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 31 RUTH
            ## CALL FUNCTION
            TextFile31 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_32lamentations.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 32 LAMENTATIONS
            ## CALL FUNCTION
            TextFile32 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_33ecclesiastes.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 33 ECCLESIASTES
            ## CALL FUNCTION
            TextFile33 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_34esther.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 34 ESTHER
            ## CALL FUNCTION
            TextFile34 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_35daniel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 35 DANIEL
            ## CALL FUNCTION
            TextFile35 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_36ezra.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            ## CALL FUNCTION
            TextFile36 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_37nehemiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            ## CALL FUNCTION
            TextFile37 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_38Ichronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            ## CALL FUNCTION
            TextFile38 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_39IIchronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            ## CALL FUNCTION
            TextFile39 = fn_TextFileCSVRead(File) 
            
        
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
        with open("texts/text_MAM_8Isamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 8 I SAMUEL
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_9IIsamuel.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 9 II SAMUEL
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
            
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2)
        
    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF KINGS TOGETHER...
    elif TextChosen == 45:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_10Ikings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 10 I KINGS
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_11IIkings.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 11 II KINGS
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
            
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2)

    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF EZRA-NEHEMIAH TOGETHER...
    elif TextChosen == 46:

        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_36ezra.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 36 EZRA
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_37nehemiah.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 37 NEHEMIAH
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File)
            
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2)

        
    ## ELSE IF TEXT CHOSEN IS BOTH BOOKS OF CHRONICLES TOGETHER...
    elif TextChosen == 47:

                ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_38Ichronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 38 I CHRONICLES
            ## CALL FUNCTION
            TextFile1 = fn_TextFileCSVRead(File)
            
        ## READ STRING FILE TO TEXT FILE VARIABLE
        with open("texts/text_MAM_39IIchronicles.csv", encoding="utf-8-sig") as File:
            
            ## TEXT CHOSEN: 39 II CHRONICLES
            ## CALL FUNCTION
            TextFile2 = fn_TextFileCSVRead(File) 
            
        ## ...THEN CREATE A TUPLE OF TEXT/STRING FILES
        TextFile = (TextFile1, TextFile2)


    ## END IF ELSE BLOCK

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #2C - TEXT FILE OPEN")

    ## RETURN VARIABLES TO PROGRAM
    return(TextFile)

## END FUNCTION () #2C - TEXT FILE OPEN

