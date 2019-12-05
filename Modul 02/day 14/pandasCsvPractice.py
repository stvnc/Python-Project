import numpy as np
import pandas as pd
import requests as rq

# df = pd.read_csv(
#     'ptabc.csv',
#     delimiter = ';', #header = 2
#     skiprows = 2,
#     engine = 'python',
#     skipfooter = 2
# )

df = pd.read_csv(
    'ptabc.csv',
    delimiter = ';', #header = 2
    skiprows = 2,
    engine = 'python',
    skipfooter = 2
)
df = df.set_index('No') #disimpan kembali
print(df)
# print(f'Gaji: {df['Gaji'].describe().loc['max']}')
print(f"Max Gaji: {df['Gaji'].max()} \n")
print(f"Min Gaji: {df['Gaji'].min()} \n")
print(f"Mean Gaji: {df['Gaji'].mean()} \n")
print(f"Median Gaji: {df['Gaji'].median()} \n")
print(f"Total Gaji: {df['Gaji'].sum()} \n")

# Menampilkan data nama usia dan gaji dari gaji terminim
print(f"{df[df['Gaji'] == df['Gaji'].min()][['Nama', 'Usia', 'Gaji']]} \n") 

# Menampilkan data nama, usia, gaji dengan gaji terminim
print(f"{df[['Nama', 'Usia', 'Gaji']][df['Gaji'] == df['Gaji'].min()]} \n")

# Menampilkan data dengan usia paling tua
print(f"{df[df['Usia'] == df['Usia'].max()]} \n") 

# Menampilkan data dengan usia diatas 25 dan kotanya adalah Jakarta
print(f"{df[(df['Usia'] > 25) & (df['Kota'] == 'jakarta')]} \n")

# Menampilkan data dengan usia diantara 25 dan 30
print(f"{df[df['Usia'].between(25, 30)]} \n")

# Menampilkan data dengan usia diatas 25 atau kota = Jakarta
print(f"{df[(df['Usia'] > 25) | (df['Kota'] == 'Jakarta')]} \n")

'''
    Baca Excel
'''
dfExcel = pd.read_excel(
    'ptabcexcel.xlsx',
    header = 3,
    skipfooter = 2
)

print(f"{dfExcel} \n")

#Mengubah Urutan Kolom
print(f"{dfExcel[['Gaji', 'Kota', 'Usia', 'Nama', 'No']]} \n")

kol = dfExcel.columns.tolist()
kol = kol[-1:] + kol[:-1]
print(f"{dfExcel[kol]} \n")

dfExcel.to_csv('filebaru.csv', index=False)
dfExcel.to_excel('filebaru.xlsx', index=False)

newDf = pd.read_excel(
    'ptabcexcel.xlsx',
    'TestPandas'
)
print(f"{newDf} \n")

htmlDf = pd.read_html(
    'coba.html'
)
print(htmlDf)

digiDf = pd.read_html('http://digidb.io/digimon-list/')
print(digiDf)

digiDf[0].to_csv('digimon.csv', index=False)
digiDf[0].to_json('digimon.json', orient = 'records')

url = 'https://pokemondb.net/pokedex/all'
x = rq.get(url)
pokemonDf = pd.read_html(x.text)
print(pokemonDf[0])
pokemonDf = pokemonDf[0]

print(pokemonDf[pokemonDf['Speed'] == pokemonDf['Speed'].max()])

# bpsDf = pd.read_excel('bps-file.xls')
# print(f"\n {bpsDf}")

'''
    df = pd.read_csv(
    'ptabc.csv',
    na_values = [
        '-', 'n.a'
    ])

    df = df.fillna({
        'Nama': 'Anonim',
        'Usia': 24,
        'Gaji': 5000000
        }
    )

    print(df)

    #forward filling
    bfill = backward fill
    ffill = forward fill
    df = df.fillna(0) -> jadi 0 yang kosong
    df = df.fillna(method = 'ffill', axis='index')
    df['Gaji'] = df['Gaji'].astype('int64')
    df = df.interpolate().fillna({
        'Nama' : 'Anonim'
    })
    df = df.dropna()
    df = df.dropna(thresh = 1) #threshold 
    df = df.dropna(subset = ['Nama', 'Usia'])
    df

'''