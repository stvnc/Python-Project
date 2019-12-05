import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'vincent28',
    database = 'day7'
)

c = db.cursor(dictionary=True)
#Query untuk mengambil keseluruhan data dari suatu tabel
sqlQuery = 'select * from karyawan'
#Query untuk memasukkan data
insertQuery = 'insert into karyawan (nama, gaji) values (%s, %s)'
#Query untuk menghapus data
deleteQuery = 'delete from karyawan where nama = %s'
#Query untuk mengupdate data
updateQuery = 'update karyawan set gaji = %s where nama = %s'
#Query untuk memasukkan kolom baru
modifyTableQuery = 'alter table karyawan add column hobby varchar(255)'
dataToInsert = ('Audi', 99000000)
dataToUpdate = (90000000, 'Anna')
dataToDelete = ('Andra', )
# c.execute(updateQuery, dataToUpdate)
# c.execute(deleteQuery, dataToDelete)
# c.execute(insertQuery, dataToInsert)
c.execute(modifyTableQuery)
db.commit()
c.execute(sqlQuery)
out = c.fetchall()
print(out)
# print(list(map(lambda x : x[0], out)))