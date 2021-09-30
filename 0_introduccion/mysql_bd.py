import mysql.connector

cnx = mysql.connector.connect(user='admin', password='alohomora',
                              host='127.0.0.1',
                              database='bancos')


cnx.close()