import numpy as np
import pandas as pd
from sqlalchemy import create_engine


df = pd.read_csv('top50.csv', encoding='ISO-8859-1')
# print(df.head())
# print(df.columns)

# unique genres:
print(df['Genre'].unique())

# how many unique genres:
print(len(df['Genre'].unique()))
# tas pats countas unikaliu elementu:
print(df['Genre'].nunique())
print(df['Genre'].value_counts())


# apply() metodas kuris paima musu parasyta f-ja ir ja pritaiko:
def sec_to_min(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes}:{seconds}'


print(df['Length.'].head())
df['Length_in_mins'] = df['Length.'].apply(sec_to_min)
print(df)

# kai irasineju butinai index=false nes jei neparasysiu prides naujus indexus
df.to_csv('df_new.csv', encoding='utf-8', header=True, index=False)


print(df['Length.'].apply(lambda x: round((x/60),2)))


# info apie indeksa
print(df.index)
print(df.shape)
print(df.sort_values('Popularity').head().to_string())
print(df.sort_values('Artist.Name').head().to_string())
print(df.isnull().count())
print(df.info())

#
# x1 = pd.read_excel('example.xls', sheet_name='example')
# print(x1.head())

# x1.to_excel('example2.xls', sheet_name='Sheet1', index=False)

html = pd.read_html('https://lt.wikipedia.org/wiki/Vilniaus_miesto_savivaldyb%C4%97')
df = html[9]
# df.to_csv('savivaldybes.csv', index=False)

engine = create_engine('sqlite:///test_db.db')
#
# df.to_sql('savivaldybes', con=engine, index=False)

read_db = pd.read_sql('savivaldybes', con=engine)
print(read_db)
