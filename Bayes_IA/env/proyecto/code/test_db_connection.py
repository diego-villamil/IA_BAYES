import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='TSY!VHzGrN(]FxGt',
        database='proyecto'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Exception as e:
    print("Error while connecting to MySQL", str(e))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
