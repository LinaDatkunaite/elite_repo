# https://cataas.com/cat kas kartą užkrauna vis skirtingą katės nuotrauką. Parašykite funkciją,
# kuriai į parametrus įrašius, kiek norime nuotraukų, išsaugotų jas mūsų kompiuteryje.
import requests
import re
# def cats_save(quantity):
#     for i in range(1, quantity+1):
#         r= requests.get('https://cataas.com/cat')
#         if r.status_code not in range(400, 600):
#             print(f"connected - saving foto {i}")
#             with open(f'cat{i}.jpg', 'wb') as f:
#                 f.write(r.content)
#         else:
#             print("not connected:", r.status_code)
# cats_save(2)


# parašykite funkciją, kuri į args priimtų url eilučių sąrašą ir grąžintų,
# kokį serverį naudoja svetainė. Atsakymas galėtų atrodyti maždaug taip:

# URL                     Server
# -------------------------------------
# https://www.delfi.lt/   DWS
# https://www.alfa.lt/    nginx/1.10.3 (Ubuntu)
# https://www.15min.lt/   nginx
# https://www.lrytas.lt/  shield
# http://www.google.com/  gws

# def server_name(*args):
#     print(f"URL\t\t\t\t\t    Server")
#     print("-"*30)
#     for i in args:
#         r = requests.get(i)
#         print(f"{r.url}\t{r.headers['Server']}")
#
# server_name('https://www.delfi.lt/', 'https://www.alfa.lt/', 'https://www.15min.lt/', 'https://www.lrytas.lt/', 'http://www.google.com/')

# Parašykite programą, kuri iš adreso https://orai.15min.lt/prognozes ištrauktų ir
# atspausdintų oro prognozę Vilniuje šiuo metu. Galima naudoti str metodus, regex.


r=requests.get("https://orai.15min.lt/prognozes")
string_text = r.text.split()

# Searching for index of these two and cutting list to contain only Vilnius data:
word_Vilnius = 'href="https://orai.15min.lt/prognoze/vilnius">Vilnius</a>'
index1=string_text.index(word_Vilnius)


vilnius = string_text[index1:index1+80]

# from list to string
Vilnius_string=""
for x in vilnius:
    Vilnius_string += " " +x

print(Vilnius_string)
# use regex to find numbers
pattern1 = re.compile(r"\d{4}\.\d{2}")
pressure = pattern1.findall(Vilnius_string)


pattern2 = re.compile(r"\d\.\d{2}\s[m][/][s]")
wind = pattern2.findall(Vilnius_string)


pattern3 = re.compile(r"\d\.\d{2}\s[m][m]")
rain = pattern3.findall(Vilnius_string)


pattern4 = re.compile(r"[\+|\s|\-]\d\°")
temperature = pattern4.findall(Vilnius_string)
print(temperature)


# Answer:
print("CITY - VILNIUS")
print(f"{'PARAMETER':}{'DAY':<15} NIGHT")
print("-"*60)
print(f"Temperature\t\t\t\t{temperature[0]}\t\t\t\t{temperature[1]}")

print(f"Wind\t\t\t\t\t{wind[0]}\t\t{wind[1]}")
print(f"Pressure\t\t\t\t{pressure[0]}\t\t\t{pressure[1]}")
print(f"Rain\t\t\t\t\t{rain[0]}\t\t\t{rain[1]}")




