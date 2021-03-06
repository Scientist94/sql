#try-except implementation
import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
 	cursor.execute("INSERT INTO populations VALUES('New York City', 'NY', '8200000')")
 	cursor.execute("INSERT INTO populations VALUES('San Francisco', 'CA', '3200000')")
 	conn.commit()

except sqlite3.OperationalError:
 	print "Oops! Something went wrong. Try again...."

conn.close()