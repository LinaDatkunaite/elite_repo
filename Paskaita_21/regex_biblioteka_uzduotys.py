#1
# parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
# Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu.

import re

def split_date(name):
    pattern=re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
    result1 = pattern.search(name)
    if result1:
        l=[]
        for i in result1.groups():
            l.append(i)
        print(f"{l[2]} {l[1]} {l[0]}")
split_date("09.09.2000")

# 2
# Iš šio teksto atspausdinkite datų sąrašą.
text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

#3
# Atspausdinkite tą patį teksta taip:
# 1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019
# 2.
# Event: Notification of acceptance
# Date: December 1, 2019
# ir t.t.



pattern = re.compile(r":\s([A-Za-z]\w+)\s(\d{1,2})\,\s([0-9]\d+)", re.MULTILINE)
pattern2 = re.compile(r".+(?=:)", re.MULTILINE)
result_date = pattern.findall(text)
result_name = pattern2.findall(text)
print(result_date)
# print(result_name)

num=1
for date, name in zip(result_date, result_name):
    print(F"{num}.\nEvent: {name}\nDate: {date[0]} {date[1]}, {date[2]}\n")
    num+=1

# kitas variantas:
# def vent_date(kazkas):
#     eventas = re.compile(r'.+?(?=:)')
#     result_eventas = eventas.findall(text)
#     pattern = re.compile(r':\s([a-z]\w+\s\d{1,2},\s\d{4})', re.M | re.I)
#     datos = pattern.findall(text)
#     for n in range(1,8):
#         print(f'Event: {result_eventas[n-1]}\nDate: {datos[n-1]}\n')
# vent_date(text)

#4
# Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių, kuriuos reikia jame išcenzūruoti sąrašą. Pvz, žodis "kvaraba" yra baisus keiksmažodis, ir mums reikia duotame tekste pakeisti k*****a. Pradėkite maždaug taip:
# iškvietus funkciją, pvz.
# cenzura()
# cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')
# mums atspausdintų
# baisūs žodžiai, tokie kaip k*****a, ž****s..
# žodžių cenzūravimui naudokite regex, o jų sukeitimui tekste naudokite .replace()\


# def cenzura(zodziai, *keiksmai):
#     pattern = re.compile(r'([A - ZĄČĘĖĮŠŲŪŪŽa - ząčęėįšųūž]+)')
#     result5 = pattern.sub('\g<1>', zodziai)
#     result = result5.lower()
#     for i in keiksmai:
#         # print(str(i))
#         # print("-"*100)
#         if str(i).lower() in result.lower():
#             x = result.replace(str(i),f"{str(i)[0]}{(len(str(i))-2)*'*'}{str(i)[-1]}")
#             result=x
#     print(result.capitalize())
#
#
# cenzura(input("iveskite komentara: "),"kvadabra","zaltys", "žaltys", "lopas")

# def cenzura(tekstas, *ka_keiciam: str):
#     for i in ka_keiciam:
#         pattern = re.compile(f'{i}', re.I)
#         x = len(i)
#         result = pattern.sub(f'{i[0]}{"*"*(x-2)}{i[-1]}', tekstas)
#         tekstas = result
#     print(tekstas)
#
# cenzura('baisūs žodžiai, tokie kaip Kvaraba, žaltys, zaltys, žaltysžaltysžaltys..', 'tokie', 'kvaraba', 'žaltys')
#
#


def cenzura(tekstas, *keiksmai):
    swear_words = [*keiksmai]
    for _ in swear_words:
        pattern = re.compile(_, re.I)
        x = len(_)
        tekstas = pattern.sub(f'{_[0]}{"*" * (x - 2)}{_[-1]}', tekstas)
    print(tekstas)
