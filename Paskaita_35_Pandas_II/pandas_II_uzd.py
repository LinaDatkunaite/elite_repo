import pandas as pd

top_left = pd.read_csv('top1-25-1.csv')
top_right = pd.read_csv('top1-25-2.csv')
bottom_left = pd.read_csv('top26-50-1.csv')
bottom_right = pd.read_csv('top26-50-2.csv')

merge_1=pd.concat([bottom_left, bottom_right], 1)
# print(merge_1.to_string())

merge_2=pd.merge(top_left, top_right, on=['Track.Name', 'Popularity'])
# print(merge_2.to_string())


df=pd.concat([merge_2, merge_1])
# print(df.to_string())


# 2 Sutvarkykite indeksą - padarykite, kad prasidėtų nuo 1.
print('\n-----------------------------------------------------------------------------------------')
df['Id']  = range(1, df.shape[0] + 1)
df.set_index('Id', inplace=True)
print(df.to_string())

# 3 Sukurkite grupavimo pagal žanrą objektą
genre_group = df.groupby('Genre')


# 4 kokie žanrai lentelėje pasitaiko daugiau negu 3 kartus?
print('\n-----------------------------------------------------------------------------------------')
newdf = genre_group.count()
print(newdf.head().to_string())
print('\n-----------------------------------------------------------------------------------------')
print(newdf[newdf['Energy']>3]['Energy'])

# 5 Koks žanras pats populiariausias? Koks mažiausiai populiarus?
# (pagal populiarumo vidurkį)
print('\n-----------------------------------------------------------------------------------------')
print(genre_group['Popularity'].mean().idxmax(), genre_group['Popularity'].mean().max())
print(genre_group['Popularity'].mean().idxmin(), genre_group['Popularity'].mean().min())

# 6 Sukurkite lentelę, kurioje matytųsi, koks žanras turi aukščiausią vidurkį kiekviename indikatoriuje, bei pats vidurkis.
# kad nereikėtų daug vargti su stulpelių pavadinimais, galima juos ištraukti su .columns.tolist(
print('\n-----------------------------------------------------------------------------------------')
list = df.columns.tolist()
max_list=[]
maxname_list=[]

for i in list[3:]:
    name = genre_group[i].mean().idxmax()
    max_value = round(genre_group[i].mean().max(),1)
    maxname_list.append(name)
    max_list.append(max_value)

Genre = pd.Series(maxname_list)
Score = pd.Series(max_list)
Indicator = pd.Series(list[3:])
print(pd.DataFrame(dict( Indicator = Indicator, Genre = Genre, Score=Score)))

# -----------------
# 6 uzduotis destytojo
print('\n-----------------------------------------------------------------------------------------')

indicators = df.columns.tolist()[3:]
zanrai = genre_group.mean()[indicators].idxmax()
skaiciai = genre_group.mean()[indicators].max()
result = pd.DataFrame([indicators, zanrai, skaiciai],
                      ['Indikatorius', 'Žanras', 'Balai']).transpose()
print(result)

# # 7 Grįžkime prie sulipdytos lentelės. Ištraukite visas eilutes, kurios turi NaN reikšmių.
print('\n-----------------------------------------------------------------------------------------')
df2  = df[(df['Genre'].isnull()) | (df['Popularity'].isnull())]
print(df2.to_string())

# 8 Stulpelyje 'Genre' NaN reikšmes pakeiskite į 'pop'
print('\n-----------------------------------------------------------------------------------------')
df['Genre'].fillna('pop', inplace=True)
print(df.to_string())

# 9 Stulpelyje 'Popularity' trūkstamas reikšmes pakeiskite į stulpelio vidurkį
print('\n-----------------------------------------------------------------------------------------')
df['Popularity'].fillna(value=df['Popularity'].mean(), inplace=True)
print(df.to_string())




