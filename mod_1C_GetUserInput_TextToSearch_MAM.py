## FUNCTION () #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH ###

def fn_GetUserInput(NumberOfCodexChosen):

    """
    ## MODULE.FUNCTION() #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH; ## RETURNS INTEGER ##
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    match NumberOfCodexChosen:

        case 1: 
            NameOfCodex = "Koren Codex"
        case 2:
            NameOfCodex = "Leningrad Codex"
        case 3:
            NameOfCodex = "Miqra According to the Masorah (MAM) Collection of Manuscripts"
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print(f"Please select text to search in the {NameOfCodex}:")
    print("\n")  ## PRINT SPACE
    print("1 - Genesis - 78063 letters")
    print("2 - Exodus - 63527 letters")
    print("3 - Leviticus - 44790 letters")
    print("4 - Numbers - 63529 letters")
    print("5 - Deuteronomy - 54892 letters")
    print("6 - Joshua - 39730 letters")
    print("7 - Judges - 38952 letters")
    print("8 - I Samuel - 51357 letters")
    print("9 - II Samuel - 42179 letters")
    print("10 - I Kings - 50625 letters")
    print("11 - II Kings - 47822 letters")
    print("12 - Isaiah - 66874 letters")
    print("13 - Jeremiah - 84899 letters")
    print("14 - Ezekiel - 74510 letters")
    print("15 - Hosea - 9389 letters")
    print("16 - Joel - 3872 letters")
    print("17 - Amos - 8034 letters")
    print("18 - Obadiah - 1119 letters")
    print("19 - Jonah - 2700 letters")
    print("20 - Micah - 5571 letters")
    print("21 - Nahum - 2255 letters")
    print("22 - Habakkuk - 2596 letters")
    print("23 - Zephaniah - 2995 letters")
    print("24 - Haggai - 2336 letters")
    print("25 - Zechariah - 12433 letters")
    print("26 - Malachi - 3450 letters")
    print("27 - Psalms - 78822 letters")
    print("28 - Proverbs - 26500 letters")
    print("29 - Job - 31851 letters")
    print("30 - Song of Songs - 5141 letters")
    print("31 - Ruth - 4949 letters")
    print("32 - Lamentations - 5974 letters")
    print("33 - Ecclesiastes - 10968 letters")
    print("34 - Esther - 12110 letters")
    print("35 - Daniel - 24280 letters")
    print("36 - Ezra - 15762 letters")
    print("37 - Nehemiah - 22507 letters")
    print("38 - I Chronicles - 44559 letters")
    print("39 - II Chronicles - 54917 letters")
    print("\n")  ## PRINT SPACE 
    print("40 - Pentateuch (Torah) - 304801 letters")
    print("41 - Prophets (Nevi'im) - 553698 letters")
    print("42 - Writings (K'tuvim) - 338340 letters")
    print("43 - Hebrew Bible (Tanach) - 1196839 letters")
    print("\n")  ## PRINT SPACE
    print("44 - Samuel (I Samuel and II Samuel as one book) - 93536 letters")
    print("45 - Kings (I Kings and II Kings as one book) - 98447 letters")
    print("46 - Ezra-Nehemiah (Ezra and Nehemiah as one book) - 38269 letters")
    print("47 - Chronicles (I Chronicles and II Chronicles as one book) - 99476 letters")
    
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please select text to search:  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfTextChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen text number # {NumberOfTextChosen}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfTextChosen)

## END FUNCTION () #1C - GET USER INPUT; CHOOSE TEXT TO SEARCH
