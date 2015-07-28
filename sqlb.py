# import sqlite lib
import sqlite3

#creating new db
conn = sqlite3.connect("new.db")

#get a cursor object
cursor = conn.cursor()

#create a table
#cursor.execute(""" CREATE TABLE population(city TEXT, state TEXT, population INT) """)

#Insert data
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 8200000)")

cursor.execute("INSERT INTO population VALUES('Guwahati', 'GHY', 1200000)")

#commit changes
conn.commit()







#close db connection
conn.close()

