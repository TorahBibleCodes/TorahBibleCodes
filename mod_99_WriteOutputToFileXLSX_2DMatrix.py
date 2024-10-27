## IMPORT MODULES
import xlsxwriter

## DECLARE VARIABLES

## DEFINE FUNCTIONS
def fn_WriteOutputToFile(YH, XW, ListOfRowsOfLetters, FileNameForMatrixXLSX):

    """
    ## MODULE.FUNCTION() #99 - 
    """

    ## CREATE XLSX WORKBOOK FILE WITH WORKSHEET; WRITE OUTPUT TO XLSX EXCEL FILE

    ## DIMENSIONS OF THE 2D MATRIX == XW COLUMNS x YH ROWS
    ## TEST PRINT OUTPUT
    print("\n")
    print(f"YH = {YH}; XW = {XW}")

    ## PURE XLSXWRITER CODE; ## NO PANDAS PROXY
    workbook = xlsxwriter.Workbook("USER_GENERATED_FILES/" + FileNameForMatrixXLSX)
    worksheet = workbook.add_worksheet()

    ## DEFINE FORMATS
    ## FORMAT: LIGHT RED FILL WITH DARK RED TEXT
    format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                   'font_color': '#9C0006'})

    ## FORMAT: GREEN FILL WITH DARK GREEN TEXT
    format2 = workbook.add_format({'bg_color': '#a4a4f5%',
                                   'font_color': '#0303fc'})

    ## FORMAT: 
    format3 = workbook.add_format({'bg_color': '#cc00ff',
                                   'font_color': '#000000'})

    ## FORMAT: 
    format4 = workbook.add_format({'bg_color': '#c08763',
                                   'font_color': '#ffffff'})

    
    
    # ## SET COLUMN WIDTHS
    worksheet.set_column_pixels(0,0,120)
    worksheet.set_column_pixels(1,(XW),30)
    worksheet.set_column_pixels(XW,XW,120)

    ## FLATTEN ListOfRowsOfLetters INTO ONE LONG 1-D LIST
    ListOfCells = []
    for EachRow in ListOfRowsOfLetters:
        for EachCell in EachRow:
            ListOfCells.append(EachCell)

   
    ## CONVERT TUPLES TO STRINGS BECAUSE XLSX WRITER CAN'T DEAL WITH TUPLES
    ListOfCells = [str(CellContent) if type(CellContent) is tuple else CellContent for CellContent in ListOfCells]
    
    ## DECLARE VARIABLES
    counter = 0

    ## START FROM FIRST CELL IN TOP LEFT:  (0,0)

    ## BEGIN FOR LOOP
    for row in range(0, YH):

        ## BEGIN FOR LOOP
        for column in range(0, (XW+2)):

            ## WRITE TO THE INDIVIDUAL CELL
            worksheet.write(row, column, ListOfCells[counter])

            ## INCREMENT COUNTER VARIABLE
            counter += 1

            ## INCREMENT XW COLUMN FOR EACH CELL GOING TO THE RIGHT
            column += 1

        ## END FOR LOOP

        ## INCREMENT YH ROW FOR EACH ROW OF CELLS
        row += 1
    
    ## END FOR LOOP

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                        'criteria': 'containing',
                                        'value':    'מ',
                                        'format':   format1})

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                        'criteria': 'containing',
                                        'value':    'ם',
                                        'format':   format1})

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                        'criteria': 'containing',
                                        'value':    'ת',
                                        'format':   format1})

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'ל',
                                       'format':   format2})

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'א',
                                       'format':   format2})

    """
    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'ר',
                                       'format':   format3})

    ## SET CONDITIONAL FORMAT FOR ELS MATCHES
    worksheet.conditional_format(0,0,YH,(XW+2), {'type':     'text',
                                       'criteria': 'containing',
                                       'value':    'ד',
                                       'format':   format4})
    """

    ## worksheet.write('A1', 'Hello world', format1)
    ## worksheet.write('A2', 'Hello world', format2)
    
    ## CLOSE XLSX EXCEL FILE
    workbook.close()
