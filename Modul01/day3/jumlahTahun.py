jumlahHari = int(input('Masukkan jumlah hari :'))

year = 360
month = 30
week = 7
sisaHari = 0

jumlahYear =  jumlahHari//year
sisaHari = jumlahHari%year

jumlahMonth = sisaHari//month
sisaHari = sisaHari%month

jumlahWeek = sisaHari//week
sisaHari = sisaHari%week

print(f'{jumlahYear} Tahun, {jumlahMonth} Bulan, {jumlahWeek} Minggu, {sisaHari} hari')