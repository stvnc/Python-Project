'''
    Ujian Modul 01 Job Connector Data Science Purwadhika
    Tanggal: 12 November 2019
    Soal   : 02 - Segitiga Kata
    Nama   : Vincent Angelo
'''
def segitigaKata(param):
    newList = list(param)
    count = 0
    rowCount = 0
    for i in range(0, int(len(newList)/2)):
        for j in range(0, i+1):
            if count == len(newList):
                break
            else:
                print(newList[count], end = ' ')
                count += 1
        rowCount += 1
        print()
        if(count == len(newList)):
            break

    count = 0
    for i in range(rowCount, 0, -1):
        for j in range(i, 0, -1):
            if count == len(newList):
                break
            print(newList[count], end = ' ')
            count += 1
        print()

userInput = str(input('Masukkan kata yang ingin dijadikan segitiga: ')).replace(' ', '')
if len(userInput) < 10:
    print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')
else:
    segitigaKata(userInput)


    
        