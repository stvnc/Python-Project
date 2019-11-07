import mysql.connector

mydb = mysql.connector.connect(user='username', password='password',
                              host='127.0.0.1', database='test',
                              auth_plugin='mysql_native_password')

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")