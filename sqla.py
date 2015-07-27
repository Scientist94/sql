# import sqlite lib
import sqlite3

#creating new db
conn = sqlite3.connect("new.db")

#get a cursor object
cursor = conn.cursor()

#create a table
cursor.execute(""" CREATE TABLE population(city TEXT, state TEXT, population INT) """)

#close db connection
conn.close()

