import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos') # Datasource
cursor = cnx.cursor() # Recordset

query = "insert into Cliente values (%s, %s, %s, %s)"

valores = (None, 'Pedro', 'Dom conocido S/N', 'Cholula')

try: 
  cursor.execute(query, valores)

  if cursor.rowcount:
    print("Registro creado")
    cursor.close()
    cnx.commit()

except Exception as e:
  print(e)
  cnx.rollback()


cnx.close()