import xlsxwriter
import xlrd
import json
import csv

# file = xlsxwriter.Workbook('testFile.xlsx')
# sheet = file.add_worksheet('InventoriGudang')

# sheet.write(0, 0, 'Nama')
# sheet.write(0, 1, 'Kota')
# sheet.write(0, 2, 'Job')

# file.close()
namaFile = str(input('Masukkan nama file yang ingin diakses: '))
namaSheet = str(input('Masukkan nama sheet yang ingin diakses: '))

file = xlrd.open_workbook(namaFile)
sheet = file.sheet_by_name(namaSheet)

newFile = xlsxwriter.Workbook(namaFile)
newSheet = newFile.add_worksheet(namaSheet)

for i in range(sheet.ncols):
    newSheet.write(0, i, sheet.cell_value(0, i))

for i in range(1, sheet.nrows):
    for j in range(sheet.ncols):
        newSheet.write(i, j, sheet.cell_value(i, j))

def addNewFile():
    currentRow = sheet.nrows-1
    status = True
    while(status==True):
        statusInput = input('Apakah anda ingin memasukkan barang baru? Masukkan Y/N (Yes or No): ')
        if statusInput == "Y":
            for i in range(sheet.ncols):
                userInput = input(f'Masukkan {sheet.cell_value(0,i)} yang ingin dimasukkan: ')
                newSheet.write(currentRow, i, userInput)
        else:
            status = False

addNewFile()
newFile.close()


