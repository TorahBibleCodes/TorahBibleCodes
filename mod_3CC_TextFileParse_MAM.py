## IMPORT MODULES
import re

## BEGIN FUNCTION() - #1 - REMOVE HTML TAGS
def fn_RemoveHTMLTags(TextString):
    HTMLFreeText = re.compile('<.*?>')

    ## RETURN VARIABLES
    return(re.sub(HTMLFreeText, '', TextString))

## END FUNCTION

## BEGIN FUNCTION() - #2 - REMOVE CURLY BRACKETS AND ANYTHING IN BETWEEN
def fn_RemoveCurlyBracketsAndContent(text):

    ## DEFINE PATTERN: MATCH CURLY BRACKETS AND ANYTHING IN BETWEEN
    pattern = r'\{.*?\}'

    ## REPLACE MATCHED PATTERNS WITH EMPTY STRING
    clean_text = re.sub(pattern, '', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION - #3 - REMOVE &NBSP; AND &THINSP;
def fn_RemoveNBSP(text):

    ## DEFINE PATTERN: MATCH &nbsp; AND $thinsp;
    pattern = r'(&nbsp;|&thinsp;)'

    ## REPLACE MATCHED PATTERNS WITH EMPTY STRING
    clean_text = re.sub(pattern, ' ', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION() - #4 - REMOVE SQUARE BRACKETS AND ANYTHING IN BETWEEN
def fn_RemoveSquareBracketsAndContent(text):

    ## DEFINE PATTERN: MATCH SQUARE BRACKETS & EVERYTHING IN BETWEEN
    pattern = r'\[.*?\]'

    ## REPLACE MATCHED PATTERNS WITH EMPTY STRING
    clean_text = re.sub(pattern, '', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION() - #5 - REMOVE PARENTHESES BUT LEAVE EVERYTHING IN BETWEEN
def fn_RemoveParenthesesOnly(text):
    
    ## PATTERN TO MATCH PARENTHESES BUT NOT TOUCH THE CONTENT WITHIN THEM
    pattern = r'\(|\)'

    ## REPLACE THE MATCHED PATTERNS WITH AN EMPTY STRING
    clean_text = re.sub(pattern, '', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION() - #6 - REMOVE PASEQ
def fn_RemovePaseq(text):

    ## PATTERN TO MATCH PASEQ
    pattern = r'\u05C0'  # Paseq

    ## REPLACE THE MATCHED PATTERNS WITH AN EMPTY STRING
    clean_text = re.sub(pattern, ' ', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION() - #7 - REMOVE COMBINING GRAPHEME JOINER
def fn_RemoveCombiningGraphemeJoiner(text):

    ## PATTERN TO MATCH 
    pattern = r'\u034F' ## COMBINING GRAPHEME JOINER

    ## REPLACE THE MATCHED PATTERNS WITH AN EMPTY STRING
    clean_text = re.sub(pattern, '', text)

    ## RETURN VARIABLES
    return(clean_text)

## END FUNCTION

## BEGIN FUNCTION
## FUNCTION () #3CC - #0 - TEXT FILE PARSE
def fn_TextFileParse(TextString):

    """
    ## MODULE.FUNCTION() #3CC - TEXT FILE PARSE ## RETURNS TextParsedWithSpaces, TextParsedNoSpaces
    """

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("WITHIN FUNCTION:  BEGIN FUNCTION #3CC TEXT FILE PARSE") ## PRINTS FOR EACH VERSE
         
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(TextString)
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("Length of TextString :", len(TextString), type(TextString))
    
    ## BEGIN TEXT FILE PARSE

    """
    ## REMOVE PASEQ
    TextWithNoPaseq = fn_RemovePaseq(TextString)

    ## TEST PRINT OUTPUT
    print("\n")  ## PRINT SPACE
    print(f"TextWithNoPaseq : {TextWithNoPaseq}")
    print(f"TextWithNoPaseq : {TextWithNoPaseq[::-1]}")
    """

    ## REMOVE HTML TAGS FROM THE STRING (EACH VERSE)
    HTMLFreeText = fn_RemoveHTMLTags(TextString)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"HTMLFreeText : {HTMLFreeText}")
    ## print(f"HTMLFreeText : {HTMLFreeText[::-1]}")

    ## REMOVE CURLY BRACKETS INCLUDING EVERYTHING IN BETWEEN
    TextWithNoCurlyBrackets = fn_RemoveCurlyBracketsAndContent(HTMLFreeText)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoCurlyBrackets : {TextWithNoCurlyBrackets}")
    ## print(f"TextWithNoCurlyBrackets : {TextWithNoCurlyBrackets[::-1]}")


    ## REMOVE &nbsp; &thinsp;
    TextWithNoNBSP = fn_RemoveNBSP(TextWithNoCurlyBrackets)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoNBSP : {TextWithNoNBSP}")
    ## print(f"TextWithNoNBSP : {TextWithNoNBSP[::-1]}")

    ## REMOVE SQUARE BRACKETS INCLUDING EVERYTHING IN BETWEEN
    TextWithNoSquareBrackets = fn_RemoveSquareBracketsAndContent(TextWithNoNBSP)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoSquareBrackets : {TextWithNoSquareBrackets}")
    ## print(f"TextWithNoSquareBrackets : {TextWithNoSquareBrackets[::-1]}")

    ## REMOVE PARENTHESES
    TextWithNoParentheses = fn_RemoveParenthesesOnly(TextWithNoSquareBrackets)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoParentheses : {TextWithNoParentheses}")
    ## print(f"TextWithNoParentheses : {TextWithNoParentheses[::-1]}")

    TextWithNoCombiningGraphemeJoiner = fn_RemoveCombiningGraphemeJoiner(TextWithNoParentheses)

    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print(f"TextWithNoCombiningGraphemeJoiner : {TextWithNoCombiningGraphemeJoiner}")
    ## print(f"TextWithNoCombiningGraphemeJoiner : {TextWithNoCombiningGraphemeJoiner[::-1]}")

    ## REMOVE MAQAFS FROM STRING - MOVED TO MOD_3C
    ## TextNoHyphensWithSpaces = TextWithNoCurlyBrackets.replace("־", " ")

    ## CHANGE VARIABLE NAME
    TextParsedWithSpaces = TextWithNoCombiningGraphemeJoiner

    ## REMOVE SPACES FROM STRING
    TextParsedNoSpaces = TextParsedWithSpaces.replace(" ", "")

    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextNoSpaces =", len(TextNoSpaces), type(TextNoSpaces))
    
    ## DECLARE VARIABLE TO DEAL WITH THE "WORDS" WITH EMPTY STRINGS
    ListOfWords = []

    ## SPLIT TEXT INTO INDIVIDUAL WORDS: CREATES LIST OF WORDS
    ListOfWordsInVerse = list(TextParsedWithSpaces.split(" "))

    ## BEGIN FOR LOOP
    for each in ListOfWordsInVerse:

        ## BEGIN IF / ELSE... DEAL WITH THE "WORDS" WITH EMPTY STRINGS
        if each =='':
            pass
        else: 
            ListOfWords.append(each)
        ## END IF / ELSE

    ## END FOR LOOP

    ## TEST PRINT OUTPUT
    ## print(SplitText)

    ## JOIN LIST OF WORDS
    TextParsedWithSpaces = " ".join(ListOfWords)
    ## print("\n")
    ## print(TextParsedWithSpaces)

    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextParsedWithSpaces =", len(TextParsedWithSpaces), type(TextParsedWithSpaces))
    
    ## TEST PRINT OUTPUT
    ##print("\n")  ## PRINT SPACE
    ##print("Length of TextParsedNoSpaces =", len(TextParsedNoSpaces), type(TextParsedNoSpaces))

    ## END TEXT FILE PARSE
  
    ## CHANGE VARIABLE NAMES
    ##TextParsedWithSpaces = TextParsedWithSpaces
    ##TextParsedNoSpaces = TextNoSpaces
    
    ## TEST PRINT OUTPUT
    ## print("\n")  ## PRINT SPACE
    ## print("WITHIN FUNCTION:  END FUNCTION #3CC - TEXT FILE PARSE") ## PRINTS FOR EACH VERSE

    ## RETURN VARIABLES TO PROGRAM - RETURNS TUPLE OF TWO TEXTS (LISTS):  1.) WITH SPACES; 2.) WITH NO SPACES
    return(TextParsedWithSpaces, TextParsedNoSpaces, ListOfWords)

## END FUNCTION () #3CC - TEXT FILE PARSE ##

