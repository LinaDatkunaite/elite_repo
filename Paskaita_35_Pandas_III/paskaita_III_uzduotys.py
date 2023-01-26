import pandas as pd
from sqlalchemy import create_engine

# df = pd.read_html("https://work.studentnews.eu/s/3695/75547-European-countries-the-table-language-population-capital-currency-phone-code-internet-code.htm")
# df = df[1]
#
# df.to_csv("Country_statistics.csv", index=True)
# df.to_excel("Country_statistics.xls",sheet_name='Sheet1', index=True, engine='openpyxl')
#
#
# engine = create_engine('sqlite:///test_db.db')
# # df.to_sql('european_countries', con=engine, index=False)
# read_db = pd.read_sql('european_countries', con=engine)
# print(read_db.to_string())


# 3 Nuskaitykite į DF šį failą
df = pd.read_csv('top_20_CA_wildfires.csv')
print(df.to_string())

# 4 Kiek unikalių reikšmių yra stulpelyje 'cause'?
print('Unique causes:', len(df['cause'].unique()))
print(df['cause'].unique())

# 5 Kokios gaisrų priežastys, kiek kartų pasitaiko lentelėje?
print('-'*100)
print(df['cause'].value_counts())

# 6 Kuriais metais buvo daugiausia gaisrų?

print('-'*100)
print('Most wildfires in: ', df['year'].value_counts().idxmax())

# 7 Kiek buvo tokių gaisrų, kuriuose žuvo žmonės?
print('-'*100)
print(df[df['deaths']>=1].shape[0])


# 8 Surūšiuokite eilutes pagal metus. Išsiaiškinkite, kaip rūšiuoti, kad naujausi gaisrai būtų viršuje
print('-'*100)
print(df.sort_values('year', ascending=False).to_string())


# 9 Parašykite funkciją, kuri mėnesio pavadinimą verstų skaičiumi. Naudodami .apply() lentelėje pakeiskite mėnesių pavadinimus skaičiais.
print('-'*100)

def month_to_number(mnth):
    months = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}
    for k, v in months.items():
        if v == mnth:
            return k
df['month'] = df['month'].apply(month_to_number)
print(df.to_string())


# Pakeiskite indeksą į stulpelį 'Miestas'
# **Sutvarkykite duomenis taip, kad gyventojų sk. reprezentuotų lengelis su 'int' reikšme: -
# Ten kur trūksta duomenų - nulis. ten, kur reikšmės ne integer, sutvarkykite, kad būtų integer.**

print('-'*100)
lithuania_cities = pd.read_html('https://lt.wikipedia.org/wiki/S%C4%85ra%C5%A1as:Lietuvos_miestai_pagal_gyventojus')
lithuania_cities = lithuania_cities[0]
lithuania_cities.set_index('Miestas', inplace=True)


columns = lithuania_cities.columns.tolist()
print(columns)
new_list = []
for item in columns:
    new_column_name = item.replace('\xa0m.', '')
    new_list.append(new_column_name)

lithuania_cities.columns = new_list
print(lithuania_cities)

lithuania_cities.drop('Eilė', axis=1, inplace=True)
lithuania_cities.drop('Tankumas (2019)', axis=1, inplace=True)

lithuania_cities.fillna(int(0),inplace=True)

print(lithuania_cities.info())

def fix_dates(value):
    if '*' in str(value):
        return int(value.replace('*', ''))
    if '(?)' in str(value):
        return int(value.replace('(?)', str(0)))
    if '(??)' in str(value):
        return int(value.replace('(??)', str(0)))
    return int(value)


lithuania_cities['1897'] = lithuania_cities['1897'].apply(fix_dates)
lithuania_cities['1923'] = lithuania_cities['1923'].apply(fix_dates)
lithuania_cities['1959'] = lithuania_cities['1959'].apply(fix_dates)
lithuania_cities['1970'] = lithuania_cities['1970'].apply(fix_dates)

print(lithuania_cities.to_string())

print(lithuania_cities.info())