#SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#using loop to iterate through db 
	for row in c.execute("SELECT firstname, lastname from employees"):
		print row