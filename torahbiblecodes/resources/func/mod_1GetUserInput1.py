## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
def fn_GetUserInput1():

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("Please select text to search:")
    print("1 - Genesis")
    print("2 - Exodus")
    print("3 - Leviticus")
    print("4 - Numbers")
    print("5 - Deuteronomy")
    print("6 - Joshua")
    print("7 - Judges")
    print("8 - I Samuel")
    print("9 - II Samuel")
    print("10 - I Kings")
    print("11 - II Kings")
    print("12 - Isaiah")
    print("13 - Jeremiah")
    print("14 - Ezekiel")
    print("15 - Hosea")
    print("16 - Joel")
    print("17 - Amos")
    print("18 - Obadiah")
    print("19 - Jonah")
    print("20 - Micah")
    print("21 - Nahum")
    print("22 - Habakkuk")
    print("23 - Zephaniah")
    print("24 - Haggai")
    print("25 - Zechariah")
    print("26 - Malachi")
    print("27 - Psalms")
    print("28 - Proverbs")
    print("29 - Job")
    print("30 - Song of Songs")
    print("31 - Ruth")
    print("32 - Lamentations")
    print("33 - Ecclesiastes")
    print("34 - Esther")
    print("35 - Daniel")
    print("36 - Ezra")
    print("37 - Nehemiah")
    print("38 - I Chronicles")
    print("39 - II Chronicles") 
    print("40 - Pentateuch (Torah)")
    print("41 - Prophets (Nevi'im)")
    print("42 - Writings (K'tuvim)")
    print("43 - Hebrew Bible (Tanach)")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    TextString = input("Please select text to search:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfTextChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("You have chosen:  ", NumberOfTextChosen, type(NumberOfTextChosen))

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfTextChosen)

## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
## END FUNCTION () #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
