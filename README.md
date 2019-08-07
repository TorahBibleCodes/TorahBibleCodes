# TorahBibleCodes
Torah Bible Codes - Open-Source Python

http://TorahBibleCodes.com
<br />
http://www.TorahBibleCodes.com
<br />
https://github.com/torahbiblecodes
<br />
https://stackoverflow.com/users/8911652/torahbiblecodes

# Known Bugs and Open Issues
None

# Current Development Status

<br />Active Development: In Progress

# Equidistant Letter Sequences (ELS)

<br />Witztum, Rips, and Rosenberg (WRR) define an Equidistant Letter Sequence (ELS) as a sequence of letters in the text whose positions - not counting spaces - form an arithmetic progression. That is to say the letters are found at the positions

n, n + d, n + 2d, ..., n + (k - 1)d

WRR define n as the start, d as the skip between letters in the search-term, and k as the length of the ELS. These three parameters uniquely identify the ELS which is denoted (n, d, k).

# The Texts Used:
## 1.) Genesis
https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Genesis/Hebrew/Tanach%20with%20Text%20Only.json

## 2.) Exodus
https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Exodus/Hebrew/Tanach%20with%20Text%20Only.json

## 3.) Leviticus
https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Leviticus/Hebrew/Tanach%20with%20Text%20Only.json

## 4.) Numbers
https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Numbers/Hebrew/Tanach%20with%20Text%20Only.json

## 5.) Deuteronomy
https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Deuteronomy/Hebrew/Tanach%20with%20Text%20Only.json

## 6.) Joshua

## 7.) Judges

## 8.) I Samuel

## 9.) II Samuel

## 10.) I Kings

## 11.) II Kings

## 12.) Isaiah

## 13.) Jeremiah

## 14.) Ezekiel

## 15.) Hosea

## 16.) Joel

## 17.) Amos

## 18.) Obadiah

## 19.) Jonah

## 20.) Micah

## 21.) Nahum

## 22.) Habakkuk

## 23.) Zephaniah

## 24.) Haggai

## 25.) Zechariah

## 26.) Malachi

## 27.) Psalms

## 28.) Proverbs

## 29.) Job

## 30.) Song of Songs

## 31.) Ruth

## 32.) Lamentations

## 33.) Ecclesiastes

## 34.) Esther

## 35.) Daniel

## 36.) Ezra

## 37.) Nehemiah

## 38.) I Chronicles

## 39.) II Chronicles


# How to Run the App / Program
<ol>
  <li>Download and Install Python on your local computer</li>
  <li>Go to folder where the TorahBibleCodes files are saved</li>
  <li>Open Command Prompt / Command Line Interface (CLI) - WINDOWS:  SHIFT RIGHT-CLICK --> OPEN COMMAND WINDOW HERE</li>
  <li>TYPE/RUN:  python p_els.py</li>
  <li>A "D" Python Dictionary Object is returned to you to interact with and further develop per your needs, and we invite you to share your open-source solutions and scientific research with the community to allow confirmation of your discoveries and data, which will lead to further shared advancement and benefit.
</ol>

# Structure of App / Program
<br />0.) COMMAND LINE INTERFACE (CLI): #0 - RUN MAIN PROGRAM FILE p_els.py TO GET DATA AND CREATE INTERACTIVE DATA OBJECTS
<br />1.) CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
<br />2.) CALL MODULE.FUNCTION() #2 - TEXT FILE OPEN
<br />3.) CALL MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
<br />4.) CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
<br />5.) CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
<br />6.) CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE CREATE
<br />7.) CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE WITH TUPLES AS KEYS, e.g. (1,1,1) = BOOK (1) GENESIS CHAPTER 1, VERSE 1...
<br />8.) CALL MODULE.FUNCTION() #8 - DATA OBJECTS CREATE; RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS
<br />9.) CALL MODULE.FUNCTION() #9 - GET NUMBER VALUE OF EACH LETTER IN STRING
<br />10.) STEP 10 - IN DEVELOPMENT

# Program Concepts:  Objects - D, DL, D5, L, S, N
## "D" Object:  Dictionary of Verses Object

For any text chosen (e.g. Genesis, Exodus, Leviticus, Numbers, Deuteronomy, or all five (5) together, or the twenty-one (21) books of the Prophets, or the thirteen (13) books of the Writings, or the thirty-nine (39) books of the entire Hebrew Bible, the text is parsed and a Python dictionary "D" is created that allows one to access each verse by 3-digit tuple key (Book, Chapter, Verse).  After choosing the text(s) to be searched, a Python dictionary "D" is created to contain each verse - accessible by 3-digit tuple key.

## Each verse (and letter) of the thirty-nine (39) books of the Hebrew Bible is accessible via the Python dictionary "D" with a unique 3-digit tuple key as per following examples:

`<br />D[1,1,1] = GENESIS 1:1
<br />D[1,1,7] = GENESIS 1:7
<br />D[1,50,26] = GENESIS 50:26
<br />D[2,1,1] = EXODUS 1:1
<br />D[2,40,38] = EXODUS 40:38
<br />D[3,1,1] = LEVITICUS 1:1
<br />D[3,27,34] = LEVITICUS 27:34
<br />D[4,1,1] = NUMBERS 1:1
<br />D[4,36,13] = NUMBERS 36:13
<br />D[5,1,1] = DEUTERONOMY 1:1
<br />D[5,34,12] = DEUTERONOMY 34:12

<br />((1, 1, 1), 'בראשיתבראאלהיםאתהשמיםואתהארץ')
<br />((1, 1, 2), 'והארץהיתהתהוובהווחשךעלפניתהוםורוחאלהיםמרחפתעלפניהמים')
<br />((1, 1, 3), 'ויאמראלהיםיהיאורויהיאור')
<br />((1, 1, 4), 'ויראאלהיםאתהאורכיטובויבדלאלהיםביןהאורוביןהחשך')
<br />((1, 1, 5), 'ויקראאלהיםלאוריוםולחשךקראלילהויהיערבויהיבקריוםאחד')
<br />((1, 1, 6), 'ויאמראלהיםיהירקיעבתוךהמיםויהימבדילביןמיםלמים')
<br />((1, 1, 7), 'ויעשאלהיםאתהרקיעויבדלביןהמיםאשרמתחתלרקיעוביןהמיםאשרמעללרקיעויהיכן')
<br />((1, 1, 8), 'ויקראאלהיםלרקיעשמיםויהיערבויהיבקריוםשני')
<br />((1, 1, 9), 'ויאמראלהיםיקווהמיםמתחתהשמיםאלמקוםאחדותראההיבשהויהיכן')
<br />((1, 1, 10), 'ויקראאלהיםליבשהארץולמקוההמיםקראימיםויראאלהיםכיטוב')
<br />((1, 1, 11), 'ויאמראלהיםתדשאהארץדשאעשבמזריעזרעעץפריעשהפרילמינואשרזרעובועלהארץויהיכן')
<br />((1, 1, 12), 'ותוצאהארץדשאעשבמזריעזרעלמינהוועץעשהפריאשרזרעובולמינהוויראאלהיםכיטוב')
<br />((1, 1, 13), 'ויהיערבויהיבקריוםשלישי')
<br />((1, 1, 14), 'ויאמראלהיםיהימארתברקיעהשמיםלהבדילביןהיוםוביןהלילהוהיולאתתולמועדיםולימיםושנים')
<br />((1, 1, 15), 'והיולמאורתברקיעהשמיםלהאירעלהארץויהיכן')
<br />((1, 1, 16), 'ויעשאלהיםאתשניהמארתהגדליםאתהמאורהגדללממשלתהיוםואתהמאורהקטןלממשלתהלילהואתהכוכבים')
<br />((1, 1, 17), 'ויתןאתםאלהיםברקיעהשמיםלהאירעלהארץ')
<br />((1, 1, 18), 'ולמשלביוםובלילהולהבדילביןהאורוביןהחשךויראאלהיםכיטוב')
<br />((1, 1, 19), 'ויהיערבויהיבקריוםרביעי')
<br />((1, 1, 20), 'ויאמראלהיםישרצוהמיםשרץנפשחיהועוףיעופףעלהארץעלפנירקיעהשמים')
<br />((1, 1, 21), 'ויבראאלהיםאתהתנינםהגדליםואתכלנפשהחיההרמשתאשרשרצוהמיםלמינהםואתכלעוףכנףלמינהוויראאלהיםכיטוב')
<br />((1, 1, 22), 'ויברךאתםאלהיםלאמרפרוורבוומלאואתהמיםבימיםוהעוףירבבארץ')
<br />((1, 1, 23), 'ויהיערבויהיבקריוםחמישי')
<br />((1, 1, 24), 'ויאמראלהיםתוצאהארץנפשחיהלמינהבהמהורמשוחיתוארץלמינהויהיכן')
<br />((1, 1, 25), 'ויעשאלהיםאתחיתהארץלמינהואתהבהמהלמינהואתכלרמשהאדמהלמינהוויראאלהיםכיטוב')
<br />((1, 1, 26), 'ויאמראלהיםנעשהאדםבצלמנוכדמותנווירדובדגתהיםובעוףהשמיםובבהמהובכלהארץובכלהרמשהרמשעלהארץ')
<br />((1, 1, 27), 'ויבראאלהיםאתהאדםבצלמובצלםאלהיםבראאתוזכרונקבהבראאתם')
<br />((1, 1, 28), 'ויברךאתםאלהיםויאמרלהםאלהיםפרוורבוומלאואתהארץוכבשהורדובדגתהיםובעוףהשמיםובכלחיההרמשתעלהארץ')
<br />((1, 1, 29), 'ויאמראלהיםהנהנתתילכםאתכלעשבזרעזרעאשרעלפניכלהארץואתכלהעץאשרבופריעץזרעזרעלכםיהיהלאכלה')
<br />((1, 1, 30), 'ולכלחיתהארץולכלעוףהשמיםולכלרומשעלהארץאשרבונפשחיהאתכלירקעשבלאכלהויהיכן')
<br />((1, 1, 31), 'ויראאלהיםאתכלאשרעשהוהנהטובמאדויהיערבויהיבקריוםהששי')
<br />((1, 2, 1), 'ויכלוהשמיםוהארץוכלצבאם')
<br />((1, 2, 2), 'ויכלאלהיםביוםהשביעימלאכתואשרעשהוישבתביוםהשביעימכלמלאכתואשרעשה')
<br />((1, 2, 3), 'ויברךאלהיםאתיוםהשביעיויקדשאתוכיבושבתמכלמלאכתואשרבראאלהיםלעשות')
<br />((1, 2, 4), 'אלהתולדותהשמיםוהארץבהבראםביוםעשותיהוהאלהיםארץושמים')
<br />((1, 2, 5), 'וכלשיחהשדהטרםיהיהבארץוכלעשבהשדהטרםיצמחכילאהמטיריהוהאלהיםעלהארץואדםאיןלעבדאתהאדמה')
<br />((1, 2, 6), 'ואדיעלהמןהארץוהשקהאתכלפניהאדמה')
<br />((1, 2, 7), 'וייצריהוהאלהיםאתהאדםעפרמןהאדמהויפחבאפיונשמתחייםויהיהאדםלנפשחיה')
<br />((1, 2, 8), 'ויטעיהוהאלהיםגןבעדןמקדםוישםשםאתהאדםאשריצר')
<br />((1, 2, 9), 'ויצמחיהוהאלהיםמןהאדמהכלעץנחמדלמראהוטובלמאכלועץהחייםבתוךהגןועץהדעתטובורע')
<br />((1, 2, 10), 'ונהריצאמעדןלהשקותאתהגןומשםיפרדוהיהלארבעהראשים')
<br />((1, 2, 11), 'שםהאחדפישוןהואהסבבאתכלארץהחוילהאשרשםהזהב')
<br />((1, 2, 12), 'וזהבהארץההואטובשםהבדלחואבןהשהם')
<br />((1, 2, 13), 'ושםהנהרהשניגיחוןהואהסובבאתכלארץכוש')
<br />((1, 2, 14), 'ושםהנהרהשלישיחדקלהואההלךקדמתאשורוהנהרהרביעיהואפרת')
<br />((1, 2, 15), 'ויקחיהוהאלהיםאתהאדםוינחהובגןעדןלעבדהולשמרה')
<br />((1, 2, 16), 'ויצויהוהאלהיםעלהאדםלאמרמכלעץהגןאכלתאכל')
<br />((1, 2, 17), 'ומעץהדעתטובורעלאתאכלממנוכיביוםאכלךממנומותתמות')
<br />((1, 2, 18), 'ויאמריהוהאלהיםלאטובהיותהאדםלבדואעשהלועזרכנגדו')
<br />((1, 2, 19), 'ויצריהוהאלהיםמןהאדמהכלחיתהשדהואתכלעוףהשמיםויבאאלהאדםלראותמהיקראלווכלאשריקראלוהאדםנפשחיההואשמו')
<br />((1, 2, 20), 'ויקראהאדםשמותלכלהבהמהולעוףהשמיםולכלחיתהשדהולאדםלאמצאעזרכנגדו')
<br />((1, 2, 21), 'ויפליהוהאלהיםתרדמהעלהאדםויישןויקחאחתמצלעתיוויסגרבשרתחתנה')
<br />((1, 2, 22), 'ויבןיהוהאלהיםאתהצלעאשרלקחמןהאדםלאשהויבאהאלהאדם')
<br />((1, 2, 23), 'ויאמרהאדםזאתהפעםעצםמעצמיובשרמבשרילזאתיקראאשהכימאישלקחהזאת')
<br />((1, 2, 24), 'עלכןיעזבאישאתאביוואתאמוודבקבאשתווהיולבשראחד')
<br />((1, 2, 25), 'ויהיושניהםערומיםהאדםואשתוולאיתבששו')
<br />((1, 3, 1), 'והנחשהיהערוםמכלחיתהשדהאשרעשהיהוהאלהיםויאמראלהאשהאףכיאמראלהיםלאתאכלומכלעץהגן')
<br />((1, 3, 2), 'ותאמרהאשהאלהנחשמפריעץהגןנאכל')
<br />((1, 3, 3), 'ומפריהעץאשרבתוךהגןאמראלהיםלאתאכלוממנוולאתגעובופןתמתון')
<br />((1, 3, 4), 'ויאמרהנחשאלהאשהלאמותתמתון')
<br />((1, 3, 5), 'כיידעאלהיםכיביוםאכלכםממנוונפקחועיניכםוהייתםכאלהיםידעיטובורע')
<br />((1, 3, 6), 'ותראהאשהכיטובהעץלמאכלוכיתאוההואלעיניםונחמדהעץלהשכילותקחמפריוותאכלותתןגםלאישהעמהויאכל')
<br />((1, 3, 7), 'ותפקחנהעינישניהםוידעוכיעירמםהםויתפרועלהתאנהויעשולהםחגרת')
<br />((1, 3, 8), 'וישמעואתקוליהוהאלהיםמתהלךבגןלרוחהיוםויתחבאהאדםואשתומפנייהוהאלהיםבתוךעץהגן')
<br />((1, 3, 9), 'ויקראיהוהאלהיםאלהאדםויאמרלואיכה')
<br />((1, 3, 10), 'ויאמראתקלךשמעתיבגןואיראכיעירםאנכיואחבא')
<br />((1, 3, 11), 'ויאמרמיהגידלךכיעירםאתההמןהעץאשרצויתיךלבלתיאכלממנואכלת')
<br />((1, 3, 12), 'ויאמרהאדםהאשהאשרנתתהעמדיהואנתנהלימןהעץואכל')
<br />((1, 3, 13), 'ויאמריהוהאלהיםלאשהמהזאתעשיתותאמרהאשההנחשהשיאניואכל')
<br />((1, 3, 14), 'ויאמריהוהאלהיםאלהנחשכיעשיתזאתארוראתהמכלהבהמהומכלחיתהשדהעלגחנךתלךועפרתאכלכלימיחייך')
<br />((1, 3, 15), 'ואיבהאשיתבינךוביןהאשהוביןזרעךוביןזרעההואישופךראשואתהתשופנועקב')
<br />((1, 3, 16), 'אלהאשהאמרהרבהארבהעצבונךוהרנךבעצבתלדיבניםואלאישךתשוקתךוהואימשלבך')
<br />((1, 3, 17), 'ולאדםאמרכישמעתלקולאשתךותאכלמןהעץאשרצויתיךלאמרלאתאכלממנוארורההאדמהבעבורךבעצבוןתאכלנהכלימיחייך')
<br />((1, 3, 18), 'וקוץודרדרתצמיחלךואכלתאתעשבהשדה')
<br />((1, 3, 19), 'בזעתאפיךתאכללחםעדשובךאלהאדמהכיממנהלקחתכיעפראתהואלעפרתשוב')
<br />((1, 3, 20), 'ויקראהאדםשםאשתוחוהכיהואהיתהאםכלחי')
<br />((1, 3, 21), 'ויעשיהוהאלהיםלאדםולאשתוכתנותעורוילבשם')
<br />((1, 3, 22), 'ויאמריהוהאלהיםהןהאדםהיהכאחדממנולדעתטובורעועתהפןישלחידוולקחגםמעץהחייםואכלוחילעלם')
<br />((1, 3, 23), 'וישלחהויהוהאלהיםמגןעדןלעבדאתהאדמהאשרלקחמשם')
<br />((1, 3, 24), 'ויגרשאתהאדםוישכןמקדםלגןעדןאתהכרביםואתלהטהחרבהמתהפכתלשמראתדרךעץהחיים')
<br />((1, 4, 1), 'והאדםידעאתחוהאשתוותהרותלדאתקיןותאמרקניתיאישאתיהוה')
<br />((1, 4, 2), 'ותסףללדתאתאחיואתהבלויהיהבלרעהצאןוקיןהיהעבדאדמה')
<br />((1, 4, 3), 'ויהימקץימיםויבאקיןמפריהאדמהמנחהליהוה')
<br />((1, 4, 4), 'והבלהביאגםהואמבכרותצאנוומחלבהןוישעיהוהאלהבלואלמנחתו')
<br />((1, 4, 5), 'ואלקיןואלמנחתולאשעהויחרלקיןמאדויפלופניו')
<br />((1, 4, 6), 'ויאמריהוהאלקיןלמהחרהלךולמהנפלופניך')
<br />((1, 4, 7), 'הלואאםתיטיבשאתואםלאתיטיבלפתחחטאתרבץואליךתשוקתוואתהתמשלבו')
<br />`

## ... etc. ... etc. ... etc. ...

### Please see the file "D.py" (also run: "p_els.py") to see and interact with the "D" Object:  Python Dictionary of Verses with a 3-digit Tuple Key

### Please run the file "p_els.py" to see and interact with the "DL" Object:  Python Dictionary of Letters with a 4-digit Tuple Key

### Please run the file "p_els.py" to see and interact with the "D5" Object:  Python Dictionary of Letters with a 5-digit Tuple Key

### Please run the file "p_els.py" to see and interact with the "L" Object:  Python List of Letters

### Please run the file "p_els.py" to see and interact with the "S" Object:  Python String of Letters

### Please run the file "p_els.py" to see and interact with the "N" Object:  Python List of Numbers

## Each Verse can be further subdivided into a string sequence of many Letter Objects (i.e. Strings of one (1) letter only) which are classes which keep track of their position within the ELS Search sequence, and accessible by extension of previous tuple syntax:  Book, Chapter, Verse, Letter

### D Object - Dictionary of Verses, accessible as data with a 3-digit Tuple Key
<br />D[1,1,1] --> GENESIS 1:1 - 1st Book, 1st Chapter, 1st Verse 
<br />D[1,1,2] --> GENESIS 1:2 - 1st Book, 1st Chapter, 2nd Verse
<br />D[1,1,3] --> GENESIS 1:3 - 1st Book, 1st Chapter, 3rd Verse

### D Object - Dictionary of Verses/Letters, accessible as data with a 3-digit Tuple Key + sub-element (0-indexed) in sequence of letters within each verse.
<br />D[1,1,1][0] --> 1st element (letter) in string/verse sequence --> 'ב'
<br />D[1,1,1][1] --> 2nd element (letter) in string/verse sequence --> 'ר'
<br />D[1,1,1][2] --> 3rd element (letter) in string/verse sequence --> 'א'
<br />D[1,1,1][-1] --> Last element in string/verse sequence...

### DL Object - Dictionary of Letters (with 4-digit key) with 4th element of tuple being the (non-0-indexed; 1-indexed) position of letter in verse...
<br />DL[1, 1, 1, 1] --> 'ב'
<br />DL[1, 1, 1, 2] --> 'ר'
<br />DL[1, 1, 1, 3] --> 'א'
<br />DL[1, 1, 1, 4] --> 'ש'
<br />DL[1, 1, 1, 5] --> 'י'
<br />DL[1, 1, 1, 6] --> 'ת'

<br />DL[5,34,12,43] --> 'י'
<br />DL[5,34,12,44] --> 'ש'
<br />DL[5,34,12,45] --> 'ר'
<br />DL[5,34,12,46] --> 'א'
<br />DL[5,34,12,47] --> 'ל'

### D5 Object - Dictionary of Letters (with 5-digit key) with 5th element of tuple being the position of letter in total sequence of text...(i.e. either all five (5) texts of the Torah together (304853 letters), or one (1) text only, or all twenty-one (21) texts of the Prophets, or all thirteen (13) texts of the Writings, or all thirty-nine (39) texts of the entire Hebrew Bible together)...
<br />D5[1, 1, 1, 1, 1] --> 'ב'
<br />D5[1, 1, 1, 2, 2] --> 'ר'
<br />D5[1, 1, 1, 3, 3] --> 'א'
<br />D5[1, 1, 1, 4, 4] --> 'ש'
<br />D5[1, 1, 1, 5, 5] --> 'י'
<br />D5[1, 1, 1, 6, 6] --> 'ת'

<br />D5[5, 34, 12, 43, 304849] --> 'י'
<br />D5[5, 34, 12, 44, 304850] --> 'ש'
<br />D5[5, 34, 12, 45, 304851] --> 'ר'
<br />D5[5, 34, 12, 46, 304852] --> 'א'
<br />D5[5, 34, 12, 47, 304853] --> 'ל'

### L Object - List of Letters
<br />L[0:6] --> ['ב', 'ר', 'א', 'ש', 'י', 'ת']

### S Object - String of Letters
<br />S[0:6] --> 'בראשית'


## N Object - List of Numbers:  Each letter's Kabbalah Numerical Gematria Value is obtainable by passing a string-sequence to a MODULE.FUNCTION() call (NOTE:  Numbers returned in the N Object are left-to-right; Hebrew letters returned in L Object are right-to-left)
string = 'בראשית'
<br />N = mod_9GetNumberValue.fn_GetNumberValue(string) --> [2, 200, 1, 300, 10, 400]

### א = 1
### ב = 2
### 3 = ג
### 4 = ד
### 5 = ה
### 6 = ו
### 7 = ז
### 8 = ח
### 9 = ט
### 10 = י
### 20 = כ / ך
### 30 = ל
### 40 = מ / ם
### 50 = נ / ן
### 60 = ס
### 70 = ע
### 80 = פ / ף
### 90 = צ / ץ
### 100 = ק
### 200 = ר
### 300 = ש
### 400 = ת

# Statistics

### Total Number of Verses in Hebrew Bible: 23206
### Total Number of Letters in Hebrew Bible: 1197120



