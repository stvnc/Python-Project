import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfBCG = pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv', na_values = 'n.a')
dfBCG.interpolate(method='linear', axis=0, limit=None, inplace=True, limit_direction='forward')
dfBCG.rename(columns = {'% Balita yang pernah mendapat imunisasi BCG' : 'Persentase'})
dfCampak = pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv', na_values = 'n.a')
dfCampak.interpolate(method='linear', axis=0, limit=None, inplace=True, limit_direction='forward')
dfCampak.rename(columns = {'% Balita yang pernah mendapat imunisasi Campak' : 'Persentase'})
dfDPT = pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv', na_values = 'n.a')
dfDPT.interpolate(method='linear', axis=0, limit=None, inplace=True, limit_direction='forward')
dfDPT.rename(columns = {'% Balita yang pernah mendapat imunisasi DPT' : 'Persentase'})
dfPolio = pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv', na_values = 'n.a')
dfPolio.interpolate(method='linear', axis=0, limit=None, inplace=True, limit_direction='forward')
dfPolio.rename(columns = {'% Balita yang pernah mendapat imunisasi Polio' : 'Persentase'})

tidakTerimunisasiBCG = []
tidakTerimunisasiCampak = []
tidakTerimunisasiDPT = []
tidakTerimunisasiPolio = []

for i in range(len(dfBCG)):
    initialPercentage = 100.0
    tempList = []
    tempList.append(dfBCG.iloc[i, 0])
    tempList.append(initialPercentage - dfBCG.iloc[i, 1])
    tidakTerimunisasiBCG.append(tempList)

for i in range(len(dfCampak)):
    initialPercentage = 100.0
    tempList = []
    tempList.append(dfCampak.iloc[i, 0])
    tempList.append(initialPercentage - dfCampak.iloc[i, 1])
    tidakTerimunisasiCampak.append(tempList)

for i in range(len(dfDPT)):
    initialPercentage = 100.0
    tempList = []
    tempList.append(dfDPT.iloc[i, 0])
    tempList.append(initialPercentage - dfDPT.iloc[i, 1])
    tidakTerimunisasiDPT.append(tempList)

for i in range(len(dfPolio)):
    initialPercentage = 100.0
    tempList = []
    tempList.append(dfPolio.iloc[i, 0])
    tempList.append(initialPercentage - dfPolio.iloc[i, 1])
    tidakTerimunisasiPolio.append(tempList)

print(dfBCG)

dfNoBCG = pd.DataFrame(tidakTerimunisasiBCG, columns=['Tahun','Persentase'])
dfNoCampak = pd.DataFrame(tidakTerimunisasiBCG, columns=['Tahun','Persentase'])
dfNoDPT = pd.DataFrame(tidakTerimunisasiBCG, columns=['Tahun','Persentase'])
dfNoPolio = pd.DataFrame(tidakTerimunisasiBCG, columns=['Tahun','Persentase'])

plt.figure(figsize = (15, 9), dpi = 80)
plt.figure(1).add_subplot(221)
plt.bar(dfBCG['Tahun'], dfBCG['% Balita yang pernah mendapat imunisasi BCG'], linewidth = 3)
plt.title('BCG', fontsize=20)
plt.xticks(dfBCG['Tahun'], rotation = 90)

plt.figure(1).add_subplot(222)
plt.bar(dfCampak['Tahun'], dfCampak['% Balita yang pernah mendapat imunisasi Campak'], linewidth = 3)
plt.title('Campak', fontsize=20)
plt.xticks(dfCampak['Tahun'], rotation = 90)

plt.figure(1).add_subplot(223)
plt.bar(dfDPT['Tahun'], dfDPT['% Balita yang pernah mendapat imunisasi DPT'], linewidth = 3)
plt.title('DPT', fontsize=20)
plt.xticks(dfDPT['Tahun'], rotation = 90)

plt.figure(1).add_subplot(224)
plt.bar(dfPolio['Tahun'], dfPolio['% Balita yang pernah mendapat imunisasi Polio'], linewidth = 3)
plt.title('Polio', fontsize=20)
plt.xticks(dfPolio['Tahun'], rotation = 90)


plt.grid(True, color = 'grey')
plt.show()


