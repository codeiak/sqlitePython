"""
Importing and using sqlite module within python program
@author: outsider
"""

"""
Overview of data types accepted in SQLite 3
    INTEGER:    A signed integer up to 8 bytes depending on the magnitute of the value
    REAL:       An 8-byte floating point value
    TEXT:       A text string, typically UTF-8 encoded (depending on the database encoding)
    BLOB:       A blob of data (binary large object) for storing binary data
    NULL:       A NULL value, represents missing data or an empty cell
"""
import sqlite3 #Module name to import

sqliteFile = 'test.sqlite'  #File of to create on first try then to use
tableName = 'table1'        #Table name within the database
tableName2 = 'table2'       #Table name within the databse
newField = 'testID'         #Name of the column
fieldType = 'INTEGER'       #Column data type

#Connecting to the database file
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

#Creating a new SQLite table with the column name
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
          .format(tn=tableName, nf=newField, ft=fieldType))

#Creating a new SQLite table with the column name and a primary key
c.execute('CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'\
          .format(tn=tableName2, nf=newField, ft=fieldType))

conn.commit()   #Committing to the database the changes made
conn.close()    #Closing the database connection after committing 
