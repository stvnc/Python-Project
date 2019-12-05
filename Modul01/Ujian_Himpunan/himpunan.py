'''
    Ujian Modul 01 Job Connector Data Science Purwadhika
    Tanggal: 12 November 2019
    Soal   : 01 - Himpunan
    Nama   : Vincent Angelo
'''

himpunanA = {2, 4, 6, 8, 10, 12, 14, 16, 18}
himpunanB = {3, 5, 7, 9, 11, 13, 15, 17, 19}
himpunanC = {-9, -8, -7, -6, -5, -4, -3, -2, -1}
himpunanD = {2, 3, 5, 7, 11, 13, 17, 19}
himpunanE = {4, 6, 8, 9, 10, 12, 14, 15, 16, 18}

# a. A ∪ B ∪ C ∪ D ∪ E
formulaA = himpunanA.union(himpunanB, himpunanC, himpunanD, himpunanE)
print(formulaA)
# b. (A ∩ B) ∪ (D ∩ E)
formulaB = (himpunanA & himpunanB).union(himpunanD  & himpunanE)
print(formulaB)
# c. (A ∪ B) ∩ (D ∪ E)
formulaC = (himpunanA | himpunanB) & (himpunanD | himpunanE)
print(formulaC)
# d. (A ∪ B) - (D ∪ E)
formulaD = (himpunanA | himpunanB) - (himpunanD | himpunanE)
print(formulaD)
# e. (A ∪ B ∪ C) - (A ∩ E)
formulaE = (himpunanA | himpunanB | himpunanC) - (himpunanA & himpunanE)
print(formulaE)