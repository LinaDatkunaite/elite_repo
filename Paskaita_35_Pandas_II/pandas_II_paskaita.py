import pandas as pd
import numpy as np

# data = [[0.213801, 0.377678, 0.644228, 0.508592, 0.480634, 0.582498],
#         [0.729803, 0.435196, 0.078172, 0.649245, 0.312637, 0.624457],
#      [0.408850, 0.001955, 0.333323, 0.274232, 0.151326, 0.444622],
#      [0.801069, 0.430484, 0.758999, 0.256924, 0.324919, 0.230131],
#      [0.768584, 0.698750, 0.103811, 0.141918, 0.587272, 0.166636]]
#
# df = pd.DataFrame(data,
#                   ['a', 'b', 'c', 'd', 'e'],
#                   ['U', 'V', 'W', 'X', 'Y', 'Z'])
# print(df)
#
# table = df[df>.15]
# print(table)
#
# # grazina true/false
# print(table.isnull())
#
# # kiek reiksmiu yra null:
# print(table.isnull().sum())
#
# # drop n/a
# print(table.dropna())
# print(table.dropna(axis=1))
#
#
# print(table.dropna(thresh=5))
#
# # uzpildyti n/a kazkuo
# print(table.fillna('Labas'))
#
# # uzpildyti vieno stulpelio reiksmes avg reiksme
# print(table['W'].fillna(value=table['W'].mean()))
#
# # uzpildyti visas reiksmes vidurkiu
# print(table.fillna(value=table.mean()))


duomenys = {'Šalis': ['Lietuva',
  'Lietuva',
  'Lietuva',
  'Latvija',
  'Latvija',
  'Latvija',
  'Estija',
  'Estija',
  'Estija'],
 'Miestas': ['Vilnius',
  'Kaunas',
  'Klaipėda',
  'Ryga',
  'Ventspilis',
  'Daugpilis',
  'Talinas',
  'Tartu',
  'Pernu'],
 'Gyv': [541, 287, 147, 716, 43, 105, 400, 101, 46]}

data = pd.DataFrame(duomenys)
# print(data)
# grouped = data.groupby('Šalis')
# print(grouped.mean())
# print(grouped['Gyv'].sum())


# print(grouped.describe())
# print(grouped.describe().transpose())
# print(grouped.describe().transpose()['Lietuva'])

data_1 = data[0:6]
print(data_1)

data_2 = data[6:]
print(data_2)


# sudejo lygegriaciai kaip union
data_new = pd.concat([data_1, data_2])
print(data_new)

# sudeti pagal stulpelius
data_new = pd.concat([data_1, data_2], axis=1)
print(data_new)

data_right = data_2.reset_index()
print(data_right)
data_right.drop(columns='index', inplace=True)
print(data_right)

naujas = pd.concat([data_1, data_right], axis=1)
print(naujas.to_string())

lenkija = {'Šalis': ['Lenkija', 'Lenkija', 'Lenkija'],
           'Miestas':['Varšuva', 'Vroclavas', 'Gdanskas'],
          'Gyv': [1688, 638, 461]}
pl = pd.DataFrame(lenkija)
data_right1 = pd.concat([data_right, pl])
with_poland = data_right1.reset_index().drop(columns='index')
print(with_poland.to_string())



with_poland = pd.concat([data_1, with_poland], axis=1)
print(with_poland.to_string())

key = 'A B C D E F'.split()

data_1['key'] = key
data_right1['key'] = key

print(data_1)
print(data_right1)

merged  = pd.merge(data_1, data_right1, on='key')
print(merged)












