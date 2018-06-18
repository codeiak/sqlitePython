"""
Importing and using sqlite module within python program
@author: outsider
"""

import sqlite3

sqliteFile = 'test.sqlite'
tableName = 'table2'
idCol = 'testID'
newCol = 'uniqueName'
colType = 'TEXT'
indexName = 'uniqueIndex'

#Connecting to the database file
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

#Adding a new column and update some records
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=tableName, cn=newCol, ct=colType))
c.execute("UPDATE {tn} SET {cn}='Sylvain' WHERE {idf}=123456"\
          .format(tn=tableName, idf=idCol, cn=newCol))

#Creating a unique index
c.execute('CREATE INDEX {ix} ON {tn}({cn})'\
          .format(ix=indexName, tn=tableName, cn=newCol))

#Dropping the unique index ... to avoid future conflicts with update/insert functions
"""
c.execute('DROP INDEX {ix}'.format(ix=indexName))
"""

conn.commit()
conn.close()

