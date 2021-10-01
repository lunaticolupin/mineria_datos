import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos') # Datasource
cursor = cnx.cursor() # Recordset

query = "insert into Cliente values (%s, %s, %s, %s)"

valores = (None, 'PedroNN', 'Dom conocido S/NMMM', 'Cholula')

try: 
  cursor.execute(query, valores)

  if cursor.rowcount:
    print("Registro creado")
    cnx.commit()

except Exception as e:
  print(e)
  cnx.rollback() 

query =  "delete from Cliente where nombreCliente like %s"

try:
  cursor.execute(query, ['%Pedro%'])
  if cursor.rowcount:
    print("Registro eliminado")
    cnx.commit()
except Exception as e:
  print(e)
  cnx.rollback() 


query = "update Cliente set nombreCliente = %s where id = %s "
valores = ('Hugo', 3)

try:
  cursor.execute(query, valores)
  if cursor.rowcount:
    print("Registro actualizado")
    cnx.commit()
except Exception as e:
  print(e)
  cnx.rollback()


cursor.close()
cnx.close()