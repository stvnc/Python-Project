hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

now = 'Rabu'
week = 7
totalDays = 100

currentIndex = hari.index(now.lower())
hariKe = (totalDays%week) + currentIndex
if(hariKe > 6):
    hariKe -= 7

print(f'{totalDays} hari dari hari {now} adalah hari {hari[hariKe]}') 