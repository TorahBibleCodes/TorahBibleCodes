import sqlite3
import sys
#dbpath = sys.path[0]+"/modules/tools/data.db"
dbpath = 'torah.db'


def createtable():
	conn = sqlite3.connect(dbpath, timeout=10, check_same_thread=False)
	c = conn.cursor()
	c.execute('''
		CREATE TABLE IF NOT EXISTS tbc (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			query INTEGER,
			result TEXT,
			result_es TEXT,
			result_en TEXT,
			book TEXT
		)
	''')



def addText(query, result, result_es, result_en, book):
		conn = sqlite3.connect(dbpath, timeout=10, check_same_thread=False)
		c = conn.cursor()
		conn.execute("insert into tbc (query, result, result_es, result_en, book) values (?, ?, ?, ?, ?)", (query, result, result_es, result_en, book))
		conn.commit()
		#print(c.lastrowid)


def getText(query):
		conn = sqlite3.connect(dbpath, timeout=10, check_same_thread=False)
		c = conn.cursor()
		c.execute("SELECT * FROM tbc WHERE query = '" + str(query) + "'")
		data = c.fetchall()
		#print(c.fetchall())
		if data is None:
				return "Problem!"
		else:
				return data
