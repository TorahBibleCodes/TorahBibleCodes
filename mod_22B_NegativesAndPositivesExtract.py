## DEFINE FUNCTION
def fn_NegativesAndPositivesExtract(DELSMLF):
    """
    Extracts and separates the negatives and positives from the given dictionary.
    
    Args:
    DELSMLF (dict): Dictionary with integer keys and values being dictionaries containing tuples as keys.
    
    Returns:
    tuple: Two dictionaries, one with positive values and one with negative values.
    """
    
    print("\nWITHIN FUNCTION: BEGIN FUNCTION #22B - EXTRACT NEGATIVES AND POSITIVES (MATCHES)")

    ## DECLARE VARIABLES
    DELSMP = {}  ## EMPTY DICT FOR POSITIVE VALUES
    DELSMN = {}  ## EMPTY DICT FOR NEGATIVE VALUES
    CounterELS = 1  ## COUNTER FOR THE ELEMENTS

    ## BEGIN FOR LOOP
    for k, v in DELSMLF.items(): ## (n,d,k) ## COUNTER COUNTS NUMBER OF ELSs
        
        ## TEST PRINT OUTPUT
        print(f"CounterELS: {CounterELS}")

        ## DECLARE VARIABLES
        DELSMP_temp = {}  ## TEMP EMPTY DICT FOR POSITIVE VALUES
        DELSMN_temp = {}  ## TEMP EMPTY DICT FOR NEGATIVE VALUES

        ## BEGIN FOR LOOP
        for EachKey in v:

            ## BEGIN IF / ELSE...
            ## IF...
            if EachKey[1] < 0: ## IF SKIP DISTANCE (d) IS NEGATIVE... (n,d,k)

                ## TEST PRINT OUTPUT
                ## print(f"(d) = {EachKey[1]}, {type(EachKey[1])}") ## SKIP DISTANCE (d)
                ## print(f"EachKey = {EachKey}") ## (n,d,k)
                ## print(f"v[EachKey] = {v[EachKey]}") ## GEMATRIA NUMBER VALUE OF EACH LETTER IN WORD []

                ##
                DELSMN_temp[EachKey] = v[EachKey]

            ## ...ELSE...
            else: ## ELSE IF SKIP DISTANCE (d) IS NOT NEGATIVE (i.e. POSITIVE)..

                ## TEST PRINT OUTPUT
                ## print(f"(d) = {EachKey[1]}, {type(EachKey[1])}") ## SKIP DISTANCE (d)
                ## print(f"EachKey = {EachKey}") ## (n,d,k)
                ## print(f"v[EachKey] = {v[EachKey]}") ##

                ##
                DELSMP_temp[EachKey] = v[EachKey]

        ## 
        DELSMN[CounterELS] = DELSMN_temp
        DELSMP[CounterELS] = DELSMP_temp

        ## TEST PRINT OUTPUT
        ## print(f"DELSMN_temp : {DELSMN_temp}")
        ## print(f"DELSMP_temp : {DELSMP_temp}")

        ## INCREMENT COUNTER
        CounterELS += 1

    ## TEST PRINT OUTPUT
    ## print(f"DELSMN: {DELSMN}")
    ## print(f"DELSMP: {DELSMP}")
    print("\nWITHIN FUNCTION: END FUNCTION #22B - EXTRACT NEGATIVES AND POSITIVES (MATCHES)")

    ## RETURN VARIABLES
    return(DELSMP, DELSMN)

"""
# Example usage
DELSMLF = {
    1: {(24263, -9, 5): [5, 40, 300, 10, 8]},
    2: {(24012, 20, 5): [40, 300, 10, 8, 10]},
    3: {
        (19732, -43, 5): [40, 300, 10, 8, 6],
        (14256, -1, 5): [40, 300, 10, 8, 6],
        (19550, 1, 5): [40, 300, 10, 8, 6],
        (19887, 14, 5): [40, 300, 10, 8, 6],
        (19820, 45, 5): [40, 300, 10, 8, 6]
    }
}

## positives, negatives = fn_NegativesAndPositivesExtract(DELSMLF)
## print("Positives:", positives)
## print("Negatives:", negatives)

Positives: {1: {}, 2: {(24012, 20, 5): [40, 300, 10, 8, 10]}, 3: {(19550, 1, 5): [40, 300, 10, 8, 6], (19887, 14, 5): [40, 300, 10, 8, 6], (19820, 45, 5): [40, 300, 10, 8, 6]}}
Negatives: {1: {(24263, -9, 5): [5, 40, 300, 10, 8]}, 2: {}, 3: {(19732, -43, 5): [40, 300, 10, 8, 6], (14256, -1, 5): [40, 300, 10, 8, 6]}}

## DELSMLF.items()
{1: {(24263, -9, 5): [5, 40, 300, 10, 8]},
    2: {(24012, 20, 5): [40, 300, 10, 8, 10]},
    3: {(19732, -43, 5): [40, 300, 10, 8, 6],
        (14256, -1, 5): [40, 300, 10, 8, 6],
        (19550, 1, 5): [40, 300, 10, 8, 6],
        (19887, 14, 5): [40, 300, 10, 8, 6],
        (19820, 45, 5): [40, 300, 10, 8, 6]}
}

"""