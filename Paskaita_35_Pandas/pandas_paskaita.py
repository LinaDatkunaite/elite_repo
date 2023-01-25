import numpy as np
import pandas as pd
#
#
# # Pandas bibliotekoje tai yra data frame:
# dict = {
#     'first_name': ["vardenis", "John", "Jane"],
#     'last_name': ["pavardenis", "Doe", "Doe"],
#     'email': ["vardenis.pav@gmail.com", "Jogn.d@gmail.com", "Jane.d@gmail.com"]
# }
#
# # serija yra tiesiog array / listas:
# dict_object = pd.Series(data=dict)
# print(dict_object)
#
# # Dataframe yra lentele su collumn ir raws
# dict_object = pd.DataFrame(data=dict)
# print(dict_object)
#
# # su pandom pasidarom:
# labels = ['a', 'b', 'c']
# data = ['abc', 'def', 'fgh']
#
# # tai yra array arba listas is elementu:
# print(pd.Series(data=data, index=labels))
#
#
# print(pd.Series([1,2,3,4], ['Vln', 'Kns', 'Klp', 'Pnv']))
#
# df = pd.read_csv('survey_results_public.csv')
#
# # raws, columns
# print(df.shape)
# print(df.info())

df = pd.DataFrame(np.random.rand(5,5),
                            ['a', 'b', 'c', 'd', 'e'],
                            ['A', 'B', 'C', 'D', 'E'])
print(df)
print(df.A)
print(df[['A']])
print(df[['A', 'B']])

# prideti stulpeli
df['Counter'] = ['1', '2', '3', '4', '5']
print(df)

# istrinti, axis =0 x asis - istrinsim eilute, axis=1 naikina stulpeli,
# tik laikinai istrina
print(df.drop('Counter', axis=1))

print(df.drop('a'))

# inplace = True jau realiai istrina stulpeli
df.drop('Counter', axis=1, inplace=True)
print(df)

# loc - location ir iloc - index location
# kiekvieno kolumno b value
print(df.loc['b'])

# issitraukt c eilute
print(df.iloc[2])

# konkreti reiksme
print(df.loc['b', 'B'])

# pirma eina eilute poto stulpelis slicinant
print(df.loc[['b', 'c'], ['B', 'C']])

# condition
# is visko
print(df[df>0.1])

# is konkretaus stulpelio
print(df[df['B']>0.4])

# jei A > 0.1 isprintink B ir C stulpelius
print(df[df['A']>0.1][['B', 'C']])

# salygu kombinavimas & | ^ + kurie stulpeliai:
print  (df   [     (df["A"]>0.4) & (df["B"]<0.8)   ]     [['B', 'C']]  )


# indeksai
print(df)
print(df.reset_index())

new_index = 'I,II,III,   IV,V'.replace(' ', '').split(',')

# stripas netinka nes nuima tik pradzioj ir gale rstrip is right nuima o lstrip is left
# new_index = 'I,II,III,   IV,V'.strip().split(',')
print(new_index)
df['Index'] = new_index
print(df)
df = df.set_index('Index')
print(df)




