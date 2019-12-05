import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port =  3306,
    user = 'root',
    passwd = 'vincent28',
    auth_plugin = 'mysql_native_password'
    # database = 'digimon'
)
print(db)


c = db.cursor()
sql = 'insert into karyawan(nama, gaji) values (%s, %s)'
val = ('Andi', 15000000)
c.execute(sql, val)
db.commit()
# print(c.fetchall())
print(c.rowcount, 'Data tersimpan')