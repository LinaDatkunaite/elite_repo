# Parašykite generatorių, kuris kaskartą inicijuotas su funkcija
# next grąžintų sekantį porinį skaičių. Pirmas sk. 2, toliau 4 ir taip be pabaigos.


# def poriniai(skaicius):
#     while True:
#         if skaicius%2==0:
#             skaicius+=2
#             yield skaicius
#         else:
#             skaicius += 1
#             yield skaicius
#
# porinis=poriniai(10)
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))
# print(next(porinis))

# def pair_numbers():
#     number = 2
#     while True:
#         yield number
#         number += 2
#
#
# generator_object = pair_numbers()
# for _ in range(1000):
#     print(next(generator_object))

# Parašykite generatorų , kuris kas kartą generuotų po vieną Fibonačio sekos skaičių.
# (Seka prasideda šiais skaičiais: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233.
# Kiekvienas šios sekos skaičius lygus dviejų prieš jį einančių skaičių sumai, daugiau google:)



# def fibonaci():
#     x = 0
#     y = 1
#     while True:
#         z = x + y
#         yield z
#         x = y
#         y = z
# fibo_object=fibonaci()
# for _ in range(10):
#     print(next(fibo_object))



# Įsivaizduokite, kad reikia nulaužti 4 skaitmenų pin kodą. Parašykite generatorių,
# kuris tikrins po viena kombinaciją, pradedant 0000, ir sustos, kai pin kodas bus teisingas.
# Pradėkite programą nuo (pvz.) PIN = '0549' ir rašykite toliau.
# Pabaigus funkciją, praiteruokite sukurtą generatorių su for ciklu,
# kad spausdintų skaičiukus iš eilės ir atspausdinus paskutinį, parašytų
# 'PIN is XXXX(jųsų pin'as)'. Atkreipkite dėmesį, kad kodas gali prasidėti nuliu.
# Sugalvokite, kaip apeiti šią problemą :).
# PIN = '0549'
# def tikrinti(x):
#     x=int(x)
#     checker=0
#     while x<10000:
#         if x!=checker:
#             yield f'{checker:04}'
#             checker+=1
#         else:
#             yield f'Your PIN is {checker:04}'
#             break
#
# patikrintas=tikrinti(PIN)
# for x in patikrintas:
#     print(x)


# ------------------------------------------

# PIN = '0549'
#
# def pin_breaker():
#     counter = 0
#     while counter < 10000:
#         guess = f'{counter:04}'
#         if guess == PIN:
#             print(f"{guess} That's your PIN!")
#             break
#         yield guess
#         counter += 1
#
#
# gen = pin_breaker()
#
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break



# Parašykite generatoriaus funkciją, kuri atidarytų nurodytą failą,
# ir grąžintų po vieną eilutę (tiesiog yield'inti reikės ne skaičių o kitą duomenų tipą.).
# Reikės prisiminti darbą su failais :)




def file_reater(tekstas):
    with open(tekstas, 'r', encoding="utf-8") as failas:
        for eilute in failas:
            yield eilute[:-1]
            # yield eilute.strip()

file_read=file_reater("Text.txt")
for item in file_read:
    print(item)

# --------------------------------------------------


def return_file_print(file_name):
    with open(file_name, "r", encoding='utf-8') as f:
        while True:
            result = f.readline()
            yield result


file = return_file_print("task1_regex")
print(next(file))
print(next(file))
print(next(file))