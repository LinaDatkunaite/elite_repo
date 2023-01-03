import re
teksas = """Pirmas telefono numeris yra +370 123 32121, antras +370 321 55566"""

pattern=re.compile(r'\+370\s\d{3}\s\d{5}')
# Search f-ja grazina pirma teisinga matcha (viena rezultata)- t.y. pirma telefona
result = pattern.search(teksas)
# print(result)
# group f-ja grazina konkrecia reiksme
print(result.group())

# susigrazint visus
result2 = pattern.findall(teksas)
print(result2[0])
print(result2[1])


def validate_email(input):
    email_regex = re.compile(r'^[a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$')
    result3=email_regex.search(input)
    email_is_valid = False
    if result3:
        email_is_valid=True
    return email_is_valid

print(validate_email('kazkas@gmail.com'))

def split_names(name):
    pattern=re.compile(r'^(?P<kreipinys>[A-Z]\w{1,3}\.)\s([A-Z]\w+)\s([A-Z]\w+)$')
    result4 = pattern.search(name)
    if result4:
        print(f"Visa eilute: {result4.group(0)}")
        print(f"Kreipinys: {result4.group(1)}")
        print(f"Vardas: {result4.group(2)}")
        print(f"Pavarde: {result4.group(3)}")
        print("--------------------")
        print(result4.group())
        print(result4.group("kreipinys"))
        print(result4.groups())
    else:
        print("Ivestis neatitinka sablono")
split_names("Mr. Clint Eastwood")

card_number = "card1: 1234 4521 5555 6665, card2 = 6666 9999 8888 4567"
pattern = re.compile(r'\b(\d{4})\s\d{4}\s\d{4}\s\d{4}')
# pakeisti galima visas arba viena grupe
# sub - yra pakeitimas
result5 = pattern.sub('\g<1> **** **** ****', card_number)
print(result5)

tekstas1 = """Trumpas tekstas apie beleka"""

# re.IGNORECASE - ignoruoti didziasias ar mazasias jei be jo isrinktu tik teksta kuris ytra is mazosios
pattern = re.compile(r"t\w+", re.IGNORECASE)
result6 = pattern.findall(tekstas1)
print(result6)


tekstas1 = """Trumpas tekstas 
apie beleka"""


pattern = re.compile(r"^\w+", re.MULTILINE)
result7 = pattern.findall(tekstas1)
print(result7)


tekstas3 = "Jonas Jonaitis +370 622 33334"
pattern = re.compile(r"""
            [A-Z]\w+    # vardas
            \s          # tarpas
            [a-z]\w+   # pavarde 
            \s          # tarpas
            \+370\s6\d{2}\s\d{5} # tel
            """, re.X | re.I)
result8 = pattern.findall(tekstas3)
print(result8)
