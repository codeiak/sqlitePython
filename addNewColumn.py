"""
Importing and using sqlite module within python program
@author: outsider
"""

import sqlite3 #Module name to import

sqliteFile = 'test.sqlite'      #Name of the database file
tableName = 'table2'            #Name of the table created
idColumn = 'testID'             #Name of the Primary Key column
newCol1 = 'table2seconCol'      #Name of the new column
newCol2 = 'table2thirdCol'      #Name of the new column
colType = 'TEXT'                #Column data type
defaultVal = 'Hello World'       #Default column value

#Connecting to the database file
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

#Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=tableName, cn=newCol1, ct=colType))

#Adding a new column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'"\
          .format(tn=tableName, cn=newCol2, ct=colType, df=defaultVal))

conn.commit()
conn.close()
