import xlsxwriter
import xlrd

newFile = xlsxwriter.Workbook("WorkbookLomba.xlsx")
newSheet = newFile.add_worksheet("Sheet 1")
newSheet2 = newFile.add_worksheet("Sheet 2")
newSheet3 = newFile.add_worksheet("Sheet 3")
newSheet4 = newFile.add_worksheet("Sheet 4")

listIndex = []
newList = []

count = 1 

for i in range(3):
    for j in range(3):
        newSheet.write(i,j,count)
        count += 1
    
newFile.close()

file = xlrd.open_workbook('WorkbookLomba.xlsx')
sheet = file.sheet_by_name("Sheet 1")

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        listIndex.append(int(sheet.cell_value(i,j)))
    newList.append(listIndex)
    listIndex = []

for i in range(len(newList)):
    print(newList[i])

print()

'''
    Challenge Sheet 2
    1 4 7
    2 5 8
    3 6 9
'''
listKosongSheet2 = []

for i in range(len(newList)):
    listKosong2Sheet2 = []
    for j in range(len(newList)):
        listKosong2Sheet2.append(newList[j][i])
    listKosongSheet2.append(listKosong2Sheet2)

for i in range(len(listKosongSheet2)):
    print(listKosongSheet2[i])

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        newSheet2.write(i, j, listKosongSheet2[i][j])

print()

'''
    Challenge Sheet 3
    3 2 1
    6 5 4
    9 8 7
'''

listKosongSheet3 = []                

# Cara 1
# for i in range(len(newList)): 
#     listKosongSheet3 = [listKosongSheet3[::-1] for listKosongSheet3 in newList]
#
# for i in range(len(listKosongSheet3)):
#     print(listKosongSheet3[i])
# print()

# Cara 2
for i in range(len(newList)):
    listKosong2Sheet3= []
    for j in range(len(newList)-1, -1, -1):
        listKosong2Sheet3.append(newList[i][j])
    listKosongSheet3.append(listKosong2Sheet3)

for i in range(len(listKosongSheet3)):
    print(listKosongSheet3[i])

print()

'''
    Challenge Sheet 4
    9 6 3
    8 5 2
    7 4 1
'''
listKosongSheet4 = []

for i in range(len(newList)-1,-1,-1):
    listKosong2Sheet4 = []
    for j in range(len(newList)-1,-1,-1):
        listKosong2Sheet4.append(int(sheet.cell_value(j,i)))
    listKosongSheet4.append(listKosong2Sheet4)
    
for i in range(len(listKosongSheet4)):
    print(listKosongSheet4[i])





            
    

