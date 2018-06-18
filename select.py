"""
Importing and using sqlite module within python program
@author: outsider
"""

import sqlite3

sqliteFile = 'test.sqlite'
tableName = 'table2'
id = 'testID'
someID = 123456
col2 = 'table2seconCol'      #Name of the new column
col3 = 'table2thirdCol'      #Name of the new column

#Connecting to the database file
conn = sqlite3.connect(sqliteFile)
c = conn.cursor()

#Contents of all columns for row that match the id number from column 1
c.execute('SELECT * FROM {tn} WHERE {cn}="Hi Sylvain"'\
          .format(tn=tableName, cn=col2))
allRows = c.fetchall()
print('1:', allRows)

#Value of a particular column for rows that match a certain value in column 1
c.execute('SELECT ({coi}) FROM {tn} WHERE {cn}="Hi Sylvain" '\
          .format(coi=col2, tn=tableName, cn=col2))
allRows = c.fetchall()
print('2:', allRows)

#Values of 2 particular columns for rows that match a certain value in column 1
c.execute('SELECT {coi},{coi1} FROM {tn} WHERE {cn}="Hi Sylvain" '\
          .format(coi=col2, coi1=col3, tn=tableName, cn=col2))
allRows = c.fetchall()
print('3:', allRows)

c.execute('SELECT * FROM {tn} WHERE {cn}="Hi Sylvain" LIMIT 10 '\
          .format(coi=col2, tn=tableName, cn=col2))
tenRows = c.fetchall()
print('4:', tenRows)

#Check whether or not an ID exists and print all columns relative to that
c.execute('SELECT * FROM {tn} WHERE {idf}={testID} '\
          .format(tn=tableName, cn=col2, idf=id, testID=someID))
idExists =  c.fetchone()
if(idExists):
    print('5: {}'.format(idExists))
else:
    print('5: {} does not exists'.format(id))


conn.close()


#This method is for cleanning the variables and prevent SQL's injections... 
def cleanNames(someVariable):
    return ''.join(char for char in someVariable if char.isalnum())




