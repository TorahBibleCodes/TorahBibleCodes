# TorahBibleCodes
Torah Bible Codes - Open-Source Python
<br />
Support your friendly, neighborhood TorahBibleCodes research scientist.
<br />
https://www.givesendgo.com/TorahBibleCodes
<br />
HOMEPAGE URL: https://TorahBibleCodes.com
<br />
https://www.TorahBibleCodes.com
<br />
GITHUB: @TorahBibleCodes https://github.com/torahbiblecodes
<br />
SOFTWARE REPO (INCLUDES USER-GUIDE PDF): @TorahBibleCodes https://github.com/torahbiblecodes/torahbiblecodes
<br />
ACADEMIA 2024 (PDF USER GUIDE): https://www.academia.edu/125087434
<br /> 
READ THE DOCS (NOT YET UPDATED FOR VERSION 0.2): @TorahBibleCodes https://torahbiblecodes-sphinx.readthedocs.io/en/latest/index.html
<br />
ACADEMIA 2023: https://www.academia.edu/104334275
<br />
STACKOVERFLOW: @TorahBibleCodes https://stackoverflow.com/users/8911652/torahbiblecodes
<br />
TWITTER: @TorahBibleCodes https://twitter.com/TorahBibleCodes
<br />
YOUTUBE: @TorahBibleCodes https://www.youtube.com/@TorahBibleCodes
<br />
YOUTUBE: @TorahBibleCodes https://www.youtube.com/channel/UCNsvtMx4JJRpNzzPq57HCqg
<br />
GIVESENDGO: @TorahBibleCodes https://www.givesendgo.com/torahbiblecodes

# Known Bugs and Open Issues
https://github.com/TorahBibleCodes/TorahBibleCodes/issues

# Current Development Status

<br />Active Development: In Progress

# Updates
<br />14 / MARCH / 2025
<br />
<br />SOFTWARE UPDATE (MINOR): ONE LINE OF CODE ADDED TO THE FILE p.py TO DEAL WITH NUMPY UPDATE THAT SCREWS UP OUTPUT FORMATTING IN THE CSV FILE - THIS IS NUMPY'S SUGGESTED SOLUTION
<br />
<br />27 / SEPTEMBER / 2024
<br />
<br />SOFTWARE UPDATE: NOW AVAILABLE SOFTWARE UPDATE VERSION 0.2
<br />
<br />1. Choice of Codices (i.e. Collections of Manuscripts): A. Koren; B. Leningrad; C. Miqra According to Masorah (MAM) - based on the Aleppo Codex.
<br />2. Possibility to search several texts as one complete book (as they were in antiquity): A. Samuel; B. Kings; C. Ezra-Nehemiah; D. Chronicles.
<br />3. Multiple Batch ELSs Searches via simple EXCEL / CSV user-input file with UNLIMITED ELS SEARCH TERMS.
<br />4. Individual CSV Data File for each ELS term with all word positions, letter positions, and verses where the ELS is found.
<br />5. Search Progress Bar with count of search terms, measurement of search time per search term, as well as estimation of total search time.
<br />6. Custom Skip Distances (d) according to User Input.
<br />7. Spaces in ELS Search Terms are elegantly handled by the program: Search for Longer, Multiple-Word Names and Phrases. 
<br />8. Letter Statistics for every text for every search.
<br />
<br />Please support our efforts if you can by donating via GIVESENDGO: 
<br />https://www.givesendgo.com/torahbiblecodes
<br />
<br />OR via BITCOIN (BTC) to the following addresses:
<br />bc1qzws4zjgzf4wll2mtztsavmyvkg72fnajfff8r7

<br />16 / JULY / 2023
<br />
<br />DEVELOPMENT UPDATE: POC (BETA) VERSION 0.1 WORKING: TorahBibleCodes: Free, Open-Source Python Equidistant Letter Sequences (ELS) Hebrew Bible Search Software

<br />ACADEMIC WHITE PAPER EXPLAINING HOW TORAH BIBLE CODES SOFTWARE WORKS: https://www.academia.edu/104334275

<br />TWITTER: @TorahBibleCodes https://twitter.com/TorahBibleCodes
<br />YOUTUBE: @TorahBibleCodes https://www.youtube.com/@TorahBibleCodes
<br />YOUTUBE: @TorahBibleCodes https://www.youtube.com/channel/UCNsvtMx4JJRpNzzPq57HCqg
<br /> BETA DEVELOPMENT PROGRAM (WORK-IN-PROGRESS) UPLOADED; More to come ASAP GOD-willing.
<br />
<br />Please support our efforts if you can by donating via GIVESENDGO: 
<br />https://www.givesendgo.com/torahbiblecodes
<br />
<br />OR via BITCOIN (BTC) to the following addresses:
<br />bc1qzws4zjgzf4wll2mtztsavmyvkg72fnajfff8r7

# Equidistant Letter Sequences (ELS)

<br />Witztum, Rips, and Rosenberg (WRR) define an Equidistant Letter Sequence (ELS) as a sequence of letters in the text whose positions - not counting spaces - form an arithmetic progression. That is to say the letters are found at the positions

n, (n + d), (n + 2d), (n + 3d),... (n + (k - 1)d)

WRR define n as the start, d as the skip between letters in the search-term, and k as the length of the ELS. These three parameters uniquely identify the ELS which is denoted (n, d, k).

# The Texts Used:
## 1.) Genesis
<br />A. KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Genesis/Hebrew/Tanach%20with%20Text%20Only.json
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 2.) Exodus
<br />A. KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Exodus/Hebrew/Tanach%20with%20Text%20Only.json
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 3.) Leviticus
<br />A. KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Leviticus/Hebrew/Tanach%20with%20Text%20Only.json
KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 4.) Numbers
<br />A. KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Numbers/Hebrew/Tanach%20with%20Text%20Only.json
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 5.) Deuteronomy
<br />A. KOREN CODEX: https://users.cecs.anu.edu.au/~bdm/dilugim/StatSci/data.html
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/blob/master/json/Tanakh/Torah/Deuteronomy/Hebrew/Tanach%20with%20Text%20Only.json
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 6.) Joshua
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 7.) Judges
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 8.) I Samuel
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 9.) II Samuel
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 10.) I Kings
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 11.) II Kings
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 12.) Isaiah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 13.) Jeremiah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 14.) Ezekiel
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 15.) Hosea
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 16.) Joel
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 17.) Amos
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 18.) Obadiah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 19.) Jonah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 20.) Micah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 21.) Nahum
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 22.) Habakkuk
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 23.) Zephaniah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 24.) Haggai
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 25.) Zechariah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 26.) Malachi
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 27.) Psalms
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 28.) Proverbs
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 29.) Job
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 30.) Song of Songs
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 31.) Ruth
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 32.) Lamentations
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 33.) Ecclesiastes
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 34.) Esther
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 35.) Daniel
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 36.) Ezra
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 37.) Nehemiah
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 38.) I Chronicles
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf

## 39.) II Chronicles
<br />B. LENINGRAD CODEX: https://github.com/TorahBibleCodes/Sefaria-Export/tree/master/json/Tanakh
<br />C. Miqra According to the Masorah (MAM) Collection of Manuscripts (based upon the ALEPPO CODEX): https://github.com/bdenckla/MAM-for-Sefaria/tree/main/out/csv-ajf


# How to Run the App / Program

READ THE DOCS: @TorahBibleCodes https://torahbiblecodes-sphinx.readthedocs.io/en/latest/index.html

## TEST DEVELOPMENT (BETA): MOVE TO --> READ THE DOCS: @TorahBibleCodes https://torahbiblecodes-sphinx.readthedocs.io/en/latest/index.html
# Structure of App / Program

<br />After running the Python file p.py, several Python / Pandas Objects are returned to you to interact with and further develop per your needs;
<br />We are currently developing the functionalities in the program to provide certain (many) specific data points, data objects, etc. so that scientifically repeatable (and therefore verifiable) results can be precisely measured, shared, tested, and either confirmed or disproved.
<br />The current BETA DEVELOPMENT version of the program does the following:

<ol>
	<li>Allows the user to select any text(s) from the Torah (Instruction) / Nevi'im (Prophets) / K'tuvim (Writings) of the Tanach (Hebrew Bible).</li>
	<li>Allows the user to choose a custom size of the 2D Matrix (X Rows by Y Columns) for the user-selected text(s) to be outputted to a CSV EXCEL file (CAUTION: Numbers approaching 1000 for X Rows will exceed the maximum allowed by EXCEL, and therefore will truncate the text).</li>
	<li>Allows the user to choose the number of desired ELS Search-Terms.</li>
	<li>Allows the user to input those specified ELS Search-Terms (NOTE: These must be typed in Hebrew characters, else EXCEPTION IS THROWN).</li>
	<li>Outputs CSV EXCEL file of the 2D Matrix for the selected text(s).</li>
	<li>Outputs CSV EXCEL file of the Gematria Number values for each word AND letter in the selected text(s)</li>
	<li>Outputs CSV EXCEL file of the Gematria Number values for each word AND letter in the ELS Search-Terms</li>
	<li>Outputs CSV EXCEL file of the ELS Search Term Matches (both POSITIVE and NEGATIVE):  Testing of several (best?) ways / algorithms for ELS Search within the text; Currently investigating REGEX, PANDAS, PURE PYTHON LINEAR SEARCH, etc.; Please see and examine the Python / Pandas Data Objects returned to see current capabilities in development.</li>
	<li>Outputs CSV EXCEL file of the Data Points for each letter and each word of each of the ELS Search-Terms so that precise, exact positions, shared positions, letter-proximity.</li>
	<li>Outputs CSV EXCEL file of Letter Statistics for that text selected.</li>
	<li>IN DEVELOPMENT: R&D for visualizations as well as integration into AI.</li>
	<li>IN DEVELOPMENT: Measurement of statistical probability, etc. of letters will be scientifically verifiable and reproduceable.</li>
</ol>

<br />We invite you to share your open-source (alternative/multiple?) solutions of further development of this open-source program (e.g. add-ons, additional features, functionalities, GUIs, etc.), as well as scientific research using these software research tools with the community to allow confirmation of your discoveries and data, which will lead to further shared advancement and mutual benefit for us all


# Program Concepts:  Objects - D (DS), DL, D5, D5K, L (LLL), S (SSS), N (NW), W (DW), ListOfWords, NW4ELS, W4ELS (DW4ELS), LO (DLO), ELSO (DELSO), gso;

READ THE DOCS: @TorahBibleCodes https://torahbiblecodes-sphinx.readthedocs.io/en/latest/index.html

# Hebrew Gematria Number Values


### 1 = א
### 2 = ב
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



## TEST DEVELOPMENT (BETA): MOVE TO --> READ THE DOCS: @TorahBibleCodes https://torahbiblecodes-sphinx.readthedocs.io/en/latest/index.html

# CENTRAL ELS SEARCH ALGORITHM:
<br />n, (n + d), (n + 2d), (n + 3d)... (n + (k-1)d)
<br />
<br />sL[6] ## == 'ת' == (n) ## WHEN TEXT SELECTED == 1 GENESIS
<br />sL[6+50] ## == 'ו' == (n + d)
<br />sL[6+50+50] ## == 'ר' == (n + 2d)
<br />sL[6+50+50+50] ## = 'ה' == (n + 3d) ## k == 4 == LengthOfELSSearchTerm
<br />
<br />sL[6] ## == 'ת' == (n) ## WHEN TEXT SELECTED == 1 GENESIS
<br />sL[56] ## == 'ו' == (n + d)
<br />sL[106] ## == 'ר' == (n + 2d)
<br />sL[156] ## = 'ה' == (n + 3d)


# Useful CLI Commands
sL.str.startswith("ב")
--> Returns Boolean (True/False) for each match (True) and for each non-match (False)

sL.str.endswith("ב")
--> Returns Boolean (True/False) for each match (True) and for each non-match (False)

sL.str.find("ב")
--> Returns Boolean-like (0 / -1) for each match (0) and for each non-match (-1)

sL.str.rfind("ב")
--> Returns Boolean-like (0 / -1) for each match (0) and for each non-match (-1)

### The following values are all equivalent; Each equals every other value
<ul>
  <li>len(sL) --> Total Number of Letters in the Pandas Series s --> Equal to len(S); len(L); len(DL); len(D5); len(N)</li>
  <li>len(S) --> Total Number of Letters in the Python String S --> Equal to len(sL); len(L); len(DL); len(D5); len(N)</li>
  <li>len(L) --> Total Number of Letters in the Python List L --> Equal to len(sL); len(S); len(DL); len(D5); len(N)</li>
  <li>len(DL) --> Total Number of Letters in the Python Dictionary DL with 4-digit Tuple Key --> Equal to len(sL); len(S); len(L); len(D5); len(N)</li>
  <li>len(D5) --> Total Number of Letters in the Python Dictionary D5 with 5-digit Tuple Key --> Equal to len(sL); len(S); len(L); len(DL); len(N)</li>
  <li>len(N) --> Total Number of Numbers in the Python List N --> Equal to len(sL); len(S); len(L); len(DL); len(D5)</li>
  
</ul>

# Statistics
### Total Number of Verses in Torah (LENINGRAD CODEX): 5846
### Total Number of Verses in Torah (KOREN CODEX): 5846 (excluding error of Numbers 25:19 in Claremont Michigan Transliteration)
### Total Number of Letters in Torah (LENINGRAD CODEX):  304850
Total Number of Letter א Aleph in Torah: 27060
<br />Total Number of Letter ב Bet in Torah: 16345
<br />Total Number of Letter ג Gimel in Torah: 2109
<br />Total Number of Letter ד Daled in Torah: 7032
<br />Total Number of Letter ה Heh/Hey/Hay in Torah: 28055
<br />Total Number of Letter ו Vav in Torah: 30533
<br />Total Number of Letter ז Zayin in Torah: 2198
<br />Total Number of Letter ח Ḥet in Torah: 7189
<br />Total Number of Letter ט Tet in Torah: 1804
<br />Total Number of Letter י Yud in Torah: 31556
<br />Total Number of Letter כ Khaf in Torah: 8610
<br />Total Number of Letter ך Khaf Sofit in Torah: 3358
<br />Total Number of Letter ל Lamed in Torah: 21570
<br />Total Number of Letter מ Mem in Torah: 14466
<br />Total Number of Letter ם Mem Sofit in Torah: 10624
<br />Total Number of Letter נ Nun in Torah: 9867
<br />Total Number of Letter ן Nun Sofit in Torah: 4259
<br />Total Number of Letter ס Samekh in Torah: 1833
<br />Total Number of Letter ע 'Ain in Torah: 11250
<br />Total Number of Letter פ Peh/Pey/Pay in Torah: 3975
<br />Total Number of Letter ף Peh/Pey/Pay Sofit in Torah: 830
<br />Total Number of Letter צ Tzadik in Torah: 2927
<br />Total Number of Letter ץ Tzadik Sofit in Torah: 1035
<br />Total Number of Letter ק Kuf in Torah: 4695
<br />Total Number of Letter ר Resh in Torah: 18125
<br />Total Number of Letter ש Shin in Torah: 15595
<br />Total Number of Letter ת Taf in Torah: 17950

### Total Number of Verses in Genesis (LENINGRAD CODEX):  1533
### Total Number of Letters in Genesis (LENINGRAD CODEX):  78069

Total Number of Letter א in Book of Genesis (LENINGRAD CODEX): 7634
<br />Total Number of Letter ב in Book of Genesis: 4332
<br />Total Number of Letter ג in Book of Genesis: 577
<br />Total Number of Letter ד in Book of Genesis: 1848
<br />Total Number of Letter ה in Book of Genesis: 6283
<br />Total Number of Letter ו in Book of Genesis: 8447
<br />Total Number of Letter ז in Book of Genesis: 428
<br />Total Number of Letter ח in Book of Genesis: 1844
<br />Total Number of Letter ט in Book of Genesis: 308
<br />Total Number of Letter י in Book of Genesis: 9041
<br />Total Number of Letter כ in Book of Genesis: 1909
<br />Total Number of Letter ך in Book of Genesis: 865
<br />Total Number of Letter ל in Book of Genesis: 5275
<br />Total Number of Letter מ in Book of Genesis: 3421
<br />Total Number of Letter ם in Book of Genesis: 2689
<br />Total Number of Letter נ in Book of Genesis: 2776
<br />Total Number of Letter ן in Book of Genesis: 1009
<br />Total Number of Letter ס in Book of Genesis: 446
<br />Total Number of Letter ע in Book of Genesis: 2823
<br />Total Number of Letter פ in Book of Genesis: 890
<br />Total Number of Letter ף in Book of Genesis: 313
<br />Total Number of Letter צ in Book of Genesis: 740
<br />Total Number of Letter ץ in Book of Genesis: 351
<br />Total Number of Letter ק in Book of Genesis: 1301
<br />Total Number of Letter ר in Book of Genesis: 4793
<br />Total Number of Letter ש in Book of Genesis: 3574
<br />Total Number of Letter ת in Book of Genesis: 4152

### Total Number of Verses in Hebrew Bible (LENINGRAD CODEX): 23206
### Total Number of Letters in Hebrew Bible (LENINGRAD CODEX): 1197042

Total Number of Letter א in Hebrew Bible: 95685
<br />Total Number of Letter ב in Hebrew Bible: 65216
<br />Total Number of Letter ג in Hebrew Bible: 10080
<br />Total Number of Letter ד in Hebrew Bible: 32371
<br />Total Number of Letter ה in Hebrew Bible: 101962
<br />Total Number of Letter ו in Hebrew Bible: 129606
<br />Total Number of Letter ז in Hebrew Bible: 9099
<br />Total Number of Letter ח in Hebrew Bible: 27598
<br />Total Number of Letter ט in Hebrew Bible: 6310
<br />Total Number of Letter י in Hebrew Bible: 137870
<br />Total Number of Letter כ in Hebrew Bible: 33466
<br />Total Number of Letter ך in Hebrew Bible: 14002
<br />Total Number of Letter ל in Hebrew Bible: 88302
<br />Total Number of Letter מ in Hebrew Bible: 57638
<br />Total Number of Letter ם in Hebrew Bible: 41291
<br />Total Number of Letter נ in Hebrew Bible: 39852
<br />Total Number of Letter ן in Hebrew Bible: 15241
<br />Total Number of Letter ס in Hebrew Bible: 7635
<br />Total Number of Letter ע in Hebrew Bible: 44811
<br />Total Number of Letter פ in Hebrew Bible: 15730
<br />Total Number of Letter ף in Hebrew Bible: 2554
<br />Total Number of Letter צ in Hebrew Bible: 11689
<br />Total Number of Letter ץ in Hebrew Bible: 3288
<br />Total Number of Letter ק in Hebrew Bible: 16278
<br />Total Number of Letter ר in Hebrew Bible: 68064
<br />Total Number of Letter ש in Hebrew Bible: 58198
<br />Total Number of Letter ת in Hebrew Bible: 63206

