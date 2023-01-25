import pandas as pd
import numpy as np
# pd.set_option('display.max_rows', None)

df = pd.read_csv('miestai.csv', encoding='utf-8', skiprows=0)
# print(df.to_string())
# print(df[0:5])

# df.head() ir df.tail(), [9:02 PM] Andrius Makutas
# skiprows=3
print(df.head(5).to_string())


# 4 Padarykite, kad indeksas būtų stulpelis 'Miestas', ir kad šis pasikeitimas išliktų originale

df.set_index('Miestas', inplace=True)
print(df)

# 5 Ištraukite reikšmę, kiek gyventojų gyveno Marijampolėje 1923m.

print(df.loc['Marijampolė', '1923'])



# 6 Ištraukite stulpelį '1897', pirmas penkias eilutes.
print((df['1897']).head())

# 7 Ištraukite stulpelius '2019', '1970', '1923', pirmas 10 eilučių.
print((df[['2019', '1970', '1923']] ).head(10))

# 8 Su .shape patikrinkite, kiek eilučių turi lentelė (pamenat numpy? :)
print(f'Eilutes: {df.shape[0]}\nStulpeliai: {df.shape[1]}')

# 9 pridėkite stulpelį su numeracija.

df['Nr']  = range(1, df.shape[0] + 1)
print(df)


# 10 Ištraukite miestus nuo 30 iki 39 pozicijos.
# print(df.columns)
new_df = df[(df['Nr'] > 29) & (df['Nr'] < 40)]
new_df.to_csv('miestai_new.csv', encoding='utf-8', header=True)



# 11 Ištrinkite numeracijos stulpelį.
# print(df.drop('Kaunas', axis=0)) cia eilute trina
print(df.drop('Nr', axis=1, inplace=True))

# 12 Kurių miestų dar nebuvo 1959m.?
print  (df   [     (df["1959"]==0)  ])

# 13 Kokie miestai 1897 turėjo daugiau gyventojų, negu 2019?
print  (df   [     (df["1897"]>df["2019"])  ])

# 14 Kuriuose miestuose padaugėjo gyventojų nuo 2011 iki 2019?
print  (df   [     (df["2019"]>df["2011"])  ][['2019', '2011']])

# 15 Kuriuose miestuose gyventojų skaičius nuosekliai mažėjo nuo pat 1897m.?
print  (df   [     (df["1897"]>df["1923"]) &  (df["1923"]>df["1959"]) &  (df["1959"]>df["1970"]) &  (df["1970"]>df["1979"]) & (df["1979"]>df["1989"])& (df["1989"]>df["2001"]) & (df["2001"]>df["2011"]) & (df["2011"]>df["2019"])       ])


# 16 Suraskite labiausiai procentaliai gyventojų skaičiumi padidėjusį ir sumažėjusį miestus nuo 1989m.

df['Percent_dif'] = round((df['2019']/df['1989']-1)*100,2)
maxname = df['Percent_dif'].idxmax()
maxvalue = df['Percent_dif'].max()
print(f'{maxname}\t {maxvalue} %')

minname = df['Percent_dif'].idxmin()
minvalue = df['Percent_dif'].min()
print(f'{minname}\t {minvalue} %')


# 17 Nuresetinkite indeksą

df.reset_index(inplace=True)
print(df)