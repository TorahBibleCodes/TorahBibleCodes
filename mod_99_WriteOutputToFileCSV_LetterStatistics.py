## IMPORT MODULES
import csv 

## DECLARE VARIABLES
headers = ["Hebrew Letter", "Number Of Instances", "Length Of Text", "Percentage Of Text as Decimal", "Percentage Of Text as %"]

## DEFINE FUNCTIONS
def fn_WriteOutputToFile(ListOfRows, FileName):

    """
    ## MODULE.FUNCTION() #99 - 
    """

    ## OPEN (IF EXISTS) / CREATE (IF NOT EXISTS) CSV FILE; WRITE OUTPUT TO CSV FILE
    with open("USER_GENERATED_FILES/" + FileName,'w', encoding="utf-8", newline='') as f:

        f_csv = csv.writer(f, delimiter=';')
        f_csv.writerow(headers) ## HEADERS OPTIONAL ## REMOVE COMMENTS BEFORE f_csv.writerow(headers) IF YOU WANT CSV FILE TO CONTAIN HEADERS
        f_csv.writerows(ListOfRows)


   
