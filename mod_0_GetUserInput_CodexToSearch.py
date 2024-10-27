## FUNCTION () #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER ##

def fn_GetUserInput():

    """
    ## MODULE.FUNCTION() #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER ##
    """

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  BEGIN FUNCTION #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER")
    
    ## GET USER INPUT
    print("\n")  ## PRINT SPACE
    print("Please select Hebrew Bible codex to search:")
    print("\n")  ## PRINT SPACE
    print("""1 - Koren Codex - Claremont Michigan Transliteration: [Torah: 304805]""")
      
    print("\n")  ## PRINT SPACE
    print("""2 - Leningrad Codex: [Torah: 304850; Prophets: 553785; Writings: 338407; Tanach: 1197042]""")

    print("\n")  ## PRINT SPACE
    print("""3 - Miqra According to the Masorah (MAM) Collection of Manuscripts: [Torah: 304801; Prophets: 553698; Writings: 338340; Tanach: 1196839]""")
   
    ## TEXT CHOSEN = USER INPUT (TEXT STRING)
    print("\n")  ## PRINT SPACE
    TextString = input("Please select codex (collection of manuscripts) to search (1: Koren; 2: Leningrad; 3: MAM):  ")
    
    ## CONVERT TEXT STRING TO INTEGER
    NumberOfCodexChosen = int(TextString)
    
    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"You have chosen codex number # {NumberOfCodexChosen}.")

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print("WITHIN FUNCTION:  END FUNCTION #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH; ## RETURNS INTEGER")

    ## RETURN VARIABLES TO PROGRAM
    return(NumberOfCodexChosen)

## END FUNCTION () #0 - GET USER INPUT; CHOOSE CODEX TO SEARCH
