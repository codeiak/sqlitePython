"""
Importing and using sqlite module within python program
@author: outsider
"""

import sqlite3 #Module name to import

sqliteFile = 'test.sqlite'
tableName = 'table2'
idCol = 'testID'  
columnName = 'table2seconCol' 

#Connecting to the database
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

#Insert an ID with a specific value in the second column
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'testing')"\
              .format(tn= tableName, idf=idCol, cn=columnName))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(idCol))
    
#Try to insert an ID (if it doesn't exist yet) with a specific value in the second column
c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'testing')"\
          .format(tn=tableName, idf=idCol, cn=columnName))

#Update the newly inserted row
c.execute("UPDATE {tn} SET {cn}=('Hi Sylvain') WHERE {idf}=(123456)"\
          .format(tn=tableName, cn=columnName, idf=idCol))

conn.commit()
conn.close()


