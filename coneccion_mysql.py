import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="3238",
        database="bigbread",
        )

    if connection.is_connected():
            print("exitosa")
    else:
        print("no se conecto")
finally:
    if connection.is_connected():
       connection.close()
       print("cerrado")