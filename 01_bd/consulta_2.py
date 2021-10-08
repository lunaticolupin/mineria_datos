import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos') # Datasource
cursor = cnx.cursor() # Recordset

id = input("ID de Cliente: ")
query = "SELECT NombreCliente from Cliente where ID = %s"

cursor.execute(query,[id])

temp = cursor.fetchone()

if temp is None:
  print("Sin resultdos")
else: 
  print(temp)

cursor.close()
cnx.close()