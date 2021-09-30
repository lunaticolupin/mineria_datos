import mysql.connector

try:
    cnx = mysql.connector.connect(user='admin', password='',
                              host='localhost',
                              database='bancos')
    print("Conexión realizada")
    cnx.close()
except Exception as e:
    print(e)

