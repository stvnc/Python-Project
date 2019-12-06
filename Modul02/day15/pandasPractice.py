import numpy as np
import pandas as pd

df = pd.read_csv('newData.csv', delim_whitespace=True)
print(df)
# df = df.replace({
#     'usia': ['-', '#', '0'],
#     'nama: '#
# })

# df['usia'] = df['usia'].replace(
#     to_replace = '-',
#     method = 'ffill'
# )
print(df)
