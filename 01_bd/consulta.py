import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos') # Datasource
cursor = cnx.cursor() # Recordset

id = input("ID de Cliente: ")
query = "SELECT * from Cliente where ID = %s"

cursor.execute(query,[id])

for item in cursor:
  print(item)

cursor.close()
cnx.close()