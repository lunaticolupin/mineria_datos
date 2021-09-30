import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos') # Datasource
cursor = cnx.cursor() # Recordset

query = "SELECT * from Cliente"

cursor.execute(query)

for item in cursor:
  print(item)

cursor.close()
cnx.close()